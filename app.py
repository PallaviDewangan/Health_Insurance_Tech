import streamlit as st
import pandas as pd
import plotly.express as px

# --- Config & Professional CSS ---
st.set_page_config(page_title="SecureLife | Official Portal", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    h1 { color: #003366; }
    .main-card { background-color: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    div.stButton > button { background-color: #003366 !important; color: white !important; border-radius: 8px !important; width: 100%; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Login"

# --- Logic: Page Flow ---
if st.session_state.page == "Login":
    st.title("🛡️ SecureLife Insurance Portal")
    st.subheader("Login to your Agent Dashboard")
    pwd = st.text_input("Access Code", type="password")
    if st.button("Access Portal"):
        if pwd == "1234": st.session_state.page = "Inputs"; st.rerun()
        else: st.error("Invalid Code.")

elif st.session_state.page == "Inputs":
    st.title("📝 Client Details")
    st.write("Please fill in the client's information accurately.")
    
    with st.expander("💡 Need to calculate your BMI?"):
        h = st.number_input("Height (m)", 1.0, 2.5, 1.7)
        w = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        st.write(f"**Your BMI is: {w/(h**2):.2f}**")

    # Layout for inputs
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
        st.write("---")
        if st.button("Generate Estimate →"): st.session_state.page = "Results"; st.rerun()

elif st.session_state.page == "Results":
    st.title("📊 Analysis Results")
    
    # Calculation Logic
    plan_cost = {"Basic": 0, "Standard": 3000, "Premium": 8000}
    premium = 5000 + (st.session_state.age * 80) + (st.session_state.bmi * 150) + \
              (st.session_state.children * 500) + plan_cost[st.session_state.plan] + \
              (7000 if st.session_state.smoker == "Yes" else 0) + \
              (3000 if st.session_state.drinker == "Regularly" else 0) + \
              (4000 if st.session_state.medical != "None" else 0)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Annual Premium Quote", f"₹{premium:,}")
        if st.button("← Back to Inputs"): st.session_state.page = "Inputs"; st.rerun()
    with col2:
        st.subheader("Transparent Cost Breakdown")
        df = pd.DataFrame({"Factor": ["Base", "Age/BMI", "Lifestyle", "Plan", "Medical"], 
                           "Cost": [5000, (st.session_state.age*80 + st.session_state.bmi*150), 
                                    (7000 if st.session_state.smoker=="Yes" else 0) + (3000 if st.session_state.drinker=="Regularly" else 0), 
                                    plan_cost[st.session_state.plan], 4000 if st.session_state.medical!="None" else 0]})
        fig = px.pie(df, values='Cost', names='Factor', hole=0.5)
        st.plotly_chart(fig, use_container_width=True)
