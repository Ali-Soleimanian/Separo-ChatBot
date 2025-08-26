import streamlit as st
from langchain_groq import ChatGroq
from config.settings import settings


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

prompt = st.chat_input("Say something")

with st.expander("Options"):
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        language_choice = st.radio("Language", ["English", "Persian", "France"], index=0)
    with col2:
        model_choice = st.radio("Model", ["llama3-70b-8192", "llama-3.1-8b-instant", "openai/gpt-oss-120b"], index=1)
    with col3:
        Temperature_choice = st.radio("Temperature", ["Low", "Medium", "High"], index=1)


if model_choice == "llama3-70b-8192":
    model_id = "llama3-70b-8192"
elif model_choice == "llama-3.1-8b-instant":
    model_id = "llama-3.1-8b-instant"
elif model_choice == "openai/gpt-oss-120b":
    model_id = "openai/gpt-oss-120b"
else:
    model_id = "openai/gpt-oss-120b"

if Temperature_choice == "Low":
    temperature_value = 0.2
elif Temperature_choice == "Medium":
    temperature_value = 0.7
elif Temperature_choice == "High":
    temperature_value = 1


llm = ChatGroq(
    model=model_id,
    api_key=settings.API_KEY,
    temperature=temperature_value,
)


if prompt:
    if language_choice == "English":
        pre_prompt = "I say any but you should answer in English: {}"
        full_prompt = pre_prompt.format(prompt)
    elif language_choice == "Persian":
        pre_prompt = "I say any but you should answer in Persian: {}"
        full_prompt = pre_prompt.format(prompt)
    elif language_choice == "France":
        pre_prompt = "I say any but you should answer in France: {}"
        full_prompt = pre_prompt.format(prompt)

    response = llm.invoke(full_prompt)
    st.chat_message("user", avatar="media/user profile.png").write(prompt)
    st.chat_message("assistant", avatar="media/bot profile.png").write(response.content)

if "first_message" not in st.session_state:
    st.session_state.first_message = True
    st.chat_message("assistant", avatar="media/bot profile.png").write("Hello, Im Separo. Im ready to help you!")

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
