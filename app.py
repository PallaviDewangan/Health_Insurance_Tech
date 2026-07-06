import streamlit as st
import pandas as pd

# --- Config ---
st.set_page_config(page_title="SecureLife | Official Portal", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "Welcome"

# --- Page 1: Welcome ---
if st.session_state.page == "Welcome":
    st.title("🛡️ SecureLife | Insurance Solutions")
    st.write("---")
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
    
    # BMI Calculator Link
    with st.expander("💡 Click here to calculate BMI"):
        h = st.number_input("Height (m)", 0.5, 2.5, 1.7)
        w = st.number_input("Weight (kg)", 10.0, 200.0, 70.0)
        st.write(f"**Calculated BMI:** {w/(h**2):.2f}")

    # All fields restored
    c1, c2, c3 = st.columns(3)
    with c1:
        st.session_state.age = st.number_input("Age", 18, 100, 25)
        st.session_state.bmi = st.number_input("BMI Index", 10.0, 50.0, 25.0)
        st.session_state.sex = st.selectbox("Sex", ["Male", "Female"])
        st.session_state.blood = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-"])
    with c2:
        st.session_state.smoker = st.selectbox("Smoker Status", ["No", "Yes"])
        st.session_state.drinker = st.selectbox("Alcohol Consumption", ["No", "Regularly"])
        st.session_state.exercise = st.selectbox("Exercise Frequency", ["Never", "Sometimes", "Regularly"])
    with c3:
        st.session_state.children = st.slider("Number of Dependents", 0, 5, 0)
        st.session_state.plan = st.selectbox("Coverage Tier", ["Basic", "Standard", "Premium"])
        st.session_state.medical = st.selectbox("Medical History", ["None", "Diabetes", "Hypertension"])
        
    if st.button("Process Quote Request →"): st.session_state.page = "Results"; st.rerun()

# --- Page 4: Results ---
elif st.session_state.page == "Results":
    st.title("📊 Financial Summary")
    # Calculation logic...
    plan_cost = {"Basic": 0, "Standard": 3000, "Premium": 8000}
    premium = 5000 + (st.session_state.age * 20) + plan_cost[st.session_state.plan] + \
              (5000 if st.session_state.smoker == "Yes" else 0) + \
              (2000 if st.session_state.drinker == "Regularly" else 0) + \
              (3000 if st.session_state.medical != "None" else 0)
    
    st.subheader(f"Annual Premium: ₹{premium:,}")
    if st.button("← Return to Entry"): st.session_state.page = "Inputs"; st.rerun()
