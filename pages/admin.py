import streamlit as st
import database as db

st.markdown("<h2 style='color: #0B4F9C;'>⚙️ Admin Control Panel</h2>", unsafe_allow_html=True)
if not st.session_state.logged_in or st.session_state.role != "admin":
    st.error("Access Denied! Admins only.")
    st.stop()

conn = db.get_connection()
import pandas as pd
df_users = pd.read_sql_query("SELECT id, username, email, role, created_at FROM users", conn)
conn.close()

st.subheader("Registered Users Database")
st.dataframe(df_users, use_container_width=True)