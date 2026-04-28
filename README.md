# 🌐 AI Language Translator — English ↔ Urdu

An AI-powered translation tool built for focused, high-quality conversion between **English and Urdu**. 
By specializing in two languages rather than many, the project delivers more reliable output, cleaner prompting, and a better user experience.

## 🚀 Live Demo

Deployed on Hugging Face Spaces — no setup required:

👉 [Open Live Demo](https://huggingface.co/spaces/AneeshDawira/AI_Language_translator)


## ✨ Features

- Bidirectional translation: **English → Urdu** and **Urdu → English**
- Clean, distraction-free **side-by-side interface**
- Fast inference powered by a **70B-parameter LLM**
- Input validation with clear feedback for unsupported content


## 🛠️ Tech Stack

- **UI:** [Gradio](https://gradio.app/)
- **Language:** Python
- **AI Inference:** [Groq API](https://groq.com/)
- **Model:** `llama-3.3-70b-versatile`
- **Hosting:** Hugging Face Spaces


## 📂 Project Structure

```
├── app.py              # Main application logic
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```


## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-translator.git
cd ai-translator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your API key

```bash
# macOS / Linux
export GROQ_API_KEY=your_api_key_here

# Windows
set GROQ_API_KEY=your_api_key_here
```

### 4. Launch the app

```bash
python app.py
```

---

## 📌 Design Decisions

Most multilingual translation tools sacrifice depth for breadth. This project takes the opposite approach — focusing exclusively on **English and Urdu** to enable tighter prompt engineering, fewer ambiguous edge cases, and more consistent translation quality.

The interface is intentionally minimal, keeping the focus entirely on the translation task.

---

## 👨‍💻 About

I'm **Aneesh**, a Computer Science Graduate specializing in AI engineering. I build practical, deployment-ready AI applications with a focus on machine learning and intelligent systems.

- 🔗 [GitHub Profile](https://github.com/Aneeshkumar179)
- 💼 [LinkedIn]((https://www.linkedin.com/in/aneesh-dawira-b863b1294/)

---

*If you find this project useful, consider leaving a ⭐ — it helps others discover the work.*
