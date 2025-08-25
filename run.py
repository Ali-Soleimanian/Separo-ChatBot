import streamlit as st
from langchain_groq import ChatGroq
from config.settings import settings

st.set_page_config(page_title="Separo ChatBot", page_icon="media/bot profile.png")




st.markdown("""
<h1 style="text-align:center;">
Welcome to <span style="
    background: linear-gradient(to right, green 25%, red);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
            font-size:50px;
">Separo</span> ChatBot
</h1>
""",
unsafe_allow_html=True)

st.write("")
st.write("")


llm = ChatGroq(
    model="llama3-70b-8192",
    api_key=settings.API_KEY,
    temperature=0.7,
)


if prompt := st.chat_input("Say something"):
    response = llm.invoke(prompt)
    st.chat_message("user", avatar="media/user profile.png").write(prompt)
    st.chat_message("assistant", avatar="media/bot profile.png").write(response.content)

