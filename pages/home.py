import streamlit as st
import components.cards as cards

def render():
    # Header Banner
    st.markdown("""
        <div style='background: linear-gradient(135deg, #1E3C72 0%, #2A5298 100%); padding: 40px; border-radius: 16px; color: white; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.1);'>
            <h1 style='margin:0; font-size: 38px;'>Health & Insurance Tech</h1>
            <p style='font-size: 18px; opacity: 0.9; margin-top: 10px;'>Rule-Based Medical Insurance Premium Estimation System</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Get Started - Create Account", use_container_width=True):
            st.session_state.current_page = "register"
            st.rerun()

    st.markdown("<br><hr><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #1E3C72;'>Explore Our Protection Plans</h3>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        cards.render_tier_card("Basic", "₹5,000", ["Hospitalization Cover", "Cashless Network", "Ambulance Cover"], is_popular=False)
    with c2:
        cards.render_tier_card("Standard", "₹10,000", ["Complete Hospitalization", "Dental & Vision Care", "Critical Illness Add-on"], is_popular=True)
    with c3:
        cards.render_tier_card("Elite", "₹18,000", ["Family Floater Cover", "Worldwide Emergency", "Zero Copay Benefits"], is_popular=False)

    st.markdown("<br><br>", unsafe_allow_html=True)
    c_sub1, c_sub2, c_sub3 = st.columns([1, 2, 1])
    with c_sub2:
        if st.button("Already have an account? Sign In", use_container_width=True):
            st.session_state.current_page = "login"
            st.rerun()