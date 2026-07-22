import streamlit as st

def render():
    st.markdown("""
        <div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
            <h2>🔑 Secure Customer Sign In</h2>
            <p style="color: gray;">Access the Rule-Based Premium Estimation Engine</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username...")
            password = st.text_input("Password", type="password", placeholder="Enter your password...")
            submitted = st.form_submit_button("Sign In & Launch Calculator 🚀", use_container_width=True)

            if submitted:
                if username.strip() and password.strip():
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.session_state['page'] = 'calculator'
                    st.rerun()
                else:
                    st.error("❌ Please enter both username and password.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Home", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()