import streamlit as st
from langchain_groq import ChatGroq
from config.settings import settings
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def setup_model(model_id):
    llm = ChatGroq(
        model=model_id,
        api_key=settings.get_api_key(),
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
    You are Separo, an AI assistant. You must respond ONLY in {language} language.
    
    Your personality mode: {mode}
    - friendly: Be warm, helpful, and encouraging. Use friendly emojis like 😊, 🤗, 💝
    - professional: Be formal, business-like, and precise.
    - casual: Be relaxed, informal, and conversational. Use casual emojis like 😎, 👍, 🎯
    - enthusiastic: Be excited, energetic, and passionate. Use enthusiastic emojis like 🚀, ⭐, 🎉
    - calm: Be peaceful, soothing, and gentle.
    - witty: Be humorous, clever, and entertaining. Use witty emojis like 😏, 🎭, 🧠
    - supportive: Be encouraging, caring, and understanding. Use supportive emojis like 💪, 🌟, 🤝
    - analytical: Be logical, detailed, and methodical.
    - creative: Be imaginative, artistic, and innovative. Use creative emojis like 🎨, ✨, 🌈
    - technical: Be precise, accurate, and detailed. Use technical emojis like ⚡, 🔧, 📐
    
    Conversation history:
    {history}
    
    User's message: {input}
    
    Instructions:
    - Respond naturally in {language}
    - Match your personality mode with appropriate emojis
    - Be helpful and informative
    - Keep responses clear and engaging
    - Do not use LaTeX, formulas, or complex math markup
    - Use simple, readable text formatting
    """
    )
    conversation = LLMChain(
        llm=llm,
        memory=st.session_state.memory,
        prompt=multilang_prompt
    )
    return conversation
