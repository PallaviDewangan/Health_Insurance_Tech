import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="SecureLife | Official Portal", layout="wide", initial_sidebar_state="collapsed")

# 2. Custom Professional CSS (Modern Insurance Style)
st.markdown("""
    <style>
    /* Theme: Navy Blue and Professional White */
    .main { background-color: #f4f7f9; }
    .stApp { color: #2c3e50; }
    
    /* Card Styling */
    .css-1r6slp0 { background-color: white; border-radius: 12px; padding: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    
    /* Button Styling */
    div.stButton > button {
        background-color: #003366 !important; 
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 0.5em 2em !important;
    }
    
    /* Headers */
    h1, h2 { color: #003366 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Session State
if 'page' not in st.session_state: st.session_state.page = "Welcome"

# --- PAGES ---
if st.session_state.page == "Welcome":
    st.title("🛡️ SecureLife Insurance Portal")
    st.write("### Professional coverage estimation powered by AI.")
    st.write("---")
    st.info("Experience our transparent, secure, and smart premium calculation engine.")
    if st.button("Access Secure Portal →"): st.session_state.page = "Login"; st.rerun()

elif st.session_state.page == "Login":
    st.title("🔐 Secure Agent Login")
    pwd = st.text_input("Enter Access Code", type="password")
    if st.button("Authenticate"):
        if pwd == "1234": st.session_state.page = "Predictor"; st.rerun()
        else: st.error("Incorrect Access Code.")

elif st.session_state.page == "Predictor":
    st.title("📋 Premium Estimation Portal")
    
    with st.container():
        c1, c2, c3 = st.columns(3)
        with c1:
            age = st.number_input("Age", 18, 100, 25)
            bmi = st.number_input("BMI Index", 10.0, 50.0, 25.0)
            sex = st.selectbox("Gender", ["Male", "Female"])
        with c2:
            smoker = st.selectbox("Smoker", ["Yes", "No"])
            drinker = st.selectbox("Drinking Habit", ["No", "Socially", "Regularly"])
            exercise = st.selectbox("Exercise", ["Never", "Sometimes", "Regularly"])
        with c3:
            plan = st.selectbox("Coverage Plan", ["Basic", "Standard", "Premium"])
            medical_cond = st.selectbox("Medical History", ["None", "Diabetes", "Hypertension", "Asthma"])
            submitted = st.button("Generate Official Quote")

    if submitted:
        premium = 5000 + (age * 80) + (bmi * 150) + (7000 if smoker == "Yes" else 0) + (3000 if drinker == "Regularly" else 0)
        
        st.markdown("---")
        col_res1, col_res2 = st.columns([1, 1])
        with col_res1:
            st.metric("Final Annual Premium Quote", f"₹{premium:,}")
            # Professional Chart
            breakdown = pd.DataFrame({"Category": ["Base", "Age", "Lifestyle", "Medical"], "Value": [5000, age*80, 5000, 4000]})
            fig = px.bar(breakdown, x="Category", y="Value", color="Category", color_discrete_sequence=px.colors.qualitative.Bold)
            st.plotly_chart(fig, use_container_width=True)
            
        with col_res2:
            st.write("### Policy Summary")
            st.write(f"Your quote includes a **{plan}** plan with comprehensive coverage.")
            st.table(pd.DataFrame({"Benefit": ["Hospitalization", "Ambulance", "Dental"], "Status": ["Included", "Included", "Standard"]}))

    if st.button("Logout"): st.session_state.page = "Welcome"; st.rerun()
