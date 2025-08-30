import streamlit as st

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

def generate_message(role, content):
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
            generate_message("user", msg.content)
        else:
            generate_message("assistant", msg.content)
