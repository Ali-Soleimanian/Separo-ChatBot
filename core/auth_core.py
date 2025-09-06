import streamlit as st
from core.database import setup_db, User

session = setup_db()

def register(username, password):
    if len(password) < 6:
        return "password_too_short"
    
    register_existing_user = session.query(User).filter_by(username=username).first()
    if register_existing_user:
        return "username_exists"
    else:
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        return True


def login(username, password):
    login_existing_user = session.query(User).filter_by(username=username, password=password).first()
    if login_existing_user:
        return True
    else:
        return False


def get_user_by_username(username):
    """Get user by username"""
    return session.query(User).filter_by(username=username).first()


def update_user_api_key(username, api_key):
    """Update user's API key"""
    user = session.query(User).filter_by(username=username).first()
    if user:
        user.api_key = api_key
        session.commit()
        return True
    return False


def get_user_api_key(username):
    """Get user's API key"""
    user = session.query(User).filter_by(username=username).first()
    if user:
        return user.api_key
    return None


def logout_user():
    """Logout user by clearing session state"""
    # Clear all session state variables
    keys_to_clear = ["loged_in", "username", "api_key", "api_error"]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]
    return True


def delete_user_account(username, password):
    """Delete user account after password confirmation"""
    if len(password) < 6:
        return "password_too_short"
    
    # Verify password before deletion
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    return "invalid_password"