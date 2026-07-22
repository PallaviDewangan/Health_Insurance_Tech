import streamlit as st
import random
from datetime import datetime, timedelta
import plotly.graph_objects as go

# --- Page Configuration ---
st.set_page_config(
    page_title="Health & Insurance Tech Engine",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Hide Default Sidebar ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
        .main { background-color: #f8f9fa; }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Session State ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

current_page = st.session_state['page']

# ==================== PAGE 1: HOME ====================
if current_page == 'home':
    st.markdown("""
        <div style="background: linear-gradient(135deg, #003366 0%, #004080 100%); color: white; padding: 40px; border-radius: 12px; text-align: center; margin-bottom: 30px;">
            <h1 style="margin: 0; font-size: 32px;">Health & Insurance Tech</h1>
            <p style="margin: 10px 0 0 0; color: #e0e0e0; font-size: 16px;">Rule-Based Medical Insurance Premium Estimation System</p>
        </div>
    """, unsafe_allow_html=True)

    col_space1, col_btn, col_space2 = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🚀 Get Started - Create Account", use_container_width=True):
            st.session_state['page'] = 'register'
            st.rerun()

    st.markdown("<br><h2 style='text-align: center;'>Explore Our Protection Plans</h2><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div style="border: 1px solid #d6d6d6; padding: 25px; border-radius: 10px; background: white; min-height: 300px;">
                <h3 style="text-align: center; color: #003366;">Basic Plan</h3>
                <h2 style="text-align: center; color: #28a745;">₹5,000 <span style="font-size: 14px; color: gray;">/year</span></h2>
                <hr>
                <p><b>Benefits:</b></p>
                <ul><li>Hospitalization Cover</li><li>Cashless Network</li><li>Ambulance Cover</li></ul>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style="border: 2px solid #0056b3; padding: 25px; border-radius: 10px; background: white; min-height: 300px;">
                <div style="text-align: center;"><span style="background: #0056b3; color: white; padding: 2px 10px; border-radius: 10px; font-size: 11px;">MOST POPULAR</span></div>
                <h3 style="text-align: center; color: #003366;">Standard Plan</h3>
                <h2 style="text-align: center; color: #28a745;">₹10,000 <span style="font-size: 14px; color: gray;">/year</span></h2>
                <hr>
                <p><b>Benefits:</b></p>
                <ul><li>Complete Hospitalization</li><li>Dental & Vision Care</li><li>Critical Illness Add-on</li></ul>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div style="border: 1px solid #d6d6d6; padding: 25px; border-radius: 10px; background: white; min-height: 300px;">
                <h3 style="text-align: center; color: #003366;">Elite Plan</h3>
                <h2 style="text-align: center; color: #28a745;">₹18,000 <span style="font-size: 14px; color: gray;">/year</span></h2>
                <hr>
                <p><b>Benefits:</b></p>
                <ul><li>Family Floater Cover</li><li>Worldwide Emergency</li><li>Zero Copay Benefits</li></ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    col_s1, col_b2, col_s2 = st.columns([1, 2, 1])
    with col_b2:
        if st.button("Already have an account? Sign In", use_container_width=True):
            st.session_state['page'] = 'login'
            st.rerun()

# ==================== PAGE 2: LOGIN ====================
elif current_page == 'login':
    st.markdown("<h2 style='text-align: center;'>🔑 Secure Customer Sign In</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            uname = st.text_input("Username")
            pword = st.text_input("Password", type="password")
            if st.form_submit_button("Sign In 🚀", use_container_width=True):
                if uname.strip() and pword.strip():
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = uname
                    st.session_state['page'] = 'calculator'
                    st.rerun()
                else:
                    st.error("Please enter credentials.")
        if st.button("← Back to Home", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()

# ==================== PAGE 3: REGISTER ====================
elif current_page == 'register':
    st.markdown("<h2 style='text-align: center;'>📝 Create Your Account</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("reg_form"):
            uname = st.text_input("Username")
            email = st.text_input("Email")
            pword = st.text_input("Password", type="password")
            if st.form_submit_button("Register Account 🚀", use_container_width=True):
                if uname.strip() and email.strip():
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = uname
                    st.session_state['page'] = 'calculator'
                    st.rerun()
                else:
                    st.error("Please fill all fields.")
        if st.button("← Back to Home", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()

# ==================== PAGE 4: CALCULATOR ====================
elif current_page == 'calculator':
    if not st.session_state['logged_in']:
        st.warning("⚠️ Please sign in first.")
        if st.button("Go to Sign In"):
            st.session_state['page'] = 'login'
            st.rerun()
    else:
        st.markdown("<div style='background: #003366; color: white; padding: 20px; border-radius: 10px; text-align: center;'><h2>⚡ Insurance Premium Calculator</h2></div><br>", unsafe_allow_html=True)
        
        with st.form("calc_form"):
            col1, col2 = st.columns(2)
            with col1:
                full_name = st.text_input("Full Name", value="")
                age = st.number_input("Age", 1, 100, 25)
                gender = st.selectbox("Gender", ["Select...", "Female", "Male", "Other"])
            with col2:
                blood_group = st.selectbox("Blood Group", ["Select...", "A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
                height = st.number_input("Height (cm)", 50.0, 250.0, 170.0)
                weight = st.number_input("Weight (kg)", 10.0, 200.0, 65.0)

            plan_tier = st.selectbox("Select Protection Plan", ["Basic Plan", "Standard Plan", "Elite Plan"])
            
            if st.form_submit_button("🚀 Generate Report", use_container_width=True):
                if full_name.strip() and gender != "Select..." and blood_group != "Select...":
                    bmi = weight / ((height/100.0) ** 2)
                    st.session_state['full_name'] = full_name
                    st.session_state['age'] = age
                    st.session_state['blood_group'] = blood_group
                    st.session_state['bmi'] = round(bmi, 2)
                    st.session_state['plan_tier'] = plan_tier
                    st.session_state['page'] = 'result'
                    st.rerun()
                else:
                    st.error("Please fill out all required fields properly.")

        if st.button("🏠 Home"):
            st.session_state['page'] = 'home'
            st.rerun()

# ==================== PAGE 5: RESULT / DASHBOARD ====================
elif current_page == 'result':
    st.markdown("""
        <div style="background: #003366; color: white; padding: 25px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
            <h1>📊 Risk & Insurance Analysis Report</h1>
        </div>
    """, unsafe_allow_html=True)

    name = st.session_state.get('full_name', 'Client')
    bmi = st.session_state.get('bmi', 22.5)
    bg = st.session_state.get('blood_group', 'B+')
    plan = st.session_state.get('plan_tier', 'Basic Plan')

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Final Premium", "₹ 6,400")
    col2.metric("Calculated BMI", str(bmi))
    col3.metric("Blood Group", bg)
    col4.metric("Risk Level", "Low Risk")

    st.markdown("---")
    
    # Graphs
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("##### Premium Component Breakdown")
        fig_bar = go.Figure(data=[go.Bar(x=['Base', 'Risk', 'BMI', 'Age'], y=[5000, 1000, 0, 400], marker_color='#0056b3')])
        fig_bar.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=250)
        st.plotly_chart(fig_bar, use_container_width=True)
    with c2:
        st.markdown("##### BMI Ratio")
        fig_pie = go.Figure(data=[go.Pie(labels=['BMI', 'Buffer'], values=[bmi, max(0, 25-bmi)], hole=.6, marker_colors=['#0056b3', '#4da6ff'])])
        fig_pie.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=250)
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("🔄 Modify Parameters", use_container_width=True):
            st.session_state['page'] = 'calculator'
            st.rerun()
    with col_b:
        if st.button("🏠 Home", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()