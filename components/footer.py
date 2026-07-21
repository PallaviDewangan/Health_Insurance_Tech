import streamlit as st

def render_footer():
    st.markdown("""
        <div style="text-align: center; color: #666; margin-top: 50px; font-size: 14px;">
            <hr>
            <p>SecureLife Insurance Dashboard © 2026 | Designed for Data-Driven Decisions</p>
        </div>
    """, unsafe_allow_html=True)