import streamlit as st
import pandas as pd
import plotly.express as px

# --- Config & Initialization ---
st.set_page_config(page_title="SecureLife | Official Portal", layout="wide")

# Initialize session state variables to avoid AttributeError
defaults = {
    'age': 25, 'bmi': 25.0, 'sex': 'Male', 'plan': 'Basic', 
    'smoker': 'No', 'medical': 'None', 'children': 0, 'page': 'Login'
}
for key, value in defaults.items():
    if key not in st.session_state: st.session_state[key] = value

# --- CSS for "Website" Feel ---
st.markdown("""
    <style>
    .card { background: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #dee2e6; }
    .hero { background: #003366; color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN PAGE ---
if st.session_state.page == "Login":
    st.markdown("<div class='hero'><h1>SecureLife Agent Portal</h1></div>", unsafe_allow_html=True)
    if st.text_input("Enter Access Code", type="password") == "1234":
        if st.button("Enter Dashboard"): st.session_state.page = "Dashboard"; st.rerun()

# --- DASHBOARD PAGE ---
elif st.session_state.page == "Dashboard":
    # 1. Sidebar (Persistent Results)
    with st.sidebar:
        st.header("💰 Live Quote")
        plan_cost = {"Basic": 0, "Standard": 3000, "Premium": 8000}
        premium = 5000 + (st.session_state.age * 20) + plan_cost.get(st.session_state.plan, 0)
        st.metric("Annual Premium", f"₹{premium:,}")
        st.write("---")
        st.write("### Policy Inclusions")
        inclusions = {"Basic": ["Hospitalization", "Ambulance"], "Standard": ["Hospitalization", "Dental"], "Premium": ["World Coverage"]}
        for item in inclusions.get(st.session_state.plan, []): st.write(f"✅ {item}")
        if st.button("Logout"): st.session_state.page = "Login"; st.rerun()

    # 2. Main Content
    st.title("Client Assessment")
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.age = st.number_input("Client Age", 18, 100, st.session_state.age)
            st.session_state.plan = st.selectbox("Coverage Plan", ["Basic", "Standard", "Premium"], index=["Basic", "Standard", "Premium"].index(st.session_state.plan))
        with col2:
            st.session_state.smoker = st.radio("Smoker Status", ["No", "Yes"], index=["No", "Yes"].index(st.session_state.smoker))
            st.session_state.children = st.number_input("Dependents", 0, 10, st.session_state.children)
        st.markdown("</div>", unsafe_allow_html=True)

    # 3. Chart
    st.subheader("Cost Breakdown")
    fig = px.bar(x=["Base", "Age", "Plan"], y=[5000, st.session_state.age*20, plan_cost.get(st.session_state.plan, 0)])
    st.plotly_chart(fig, use_container_width=True)
