import streamlit as st

def render():
    st.markdown("### 🛡️ 4. Insurance Plan and Coverage")
    col1, col2 = st.columns(2)
    with col1:
        plan_type = st.selectbox("Select Protection Plan", ["Basic", "Standard", "Elite"])
    with col2:
        sum_insured = st.selectbox("Coverage Amount (Sum Insured)", ["₹5,00,000", "₹10,00,000", "₹25,00,000", "₹50,00,000"])
        
    return {
        "plan_type": plan_type,
        "sum_insured": sum_insured
    }