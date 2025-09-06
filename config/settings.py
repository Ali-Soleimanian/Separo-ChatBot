import streamlit as st
from core.auth_core import get_user_api_key

class Settings:
    def __init__(self):
        self.API_BASE = "https://api.groq.com/openai/v1"
    
    def get_api_key(self):
        """Get API key from user database or session state"""
        if st.session_state.get("loged_in") and st.session_state.get("username"):
            username = st.session_state.get("username")
            api_key = get_user_api_key(username)
            if api_key:
                return api_key
        
        return st.session_state.get("api_key", None)

settings = Settings()