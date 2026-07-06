import streamlit as st
import pandas as pd
import plotly.express as px

# --- Config ---
st.set_page_config(page_title="SecureLife | Pro", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    h1 { color: #003366; }
    .css-1r6slp0 { background-color: white; border-radius: 15px; padding: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Welcome"

# --- Pages ---
if st.session_state.page == "Welcome":
    st.title("🛡️ SecureLife Insurance Portal")
    st.write("### Enterprise-Grade Premium Estimation")
    if st.button("Enter Portal →"): st.session_state.page = "Login"; st.rerun()

elif st.session_state.page == "Login":
    st.title("🔐 Secure Agent Access")
    pwd = st.text_input("Access Code", type="password")
    if st.button("Login"):
        if pwd == "1234": st.session_state.page = "Predictor"; st.rerun()
        else: st.error("Access Denied.")

elif st.session_state.page == "Predictor":
    st.title("📋 Premium Estimation Dashboard")
    
    # Inputs in Sidebar for a CLEAN main view
    with st.sidebar:
        st.header("Client Details")
        age = st.number_input("Age", 18, 100, 25)
        bmi = st.number_input("BMI Index", 10.0, 50.0, 25.0)
        sex = st.selectbox("Gender", ["Male", "Female"])
        plan = st.selectbox("Plan Tier", ["Basic", "Standard", "Premium"])
        smoker = st.radio("Smoker?", ["No", "Yes"])
        drinker = st.radio("Drink Alcohol?", ["No", "Regularly"])
        children = st.slider("Children", 0, 5, 0)
        medical_cond = st.selectbox("Medical History", ["None", "Diabetes", "Hypertension"])

    # Main Dashboard Logic
    # Math: Base 5000 + minor weighted factors
    plan_cost = {"Basic": 0, "Standard": 2000, "Premium": 5000}
    premium = 5000 + (age * 50) + (bmi * 100) + (children * 300) + plan_cost[plan] + (5000 if smoker == "Yes" else 0) + (2000 if drinker == "Regularly" else 0)

    # UI Layout
    col1, col2 = st.columns([1, 1])
    with col1:
        st.metric("Annual Premium", f"₹{premium:,}")
        st.write("---")
        st.subheader("Transparent Breakdown")
        df = pd.DataFrame({"Factor": ["Base", "Age/BMI", "Lifestyle", "Plan Tier", "Dependents"], 
                           "Cost": [5000, (age*50 + bmi*100), (7000 if smoker=="Yes" else 0) + (2000 if drinker=="Regularly" else 0), plan_cost[plan], children*300]})
        fig = px.pie(df, values='Cost', names='Factor', hole=0.4, color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("Policy Benefits")
        st.info(f"You have selected the **{plan} Plan**.")
        st.write("✅ Worldwide Coverage\n✅ Cashless Hospitalization\n✅ 24/7 Support")
        if st.button("Download Policy Brochure"): st.success("Downloading...")

    if st.sidebar.button("Exit Portal"): st.session_state.page = "Welcome"; st.rerun()
