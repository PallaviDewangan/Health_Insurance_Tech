import streamlit as st

def render():
    st.markdown("""
        <div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
            <h2>📝 Create Your Account</h2>
            <p style="color: gray;">Health & Insurance Tech Registration Portal</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("register_form"):
            username = st.text_input("Username", placeholder="Choose a username...")
            email = st.text_input("Email Address", placeholder="Enter your email...")
            password = st.text_input("Password", type="password", placeholder="Create a secure password...")
            submitted = st.form_submit_button("Register Account 🚀", use_container_width=True)

            if submitted:
                if username.strip() and email.strip() and password.strip():
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = username
                    st.success("✅ Account created successfully!")
                    st.session_state['page'] = 'calculator'
                    st.rerun()
                else:
                    st.error("❌ Please fill out all registration fields.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Home", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()