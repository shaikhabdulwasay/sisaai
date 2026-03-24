# SISA AI — The Monolith

A stunning, high-end futuristic AI Chat interface built using Streamlit and Ollama. Run a local Language Model (qwen3.5:0.8b) without needing any cloud API keys — keeping your data completely private behind a gorgeous glassmorphic dark theme.

> 📸 *(Add your actual screenshot here!)*

---

## 🚀 Features

- **Responsive & Futuristic UI** — Enjoy glassmorphism, blurred chat bubbles, and the dynamic Orbitron font.
- **Local AI Engine** — Powered by Ollama using the `qwen3.5:0.8b` model for ultra-fast, fully offline chat.
- **Conversation History** — Your current chat is preserved and readable from the sidebar at all times.
- **Complete Privacy** — Your data never leaves your machine.

---

## 🛠️ How to Run This Project

Since this app relies on a **local AI model (Ollama)** running on your computer, follow the steps below to get it up and running.

### Step 1 — Install Ollama & Pull the Model

Download and install [Ollama](https://ollama.com/), then pull the model:

```bash
ollama run qwen3.5:0.8b
```

### Step 2 — Clone the Repository

```bash
git clone https://github.com/your-username/sisa-ai.git
cd sisa-ai
```

### Step 3 — Set Up a Python Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### Step 4 — Install Dependencies

```bash
pip install streamlit ollama
```

### Step 5 — Run the App

```bash
streamlit run test1.py
```

Your browser will open automatically. Start chatting!

---

## 📤 How to Share or Display Your Work

Since the AI backend runs locally on your machine, you **cannot** share a live URL with others. Here are your best options:

### Option 1 — Portfolio Route *(Recommended)*

Record a screen recording or GIF of the app in action and upload it to this repository. This lets recruiters, friends, and clients instantly see what you built — no setup required on their end.

**Tools you can use:**
- OBS Studio
- Snipping Tool (Windows 11)
- Any screen recorder of your choice

### Option 2 — Cloud Hosting *(Requires code changes)*

To host this on the web (e.g., Streamlit Community Cloud or Vercel), replace the local Ollama backend with a cloud-based API such as **Groq**, **OpenAI**, or **Hugging Face**.

> **Why?** Cloud servers cannot reach the Ollama instance running on your laptop — that's what makes this private, but also what limits direct hosting.

### Option 3 — Share With Other Developers

Other developers can clone this repo and run it exactly as you do by following the **How to Run** steps above.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| AI Backend | Ollama (`qwen3.5:0.8b`) |
| Language | Python |
| Styling | Custom CSS — Glassmorphism + Orbitron |

---

## 📄 License

This project is open source. Feel free to fork, modify, and build on top of it.
