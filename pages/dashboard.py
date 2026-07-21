import streamlit as st
import plotly.express as px

st.markdown("<h2 style='color: #0B4F9C;'>📊 User Dashboard</h2>", unsafe_allow_html=True)
if not st.session_state.logged_in:
    st.warning("Please log in to view your dashboard personalized data.")
    st.stop()

st.success(f"Welcome back, **{st.session_state.username}**!")

c1, c2, c3 = st.columns(3)
c1.metric("Active Policies", "1")
c2.metric("Claim Eligibility", "Available 🟢")
c3.metric("Policy Health", "Excellent 98%")

st.markdown("---")
st.subheader("📈 Annual Premium Breakdown")
fig = px.bar(x=["Base Premium", "Age Factor", "BMI", "Lifestyle", "Tax"], y=[5000, 2500, 1800, 2200, 1060], labels={"x": "Category", "y": "Amount (₹)"})
st.plotly_chart(fig, use_container_width=True)