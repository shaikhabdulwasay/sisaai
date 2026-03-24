import streamlit as st
import ollama

# --- Page Configuration ---
st.set_page_config(page_title="SISA ai | Futuristic", layout="wide", initial_sidebar_state="expanded")

# --- Futuristic Custom Styling ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');

    /* Global Typography */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Title Styling */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 4rem;
        font-weight: 700;
        color: #ffffff;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.3);
        margin-bottom: 0rem;
        padding-top: 1rem;
    }
    
    .sub-title {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #aaaaaa;
        margin-bottom: 3rem;
        letter-spacing: 0.2em;
        text-transform: uppercase;
    }

    /* Chat Messages Glassmorphism */
    .stChatMessage {
        border-radius: 12px !important;
        padding: 1.5rem !important;
        margin-bottom: 1.5rem !important;
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5) !important;
        color: #ffffff !important;
    }
    
    .stChatMessage[data-testid="chat-message-user"] {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
    }

    /* Primary Input Field */
    [data-testid="stChatInput"] {
        background: rgba(20, 20, 20, 0.8) !important;
        backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px !important;
    }
    
    /* Make chat input text white */
    [data-testid="stChatInput"] textarea {
        color: #ffffff !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
    }
    
    .sidebar-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1.5rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    }

    /* Custom Buttons - Glow Effect */
    .stButton > button {
        background-color: transparent !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        letter-spacing: 0.05em !important;
        padding: 0.6rem 1.2rem !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        font-size: 0.85rem !important;
    }
    .stButton > button:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.4) !important;
        transform: translateY(-2px);
    }

    /* History snippets */
    .history-item {
        font-size: 0.85rem;
        color: #cccccc;
        margin-bottom: 1rem;
        padding: 0.8rem;
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-right: 3px solid rgba(255, 255, 255, 0.5); /* Accent edge */
        border-radius: 6px;
        transition: all 0.2s ease;
    }
    .history-item:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateX(2px);
    }
    .history-role {
        font-family: 'Orbitron', sans-serif;
        font-size: 0.6rem;
        text-transform: uppercase;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.4rem;
        letter-spacing: 0.1em;
    }
    
    /* Modify Spinner color */
    .stSpinner > div > div {
        border-color: rgba(255,255,255,0.2) !important;
        border-top-color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# --- App Header ---
st.markdown('<div class="main-title">SISA ai</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">System // Online</div>', unsafe_allow_html=True)

# --- Session State Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Sidebar: Settings & History ---
with st.sidebar:
    st.markdown('<div class="sidebar-title">Operations</div>', unsafe_allow_html=True)
    
    # Reset Conversation Button
    if st.button("Initialize Reset", use_container_width=True):
        st.session_state.messages = []
        if hasattr(st, "rerun"):
            st.rerun()
        else:
            st.experimental_rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-title">Data Logs</div>', unsafe_allow_html=True)
    
    # Display simplified history overview
    if not st.session_state.messages:
        st.markdown("<div style='color: #666666; font-size: 0.85rem; font-style: italic;'>Awaiting input streams...</div>", unsafe_allow_html=True)
    else:
        for msg in reversed(st.session_state.messages):
            role_text = "USER" if msg["role"] == "user" else "SISA"
            snippet = msg['content'][:60] + ("..." if len(msg['content']) > 60 else "")
            st.markdown(f"""
                <div class="history-item">
                    <div class="history-role">{role_text}</div>
                    {snippet}
                </div>
            """, unsafe_allow_html=True)

# --- Main Chat Interface ---
# Display historical messages dynamically
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input & Backend Call ---
if prompt := st.chat_input("Transmit data query..."):
    # 1. Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # 2. Add user message to session state history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 3. Display assistant placeholder, loader, and fetch response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Processing Data Stream..."):
            try:
                # Backend call to local Ollama model
                response = ollama.chat(
                    model="qwen3.5:0.8b",
                    messages=st.session_state.messages
                )
                answer = response["message"]["content"]
                message_placeholder.markdown(answer)
            except Exception as e:
                answer = f"**System Error:** Neural uplink severed. Ensure Ollama is running. ({str(e)})"
                message_placeholder.error(answer)
        
    # 4. Save assistant response to session state history
    st.session_state.messages.append({"role": "assistant", "content": answer})
    
    # Refresh to immediately update the sidebar history
    if hasattr(st, "rerun"):
        st.rerun()
    else:
        st.experimental_rerun()