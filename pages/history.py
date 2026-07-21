import streamlit as st
import database as db

st.markdown("<h2 style='color: #0B4F9C;'>📜 Activity & Calculation History</h2>", unsafe_allow_html=True)
if not st.session_state.logged_in:
    st.warning("Please log in to see your history logs.")
    st.stop()

df = db.get_user_history(st.session_state.username)
if not df.empty:
    st.dataframe(df, use_container_width=True)
else:
    st.info("No history logs found yet. Run the calculator or log in to generate activity records.")