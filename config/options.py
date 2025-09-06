import streamlit as st
from core.auth_core import get_user_api_key, update_user_api_key, logout_user, delete_user_account


def get_options():
    with st.container():
        st.markdown("#### 🔑 API Configuration")
        
        current_api_key = ""
        if st.session_state.get("loged_in") and st.session_state.get("username"):
            current_api_key = get_user_api_key(st.session_state.get("username")) or ""
        else:
            current_api_key = st.session_state.get("api_key", "")
        
        api_key = st.text_input(
            "Groq API Key", 
            value=current_api_key,
            type="password",
            help="Enter your Groq API key. This will be stored in your user profile.",
            placeholder="gsk_..."
        )
        
        if api_key:
            if st.session_state.get("loged_in") and st.session_state.get("username"):
                username = st.session_state.get("username")
                if update_user_api_key(username, api_key):
                    st.success("API key saved to your profile!")
                else:
                    st.error("Failed to save API key")
            else:
                st.session_state.api_key = api_key
                st.success("API key saved!")
        else:
            st.error("⚠️ **API Key Required** - Please enter your Groq API key to use the chat.")
            st.info("💡 **Tip:** You can get a free API key from [console.groq.com](https://console.groq.com)")
    
    st.divider()
    
    with st.container():
        st.markdown("#### Assistant Settings")
        st.markdown("**Language**")
        language_choice = st.selectbox(
            "Select Language",
            ["English", "Persian", "French", "Spanish", "German", "Italian", 
            "Portuguese", "Russian", "Chinese", "Japanese", "Korean", "Arabic",
            "Hindi", "Turkish", "Dutch", "Swedish", "Norwegian", "Danish",
            "Polish", "Czech", "Hungarian", "Greek", "Hebrew", "Thai",
            "Vietnamese", "Indonesian", "Malay", "Filipino", "Ukrainian", "Romanian"],
            index=0,
            label_visibility="collapsed"
        )
        
        st.markdown("**Model**")
        model_choice = st.selectbox(
            "Select Model",
            [
                "llama-3.3-70b-versatile",
                "llama-3.1-8b-instant",
                "openai/gpt-oss-120b"
            ],
            index=0,
            label_visibility="collapsed"
        )
        
        st.markdown("**Assistant Mode**")
        assistant_mode_choice = st.selectbox(
            "Select Personality",
            [
                "friendly",
                "professional",
                "casual",
                "enthusiastic",
                "calm",
                "witty",
                "supportive",
                "analytical",
                "creative",
                "technical"
            ],
            index=1,
            label_visibility="collapsed"
        )

    st.divider()
    
    if st.session_state.get("loged_in") and st.session_state.get("username"):
        with st.container():
            st.markdown("#### User Settings")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Logout", use_container_width=True, type="secondary"):
                    if logout_user():
                        st.success("Successfully logged out!")
                        st.rerun()
                    else:
                        st.error("Failed to logout")
            
            with col2:
                if st.button("Delete Account", use_container_width=True, type="primary"):
                    st.session_state.show_delete_confirmation = True
            
            if st.session_state.get("show_delete_confirmation", False):
                st.warning("**Danger Zone** - This action cannot be undone!")
                
                with st.form("delete_account_form"):
                    st.markdown("**Confirm Account Deletion**")                    
                    password = st.text_input(
                        "Password", 
                        type="password",
                        placeholder="Enter your password to confirm deletion"
                    )
                    
                    col_confirm, col_cancel = st.columns(2)
                    
                    with col_confirm:
                        confirm_delete = st.form_submit_button(
                            "Delete My Account", 
                            use_container_width=True,
                            type="primary"
                        )
                    
                    with col_cancel:
                        cancel_delete = st.form_submit_button(
                            "Cancel", 
                            use_container_width=True,
                            type="secondary"
                        )
                    
                    if confirm_delete and password:
                        username = st.session_state.get("username")
                        delete_result = delete_user_account(username, password)
                        if delete_result == True:
                            st.success("Account deleted successfully!")
                            logout_user()
                            st.rerun()
                        elif delete_result == "invalid_password":
                            st.error("Invalid password. Account not deleted.")
                    
                    if cancel_delete:
                        st.session_state.show_delete_confirmation = False
                        st.rerun()

    return language_choice, model_choice, assistant_mode_choice


