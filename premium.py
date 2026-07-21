"""
premium.py
Core Actuarial Calculation Engine for Guardian Health Insurance.
Computes deterministic premium estimations based on pre-defined health,
lifestyle, policy duration, and family coverage rules.
"""

import math
import json
from typing import Dict, List, Union

# ==========================================
# CONSTANTS
# ==========================================
BASE_PRICES = {
    "Basic": 5000.0,
    "Silver": 10000.0,
    "Gold": 18000.0
}

HIGH_RISK_OCCUPATIONS = {
    "Mining", "Construction", "Aviation", "Chemical Industry",
    "Firefighter", "Police", "Army", "Pilot", "Heavy Machinery", "Oil & Gas"
}

# ==========================================
# ACTUARIAL HELPER FUNCTIONS
# ==========================================

def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    """
    Calculates BMI rounded to 2 decimal places.
    Formula: BMI = weight_kg / (height_m ^ 2)
    """
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be positive, non-zero values.")
    height_m = height_cm / 100.0
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi: float) -> str:
    """
    Categorizes the BMI into CDC standard ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.99:
        return "Healthy"
    elif 25.0 <= bmi <= 29.99:
        return "Overweight"
    else:
        return "Obese"

def calculate_age_surcharge(age: int) -> float:
    """
    Determines age surcharge rate based on age brackets.
    """
    if age < 18 or age > 100:
        raise ValueError("Age must be between 18 and 100.")
    if age < 25:
        return 0.0
    elif age <= 35:
        return 0.10
    elif age <= 45:
        return 0.25
    elif age <= 55:
        return 0.50
    elif age <= 65:
        return 0.75
    else:
        return 1.00

def calculate_bmi_surcharge(category: str) -> float:
    """
    Determines BMI category surcharge rate.
    """
    if category == "Underweight":
        return 0.05
    elif category == "Healthy":
        return 0.00
    elif category == "Overweight":
        return 0.10
    elif category == "Obese":
        return 0.25
    else:
        return 0.00

def calculate_medical_surcharge(bp_systolic: int, bp_diastolic: int, 
                              diabetes: int, heart_disease: int, 
                              surgery: int) -> Dict[str, float]:
    """
    Returns dictionary of medical surcharges.
    """
    surcharges = {
        "bp": 0.15 if (bp_systolic > 140 or bp_diastolic > 90) else 0.0,
        "diabetes": 0.20 if diabetes else 0.0,
        "heart": 0.40 if heart_disease else 0.0,
        "surgery": 0.10 if surgery else 0.0
    }
    return surcharges

def calculate_lifestyle_surcharge(smoking: int, alcohol: int, 
                                sleep_hours: float, occupation: str) -> Dict[str, float]:
    """
    Returns dictionary of lifestyle surcharges.
    """
    if sleep_hours < 0 or sleep_hours > 24:
        raise ValueError("Sleep hours must be between 0 and 24 hours.")
        
    is_high_risk = occupation.strip().title() in HIGH_RISK_OCCUPATIONS
    
    surcharges = {
        "smoking": 0.30 if smoking else 0.0,
        "alcohol": 0.15 if alcohol else 0.0,
        "sleep": 0.10 if sleep_hours < 6.0 else 0.0,
        "occupation": 0.15 if is_high_risk else 0.0
    }
    return surcharges

def calculate_family_surcharge(family_members: int) -> float:
    """
    Calculates surcharge for additional family members covered.
    30% surcharge per additional member.
    """
    if family_members < 0:
        raise ValueError("Family members covered cannot be negative.")
    return family_members * 0.30

def calculate_discounts(exercise: str, existing_insurance: int, 
                        duration: int) -> Dict[str, float]:
    """
    Returns dictionary of discount rates.
    """
    has_exercise_disc = exercise.strip().title() in ["Regular", "Moderate"]
    duration_disc = 0.0
    if duration == 2:
        duration_disc = 0.05
    elif duration == 3:
        duration_disc = 0.10

    discounts = {
        "exercise": 0.05 if has_exercise_disc else 0.0,
        "loyalty": 0.05 if existing_insurance else 0.0,
        "duration": duration_disc
    }
    return discounts

def determine_risk_level(total_surcharge_percent: float) -> str:
    """
    Categorizes the health and lifestyle risk tier.
    """
    surcharge_val = total_surcharge_percent * 100.0
    if surcharge_val <= 15:
        return "Low"
    elif surcharge_val <= 40:
        return "Medium"
    elif surcharge_val <= 70:
        return "High"
    else:
        return "Critical"

def generate_recommendation(risk_level: str, bmi_category: str, smoking: int,
                           bp_systolic: int, bp_diastolic: int, diabetes: int) -> str:
    """
    Compiles a string of recommendations based on input risk parameters.
    """
    recs = []
    
    if smoking:
        recs.append("Smoking significantly increases your premium. Consider quitting to improve health and lower rates.")
    if bp_systolic > 140 or bp_diastolic > 90:
        recs.append("Maintain regular blood pressure monitoring and adopt a low-sodium diet.")
    if diabetes:
        recs.append("Routine diabetic management, sugar controls, and physician follow-ups are highly recommended.")
    if bmi_category == "Obese":
        recs.append("Weight management program and regular exercises may help reduce future health risks and premium brackets.")
    if risk_level == "Critical":
        recs.append("Critical risk tier. Comprehensive medical consultation is strongly recommended immediately.")
    
    # If no high risk markers, output standard healthy recommendation
    if not recs:
        if bmi_category == "Healthy" and risk_level == "Low":
            recs.append("Excellent health profile. Continue maintaining your active lifestyle and balanced diet.")
        else:
            recs.append("Regular routine health checkups are advised to maintain your wellness profile.")
            
    return " ".join(recs)

# ==========================================
# MAIN CALCULATION ENGINE
# ==========================================

def calculate_premium(data: Dict[str, Union[int, float, str]]) -> Dict[str, Union[int, float, str, Dict]]:
    """
    Primary engine that runs calculation rules and returns premium figures,
    risks, recommendations, and the serializable breakdown.
    """
    # 1. Parameter validations
    age = int(data.get("age", 30))
    gender = str(data.get("gender", "Male"))
    height = float(data.get("height", 170.0))
    weight = float(data.get("weight", 70.0))
    bp_systolic = int(data.get("bp_systolic", 120))
    bp_diastolic = int(data.get("bp_diastolic", 80))
    diabetes = int(data.get("diabetes", 0))
    heart_disease = int(data.get("heart_disease", 0))
    surgery = int(data.get("surgery", 0))
    smoking = int(data.get("smoking", 0))
    alcohol = int(data.get("alcohol", 0))
    exercise = str(data.get("exercise", "None"))
    sleep_hours = float(data.get("sleep_hours", 8.0))
    occupation = str(data.get("occupation", "None"))
    family_members = int(data.get("family_members", 0))
    existing_insurance = int(data.get("existing_insurance", 0))
    duration = int(data.get("duration", 1))
    plan_name = str(data.get("plan_name", "Basic"))

    if age < 18 or age > 100:
        raise ValueError("Age must be between 18 and 100.")
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive, non-zero values.")
    if sleep_hours < 0 or sleep_hours > 24:
        raise ValueError("Sleep hours must be between 0 and 24 hours.")
    if family_members < 0:
        raise ValueError("Family members covered cannot be negative.")
    if plan_name not in BASE_PRICES:
        raise ValueError(f"Invalid plan name '{plan_name}'. Must be one of {list(BASE_PRICES.keys())}.")

    # 2. Base Premium Selection
    base_premium = BASE_PRICES[plan_name]

    # 3. Calculation of BMI
    bmi = calculate_bmi(height, weight)
    bmi_category = get_bmi_category(bmi)

    # 4. Calculation of surcharges (rates)
    age_surcharge_rate = calculate_age_surcharge(age)
    bmi_surcharge_rate = calculate_bmi_surcharge(bmi_category)
    
    meds = calculate_medical_surcharge(bp_systolic, bp_diastolic, diabetes, heart_disease, surgery)
    lifestyles = calculate_lifestyle_surcharge(smoking, alcohol, sleep_hours, occupation)
    family_surcharge_rate = calculate_family_surcharge(family_members)

    total_surcharge_rate = (
        age_surcharge_rate + bmi_surcharge_rate + 
        sum(meds.values()) + sum(lifestyles.values()) + 
        family_surcharge_rate
    )

    # 5. Calculation of discounts (rates)
    discounts = calculate_discounts(exercise, existing_insurance, duration)
    total_discount_rate = sum(discounts.values())

    # 6. Apply Rates to Base Premium
    age_surcharge_amt = round(base_premium * age_surcharge_rate, 2)
    bmi_surcharge_amt = round(base_premium * bmi_surcharge_rate, 2)
    
    bp_surcharge_amt = round(base_premium * meds["bp"], 2)
    diabetes_surcharge_amt = round(base_premium * meds["diabetes"], 2)
    heart_surcharge_amt = round(base_premium * meds["heart"], 2)
    surgery_surcharge_amt = round(base_premium * meds["surgery"], 2)

    smoking_surcharge_amt = round(base_premium * lifestyles["smoking"], 2)
    alcohol_surcharge_amt = round(base_premium * lifestyles["alcohol"], 2)
    sleep_surcharge_amt = round(base_premium * lifestyles["sleep"], 2)
    occ_surcharge_amt = round(base_premium * lifestyles["occupation"], 2)
    family_surcharge_amt = round(base_premium * family_surcharge_rate, 2)

    exercise_discount_amt = round(base_premium * discounts["exercise"], 2)
    loyalty_discount_amt = round(base_premium * discounts["loyalty"], 2)
    duration_discount_amt = round(base_premium * discounts["duration"], 2)

    total_surcharges_amt = (
        age_surcharge_amt + bmi_surcharge_amt + 
        bp_surcharge_amt + diabetes_surcharge_amt + heart_surcharge_amt + surgery_surcharge_amt +
        smoking_surcharge_amt + alcohol_surcharge_amt + sleep_surcharge_amt + occ_surcharge_amt +
        family_surcharge_amt
    )
    
    total_discounts_amt = exercise_discount_amt + loyalty_discount_amt + duration_discount_amt

    # 7. Final Premium Compilation
    annual_premium = base_premium + total_surcharges_amt - total_discounts_amt
    annual_premium = max(0.0, round(annual_premium, 2))

    # Monthly Premium = (Annual Premium / 12) + 2% handling fee
    monthly_premium = round((annual_premium / 12.0) * 1.02, 2)

    # 8. Determine Risk & Recommendations
    risk_level = determine_risk_level(total_surcharge_rate)
    recommendation = generate_recommendation(risk_level, bmi_category, smoking, bp_systolic, bp_diastolic, diabetes)

    # 9. Format Breakdown Dictionary
    breakdown = {
        "Base Premium": base_premium,
        "Age Surcharge": age_surcharge_amt,
        "BMI Surcharge": bmi_surcharge_amt,
        "Blood Pressure Surcharge": bp_surcharge_amt,
        "Diabetes Surcharge": diabetes_surcharge_amt,
        "Heart Disease Surcharge": heart_surcharge_amt,
        "Surgery Surcharge": surgery_surcharge_amt,
        "Smoking Surcharge": smoking_surcharge_amt,
        "Alcohol Surcharge": alcohol_surcharge_amt,
        "Sleep Surcharge": sleep_surcharge_amt,
        "Occupation Surcharge": occ_surcharge_amt,
        "Family Surcharge": family_surcharge_amt,
        "Exercise Discount": -exercise_discount_amt,
        "Existing Insurance Discount": -loyalty_discount_amt,
        "Duration Discount": -duration_discount_amt,
        "Final Premium": annual_premium
    }

    return {
        "annual_premium": annual_premium,
        "monthly_premium": monthly_premium,
        "base_premium": base_premium,
        "bmi": bmi,
        "bmi_category": bmi_category,
        "risk_level": risk_level,
        "total_surcharge_percent": int(round(total_surcharge_rate * 100)),
        "total_discount_percent": int(round(total_discount_rate * 100)),
        "recommendation": recommendation,
        "breakdown": breakdown
    }

if __name__ == "__main__":
    # Sample Test Run
    sample_data = {
        "age": 45,
        "gender": "Male",
        "height": 175.0,
        "weight": 85.0,
        "bp_systolic": 145,
        "bp_diastolic": 95,
        "diabetes": 1,
        "heart_disease": 0,
        "surgery": 1,
        "smoking": 1,
        "alcohol": 0,
        "exercise": "Regular",
        "sleep_hours": 5.5,
        "occupation": "Construction",
        "family_members": 2,
        "existing_insurance": 1,
        "duration": 3,
        "plan_name": "Gold"
    }
    
    print("--- Running Actuarial Rule Engine Test ---")
    result = calculate_premium(sample_data)
    print(json.dumps(result, indent=4))
    print("--- Test Completed successfully ---")