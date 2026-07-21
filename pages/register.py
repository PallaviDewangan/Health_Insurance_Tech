import streamlit as st
import database as db

def render():
    st.markdown("<h2 style='color: #1E3C72; text-align: center;'>📝 Create Your Account</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Health & Insurance Tech Registration Portal</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("reg_form_high"):
            username = st.text_input("Username", placeholder="e.g. pallavi_dev")
            email = st.text_input("Email Address", placeholder="name@example.com")
            password = st.text_input("Password", type="password", placeholder="Enter secure password")
            
            submitted = st.form_submit_button("Register Account 🚀", use_container_width=True)
            if submitted:
                if username and password:
                    success = db.register_user(username, password, email)
                    if success:
                        st.success("Account created successfully! Redirecting...")
                        st.session_state.current_page = "login"
                        st.rerun()
                    else:
                        st.error("Username already exists. Try signing in instead.")
                else:
                    st.warning("Please fill in all required fields.")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Home"):
            st.session_state.current_page = "home"
            st.rerun()