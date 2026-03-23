import os
import streamlit as st
import streamlit.components.v1 as components
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from streamlit_mic_recorder import mic_recorder
from gtts import gTTS
import base64
import hashlib
import io

# Load environment variables
load_dotenv()

# --- Page Config & Theme ---
st.set_page_config(page_title="AI Human Voice Assistant", page_icon="🤖", layout="wide")

st.markdown("""
<style>
    .main { background: #0e1117; color: white; border-radius: 12px; }
    .stChatMessage { margin-bottom: 2rem; border-radius: 15px; border: 1px solid #30363d; background: #161b22; }
</style>
""", unsafe_allow_html=True)

# --- AI & Voice Helper ---
def get_gemini_client():
    return ChatOpenAI(
        model="google/gemini-2.0-flash-001",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0.7,
        default_headers={"HTTP-Referer": "http://localhost:8501", "X-Title": "VoiceBot"}
    )

def transcribe(audio_bytes):
    chat = get_gemini_client()
    b64 = base64.b64encode(audio_bytes).decode('utf-8')
    prompt = [HumanMessage(content=[
        {"type": "text", "text": "Precisely transcribe this audio content into text."},
        {"type": "image_url", "image_url": {"url": f"data:audio/wav;base64,{b64}"}}
    ])]
    return chat.invoke(prompt).content

def speak_answer(text):
    try:
        # Standard gTTS MP3 generation
        tts = gTTS(text=text, lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        audio_data = fp.read()
        b64 = base64.b64encode(audio_data).decode('utf-8')
        
        # Display Player and Autoplay Bridge
        st.audio(audio_data, format="audio/mp3")
        
        # This script was working previously to force Safari/Chrome autoplay
        md = f"""
            <audio id="auto-audio" autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            <script>
                var audio = document.getElementById("auto-audio");
                if (audio) {{
                    audio.play().catch(e => console.log(e));
                }}
            </script>
        """
        st.markdown(md, unsafe_allow_html=True)
        return audio_data
    except Exception as e:
        st.error(f"Voice Error: {e}")
        return None

# --- Main App ---
st.title("🤖 Human AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "done" not in st.session_state:
    st.session_state.done = set()

with st.sidebar:
    st.header("Voice Dashboard")
    st.warning("Click the Record button. Speak. The AI will respond and speak back automatically.")
    audio_mic = mic_recorder(start_prompt="🔴 Press to Speak", stop_prompt="⏹️ STOP & SEND", key='mic')
    if st.button("🗑️ Reset All"):
        st.session_state.messages = []
        st.session_state.done = set()
        st.rerun()

# Processing Loop
user_text = st.chat_input("Ask me anything...")

if audio_mic:
    h = hashlib.md5(audio_mic['bytes']).hexdigest()
    if h not in st.session_state.done:
        st.session_state.done.add(h)
        with st.status("Listening with Gemini 2.0...", expanded=False) as s:
            user_text = transcribe(audio_mic['bytes'])
            s.update(label=f"You said: {user_text}", state="complete")

# Render History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "audio" in msg:
            st.audio(msg["audio"], format="audio/mp3")

# New Assistant Action
if user_text:
    # 1. User Message
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"): st.markdown(user_text)

    # 2. AI Message
    with st.chat_message("assistant"):
        with st.status("AI is thinking and talking...", expanded=True) as s:
            # Generate Text
            chat = get_gemini_client()
            history = [SystemMessage(content="Professional human-like assistant. Be warm and brief.")]
            for m in st.session_state.messages:
                if m["role"] == "user": history.append(HumanMessage(content=m["content"]))
                else: history.append(SystemMessage(content=m["content"]))
            
            resp_text = chat.invoke(history).content
            st.markdown(resp_text)
            
            # Generate Voice
            audio_bytes = speak_answer(resp_text)
            
            st.session_state.messages.append({"role": "assistant", "content": resp_text, "audio": audio_bytes})
            s.update(label="AI finished!", state="complete")
    
    st.rerun()
