import streamlit as st
import calculator.personal as personal
import calculator.medical as medical
import calculator.lifestyle as lifestyle
import calculator.insurance as insurance

def render():
    st.markdown("""
        <div style='background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%); padding: 30px; border-radius: 12px; color: white; margin-bottom: 25px;'>
            <h2 style='margin: 0; color: white;'>⚡ Health & Insurance Tech Engine</h2>
            <p style='margin: 5px 0 0 0; opacity: 0.9;'>Complete your health profile below to calculate your instant custom insurance policy and premium.</p>
        </div>
    """, unsafe_allow_html=True)

    # Render modular sections inside nice containers
    with st.container():
        p_data = personal.render()
    
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container():
        m_data = medical.render()
        
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container():
        l_data = lifestyle.render()
        
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container():
        i_data = insurance.render()
    
    st.markdown("<br><hr><br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Generate Quote & View Full Report 🚀", use_container_width=True):
            # Save data into session state
            st.session_state.p_data = p_data
            st.session_state.m_data = m_data
            st.session_state.l_data = l_data
            st.session_state.i_data = i_data
            
            # Switch to result page
            st.session_state.current_page = "result"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Return to Home"):
        st.session_state.current_page = "home"
        st.rerun()