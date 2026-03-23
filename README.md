# 🤖 Human Voice AI Assistant

A powerful, highly responsive, and full-stack Voice AI Assistant built specifically for Mac, leveraging the intelligence of **Gemini 2.0 Flash** and the high-fidelity native text-to-speech capabilities of Mac (Safari-optimized).

## ✨ Features

- **Gemini 2.0 Vision/Audio Integration**: Accurately transcribes user voice inputs using Gemini's multi-modal capabilities.
- **Safari-Perfect Audio**: Uses an advanced dual-layer generation technique (`gTTS` to `WAV` via `ffmpeg`) ensuring 100% compatibility and avoiding the dreadful "Error" block on Safari and Chrome.
- **Lightning Fast**: Optimized backend ensures the absolute minimum latency between transcription, thinking, and talking back.
- **Loop-Safe Architecture**: Session state locks guarantee the AI will never repeat the same answer or continuously loop.
- **Clean UI**: A beautiful, dark-themed Streamlit interface resembling modern chat applications.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.9+
- `ffmpeg` (Required for audio conversion to Safari-compatible WAV formats)

To install `ffmpeg` on macOS:
```bash
brew install ffmpeg
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/anshgupta110805/Human-AI-Assistant-for-vishal-.git
cd Human-AI-Assistant-for-vishal-
```

2. Create and activate a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenRouter API Key:
```env
OPENROUTER_API_KEY=your_api_key_here
```

### Running the App

Start the Streamlit development server:

```bash
streamlit run app.py --server.headless true
```
Navigate to the provided Local URL (typically `http://localhost:8501`) to interact with the Voice Assistant.

## 🛠️ Tech Stack

- **Frontend**: Streamlit, Custom HTML/JS Audio Bridges
- **LLM/Transcription**: Langchain, Google Gemini 2.0 Flash (via OpenRouter)
- **Audio Processing**: Streamlit-Mic-Recorder, gTTS, FFmpeg, Base64

## 📝 Usage

1. Click on the **🔴 Press to Speak** button in the sidebar.
2. Speak your query and click **⏹️ STOP & SEND**.
3. Wait momentarily while the AI processes. The text response will appear, and the AI will speak its response back to you automatically!
