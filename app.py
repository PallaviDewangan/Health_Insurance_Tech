import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config & Professional CSS
st.set_page_config(page_title="SecureLife | Official Portal", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f9; }
    div.stButton > button { background-color: #003366 !important; color: white !important; border-radius: 8px !important; }
    h1, h2 { color: #003366 !important; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Welcome"

# --- PAGES ---
if st.session_state.page == "Welcome":
    st.title("🛡️ SecureLife Insurance Portal")
    if st.button("Access Portal →"): st.session_state.page = "Login"; st.rerun()

elif st.session_state.page == "Login":
    st.title("🔐 Secure Agent Login")
    pwd = st.text_input("Access Code", type="password")
    if st.button("Authenticate"):
        if pwd == "1234": st.session_state.page = "Predictor"; st.rerun()
        else: st.error("Incorrect Code.")

elif st.session_state.page == "Predictor":
    st.title("📋 Premium Estimation Portal")
    
    # BMI Calculator
    with st.expander("💡 Need to calculate your BMI?"):
        h = st.number_input("Height (m)", 1.0, 2.5, 1.7)
        w = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        st.write(f"**Your BMI is: {w/(h**2):.2f}**")

    # Inputs
    c1, c2, c3 = st.columns(3)
    with c1:
        age = st.number_input("Age", 18, 100, 25)
        bmi = st.number_input("BMI Index", 10.0, 50.0, 25.0)
        sex = st.selectbox("Gender", ["Male", "Female"])
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    with c2:
        smoker = st.selectbox("Smoker", ["Yes", "No"])
        drinker = st.selectbox("Drinking Habit", ["No", "Socially", "Regularly"])
        exercise = st.selectbox("Exercise", ["Never", "Sometimes", "Regularly"])
        children = st.slider("Number of Children", 0, 5, 0)
    with c3:
        plan = st.selectbox("Coverage Plan", ["Basic", "Standard", "Premium"])
        medical_cond = st.selectbox("Medical History", ["None", "Diabetes", "Hypertension", "Asthma"])
        submitted = st.button("Generate Official Quote")

    if submitted:
        # Calculation Logic
        plan_cost = 0
        if plan == "Standard": plan_cost = 3000
        elif plan == "Premium": plan_cost = 8000
        
        smoker_cost = 7000 if smoker == "Yes" else 0
        drinker_cost = 3000 if drinker == "Regularly" else 0
        medical_cost = 4000 if medical_cond != "None" else 0
        
        premium = 5000 + (age * 80) + (bmi * 150) + (children * 500) + smoker_cost + drinker_cost + plan_cost + medical_cost
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Final Annual Premium Quote", f"₹{premium:,}")
            # Chart
            breakdown = pd.DataFrame({
                "Category": ["Base", "Age", "Lifestyle", "Plan", "Medical"], 
                "Value": [5000, age*80, smoker_cost + drinker_cost, plan_cost, medical_cost]
            })
            fig = px.bar(breakdown, x="Category", y="Value", color="Category")
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            st.write("### Policy Summary")
            st.write(f"Your quote includes a **{plan}** plan.")
            st.table(pd.DataFrame({"Benefit": ["Hospitalization", "Ambulance", "Dental"], "Status": ["Included", "Included", "Standard"]}))

    if st.button("Logout"): st.session_state.page = "Welcome"; st.rerun()
