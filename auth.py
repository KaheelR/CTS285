import streamlit as st

def register_user(username, password, confirm):
    if not username.strip():
        return False, "Username cannot be empty."
    if username in st.session_state.users:
        return False, "Username already exists."
    if len(password) < 4:
        return False, "Password must be at least 4 characters."
    if password != confirm:
        return False, "Passwords do not match."

    st.session_state.users[username] = password
    return True, f"Account created for {username}!"

def validate_login(username, password):
    return username in st.session_state.users and st.session_state.users[username] == password
