import streamlit as st
import components.sidebar as sidebar

st.set_page_config(
    page_title="Health & Insurance Tech",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Energy UI & Modern CSS Overhaul
st.markdown("""
    <style>
    .main {background-color: #F4F7F6;}
    .stButton>button {
        background: linear-gradient(135deg, #0072FF 0%, #00C6FF 100%);
        color: white;
        border-radius: 8px;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 12px rgba(0, 114, 255, 0.3);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 114, 255, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session States
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""

# Render Sidebar Navigation
sidebar.render()

# Page Routing Engine
page = st.session_state.current_page

if page == "home":
    import pages.home as home
    home.render()
elif page == "register":
    import pages.register as register
    register.render()
elif page == "login":
    import pages.login as login
    login.render()
elif page == "calculator":
    import pages.calculator as calculator
    calculator.render()
elif page == "result":
    import calculator.result as result_page
    result_page.render()