import streamlit as st
import random
from datetime import datetime, timedelta
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
    page_title="Health & Insurance Tech Engine",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS Styling to Remove Unwanted Sidebars & Clean UI ---
st.markdown("""
    <style>
        /* Hide default multi-page navigation list if any */
        [data-testid="stSidebarNav"] {display: none;}
        
        /* General Theme Enhancements */
        .main { background-color: #f9fbff; }
        .stButton>button {
            border-radius: 6px;
            font-weight: 600;
        }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Session State ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# --- Custom Sidebar (Only visible when logged in or for navigation) ---
with st.sidebar:
    st.markdown("<h3>🛡️ Navigation Panel</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    if st.session_state['logged_in']:
        st.markdown(f"""
            <div style="background: #e6f4ea; padding: 12px; border-radius: 6px; border-left: 4px solid #34a853; margin-bottom: 15px;">
                <p style="margin:0; font-size: 13px; color: #137333;"><b>Logged in as:</b></p>
                <p style="margin:0; font-size: 15px; color: #202124;"><b>{st.session_state['username']}</b></p>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Logout", use_container_width=True, type="secondary"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ""
            st.session_state['page'] = 'home'
            st.rerun()
        
        st.markdown("---")
        if st.button("📊 Calculator Dashboard", use_container_width=True):
            st.session_state['page'] = 'calculator'
            st.rerun()
    else:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()
        if st.button("🔑 Sign In / Register", use_container_width=True):
            st.session_state['page'] = 'auth'
            st.rerun()

current_page = st.session_state['page']

# ==================== 1. HOME PAGE ====================
if current_page == 'home':
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1f4e79 0%, #2e75b6 100%); color: white; padding: 40px; border-radius: 10px; text-align: center; margin-bottom: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <h1 style="margin: 0; font-size: 36px; font-weight: 700;">Health & Insurance Tech</h1>
            <p style="margin: 12px 0 0 0; color: #f0f4f8; font-size: 16px;">Rule-Based Medical Insurance Premium Estimation System</p>
        </div>
    """, unsafe_allow_html=True)

    col_space1, col_btn, col_space2 = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🚀 Get Started - Create Account", use_container_width=True, type="primary"):
            st.session_state['page'] = 'auth'
            st.rerun()

    st.markdown("<br><h2 style='text-align: center; color: #1f4e79;'>Explore Our Protection Plans</h2><br>", unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("""
            <div style="border: 1px solid #dcdcdc; padding: 25px; border-radius: 8px; background: white; min-height: 300px;">
                <h3 style="text-align: center; color: #1f4e79; margin-top:0;">Basic Plan</h3>
                <h2 style="text-align: center; color: #28a745; margin: 15px 0;">₹5,000 <span style="font-size: 13px; color: gray; font-weight:normal;">/year</span></h2>
                <hr style="border:none; border-top:1px solid #eee; margin: 15px 0;">
                <p style="font-size: 13px; font-weight: bold; color: #333;">Plan Benefits:</p>
                <ul style="padding-left: 18px; color: #555; font-size: 13px; line-height: 1.8;">
                    <li>Hospitalization Cover</li>
                    <li>Cashless Network</li>
                    <li>Ambulance Cover</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    with p2:
        st.markdown("""
            <div style="border: 2px solid #2e75b6; padding: 25px; border-radius: 8px; background: #f4f8fc; min-height: 300px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
                <div style="text-align: center; margin-bottom: 5px;"><span style="background: #2e75b6; color: white; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: bold;">MOST POPULAR</span></div>
                <h3 style="text-align: center; color: #1f4e79; margin-top:0;">Standard Plan</h3>
                <h2 style="text-align: center; color: #28a745; margin: 15px 0;">₹10,000 <span style="font-size: 13px; color: gray; font-weight:normal;">/year</span></h2>
                <hr style="border:none; border-top:1px solid #dcdcdc; margin: 15px 0;">
                <p style="font-size: 13px; font-weight: bold; color: #333;">Plan Benefits:</p>
                <ul style="padding-left: 18px; color: #555; font-size: 13px; line-height: 1.8;">
                    <li>Complete Hospitalization</li>
                    <li>Dental & Vision Care</li>
                    <li>Critical Illness Add-on</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    with p3:
        st.markdown("""
            <div style="border: 1px solid #dcdcdc; padding: 25px; border-radius: 8px; background: white; min-height: 300px;">
                <h3 style="text-align: center; color: #1f4e79; margin-top:0;">Elite Plan</h3>
                <h2 style="text-align: center; color: #28a745; margin: 15px 0;">₹18,000 <span style="font-size: 13px; color: gray; font-weight:normal;">/year</span></h2>
                <hr style="border:none; border-top:1px solid #eee; margin: 15px 0;">
                <p style="font-size: 13px; font-weight: bold; color: #333;">Plan Benefits:</p>
                <ul style="padding-left: 18px; color: #555; font-size: 13px; line-height: 1.8;">
                    <li>Family Floater Cover</li>
                    <li>Worldwide Emergency</li>
                    <li>Zero Copay Benefits</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c_sp1, c_btn2, c_sp2 = st.columns([1, 2, 1])
    with c_btn2:
        if st.button("Already have an account? Sign In", use_container_width=True):
            st.session_state['page'] = 'auth'
            st.rerun()

# ==================== 2 & 3. UNIFIED AUTHENTICATION (SIGN IN & REGISTER) ====================
elif current_page == 'auth':
    st.markdown("<h2 style='text-align: center; color: #1f4e79;'>🔐 Customer Portal Authentication</h2><br>", unsafe_allow_html=True)
    
    col_space1, col_main, col_space2 = st.columns([1, 1.5, 1])
    with col_main:
        auth_mode = st.radio("Choose Action", ["Sign In", "Create New Account"], horizontal=True, label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if auth_mode == "Sign In":
            st.markdown("### 🔑 Secure Customer Sign In")
            with st.form("signin_form"):
                uname = st.text_input("Username")
                pword = st.text_input("Password", type="password")
                st.markdown("<br>", unsafe_allow_html=True)
                submitted = st.form_submit_button("Sign In & Launch Calculator 🚀", use_container_width=True, type="primary")
                
                if submitted:
                    if uname.strip() and pword.strip():
                        st.session_state['logged_in'] = True
                        st.session_state['username'] = uname
                        st.session_state['page'] = 'calculator'
                        st.rerun()
                    else:
                        st.error("Please enter both username and password.")
        else:
            st.markdown("### 📝 Create Your Account")
            with st.form("register_form"):
                reg_uname = st.text_input("Choose Username")
                reg_email = st.text_input("Email Address")
                reg_pword = st.text_input("Choose Password", type="password")
                st.markdown("<br>", unsafe_allow_html=True)
                reg_submitted = st.form_submit_button("Register & Proceed 🚀", use_container_width=True, type="primary")
                
                if reg_submitted:
                    if reg_uname.strip() and reg_email.strip() and reg_pword.strip():
                        st.session_state['logged_in'] = True
                        st.session_state['username'] = reg_uname
                        st.session_state['page'] = 'calculator'
                        st.rerun()
                    else:
                        st.error("Please fill in all required registration fields.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Home", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()
# ==================== 4. BLANK CALCULATOR PAGE ====================
elif current_page == 'calculator':
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1f4e79 0%, #2e75b6 100%); color: white; padding: 25px; border-radius: 8px; text-align: center; margin-bottom: 20px;">
            <h2 style="margin:0;">⚡ Health & Insurance Tech Engine</h2>
            <p style="margin:5px 0 0 0; font-size: 14px; color: #e0e0e0;">Complete your health profile below to calculate your instant custom insurance policy and premium.</p>
        </div>
    """, unsafe_allow_html=True)
    
    with st.form("calculator_form"):
        st.markdown("### 📋 1. Personal Details")
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name", value="", placeholder="Enter your full name")
            # Using value=0 or letting user input freely with empty prompts
            age = st.number_input("Age", min_value=0, max_value=120, value=0, step=1, format="%d")
            gender = st.selectbox("Gender", ["Select Gender...", "Female", "Male", "Other"])
        with col2:
            blood_group = st.selectbox("Blood Group", ["Select Blood Group...", "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
            height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, value=0.0, format="%.1f")
            weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=0.0, format="%.1f")

        st.markdown("---")
        st.markdown("### 🩺 2. Medical Details")
        mcol1, mcol2 = st.columns(2)
        with mcol1:
            diabetes = st.selectbox("Diabetes History", ["Select...", "No", "Yes"])
            bp_status = st.selectbox("Blood Pressure Status", ["Select...", "Normal", "High", "Low"])
        with mcol2:
            surgeries = st.selectbox("History of Major Surgeries", ["Select...", "No", "Yes"])
            family_illness = st.selectbox("Family History of Critical Illness", ["Select...", "No", "Yes"])

        st.markdown("---")
        st.markdown("### 🏃 3. Lifestyle Details")
        lcol1, lcol2 = st.columns(2)
        with lcol1:
            smoking = st.selectbox("Smoking Habit", ["Select...", "No", "Yes"])
            alcohol = st.selectbox("Alcohol Consumption", ["Select...", "No", "Yes"])
        with lcol2:
            sleep_hours = st.number_input("Average Sleeping Hours (per night)", min_value=0, max_value=24, value=0)
            activity_level = st.selectbox("Daily Exercise & Activity Level", ["Select...", "Sedentary (Desk Job / Little to no exercise)", "Moderate (Light workouts 1-3 days/week)", "Active (Regular physical workouts)"])

        st.markdown("---")
        st.markdown("### 🛡️ 4. Insurance Plan and Coverage")
        icol1, icol2 = st.columns(2)
        with icol1:
            plan_tier = st.selectbox("Select Protection Plan", ["Select Plan...", "Basic Plan", "Standard Plan", "Elite Plan"])
        with icol2:
            sum_insured = st.selectbox("Coverage Amount (Sum Insured)", ["Select Amount...", "₹5,00,000", "₹10,00,000", "₹20,00,000"])

        st.markdown("<br>", unsafe_allow_html=True)
        submitted_calc = st.form_submit_button("🚀 Generate Quote & View Full Report", use_container_width=True, type="primary")
        
        if submitted_calc:
            # Validation to ensure user fills everything correctly
            if (full_name.strip() and 
                age > 0 and 
                gender != "Select Gender..." and 
                blood_group != "Select Blood Group..." and 
                height > 0 and 
                weight > 0 and
                plan_tier != "Select Plan..."):
                
                bmi = weight / ((height/100.0) ** 2)
                st.session_state['full_name'] = full_name
                st.session_state['age'] = age
                st.session_state['blood_group'] = blood_group
                st.session_state['bmi'] = round(bmi, 2)
                st.session_state['plan_tier'] = plan_tier
                st.session_state['page'] = 'result'
                st.rerun()
            else:
                st.error("⚠️ Please fill in all the required personal details, measurements, and select a valid plan before generating the report.")

# ==================== 5. RESULT DASHBOARD PAGE ====================
elif current_page == 'result':
    st.markdown("""
        <div style="background: #1f4e79; color: white; padding: 25px; border-radius: 8px; text-align: center; margin-bottom: 20px;">
            <h1 style="margin:0;">📊 Comprehensive Risk & Insurance Analysis Report</h1>
        </div>
    """, unsafe_allow_html=True)

    name = st.session_state.get('full_name', 'Client')
    age = st.session_state.get('age', 25)
    bmi = st.session_state.get('bmi', 22.5)
    bg = st.session_state.get('blood_group', 'B+')
    plan = st.session_state.get('plan_tier', 'Basic Plan')

    st.markdown(f"**Customer Profile:** {name} | **Age:** {age} | **Selected Plan:** {plan}")
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Final Annual Premium", "₹ 6,400")
    col2.metric("Calculated BMI", str(bmi))
    col3.metric("Blood Group", bg)
    col4.metric("Underwriting Risk", "Low Risk")

    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Premium Component Contribution Chart")
        fig_bar = go.Figure(data=[go.Bar(x=['Base Plan', 'Risk Factors', 'BMI Rule', 'Age Multiplier'], y=[5000, 1000, 0, 400], marker_color='#1f4e79')])
        fig_bar.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
        st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        st.subheader("BMI Ratio Assessment")
        fig_pie = go.Figure(data=[go.Pie(labels=['Current BMI', 'Optimal Health Buffer'], values=[bmi, max(0, 25-bmi)], hole=.6)])
        fig_pie.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("← Modify Input Parameters", use_container_width=True):
            st.session_state['page'] = 'calculator'
            st.rerun()
    with col_b:
        if st.button("🏠 Return to Dashboard Home", use_container_width=True, type="primary"):
            st.session_state['page'] = 'home'
            st.rerun()