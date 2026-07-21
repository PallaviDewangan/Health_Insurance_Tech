import streamlit as st

def render():
    st.markdown("### 🩺 2. Medical Details")
    col1, col2 = st.columns(2)
    with col1:
        diabetes = st.selectbox("Diabetes History", ["No", "Yes"])
        bp_level = st.selectbox("Blood Pressure Status", ["Normal", "High / Hypertensive"])
    with col2:
        previous_surgeries = st.selectbox("History of Major Surgeries", ["No", "Yes"])
        family_history = st.selectbox("Family History of Critical Illness", ["No", "Yes"])
        
    return {
        "diabetes": diabetes,
        "bp_level": bp_level,
        "previous_surgeries": previous_surgeries,
        "family_history": family_history
    }