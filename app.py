import gradio as gr
import openai
import os

# Connect to Groq API using your secret key
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"
MODEL = "llama-3.3-70b-versatile"  # AI model we are using

# Check if text is English (ASCII only = English)
def is_english(text):
    try: text.encode("ascii"); return True
    except: return False

# Check if text contains Urdu characters
def is_urdu(text):
    return any('\u0600' <= ch <= '\u06FF' for ch in text)

# Main function — detects language and translates
def translate_text(text, mode):
    if not openai.api_key: return "", "❌ API key not set."
    if not text.strip(): return "", "⚠️ Please enter some text."

    text = text.strip()

    # Auto detect which language user typed
    detected = "English" if is_english(text) else "Urdu" if is_urdu(text) else None

    if not detected: return "", "⚠️ Only English and Urdu supported."

    # Make sure user input matches selected mode
    if mode == "English → Urdu" and detected != "English": return "", "⚠️ Enter English text."
    if mode == "Urdu → English" and detected != "Urdu": return "", "⚠️ اردو متن درج کریں۔"

    # Set the target language
    target = "Urdu" if detected == "English" else "English"

    try:
        # Send text to AI and get translation
        res = openai.ChatCompletion.create(
            model=MODEL,
            messages=[{"role": "user", "content": f"Translate this {detected} to {target}:\n{text}"}],
            temperature=0.3
        )
        return res['choices'][0]['message']['content'], f"✅ {detected} → {target}"
    except Exception as e:
        return "", f"❌ {str(e)}"

# CSS — dark theme, side by side layout, styled buttons and textboxes
css = """
body { background: linear-gradient(135deg, #0a0f1e, #0f172a) !important; }
.gradio-container { max-width: 1400px !important; width: 95% !important; margin: auto !important; }
.main-row { display: flex !important; flex-direction: row !important; gap: 24px !important; flex-wrap: nowrap !important; }
.main-row > * { flex: 1 1 50% !important; min-width: 0 !important; }
textarea { background: #0f172a !important; color: #e2e8f0 !important; border-radius: 12px !important; border: 1px solid #4f46e5 !important; font-size: 1rem !important; min-height: 200px !important; }
.status-box textarea { min-height: unset !important; height: 45px !important; }
button { background: linear-gradient(90deg, #4f46e5, #06b6d4) !important; color: white !important; font-size: 1.1rem !important; border-radius: 12px !important; font-weight: 700 !important; }
footer { visibility: hidden; }
"""

# Build the UI
with gr.Blocks(css=css) as demo:
    gr.Markdown("# 🌐 AI Bilingual Translator\n### English ↔ Urdu")

    with gr.Row(elem_classes="main-row"):

        # Left side — user types here
        with gr.Column():
            gr.Markdown("### ✍️ Input")
            input_text = gr.Textbox(placeholder="Enter English or Urdu text...", lines=12, label="")
            mode = gr.Radio(["English → Urdu", "Urdu → English"], value="English → Urdu", label="Mode")
            btn = gr.Button("🚀 Translate")

        # Right side — translation appears here
        with gr.Column():
            gr.Markdown("### 📄 Output")
            output_text = gr.Textbox(lines=12, label="")
            status = gr.Textbox(label="Status", interactive=False, lines=1, elem_classes="status-box")

    # When button clicked, run translate_text function
    btn.click(translate_text, inputs=[input_text, mode], outputs=[output_text, status])

demo.launch()