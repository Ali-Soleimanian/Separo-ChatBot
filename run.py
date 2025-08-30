import streamlit as st
from core.setup_llm import setup_conversation, setup_model
from ui.view import setup_page
from config.options import get_options
from core.chat import generate_message, show_chat_history, show_first_message


def main():
    setup_page()
    language_choice, model_id, assistant_mode_choice = get_options()
    llm = setup_model(model_id, assistant_mode_choice)
    conversation = setup_conversation(llm=llm)
    show_first_message(language_choice)
    setup_conversation(llm)
    show_chat_history()

    prompt = st.chat_input("Say something")
    if prompt:
    
        response = conversation.run(language=language_choice, input=prompt, mode=assistant_mode_choice)

        generate_message("user", prompt)
        generate_message("assistant", response)

main()