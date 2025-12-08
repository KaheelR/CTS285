import streamlit as st
from utils.auth import register_user

def show_register_form():
    st.header("Register")

    # If a successful registration happened in the previous run:
    if st.session_state.get("reg_clear", False):
        st.session_state.reg_username = ""
        st.session_state.reg_password = ""
        st.session_state.reg_confirm = ""
        del st.session_state["reg_clear"]  # important: prevents infinite clearing

    with st.form("register_form"):
        username = st.text_input("Username", key="reg_username")
        password = st.text_input("Password", type="password", key="reg_password")
        confirm = st.text_input("Confirm Password", type="password", key="reg_confirm")
        submit = st.form_submit_button("Register")

    if submit:
        result, msg = register_user(username, password, confirm)

        if result:
            st.success(msg)
            # Tell next rerun to clear inputs
            st.session_state["reg_clear"] = True
        else:
            st.error(msg)
