import streamlit as st
from langchain_groq import ChatGroq
from config.settings import settings


llm = ChatGroq(
    # model="llama3-70b-8192",
    # model="llama-3.1-8b-instant",
    model="openai/gpt-oss-120b",
    api_key=settings.API_KEY,
    temperature=0.7,
)


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
""",
unsafe_allow_html=True)

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

with st.expander("Options"):

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        language_choice = st.radio("Language", ["English", "Persian", "France"], index=0)
    with col2:
        model_choice = st.radio("Model", ["llama3-70b-8192", "llama-3.1-8b-instant", "openai/gpt-oss-120b"], index=1)
    with col3:
        choice3 = st.radio("Temperature", ["Low", "Medium", "High"], index=1)



prompt = st.chat_input("Say something")
if prompt:
    response = llm.invoke(prompt)
    st.chat_message("user", avatar="media/user profile.png").write(prompt)
    st.chat_message("assistant", avatar="media/bot profile.png").write(response.content)


