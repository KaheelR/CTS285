import streamlit as st
from components.login_form import show_login_form
from components.register_form import show_register_form
from components.dashboard_metrics import show_dashboard
from utils.state import init_session_state

# Initialize session state
init_session_state()

st.set_page_config(page_title="Citizen Wellness Portal", page_icon="🏥", layout="wide")

# Sidebar to switch between login/registration/dashboard
if st.session_state.logged_in_user:
    show_dashboard()
else:
    option = st.sidebar.radio("Go to", ["Login", "Register"])
    if option == "Login":
        show_login_form()
    else:
        show_register_form()
