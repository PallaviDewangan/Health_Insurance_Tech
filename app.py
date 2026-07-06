import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="SecureLife | Premium Portal", layout="wide")

# Custom CSS for Professional UI
st.markdown("""
    <style>
    .main-card { background-color: #ffffff; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .stMetric { background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; }
    h1 { color: #1e3d59; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Welcome"

# --- Logic ---
if st.session_state.page == "Welcome":
    st.title("🛡️ SecureLife Insurance Portal")
    st.write("Professional, Transparent, and Smart Premium Estimation.")
    if st.button("Start Assessment"): st.session_state.page = "Predictor"; st.rerun()

elif st.session_state.page == "Predictor":
    st.title("📋 Policy Premium Estimator")
    
    # BMI Section
    with st.expander("💡 Need help calculating BMI?"):
        h = st.number_input("Height (m)", 1.0, 2.5, 1.7)
        w = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        st.write(f"Your BMI: **{w/(h**2):.2f}**")

    # Input Form
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1:
            age = st.number_input("Age", 18, 100, 25)
            bmi = st.number_input("BMI Index", 10.0, 50.0, 25.0)
            sex = st.selectbox("Gender", ["Male", "Female"])
        with c2:
            smoker = st.selectbox("Smoker", ["Yes", "No"])
            exercise = st.selectbox("Exercise Frequency", ["Never", "Sometimes", "Regularly"])
            children = st.slider("Number of Children", 0, 5, 0)
        with c3:
            plan = st.selectbox("Coverage Plan", ["Basic", "Standard", "Premium"])
            medical_cond = st.selectbox("Pre-existing Condition", ["None", "Diabetes", "Hypertension", "Asthma", "Heart Disease"])
            blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        
        submitted = st.button("Calculate Professional Quote")
        st.markdown('</div>', unsafe_allow_html=True)

    if submitted:
        # Professional Pricing Model
        premium = 5000 + (age * 80) + (bmi * 150) + (children * 500)
        if smoker == "Yes": premium += 7000
        if plan == "Standard": premium += 3000
        elif plan == "Premium": premium += 8000
        if medical_cond != "None": premium += 4000
        
        st.markdown("---")
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.metric("Estimated Annual Premium", f"₹{premium:,}")
        with col_res2:
            st.subheader("Plan Comparison")
            st.table(pd.DataFrame({"Plan": ["Basic", "Standard", "Premium"], "Coverage": ["5L", "10L", "25L"]}))

    if st.button("Logout"): st.session_state.page = "Welcome"; st.rerun()
