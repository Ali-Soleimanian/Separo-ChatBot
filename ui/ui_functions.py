import streamlit as st

def header():
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
    st.write("")
    st.write("")



def footer():
    with st.container():
                st.markdown("""
                <style>
                body::after {
                    content: "🌱 Developed & Designed by Ali Soleimanian";
                    position: fixed;
                    bottom: 0;
                    left: 0;
                    width: 100%;
                    text-align: center;
                    font-size: 14px;
                    color: white;
                    background: #16a34a;
                    padding: 10px;
                    z-index: 9999;
                }
                </style>
                """, unsafe_allow_html=True)


