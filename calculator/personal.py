import streamlit as st

def render():
    st.markdown("### 📋 1. Personal Details")
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name", value="Pallavi Dewangan")
        age = st.number_input("Age", 18, 100, value=21)
        gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    with col2:
        blood_group = st.selectbox("Blood Group", ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])
        height = st.number_input("Height (cm)", 100, 220, value=170)
        weight = st.number_input("Weight (kg)", 30, 150, value=65)
    
    return {
        "full_name": full_name,
        "age": age,
        "gender": gender,
        "blood_group": blood_group,
        "height": height,
        "weight": weight
    }