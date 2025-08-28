import streamlit as st
from langchain_groq import ChatGroq
from options import get_options
from config.settings import settings
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def setup_model(model_id, temperature_value):
    llm = ChatGroq(
        model=model_id,
        api_key=settings.API_KEY,
        temperature=temperature_value,
    )
    return llm

def setup_conversation(llm):
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(
            input_key="input",
            memory_key="history",
            return_messages=False)

    multilang_prompt = PromptTemplate(
        input_variables=["language", "history", "input"],
        template = """You must answer only in {language}.
    This is the conversation so far:
    {history}
    User said: {input}
    your personl name is Separo
    Never use LaTeX, formulas, or math markup. 
    Always give clean text output only.
    """
    )
    conversation = LLMChain(
        llm=llm,
        memory=st.session_state.memory,
        prompt=multilang_prompt
    )
    return conversation