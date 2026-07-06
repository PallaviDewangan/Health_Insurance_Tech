import streamlit as st
import pandas as pd

# --- Config ---
st.set_page_config(page_title="SecureLife | Official Portal", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    h1 { color: #003366; }
    .metric-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #003366; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Welcome"

# --- Page 1: Welcome (Corporate Style) ---
if st.session_state.page == "Welcome":
    st.title("🛡️ SecureLife | Insurance Solutions")
    st.write("---")
    st.subheader("Welcome to the SecureLife Agent Portal.")
    st.write("Streamline your premium calculations and manage client policy requests through our secure infrastructure.")
    if st.button("Proceed to Authentication →"): st.session_state.page = "Login"; st.rerun()

# --- Page 2: Login ---
elif st.session_state.page == "Login":
    st.title("🔐 SecureLife Agent Login")
    pwd = st.text_input("Enter Access Code", type="password")
    if st.button("Access Portal"):
        if pwd == "1234": st.session_state.page = "Inputs"; st.rerun()
        else: st.error("Invalid Code.")

# --- Page 3: Inputs ---
elif st.session_state.page == "Inputs":
    st.title("📝 Client Policy Data Entry")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.session_state.age = st.number_input("Age", 18, 100, 25)
        st.session_state.bmi = st.number_input("BMI Index", 10.0, 50.0, 25.0)
        st.session_state.blood = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-"])
    with c2:
        st.session_state.smoker = st.selectbox("Smoker Status", ["No", "Yes"])
        st.session_state.drinker = st.selectbox("Alcohol Consumption", ["No", "Regularly"])
        st.session_state.children = st.slider("Dependents", 0, 5, 0)
    with c3:
        st.session_state.plan = st.selectbox("Coverage Tier", ["Basic", "Standard", "Premium"])
        st.session_state.medical = st.selectbox("Medical History", ["None", "Diabetes", "Hypertension"])
        if st.button("Process Quote Request →"): st.session_state.page = "Results"; st.rerun()

# --- Page 4: Results ---
elif st.session_state.page == "Results":
    st.title("📊 Financial Summary")
    plan_cost = {"Basic": 0, "Standard": 3000, "Premium": 8000}
    base = 5000
    age_cost = st.session_state.age * 20
    lifestyle = (5000 if st.session_state.smoker == "Yes" else 0) + (2000 if st.session_state.drinker == "Regularly" else 0)
    medical = 3000 if st.session_state.medical != "None" else 0
    premium = base + age_cost + lifestyle + medical + plan_cost[st.session_state.plan]
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"<div class='metric-card'><h3>Annual Premium</h3><h2>₹{premium:,}</h2></div>", unsafe_allow_html=True)
        if st.button("← Return to Entry"): st.session_state.page = "Inputs"; st.rerun()
        
    with col2:
        st.subheader("Coverage Breakdown")
        st.table(pd.DataFrame({
            "Component": ["Base Coverage", "Age/BMI Adjustment", "Lifestyle Assessment", "Plan Selection", "Medical History"],
            "Amount (₹)": [base, age_cost, lifestyle, plan_cost[st.session_state.plan], medical]
        }))
