# Design System Strategy: The Ethereal Core

## 1. Overview & Creative North Star
The Creative North Star for this design system is **"The Ethereal Core."** 

In a landscape of cluttered, grid-heavy AI tools, this system prioritizes a "spatial" experience over a "functional" one. We are moving away from the "Dashboard" archetype and toward an "Ambient Interface." By utilizing high-contrast typography scales and intentional asymmetry, we create a sense of digital weightlessness. The UI shouldn't feel like a collection of boxes; it should feel like a series of light-emitting surfaces floating in a deep, pressurized void. We achieve this by breaking the traditional container-and-border logic in favor of tonal depth and refractive glass elements.

---

## 2. Colors
Our palette is rooted in the "Deep Void" (#131313), using high-frequency blues and cyans to represent the "spark" of AI intelligence.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to define sections. Period. Traditional borders create visual noise that breaks the minimalist illusion. Boundaries must be defined solely through:
- **Background Shifts:** Placing a `surface-container-low` (#1C1B1B) sidebar against a `surface` (#131313) main stage.
- **Tonal Transitions:** Using `surface-container-highest` (#353534) for hover states to create a "lift" through color rather than a stroke.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of frosted glass. 
- **The Base:** Use `surface` (#131313) for the primary application background.
- **The Secondary Tier:** Use `surface-container-low` (#1C1B1B) for persistent elements like the sidebar navigation.
- **The Content Tier:** Use `surface-container` (#201F1F) for chat bubbles or cards.
- **The Interactive Tier:** Use `surface-bright` (#393939) for elements that require the user’s immediate focus.

### The "Glass & Gradient" Rule
To achieve the "Futuristic Minimalist" aesthetic, floating elements (Modals, Tooltips, Model Selection) must use Glassmorphism. 
- **Formula:** Apply a semi-transparent `surface-container-high` at 60% opacity with a `backdrop-blur` of 20px. 
- **Signature Textures:** For primary actions (CTAs), do not use flat colors. Use a linear gradient transitioning from `primary` (#ADC6FF) to `primary-container` (#4B8EFF) at a 135-degree angle. This adds a "soul" to the button, making it appear as a light source.

---

## 3. Typography
We use a high-contrast pairing of **Space Grotesk** and **Inter**.

- **The Tech Signal (Space Grotesk):** Use for `display` and `headline` scales. Its geometric, slightly aggressive terminals signal "High-Tech." Use `display-lg` for showcase titles to create an editorial, oversized feel.
- **The Human Element (Inter):** Use for `title`, `body`, and `label` scales. Inter provides the readability required for long-form AI responses. 
- **Intentional Scale:** Use `label-sm` in `on-surface-variant` for metadata. The massive gap between `display-lg` (3.5rem) and `body-md` (0.875rem) creates the "Editorial" tension that defines high-end design.

---

## 4. Elevation & Depth
Depth in this system is an atmospheric effect, not a structural one.

- **The Layering Principle:** Instead of shadows, stack containers. A `surface-container-lowest` (#0E0E0E) input bar sitting atop a `surface-container` chat area creates a "recessed" feel without a single shadow.
- **Ambient Shadows:** If a floating element (like a model selection dropdown) requires a shadow, it must be an "Ambient Glow." Use the `primary` color at 8% opacity with a 40px blur. This mimics the light emitted from the "Electric Blue" core.
- **The "Ghost Border" Fallback:** If accessibility requires a container edge, use a "Ghost Border." Use the `outline-variant` token at **15% opacity**. It should be felt, not seen.
- **Refractive Edges:** For glass elements, apply a 1px top-stroke using `outline` at 20% opacity. This simulates the way light catches the edge of a glass pane.

---

## 5. Components

### Chat Bubbles
- **User Bubbles:** Use `primary-container` (#4B8EFF). Roundedness: `xl` (1.5rem). Align to the right with a 16% horizontal margin to create asymmetry.
- **AI Bubbles:** No background container. Use `on-surface` text directly on the `surface` background. Use a `tertiary` (#00DBE9) vertical accent line (2px wide) on the left to denote "AI Processing."

### Sidebar Navigation
- **Styling:** `surface-container-low` (#1C1B1B). No border on the right. 
- **Active State:** Instead of a background change, use a `primary` "glow" dot next to the label and shift the text to `primary-fixed-dim` (#ADC6FF).

### Model Selection Cards
- **Structure:** Use `surface-container-high` (#2A2A2A). 
- **Interaction:** On hover, transition the background to a subtle gradient of `surface-variant` and increase the `backdrop-blur`. 
- **Typography:** Model names in `title-md` (Space Grotesk). Descriptions in `body-sm` (Inter).

### Input Fields
- **Styling:** `surface-container-lowest` (#0E0E0E). Roundedness: `full` (9999px) for a sleek, pill-shaped look.
- **Focus State:** Do not use a heavy border. Use a subtle outer glow (4px) of `primary` at 20% opacity.

---

## 6. Do's and Don'ts

### Do
- **DO** use white space aggressively. If a section feels cramped, double the spacing (e.g., move from `spacing-8` to `spacing-16`).
- **DO** use `tertiary` (#00DBE9) for small data visualizations or "AI Thinking" animations. It provides a "High-Tech" counterpoint to the blue primary.
- **DO** use `surface-bright` for subtle "shine" effects on interactive components.

### Don'ts
- **DON'T** use 100% white (#FFFFFF). Always use `on-surface` (#E5E2E1) to reduce eye strain in the dark environment.
- **DON'T** use standard "drop shadows" (Black/0,0,0). Shadows must always be tinted with the `primary` or `surface-tint` color.
- **DON'T** use dividers. If you need to separate content, use a `spacing-6` gap or a subtle shift from `surface-container` to `surface-container-low`.
- **DON'T** use center-alignment for everything. Use "Editorial Asymmetry"—align the header left, the chat input center, and the metadata right to keep the eye moving.