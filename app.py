import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="SecureLife Insurance Portal", layout="wide")

# --- Styling ---
st.markdown("""
    <style>
    .stMetric { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Welcome"

if st.session_state.page == "Welcome":
    st.title("🛡️ SecureLife Insurance Portal")
    st.write("Professional coverage estimation powered by AI.")
    if st.button("Access Portal"): st.session_state.page = "Login"; st.rerun()

elif st.session_state.page == "Login":
    st.title("🔐 Agent Access")
    pwd = st.text_input("Enter Credentials", type="password")
    if st.button("Login"):
        if pwd == "1234": st.session_state.page = "Predictor"; st.rerun()
        else: st.error("Invalid Credentials")

elif st.session_state.page == "Predictor":
    st.title("📋 Policy Premium Estimator")
    
    with st.expander("💡 BMI Calculator"):
        h = st.number_input("Height (meters)", 1.0, 2.5, 1.7)
        w = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        st.info(f"Your BMI is: {w/(h**2):.2f}")

    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input("Age", 18, 100, 25)
        bmi = st.number_input("BMI (Use tool above)", 10.0, 50.0, 25.0)
        sex = st.selectbox("Sex", ["Male", "Female"])
    with c2:
        smoker = st.selectbox("Smoker", ["Yes", "No"])
        drinker = st.selectbox("Drinking Habit", ["Regularly", "Socially", "No"])
        exercise = st.selectbox("Exercise Frequency", ["Yes", "No", "Sometimes"])
    with c3:
        plan = st.selectbox("Policy Plan", ["Basic", "Standard", "Premium"])
        medical_cond = st.selectbox("Pre-existing Condition", ["None", "Diabetes", "Hypertension", "Asthma", "Thyroid"])

    if st.button("Generate Professional Estimate"):
        premium = 20000 + (age * 150) + (bmi * 400)
        if smoker == "Yes": premium += 25000
        if plan == "Standard": premium += 5000
        elif plan == "Premium": premium += 15000
        
        st.metric("Estimated Annual Premium", f"₹{premium:,}")
        
        # Risk Assessment
        st.subheader("Risk Analysis")
        if smoker == "Yes" or medical_cond != "None":
            st.warning("Profile: High Risk. (Additional premium applied)")
        else:
            st.success("Profile: Low Risk. (You qualify for health benefits)")
            
        # Comparison Table
        st.subheader("Plan Comparison")
        data = {"Plan": ["Basic", "Standard", "Premium"], "Coverage": ["5 Lakh", "10 Lakh", "25 Lakh"]}
        st.table(pd.DataFrame(data))

    if st.button("Logout"): st.session_state.page = "Welcome"; st.rerun()
