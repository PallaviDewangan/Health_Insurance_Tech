import streamlit as st

def render():
    st.markdown("""
        <div style='background: linear-gradient(135deg, #1E3C72 0%, #2A5298 100%); padding: 30px; border-radius: 14px; color: white; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.1);'>
            <h1 style='margin:0; font-size: 34px;'>Health & Insurance Tech</h1>
            <p style='font-size: 16px; opacity: 0.9; margin-top: 8px;'>Rule-Based Medical Insurance Premium Estimation System</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)