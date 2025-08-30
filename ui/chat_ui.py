import streamlit as st
from ui_functions import footer

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
