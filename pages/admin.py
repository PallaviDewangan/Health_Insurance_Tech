import streamlit as st

def render():
    st.markdown("""
        <div style="background: #343a40; color: white; padding: 25px; border-radius: 10px; text-align: center; margin-bottom: 25px;">
            <h2>🛠️ Admin & System Control Panel</h2>
            <p>Restricted access: System metrics, logs, and database management.</p>
        </div>
    """, unsafe_allow_html=True)

    # Simple security check to prevent regular users from seeing admin controls
    # (You can change "admin" to match your specific admin username or role logic)
    current_user = st.session_state.get('username', '')
    is_logged_in = st.session_state.get('logged_in', False)

    # Optional: Set a password or require admin login to view
    # For extra security, you can toggle a quick password check here:
    admin_unlocked = st.session_state.get('admin_unlocked', False)

    if not admin_unlocked:
        st.warning("🔒 This is a restricted area. Please enter the admin passphrase to continue.")
        
        with st.form("admin_auth_form"):
            admin_pass = st.text_input("Admin Passphrase", type="password", placeholder="Enter admin password")
            unlock_submitted = st.form_submit_button("Unlock Admin Panel")
            
            if unlock_submitted:
                # Replace "admin123" with your secure password or backend validation check
                if admin_pass == "admin123": 
                    st.session_state['admin_unlocked'] = True
                    st.success("🔓 Access granted!")
                    st.rerun()
                else:
                    st.error("❌ Incorrect passphrase. Access denied.")
        return

    # --- ADMIN CONTENT (Only visible after unlocking) ---
    try:
        st.subheader("📊 System Performance & User Logs")
        
        # Display safe summary metrics instead of raw backend debug tracebacks
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="System Status", value="Online 🟢")
        with col2:
            st.metric(label="Active Sessions", value="1")
        with col3:
            st.metric(label="Model Version", value="v1.2.0")

        st.markdown("---")
        st.subheader("Database & File Controls")
        
        if st.button("Clear Cache / Refresh App State"):
            st.cache_data.clear()
            st.success("✨ Cache cleared successfully!")

    except Exception as e:
        # Prevent database or backend exceptions from printing raw code on the page
        st.error("⚠️ An error occurred while loading admin metrics.")

    st.markdown("---")
    if st.button("Exit Admin Panel"):
        st.session_state['admin_unlocked'] = False
        st.session_state['page'] = 'home'
        st.rerun()