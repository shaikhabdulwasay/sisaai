# SISA AI — The Monolith

> **A fully offline, privacy-first conversational AI chat application with a high-end futuristic glassmorphic UI — powered by a local LLM running entirely on your machine.**

A stunning, high-end futuristic AI Chat interface built using Streamlit and Ollama. Run a local Language Model (`qwen3.5:0.8b`) without needing any cloud API keys — keeping your data completely private behind a gorgeous glassmorphic dark theme.

> 📸 *Demo*

https://github.com/user-attachments/assets/05d487bb-1abc-4662-8c1b-a085ec0d7dd1

---

## 🌟 Project Highlights

- **100% Offline & Private** — The AI model runs locally via Ollama. No API keys, no subscriptions, no data ever sent to the cloud.
- **Production-Quality UI** — Custom multi-layer CSS theming with glassmorphism (backdrop-blur, RGBA transparency), the futuristic Orbitron display font, and polished hover/transition animations.
- **Real-Time Conversation Sidebar** — A live scrollable log of the full conversation history is displayed in the sidebar, updating after every message.
- **Robust Error Handling** — Clear, user-friendly diagnostics are surfaced when the local model server is offline, preventing silent failures.
- **Lightweight & Fast** — The `qwen3.5:0.8b` quantized model enables ultra-fast local inference even on modest hardware.
- **One-Click Reset** — Instantly wipe the conversation history and start fresh with a single button.

---

## 🚀 Features

- **Responsive & Futuristic UI** — Glassmorphism chat bubbles, blurred glass panels, and the dynamic Orbitron font for a next-generation aesthetic.
- **Local AI Engine** — Powered by Ollama using the `qwen3.5:0.8b` model for ultra-fast, fully offline conversational AI.
- **Persistent Conversation History** — Full chat history is preserved in session state and displayed in the sidebar in real time.
- **Complete Privacy** — Your data never leaves your machine. No telemetry, no cloud calls.
- **Custom Dark Theme** — Near-black background (`#0a0a0a`), pure white accents, and a consistent dark surface palette configured via `config.toml`.
- **Reactive State Management** — Streamlit `st.session_state` keeps the UI and model context perfectly in sync across rerenders.

---

## 🏗️ Architecture & Design Decisions

```
┌─────────────────────────────────────────────┐
│               Browser (UI)                  │
│  ┌──────────────┐   ┌──────────────────────┐│
│  │   Sidebar    │   │    Main Chat Area    ││
│  │  (History)   │   │ (Messages + Input)   ││
│  └──────────────┘   └──────────────────────┘│
└────────────────────┬────────────────────────┘
                     │ HTTP (localhost)
              ┌──────▼──────┐
              │  Streamlit  │  Python app server
              │   Server    │  (session state, UI rendering)
              └──────┬──────┘
                     │ Ollama Python SDK
              ┌──────▼──────┐
              │   Ollama    │  Local LLM runtime
              │  (qwen3.5)  │  (runs on your CPU/GPU)
              └─────────────┘
```

- **Frontend:** Streamlit provides a reactive Python-based web framework. All UI customization is done through injected CSS via `st.markdown(unsafe_allow_html=True)`, avoiding the need for a separate frontend framework.
- **AI Backend:** Ollama serves the quantized `qwen3.5:0.8b` model via a local REST API. The Python `ollama` SDK wraps the API calls cleanly.
- **State Management:** `st.session_state` stores the full message list, ensuring the model always receives the complete conversation context for coherent multi-turn dialogue.
- **Theming:** A `config.toml` file in `.streamlit/` sets the global dark theme, while per-component CSS overrides fine-tune individual elements (glassmorphic cards, glow effects, etc.).

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
git clone https://github.com/shaikhabdulwasay/sisaai.git
cd sisaai
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

The application lives inside the `testStreamlit/` directory (which also contains the `.streamlit/config.toml` theme file):

```bash
cd testStreamlit
streamlit run test1.py
```

Your browser will open automatically at `http://localhost:8501`. Start chatting!

---

## 🧰 Tech Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Frontend Framework | [Streamlit](https://streamlit.io/) | Reactive Python web app framework |
| AI Runtime | [Ollama](https://ollama.com/) | Local LLM server & model management |
| Language Model | Qwen 3.5 (0.8B) | Quantized on-device conversational AI |
| Language | Python 3.8+ | Application logic & Ollama SDK |
| Styling | Custom CSS | Glassmorphism, Orbitron font, animations |
| Theme Config | Streamlit `config.toml` | Global dark palette & color tokens |

---

## 🔒 Privacy & Security

SISA AI is designed with a **privacy-first** philosophy:

- All AI inference happens **locally** on your hardware via Ollama.
- No conversation data is transmitted to any external server.
- No API keys or cloud accounts are required.
- The app runs entirely within your local network (`localhost`).

---

## 🗺️ Potential Future Enhancements

- [ ] Model selector — switch between multiple locally installed Ollama models
- [ ] Persistent chat history — save and reload past conversations from disk
- [ ] Export conversation — download the chat as a `.txt` or `.md` file
- [ ] Streaming responses — display the AI's reply token-by-token as it generates
- [ ] Multi-language support — chat in languages supported by the underlying model
- [ ] System prompt customization — set a custom persona or instructions for the AI

---

## 📄 License

This project is open source. Feel free to fork, modify, and build on top of it.

---

> 💼 Want to add this project to your LinkedIn profile? See [`LINKEDIN_PROJECT.md`](./LINKEDIN_PROJECT.md) for a ready-to-paste project description, skill tags, and a LinkedIn post caption.

---

**DEVELOPED BY SHAIKH ABDUL WASAY**
