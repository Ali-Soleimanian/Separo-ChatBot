import streamlit as st



def get_options():
    with st.expander("Options"):
        col1, col2, col3 = st.columns(3, gap="large")
        with col1:
            language_choice = st.radio("Language", ["English", "Persian", "French"], index=0)
        with col2:
            model_choice = st.radio("Model", ["llama3-70b-8192", "llama-3.1-8b-instant", "openai/gpt-oss-120b"], index=1)
        with col3:
            Temperature_choice = st.radio("Temperature", ["Low", "Medium", "High"], index=1)

    if Temperature_choice == "Low":
        temperature_value = 0.2
    elif Temperature_choice == "Medium":
        temperature_value = 0.7
    elif Temperature_choice == "High":
        temperature_value = 1

    return language_choice, model_choice, temperature_value


