import streamlit as st
from ui.ui_functions import footer
from core.setup_llm import setup_conversation, setup_model
from config.options import get_options
from core.chat_core import run_conversation

def setup_page():
    st.set_page_config(page_title="Separo ChatBot", page_icon="media/bot profile.png")

    st.markdown("""
    <h1 style="text-align:center; font-size:50px;">
    Welcome to <span style="
        background: linear-gradient(to right, green 25%, red);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size:57px;
    ">Separo</span> ChatBot
    </h1>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("""
    <style>
    div[role=radiogroup] > label > div:first-child {
        background-color: #22c55e !important;
        border: 2px solid #16a34a !important;
    }
    </style>
    """, unsafe_allow_html=True)

    footer()


def show_first_message(language_choice):

    if "last_language" not in st.session_state:
        st.session_state.last_language = None
    if st.session_state.last_language != language_choice:
        if language_choice == "English":
            st.chat_message("assistant", avatar="media/bot profile.png").write("Hello, Im Separo. Im ready to help you!")
        elif language_choice == "Persian":
            st.chat_message("assistant", avatar="media/bot profile.png").write("!سلام، من سپارو هستم. آماده‌ام که به شما کمک کنم")
        elif language_choice == "French":
            st.chat_message("assistant", avatar="media/bot profile.png").write("Bonjour, je suis Separo. Je suis prêt à vous aider!")


def show_message(role, content):
    if role == "user":
        st.chat_message("user", avatar="media/user profile.png").write(content)
    else:
        assistant_msg = st.chat_message("assistant", avatar="media/bot profile.png")
        if "$" in content or "\\" in content:
            assistant_msg.markdown(content, unsafe_allow_html=True)
        else:
            assistant_msg.write(content)


def show_chat_history():
    for msg in st.session_state.memory.chat_memory.messages:
        if msg.type == "human":
            show_message("user", msg.content)
        else:
            show_message("assistant", msg.content)


def run_chat():
    setup_page()
    language_choice, model_id, assistant_mode_choice = get_options()
    llm = setup_model(model_id, assistant_mode_choice)
    conversation = setup_conversation(llm=llm)
    show_first_message(language_choice)
    setup_conversation(llm)
    show_chat_history()

    prompt = st.chat_input("Say something")
    if prompt:
        response = run_conversation(conversation, language_choice, prompt, assistant_mode_choice)
        show_message("user", prompt)
        show_message("assistant", response)