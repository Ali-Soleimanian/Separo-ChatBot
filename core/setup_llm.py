import streamlit as st
from langchain_groq import ChatGroq
from config.settings import settings
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def setup_model(model_id, assistant_mode_value):
    llm = ChatGroq(
        model=model_id,
        api_key=settings.API_KEY,
        temperature=0.7
    )
    return llm

def setup_conversation(llm):
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(
            input_key="input",
            memory_key="history",
            return_messages=False)

    multilang_prompt = PromptTemplate(
        input_variables=["language", "history", "input", "mode"],
        template = """
    assistant your name is Separo
    You must answer only in {language}.
    The conversation so far:
    {history}
    User said: {input}

    Do not use LaTeX, formulas, or math markup.
    Always provide clear and simple text output.
    you are {mode} use Emojis about it
    """
    )
    conversation = LLMChain(
        llm=llm,
        memory=st.session_state.memory,
        prompt=multilang_prompt
    )
    return conversation