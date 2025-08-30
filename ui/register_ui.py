import streamlit as st
from ui.ui_functions import footer, header
from core.auth_core import register
import time



def show_register():
    regiter_result = None
    st.set_page_config(page_title="Separo Register", page_icon="media/bot profile.png")

    header()

    st.subheader("Pleas Register a new account")
    get_register_username = st.text_input("Username",autocomplete="off")
    get_register_password = st.text_input("Password",type="password", autocomplete="off")

    col1, col2 = st.columns([1, 7])

    with col1:
        if st.button('Register'):
            regiter_result = register(username=get_register_username, password=get_register_password)
    if regiter_result is not None:
        if regiter_result:
            st.success("you are registerd successfully, please login")
            time.sleep(3)
            st.session_state.show_login = True
            st.session_state.show_register = False
            st.rerun()
        else:
                st.error("username already exist")


    with col2:
        if st.button("Allready registerd? login now"):
            st.session_state.show_login = True
            st.session_state.show_register = False
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