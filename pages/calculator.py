import streamlit as st

def render():
    st.markdown("""
        <div style="background: linear-gradient(135deg, #003366 0%, #004080 100%); color: white; padding: 30px; border-radius: 12px; text-align: center; margin-bottom: 25px;">
            <h1 style="margin: 0; font-size: 26px;">⚡ Health & Insurance Tech Engine</h1>
            <p style="margin: 5px 0 0 0; color: #e0e0e0;">Complete your health profile below to calculate your instant custom insurance policy and premium.</p>
        </div>
    """, unsafe_allow_html=True)

    with st.form("calculator_form"):
        # 1. Personal Details
        st.subheader("📋 1. Personal Details")
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name", value="", placeholder="Enter your full name...")
            age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)
            gender = st.selectbox("Gender", ["Select Gender...", "Female", "Male", "Other"])
        with col2:
            blood_group = st.selectbox("Blood Group", ["Select Blood Group...", "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
            height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.5)
            weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=65.0, step=0.5)

        st.markdown("---")

        # 2. Medical Details
        st.subheader("🩺 2. Medical Details")
        mcol1, mcol2 = st.columns(2)
        with mcol1:
            diabetes = st.selectbox("Diabetes History", ["No", "Pre-Diabetes", "Type 1", "Type 2"])
            bp_status = st.selectbox("Blood Pressure Status", ["Normal", "Pre-Hypertension", "Hypertension"])
        with mcol2:
            surgeries = st.selectbox("History of Major Surgeries", ["No", "Yes"])
            family_illness = st.selectbox("Family History of Critical Illness", ["No", "Yes"])

        st.markdown("---")

        # 3. Lifestyle Details
        st.subheader("🏃 3. Lifestyle Details")
        lcol1, lcol2 = st.columns(2)
        with lcol1:
            smoking = st.selectbox("Smoking Habit", ["No", "Occasional", "Regular"])
            alcohol = st.selectbox("Alcohol Consumption", ["No", "Social", "Regular"])
        with lcol2:
            sleep_hours = st.slider("Average Sleeping Hours (per night)", 1, 12, 7)
            activity = st.selectbox("Daily Exercise & Activity Level", ["Sedentary (Desk Job / Little to no exercise)", "Moderate (Light workouts 1-3 days/week)", "Active (Regular daily exercise)"])

        st.markdown("---")

        # 4. Insurance Plan and Coverage
        st.subheader("📑 4. Insurance Plan and Coverage")
        icol1, icol2 = st.columns(2)
        with icol1:
            plan_tier = st.selectbox("Select Protection Plan", ["Basic Plan", "Standard Plan", "Elite Plan"])
        with icol2:
            coverage_amount = st.selectbox("Coverage Amount (Sum Insured)", ["₹5,000,000", "₹10,000,000", "₹25,000,000"])

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🚀 Generate Quote & View Full Report", use_container_width=True)

        if submitted:
            if not full_name.strip():
                st.error("❌ Please enter your Full Name.")
            elif gender == "Select Gender...":
                st.error("❌ Please select your Gender.")
            elif blood_group == "Select Blood Group...":
                st.error("❌ Please select your Blood Group.")
            else:
                height_m = height / 100.0
                bmi_val = weight / (height_m ** 2)

                st.session_state['full_name'] = full_name
                st.session_state['age'] = age
                st.session_state['gender'] = gender
                st.session_state['blood_group'] = blood_group
                st.session_state['bmi'] = round(bmi_val, 2)
                st.session_state['plan_tier'] = plan_tier
                st.session_state['coverage'] = coverage_amount
                
                st.session_state['page'] = 'result'
                st.rerun()

    st.markdown("---")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state['page'] = 'home'
        st.rerun()