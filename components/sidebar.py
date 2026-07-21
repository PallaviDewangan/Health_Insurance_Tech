import streamlit as st

def render():
    with st.sidebar:
        st.markdown("### ⚡ Navigation Panel")
        st.markdown("---")
        if st.session_state.get("logged_in", False):
            st.success(f"Logged in as: **{st.session_state.get('username', 'User')}**")
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.current_page = "home"
                st.rerun()
        else:
            if st.button("🏠 Home", use_container_width=True):
                st.session_state.current_page = "home"
                st.rerun()
            if st.button("🔑 Sign In", use_container_width=True):
                st.session_state.current_page = "login"
                st.rerun()
            if st.button("📝 Register", use_container_width=True):
                st.session_state.current_page = "register"
                st.rerun()