import streamlit as st
import pandas as pd
import plotly.express as px

# --- Config ---
st.set_page_config(page_title="SecureLife | Official Portal", layout="wide")
st.markdown("""<style>.main-card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; }</style>""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Welcome"

# --- Page 1: Welcome ---
if st.session_state.page == "Welcome":
    st.title("🛡️ SecureLife Insurance Portal")
    st.write("Professional, Transparent, and Smart Premium Estimation.")
    if st.button("Start Assessment →"): st.session_state.page = "Login"; st.rerun()

# --- Page 2: Login ---
elif st.session_state.page == "Login":
    st.title("🔐 Agent Login")
    pwd = st.text_input("Enter Access Code", type="password")
    if st.button("Login"):
        if pwd == "1234": st.session_state.page = "Inputs"; st.rerun()
        else: st.error("Invalid Code.")

# --- Page 3: Inputs ---
elif st.session_state.page == "Inputs":
    st.title("📝 Client Details")
    
    # BMI Tool
    with st.expander("💡 BMI Calculator"):
        h = st.number_input("Height (m)", 1.0, 2.5, 1.7)
        w = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        st.write(f"**BMI: {w/(h**2):.2f}**")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.session_state.age = st.number_input("Age", 18, 100, 25)
        st.session_state.bmi = st.number_input("BMI Index", 10.0, 50.0, 25.0)
        st.session_state.sex = st.selectbox("Gender", ["Male", "Female"])
        st.session_state.blood = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    with c2:
        st.session_state.smoker = st.selectbox("Smoker?", ["No", "Yes"])
        st.session_state.drinker = st.selectbox("Drinking Habit", ["No", "Regularly"])
        st.session_state.exercise = st.selectbox("Exercise", ["Never", "Sometimes", "Regularly"])
        st.session_state.children = st.slider("Number of Children", 0, 5, 0)
    with c3:
        st.session_state.plan = st.selectbox("Coverage Plan", ["Basic", "Standard", "Premium"])
        st.session_state.medical = st.selectbox("Medical History", ["None", "Diabetes", "Hypertension"])
        if st.button("Generate Estimate →"): st.session_state.page = "Results"; st.rerun()

# --- Page 4: Results ---
elif st.session_state.page == "Results":
    st.title("📊 Analysis Results")
    
    # Precise Math: Base is 5000. Factors are added ONLY if selected.
    plan_cost = {"Basic": 0, "Standard": 3000, "Premium": 8000}
    
    premium = 5000 # Base
    premium += (st.session_state.age * 20) # Lower multiplier for base age
    premium += ((st.session_state.bmi - 18) * 50) if st.session_state.bmi > 18 else 0
    premium += (st.session_state.children * 200)
    premium += plan_cost[st.session_state.plan]
    premium += 5000 if st.session_state.smoker == "Yes" else 0
    premium += 2000 if st.session_state.drinker == "Regularly" else 0
    premium += 3000 if st.session_state.medical != "None" else 0
    
    st.metric("Annual Premium Quote", f"₹{premium:,}")
    
    # Graph Breakdown
    df = pd.DataFrame({"Factor": ["Base", "Age/BMI", "Lifestyle", "Plan", "Medical"], 
                       "Cost": [5000, (st.session_state.age*20), 
                                (5000 if st.session_state.smoker=="Yes" else 0) + (2000 if st.session_state.drinker=="Regularly" else 0), 
                                plan_cost[st.session_state.plan], 3000 if st.session_state.medical!="None" else 0]})
    fig = px.pie(df, values='Cost', names='Factor', hole=0.5)
    st.plotly_chart(fig)
    
    if st.button("← Back to Inputs"): st.session_state.page = "Inputs"; st.rerun()
