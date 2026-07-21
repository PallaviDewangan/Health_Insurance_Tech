import streamlit as st
import database as db

def render():
    st.markdown("<h2 style='color: #1E3C72; text-align: center;'>🔑 Secure Customer Sign In</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Access the Rule-Based Premium Estimation Engine</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form_high"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            login_btn = st.form_submit_button("Sign In & Launch Calculator 🚀", use_container_width=True)
            if login_btn:
                role = db.verify_user(username, password)
                if role:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.role = role
                    st.success("Login Successful!")
                    st.session_state.current_page = "calculator"
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Home"):
            st.session_state.current_page = "home"
            st.rerun()