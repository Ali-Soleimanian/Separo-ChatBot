import streamlit as st
from langchain_groq import ChatGroq
from config.settings import settings

st.set_page_config(page_title="Separo ChatBot", page_icon="🤖")

st.markdown(
    "<h1 style='text-align:center;'> Welcome to Separo ChatBot</h1>",
    unsafe_allow_html=True
)

user_input = st.text_area("")

llm = ChatGroq(
    model="llama3-70b-8192",
    api_key=settings.API_KEY,
    temperature=0.7,
)

if st.button("Send"):
    if user_input.strip():
        response = llm.invoke(user_input)
        st.success(response.content)
    else:
        st.warning("pleas type somthing")