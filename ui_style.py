import streamlit as st

def inject_custom_css():
    custom_css = """
    <style>
    /* Page background */
    .stApp {
        background-color: #0e1117;
    }

    /* Chat messages */
    .user-msg {
        background-color: #1f2937;
        color: white;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 8px;
    }

    .bot-msg {
        background-color: #111827;
        color: #9ca3af;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 8px;
        border-left: 4px solid #10b981;
    }

    /* Upload box */
    .upload-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #1f2937;
        border: 1px dashed #4b5563;
    }

    /* Input box styling */
    textarea {
        background-color: #1f2937 !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
