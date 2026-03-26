# SISA AI — The Monolith

A stunning, high-end futuristic AI Chat interface built using Streamlit and Ollama. Run a local Language Model (qwen3.5:0.8b) without needing any cloud API keys — keeping your data completely private behind a gorgeous glassmorphic dark theme.

> 📸 *

https://github.com/user-attachments/assets/c556a1bd-d715-4b93-959e-a2191713ca3a

*

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
git clone https://github.com/shaikhabdulwasay/sisa-ai.git
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
