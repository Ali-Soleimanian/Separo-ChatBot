
import streamlit as st
from ui.login_ui import show_login
from ui.register_ui import show_register
from ui.auth_page import main_menu


if 'show_login' not in st.session_state:
    st.session_state.show_login = False

if 'show_register' not in st.session_state:
    st.session_state.show_register = False

if "existing_user" not in st.session_state:
    st.session_state.existing_user = False


def main():
    if st.session_state.show_login:
        show_login()
    elif st.session_state.show_register:
        show_register()
    else:
        main_menu()
