import streamlit as st
from utils.auth import register_user

def show_register_form():
    # Initialize only if the key does not exist
    if "reg_username" not in st.session_state:
        st.session_state.reg_username = ""

    username = st.text_input("Username", key="reg_username")
    
    st.header("Register")
    with st.form("register_form"):
        username = st.text_input("Username", key="reg_username")
        password = st.text_input("Password", type="password", key="reg_password")
        confirm = st.text_input("Confirm Password", type="password", key="reg_confirm")
        submit = st.form_submit_button("Register")

    if submit:
        result, msg = register_user(username, password, confirm)
        if result:
            st.success(msg)
            st.session_state.reg_username = ""
            st.session_state.reg_password = ""
            st.session_state.reg_confirm = ""
        else:
            st.error(msg)
