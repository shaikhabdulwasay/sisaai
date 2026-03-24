# SISA ai - The Monolith 

A stunning, high-end futuristic AI Chat interface built using Streamlit and Ollama. This application runs a local Language Model (qwen3.5:0.8b) without needing cloud API keys, providing complete privacy and a gorgeous glassmorphic dark theme.

![SISA ai Preview](.stitch/designs/0f71b9f0dac24509ac73cb627dce8faf.webp) *(Note: Add your actual screenshot here!)*

## 🚀 Features
- **Responsive & Futuristic UI:** Glassmorphism, blurred chat bubbles, and the dynamic Orbitron font.
- **Local AI Engine:** Powered by Ollama using the `qwen3.5:0.8b` model for ultra-fast, offline chat capabilities.
- **Conversation History:** Maintains memory of the current chat, easily readable from the sidebar.
- **Complete Privacy:** Your data never leaves your machine.

## 🛠️ How to Display / Share Your Work

Since this application relies on a **Local AI model (Ollama)** running on your computer, you cannot simply share a URL for someone else to use it natively. Below are your best options to display your work:

### 1. The Portfolio Route (Recommended)
Take a screen recording (video or GIF) of the app in action and upload it to this GitHub repository. This lets recruiters, friends, and clients instantly see what you built without installing anything.
- **Tool:** Use OBS Studio, Snipping Tool (Windows 11), or generic screen recorders.

### 2. The Cloud Route (Requires changes)
If you want to host this on the web (e.g., **Streamlit Community Cloud** or **Vercel**), you will need to replace the local `ollama` backend with a cloud-based API (like Groq, OpenAI, or Hugging Face). 
- *Why?* Because servers on the internet cannot access the Ollama processing running locally on your laptop!

### 3. Share the "Run Instructions" (For other developers)
Other developers can clone this repository and run it exactly as you do.

**Instructions for them:**
1. Install [Ollama](https://ollama.com/) and download the model:
   ```cmd
   ollama run qwen3.5:0.8b
   ```
2. Clone this repo, set up a Python virtual environment, and install dependencies:
   ```cmd
   pip install streamlit ollama
   ```
3. Run the app:
   ```cmd
   streamlit run test1.py
   ```
