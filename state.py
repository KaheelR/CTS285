import streamlit as st

def init_session_state():
    if "users" not in st.session_state:
        st.session_state.users = {}
    if "logged_in_user" not in st.session_state:
        st.session_state.logged_in_user = None
