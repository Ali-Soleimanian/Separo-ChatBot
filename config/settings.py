import streamlit as st
from core.auth_core import get_user_api_key

class Settings:
    def __init__(self):
        self.API_BASE = "https://api.groq.com/openai/v1"  # Default Groq API base
    
    def get_api_key(self):
        """Get API key from user database or session state"""
        # First try to get from current logged-in user
        if st.session_state.get("loged_in") and st.session_state.get("username"):
            username = st.session_state.get("username")
            api_key = get_user_api_key(username)
            if api_key:
                return api_key
        
        # Fallback to session state (for backward compatibility)
        return st.session_state.get("api_key", None)

settings = Settings()