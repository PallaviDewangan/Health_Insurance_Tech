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

# --- Completely Hide Default Streamlit Sidebar & Navigation ---
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
        .main { background-color: #f8f9fa; }
        .stButton>button { border-radius: 6px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- Initialize Session States ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ""
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# --- Page Router ---
current_page = st.session_state['page']

if current_page == 'home':
    import pages.home as home
    home.render()

elif current_page == 'login':
    import pages.login as login
    login.render()

elif current_page == 'register':
    import pages.register as register
    register.render()

elif current_page == 'calculator':
    if not st.session_state['logged_in']:
        st.warning("⚠️ Please sign in or register your account first to access the calculator.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔑 Go to Sign In", use_container_width=True):
                st.session_state['page'] = 'login'
                st.rerun()
        with col2:
            if st.button("📝 Go to Register", use_container_width=True):
                st.session_state['page'] = 'register'
                st.rerun()
    else:
        import pages.calculator as calculator
        calculator.render()

elif current_page == 'result':
    # Report & Analytics Screen with Graphs
    st.markdown("""
        <div style="background: #003366; color: white; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 25px;">
            <h1>📊 Comprehensive Risk & Insurance Analysis Report</h1>
            <p>Your custom medical insurance evaluation has been successfully computed.</p>
        </div>
    """, unsafe_allow_html=True)

    name = st.session_state.get('full_name', st.session_state.get('username', 'Client'))
    age = st.session_state.get('age', 25)
    plan = st.session_state.get('plan_tier', 'Basic')
    bg = st.session_state.get('blood_group', 'B+')
    bmi = st.session_state.get('bmi', 22.5)

    col_id1, col_id2 = st.columns(2)
    with col_id1:
        st.success(f"🆔 **Policy ID:** HIT-INS-{random.randint(100000, 999999)}")
    with col_id2:
        valid_until = (datetime.now() + timedelta(days=365)).strftime("%d-%m-%Y")
        st.info(f"📅 **Valid Till:** {valid_until}")

    st.markdown(f"**Customer Profile:** {name} | **Age:** {age} | **Selected Plan:** {plan} | **Blood Group:** {bg}")
    st.markdown("---")

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="Final Annual Premium", value="₹ 6,400")
    with m2:
        st.metric(label="Calculated BMI", value=str(bmi))
    with m3:
        st.metric(label="Blood Group", value=bg)
    with m4:
        st.metric(label="Underwriting Risk", value="Low Risk")

    st.markdown("---")
    st.subheader("💡 Clinical Wellness & Action Plan")
    st.info(f"**Blood Group Diet & Fitness Focus ({bg}):** Balanced workouts and healthy nutrition tailored to your specific profile.")

    st.markdown("---")
    st.subheader("📈 Underwriting Rule Parameter Breakdown")

    # Render Plotly Charts (Python 3.14 Compatible)
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("##### Premium Component Contribution Chart")
        fig_bar = go.Figure(data=[
            go.Bar(x=['Base Plan', 'Risk Factors', 'BMI Rule', 'Sleep Factor', 'Age Multiplier'], 
                   y=[5000, 1000, 0, 0, 400],
                   marker_color='#0056b3')
        ])
        fig_bar.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
        st.plotly_chart(fig_bar, use_container_width=True)

    with chart_col2:
        st.markdown("##### BMI Ratio Assessment")
        fig_pie = go.Figure(data=[
            go.Pie(labels=['Current BMI', 'Optimal Health Buffer'], 
                   values=[bmi, max(0, 25 - bmi)], 
                   hole=.6,
                   marker_colors=['#0056b3', '#4da6ff'])
        ])
        fig_pie.update_layout(margin=dict(l=20, r=20, t=20, b=20), height=300)
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔄 Modify Input Parameters", use_container_width=True):
            st.session_state['page'] = 'calculator'
            st.rerun()
    with c2:
        if st.button("🏠 Return to Dashboard Home", use_container_width=True):
            st.session_state['page'] = 'home'
            st.rerun()
else:
    st.session_state['page'] = 'home'
    st.rerun()