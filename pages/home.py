import streamlit as st

def render():
    # Hero Banner
    st.markdown("""
        <div style="background: linear-gradient(135deg, #003366 0%, #004080 100%); color: white; padding: 40px; border-radius: 12px; text-align: center; margin-bottom: 30px;">
            <h1 style="margin: 0; font-size: 32px;">Health & Insurance Tech</h1>
            <p style="margin: 10px 0 0 0; color: #e0e0e0; font-size: 16px;">Rule-Based Medical Insurance Premium Estimation System</p>
        </div>
    """, unsafe_allow_html=True)

    # Top CTA
    col_space1, col_btn, col_space2 = st.columns([1, 2, 1])
    with col_btn:
        if st.button("🚀 Get Started - Create Account", use_container_width=True):
            st.session_state['page'] = 'register'
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Explore Our Protection Plans</h2>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # 3 Protection Plan Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style="border: 1px solid #d6d6d6; padding: 25px; border-radius: 10px; background: white; min-height: 320px;">
                <h3 style="text-align: center; color: #003366;">Basic Plan</h3>
                <h2 style="text-align: center; color: #28a745;">₹5,000 <span style="font-size: 14px; color: gray;">/year</span></h2>
                <hr style="margin: 15px 0;">
                <p><b>Plan Benefits:</b></p>
                <ul style="padding-left: 20px; font-size: 14px; color: #333;">
                    <li>Hospitalization Cover</li>
                    <li>Cashless Network</li>
                    <li>Ambulance Cover</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div style="border: 2px solid #0056b3; padding: 25px; border-radius: 10px; background: white; min-height: 320px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);">
                <div style="text-align: center;"><span style="background: #0056b3; color: white; padding: 2px 10px; border-radius: 10px; font-size: 11px; font-weight: bold;">MOST POPULAR</span></div>
                <h3 style="text-align: center; color: #003366; margin-top: 5px;">Standard Plan</h3>
                <h2 style="text-align: center; color: #28a745;">₹10,000 <span style="font-size: 14px; color: gray;">/year</span></h2>
                <hr style="margin: 15px 0;">
                <p><b>Plan Benefits:</b></p>
                <ul style="padding-left: 20px; font-size: 14px; color: #333;">
                    <li>Complete Hospitalization</li>
                    <li>Dental & Vision Care</li>
                    <li>Critical Illness Add-on</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div style="border: 1px solid #d6d6d6; padding: 25px; border-radius: 10px; background: white; min-height: 320px;">
                <h3 style="text-align: center; color: #003366;">Elite Plan</h3>
                <h2 style="text-align: center; color: #28a745;">₹18,000 <span style="font-size: 14px; color: gray;">/year</span></h2>
                <hr style="margin: 15px 0;">
                <p><b>Plan Benefits:</b></p>
                <ul style="padding-left: 20px; font-size: 14px; color: #333;">
                    <li>Family Floater Cover</li>
                    <li>Worldwide Emergency</li>
                    <li>Zero Copay Benefits</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Bottom Sign In CTA
    col_s1, col_b2, col_s2 = st.columns([1, 2, 1])
    with col_b2:
        if st.button("Already have an account? Sign In", use_container_width=True):
            st.session_state['page'] = 'login'
            st.rerun()