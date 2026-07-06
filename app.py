import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Health Insurance AI", layout="centered")

# --- Global Styling ---
st.markdown("""
    <style>
    .stMetric { background-color: #f0f2f6; padding: 20px; border-radius: 10px; border: 1px solid #ddd; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #007bff; color: white; border: none; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- Session State Management ---
if 'page' not in st.session_state:
    st.session_state.page = "Welcome"

# --- Page 1: Welcome ---
if st.session_state.page == "Welcome":
    st.title("🏥 Health Insurance AI")
    st.write("Get started to calculate your annual premium.")
    if st.button("Get Started →"):
        st.session_state.page = "Login"
        st.rerun()

# --- Page 2: Login ---
elif st.session_state.page == "Login":
    st.title("🔐 Secure Access")
    pwd = st.text_input("Enter Access Code", type="password")
    if st.button("Login"):
        if pwd == "1234":
            st.session_state.page = "Predictor"
            st.rerun()
        else:
            st.error("Incorrect Code!")

# --- Page 3: Predictor ---
elif st.session_state.page == "Predictor":
    st.title("📋 Premium Calculation")
    age = st.number_input("Age", 18, 100, 25)
    bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    
    if st.button("Calculate"):
        premium = 15000 + (age * 150) + (bmi * 400)
        if smoker == "Yes": premium += 25000
        st.metric("Estimated Premium", f"₹{premium:,}")
        st.session_state.last_premium = premium

    if 'last_premium' in st.session_state:
        if st.button("Generate Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(200, 10, f"Premium: INR {st.session_state.last_premium:,}", ln=True)
            pdf_data = pdf.output(dest='S').encode('latin-1')
            st.download_button("Download PDF", pdf_data, "report.pdf", "application/pdf")
