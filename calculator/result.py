import streamlit as st
import plotly.express as px
import random
from datetime import datetime, timedelta

def render():
    # Retrieve data from session state
    p = st.session_state.get("p_data", {"full_name": "Valued User", "age": 25, "height": 170, "weight": 65, "blood_group": "O+"})
    m = st.session_state.get("m_data", {"diabetes": "No", "bp_level": "Normal", "previous_surgeries": "No", "family_history": "No"})
    l = st.session_state.get("l_data", {"smoker": "No", "alcohol": "No", "sleeping_hours": 7, "daily_activity": "Moderately Active"})
    i = st.session_state.get("i_data", {"plan_type": "Standard", "sum_insured": "₹10,00,000"})

    # Generate persistent Insurance ID and Validity if not already present
    if "insurance_id" not in st.session_state:
        st.session_state.insurance_id = f"HIT-INS-{random.randint(100000, 999999)}"
        st.session_state.valid_till = (datetime.now() + timedelta(days=365)).strftime("%d-%m-%Y")

    # Header section
    st.markdown(f"<h2 style='color: #1E3C72;'>📋 Comprehensive Risk & Insurance Analysis Report</h2>", unsafe_allow_html=True)
    st.markdown(f"**Customer Profile:** {p['full_name']} | **Age:** {p['age']} | **Selected Plan:** {i['plan_type']} ({i['sum_insured']})")
    st.markdown(f"**Insurance ID:** `{st.session_state.insurance_id}` | **Valid Till:** `{st.session_state.valid_till}`")
    st.markdown("---")

    # Calculations
    height_m = p["height"] / 100
    bmi = round(p["weight"] / (height_m ** 2), 2)
    
    # BMI Status & Exercise Prescription Logic
    if bmi < 18.5:
        bmi_status = "Underweight"
        exercise_plan = "🏋️‍♂️ **Hypertrophy & Strength Focus:** 3x weekly compound weight training (squats, deadlifts, push-ups) paired with caloric surplus and healthy proteins to build muscle mass safely."
    elif 18.5 <= bmi < 24.9:
        bmi_status = "Normal (Healthy)"
        exercise_plan = "🏃‍♀️ **Maintenance & Endurance Routine:** 30 minutes of moderate aerobic activity (jogging, cycling, or swimming) 5 days a week, complemented by core yoga and flexibility training."
    elif 25 <= bmi < 29.9:
        bmi_status = "Overweight"
        exercise_plan = "🔥 **Fat Loss & Cardio Shred:** 45 minutes of brisk walking, low-impact HIIT, or elliptical training 5 days a week with controlled calorie tracking."
    else:
        bmi_status = "Obese"
        exercise_plan = "🚶‍♂️ **Low-Impact Rehabilitation & Mobility:** Supervised daily 30-minute walks, water aerobics, and gentle joint mobility exercises to reduce cardiovascular strain."

    blood_tips = {
        "O+": "Focus on high-protein diets, lean meats, and intense cardiovascular conditioning.",
        "O-": "Prioritize regular vigorous physical exercise and fresh green vegetables.",
        "A+": "Thrives on vegetarian diets, yoga, tai chi, and low-stress aerobic routines.",
        "A-": "Calming exercises like yoga and meditation combined with a plant-rich diet.",
        "B+": "Balanced workouts (hiking, cycling, tennis) and moderate dairy protein intake.",
        "B-": "Structured consistency with moderate weightlifting and interval training.",
        "AB+": "A mix of calming activities (yoga) and moderate cardio workouts.",
        "AB-": "Centering exercises, swimming, and immunity-boosting antioxidant nutrition."
    }

    # Financial Cost Rules
    plan = i["plan_type"]
    base_amt = 5000 if plan == "Basic" else (10000 if plan == "Standard" else 18000)
    risk_add = 3500 if l["smoker"] == "Yes" or m["diabetes"] == "Yes" else 1000
    bmi_penalty = 1500 if bmi >= 25 or bmi < 18.5 else 0
    sleep_penalty = 1000 if l["sleeping_hours"] < 6 or l["sleeping_hours"] > 9 else 0
    activity_discount = -1000 if "Very Active" in l["daily_activity"] else 0
    
    final_premium = max(4000, base_amt + risk_add + bmi_penalty + sleep_penalty + activity_discount + (p["age"] * 20))

    # Metric Cards Display
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Final Annual Premium", f"₹{final_premium:,}")
    m2.metric("Calculated BMI", f"{bmi}", delta=bmi_status)
    m3.metric("Blood Group", p["blood_group"])
    risk_label = "Low Risk" if (risk_add == 1000 and sleep_penalty == 0) else "Moderate/High Risk"
    m4.metric("Underwriting Risk", risk_label)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Detailed Wellness & Exercise Prescription Box
    st.markdown(
        f"""
        <div style='background: linear-gradient(135deg, #E0F7FA 0%, #E8F4F8 100%); padding: 25px; border-left: 6px solid #0072FF; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.03);'>
            <h4 style='color: #0072FF; margin-top: 0;'>💡 Clinical Wellness & Action Plan</h4>
            <p><strong>Blood Group Diet & Fitness Focus ({p['blood_group']}):</strong> {blood_tips.get(p['blood_group'], 'Maintain active hydration and balanced nutrition.')}</p>
            <hr style='border: 0; border-top: 1px solid #b2ebf2;'>
            <p style='margin-bottom: 0;'><strong>Targeted Physical Routine:</strong> {exercise_plan}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Detailed Additional Breakdown Table / Metrics
    st.markdown("### 🔍 Underwriting Rule Parameter Breakdown")
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown(f"""
        - **Base Plan Cost ({plan}):** ₹{base_amt:,}
        - **Lifestyle & Medical Risk Surcharge:** ₹{risk_add:,}
        - **BMI Range Penalty Factor:** ₹{bmi_penalty:,}
        """)
    with col_d2:
        st.markdown(f"""
        - **Sleeping Hours Adjustment:** ₹{sleep_penalty:,}
        - **Activity Level Rebate:** -₹{abs(activity_discount):,}
        - **Age Multiplier Adjustment:** ₹{p['age'] * 20:,}
        - **Total Estimated Policy Valuation:** **₹{final_premium:,} / year**
        """)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Visual Analytics Charts
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        fig_cost = px.bar(
            x=["Base Plan", "Risk Factors", "BMI Rule", "Sleep Factor", "Age Multiplier"],
            y=[base_amt, risk_add, bmi_penalty, sleep_penalty, p["age"] * 20],
            labels={"x": "Cost Component", "y": "Amount (₹)"},
            title="Premium Component Contribution Chart"
        )
        st.plotly_chart(fig_cost, use_container_width=True)
        
    with col_g2:
        fig_bmi = px.pie(
            names=["Current BMI", "Optimal Health Buffer"],
            values=[bmi, max(0, 25 - bmi)],
            hole=0.6,
            title="BMI Ratio Assessment"
        )
        st.plotly_chart(fig_bmi, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Action buttons
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        if st.button("← Modify Input Parameters", use_container_width=True):
            st.session_state.current_page = "calculator"
            st.rerun()
    with col_b2:
        if st.button("🏠 Return to Dashboard Home", use_container_width=True):
            st.session_state.current_page = "home"
            st.rerun()