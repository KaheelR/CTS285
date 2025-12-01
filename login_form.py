import streamlit as st
from utils.auth import validate_login

def show_login_form():
    st.header("Login")
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    if submit:
        if validate_login(username, password):
            st.session_state.logged_in_user = username
            st.success(f"Welcome back, {username}!")
        else:
            st.error("Invalid username or password.")
