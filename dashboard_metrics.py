import streamlit as st

def show_dashboard():
    st.header(f"Welcome, {st.session_state.logged_in_user}! 👋")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Users", "134")
    col2.metric("Active Citizens", "120")
    col3.metric("Check-ins Today", "45")
    col4.metric("New Registrations", "12")

    if st.button("Logout"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
