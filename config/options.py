import streamlit as st



def get_options():
    with st.expander("Options"):
        col1, col2, col3 = st.columns(3, gap="large")
        with col1:
            language_choice = st.radio("Language", ["English", "Persian", "French"], index=0)
        with col2:
            model_choice = st.radio("Model", ["llama3-70b-8192", "llama-3.1-8b-instant", "openai/gpt-oss-120b"], index=1)
        with col3:
            assistant_mode_choice = st.radio("assistant mode", ["friendly", "normal", "cool"], index=1)


    return language_choice, model_choice, assistant_mode_choice


