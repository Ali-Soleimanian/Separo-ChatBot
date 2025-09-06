import streamlit as st
from ui.ui_functions import footer, header
from core.auth_core import login
import time


def show_login():
    login_result = None
    st.set_page_config(page_title="Separo Login", page_icon="media/bot profile.png")

    header()

    st.subheader("Please login into your account")
    get_login_username = st.text_input("Username",autocomplete="off")
    get_ligin_password = st.text_input("Password",type="password", autocomplete="off")

    col1, col2 = st.columns([1, 7])

    with col1:
        if st.button('Login'):
            login_result = login(username=get_login_username, password=get_ligin_password)
    if login_result is not None:
        if login_result:
            st.session_state.show_login = False
            st.success("you are logedin successfully")
            st.session_state.loged_in = True
            st.rerun()
        else:
            st.error("credentials wrong")

    with col2:
        if st.button("Haven't registered? Register now"):
            st.session_state.show_register = True
            st.session_state.show_login = False
            st.rerun()

    st.markdown("""
    <style>
    div[role=radiogroup] > label > div:first-child {
        background-color: #22c55e !important;
        border: 2px solid #16a34a !important;
    }
    </style>
    """, unsafe_allow_html=True)

    footer()

    return get_login_username, get_ligin_password