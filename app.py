import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Health Insurance AI", layout="centered")

# --- Styling ---
st.markdown("""
    <style>
    .stMetric { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #ddd; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #007bff; color: white; border: none; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "Welcome"

# --- Main Logic ---
if st.session_state.page == "Welcome":
    st.title("🏥 Health Insurance AI")
    if st.button("Get Started →"): st.session_state.page = "Predictor"; st.rerun()

elif st.session_state.page == "Predictor":
    st.title("📋 Premium Calculation")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", 18, 100, 25)
        bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
        sex = st.selectbox("Sex", ["Male", "Female"])
        blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
        plan_type = st.selectbox("Plan Type", ["Basic", "Standard", "Premium"])
    with col2:
        smoker = st.selectbox("Smoker", ["Yes", "No"])
        exercise = st.selectbox("Exercise Regularly?", ["Yes", "No"])
        pre_existing = st.checkbox("Pre-existing Medical Condition (e.g. Diabetes)")
        children = st.slider("Number of Children", 0, 5, 0)
    
    if st.button("Calculate My Premium"):
        # Advanced Logic
        premium = 15000 + (age * 150) + (bmi * 400) + (children * 3000)
        if smoker == "Yes": premium += 25000
        if plan_type == "Standard": premium += 5000
        elif plan_type == "Premium": premium += 15000
        if exercise == "No": premium += 3000
        if pre_existing: premium += 10000
        
        st.metric("Estimated Annual Premium", f"₹{premium:,}")
        st.session_state.last_premium = premium
        st.session_state.plan_details = plan_type
        
        st.subheader("Your Health Insights")
        fig, ax = plt.subplots()
        ax.bar(['Your BMI', 'Healthy BMI'], [bmi, 25], color=['#4CAF50', '#FF5722'])
        st.pyplot(fig)
        
    # PDF Download
    if 'last_premium' in st.session_state:
        if st.button("Generate & Download PDF Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(200, 10, "Insurance Estimate Report", ln=True, align='C')
            pdf.set_font("Arial", size=12)
            pdf.ln(10)
            pdf.cell(200, 10, f"Total Estimated Premium: INR {st.session_state.last_premium:,}", ln=True)
            pdf.cell(200, 10, f"Plan Type: {st.session_state.plan_details}", ln=True)
            pdf.cell(200, 10, f"Blood Group: {blood_group}", ln=True)
            pdf_data = pdf.output(dest='S').encode('latin-1')
            st.download_button("Download Report Now", pdf_data, "report.pdf", "application/pdf")

    if st.button("Logout"): st.session_state.page = "Welcome"; st.rerun()
