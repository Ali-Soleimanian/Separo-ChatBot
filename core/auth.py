from core.database import setup_db, User
import streamlit as st

session = setup_db()

def register(username, password):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        st.session_state.existing_user = True
    else:
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
