import streamlit as st
from setup_llm import setup_conversation, setup_model
from view import setup_page
from options import get_options
from chat import generate_message, show_chat_history, show_first_message


def main():
    setup_page()
    language_choice, model_id, temperature_valu = get_options()
    llm = setup_model(model_id, temperature_valu)
    conversation = setup_conversation(llm=llm)
    show_first_message(language_choice)
    setup_conversation(llm)
    show_chat_history()

    prompt = st.chat_input("Say something")
    if prompt:
    
        response = conversation.run(language=language_choice, input=prompt)

        generate_message("user", prompt)
        generate_message("assistant", response)

main()