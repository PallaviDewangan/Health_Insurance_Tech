import streamlit as st

st.markdown("<h2 style='color: #0B4F9C;'>👤 Customer Profile</h2>", unsafe_allow_html=True)
if not st.session_state.logged_in:
    st.warning("Please log in to view your profile.")
    st.stop()

st.markdown(f"""
<div style='background:white; padding:30px; border-radius:20px; box-shadow:0px 10px 25px rgba(0,0,0,0.08);'>
    <h3>Name : {st.session_state.username.capitalize()}</h3>
    <p><b>Age :</b> 21 Years</p>
    <p><b>Gender :</b> Female</p>
    <p><b>Policy :</b> Gold Plan</p>
    <p><b>Status :</b> <span style='color:green;'>Active</span></p>
    <p><b>Policy Number :</b> SL-2026-00045</p>
    <p><b>Valid Till :</b> 31 Dec 2027</p>
</div>
""", unsafe_allow_html=True)