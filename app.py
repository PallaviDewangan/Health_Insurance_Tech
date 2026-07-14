import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SecureLife | Pro", layout="wide")

# Custom CSS for a modern "Website" feel
st.markdown("""
    <style>
    .hero { background: #003366; color: white; padding: 20px; border-radius: 10px; }
    .card { background: #ffffff; padding: 20px; border-radius: 10px; border: 1px solid #e6e6e6; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Login"

# --- LOGIN PAGE ---
if st.session_state.page == "Login":
    st.markdown("<div class='hero'><h1>SecureLife Agent Portal</h1></div>", unsafe_allow_html=True)
    if st.text_input("Access Code", type="password") == "1234":
        if st.button("Enter Dashboard"): st.session_state.page = "Dashboard"; st.rerun()

# --- MAIN DASHBOARD ---
elif st.session_state.page == "Dashboard":
    # 1. Calculation Logic (Reactive)
    plan_cost = {"Basic": 0, "Standard": 3000, "Premium": 8000}
    
    # Defaults
    if 'age' not in st.session_state: st.session_state.age = 25
    
    # --- SIDEBAR (The Results Hub) ---
    with st.sidebar:
        st.header("💰 Live Quote")
        # Logic
        premium = 5000 + (st.session_state.age * 20) + plan_cost.get(st.session_state.plan, 0)
        st.metric("Annual Premium", f"₹{premium:,}")
        st.write("---")
        st.write("### Plan Inclusions")
        st.write("✅ Hospitalization\n✅ Ambulance\n✅ Tax Benefits")
        if st.button("Logout"): st.session_state.page = "Login"; st.rerun()

    # --- MAIN CONTENT AREA ---
    st.title("Client Assessment Form")
    
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.age = st.number_input("Client Age", 18, 100, 25)
            st.session_state.plan = st.selectbox("Coverage Plan", ["Basic", "Standard", "Premium"])
            st.session_state.bmi = st.slider("BMI Index", 15, 40, 22)
        with col2:
            st.session_state.smoker = st.radio("Smoker Status", ["No", "Yes"])
            st.session_state.medical = st.selectbox("Medical Condition", ["None", "Diabetes", "Hypertension"])
        st.markdown("</div>", unsafe_allow_html=True)

    # --- CHART AREA ---
    st.subheader("Visual Analysis")
    chart_data = pd.DataFrame({"Category": ["Base", "Age", "Plan", "Lifestyle"], "Cost": [5000, st.session_state.age*20, plan_cost[st.session_state.plan], 5000 if st.session_state.smoker == "Yes" else 0]})
    fig = px.bar(chart_data, x="Category", y="Cost", color="Category")
    st.plotly_chart(fig, use_container_width=True)
