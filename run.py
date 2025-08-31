import streamlit as st
from ui.login_ui import show_login
from ui.register_ui import show_register
from ui.auth_page import main_menu
from ui.chat_ui import run_chat





def main():
    if 'show_login' not in st.session_state:
        st.session_state.show_login = False

    if 'show_register' not in st.session_state:
        st.session_state.show_register = False

    if 'loged_in' not in st.session_state:
        st.session_state.loged_in = False

    if st.session_state.show_login:
        show_login()
    elif st.session_state.show_register:
        show_register()
    elif st.session_state.loged_in:
        run_chat()
    else:
        main_menu()

main()