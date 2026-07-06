elif st.session_state.page == "Predictor":
    st.title("📋 Premium Calculation")
    
    # Inputs
    age = st.number_input("Age", 18, 100, 25)
    bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
    sex = st.selectbox("Sex", ["Male", "Female"])
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    children = st.slider("Number of Children", 0, 5, 0)
    region = st.selectbox("Region", ["North", "South", "East", "West"])
    
    if st.button("Calculate"):
        # Logic
        premium = 15000 + (age * 150) + (bmi * 400) + (children * 3000)
        if smoker == "Yes": premium += 25000
        if sex == "Female": premium -= 2000
        
        st.metric("Estimated Annual Premium", f"₹{premium:,}")
        st.session_state.last_premium = premium
        
        # Graph (Visual Insights)
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
            pdf.cell(200, 10, f"Total Estimated Premium: INR {st.session_state.last_premium:,}", ln=True)
            pdf_data = pdf.output(dest='S').encode('latin-1')
            st.download_button("Download Report Now", pdf_data, "report.pdf", "application/pdf")
