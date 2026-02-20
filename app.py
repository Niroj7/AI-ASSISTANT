import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import os
import time
import PyPDF2

# -------------------------------
# LOADING API KEY
# -------------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ_API_KEY missing in .env")
    st.stop()

client = Groq(api_key=api_key)

# -------------------------------
# PAGE SETTINGS
# -------------------------------
st.set_page_config(
    page_title="Niroj AI Assistant",
    page_icon="🤖",
    layout="wide",
)

# -------------------------------
# DARK MODE UI
# -------------------------------
st.markdown("""
<style>
body { background-color: #1a1d21; color: white; }

.chat-bubble { 
    padding: 12px; 
    margin: 8px 0; 
    border-radius: 10px; 
}

.user-bubble { 
    background:#2f3e46; 
    border-left:5px solid #4FFF8F; 
}

.bot-bubble  { 
    background:#2a2f35; 
    border-left:5px solid #4F9DFF; 
}

.typing-bubble {
    background: #2a2f35;
    padding: 10px;
    border-radius: 8px;
    margin-top: 8px;
    width: 160px;
    border-left: 5px solid #4F9DFF;
    color: #9ca3af;
    font-style: italic;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# SESSION STATE
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "memory" not in st.session_state:
    st.session_state.memory = []  # last 10 interactions


# -------------------------------
# MEMORY MODE FUNCTION
# -------------------------------
def update_memory(user_msg, bot_msg):
    st.session_state.memory.append(f"User: {user_msg}\nAssistant: {bot_msg}")
    st.session_state.memory = st.session_state.memory[-10:]  # keep last 10


# -------------------------------
# PDF HANDLER
# -------------------------------
def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text() or ""
        text += extracted + "\n"
    return text


# -------------------------------
# ASK GROQ
# -------------------------------
def ask_groq():
    memory_context = "\n\n--- MEMORY CONTEXT ---\n" + "\n".join(st.session_state.memory)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are Niroj Assistant — friendly, fast, helpful."},
            {"role": "system", "content": memory_context},
            *st.session_state.messages
        ]
    )

    return response.choices[0].message.content


# -------------------------------
# SIDEBAR SHORTCUTS
# -------------------------------
st.sidebar.title("⚙️ Tools")

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.session_state.input_text = ""
    st.session_state.memory = []
    st.rerun()

st.sidebar.write("Memory Mode: **ON**")
st.sidebar.markdown("---")


# -------------------------------
# HEADER
# -------------------------------
st.markdown("<h1 style='text-align:center;'>🤖 Niroj AI Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Ask anything. I act according to your desire.</p>", unsafe_allow_html=True)


# -------------------------------
# CENTERED FILE UPLOAD
# -------------------------------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<h3 style='text-align:center;'>📤 Upload File</h3>", unsafe_allow_html=True)

    file = st.file_uploader(" ", type=["pdf", "txt", "csv"])

    if file:
        st.success("File uploaded successfully!")

        if file.type == "application/pdf":
            text = extract_pdf_text(file)
        else:
            text = file.read().decode("utf-8")

        st.session_state.messages.append(
            {"role": "user", "content": f"Analyze this file:\n{text}"}
        )

        st.info("📘 File loaded. Ask questions about it.")
        st.rerun()


# -------------------------------
# DISPLAY CHAT
# -------------------------------
for msg in st.session_state.messages:
    css_class = "user-bubble" if msg["role"] == "user" else "bot-bubble"
    st.markdown(
        f"<div class='chat-bubble {css_class}'><b>{msg['role'].upper()}</b><br>{msg['content']}</div>",
        unsafe_allow_html=True,
    )


# -------------------------------
# SEND MESSAGE FUNCTION
# -------------------------------
def send_message():
    user_msg = st.session_state.input_text

    if user_msg.strip():
        # Add user message
        st.session_state.messages.append({"role": "user", "content": user_msg})

        # Typing bubble
        typing_placeholder = st.empty()
        typing_placeholder.markdown(
            "<div class='typing-bubble'>🤖 Bot is typing...</div>",
            unsafe_allow_html=True
        )

        # Bot response
        bot_reply = ask_groq()

        # Remove typing bubble
        typing_placeholder.empty()

        # Add bot message
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

        # Update memory
        update_memory(user_msg, bot_reply)

    # Clear input field
    st.session_state.input_text = ""


# -------------------------------
# INPUT BOX (AUTO CLEAR)
# -------------------------------
st.text_input(
    "Type your message...",
    key="input_text",
    on_change=send_message
)
