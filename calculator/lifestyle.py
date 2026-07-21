import streamlit as st

def render():
    st.markdown("### 🏃‍♂️ 3. Lifestyle Details")
    col1, col2 = st.columns(2)
    with col1:
        smoker = st.selectbox("Smoking Habit", ["No", "Yes"])
        alcohol = st.selectbox("Alcohol Consumption", ["No", "Regular", "Occasional"])
    with col2:
        sleeping_hours = st.slider("Average Sleeping Hours (per night)", 3, 12, value=7)
        daily_activity = st.selectbox(
            "Daily Exercise & Activity Level", 
            [
                "Sedentary (Desk Job / Little to no exercise)", 
                "Moderately Active (Light workout 2-3 days/week)", 
                "Very Active (Daily intense gym / Athlete)"
            ]
        )
        
    return {
        "smoker": smoker,
        "alcohol": alcohol,
        "sleeping_hours": sleeping_hours,
        "daily_activity": daily_activity
    }