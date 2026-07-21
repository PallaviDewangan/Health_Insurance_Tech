import streamlit as st

def render_tier_card(tier_name, price, features, is_popular=False):
    if is_popular:
        st.markdown(f"""
        <div style='background: #F0F7FF; border: 2px solid #0072FF; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); text-align: center;'>
            <span style='background: #0072FF; color: white; padding: 3px 8px; font-size: 10px; border-radius: 4px; font-weight: bold;'>MOST POPULAR</span>
            <h4 style='color: #1E3C72; margin-top: 10px;'>{tier_name} Plan</h4>
            <h2 style='color: #28a745;'>{price} <span style='font-size:12px;color:#666;'>/year</span></h2>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='background: white; border: 2px solid #E0E0E0; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); text-align: center;'>
            <h4 style='color: #1E3C72; margin-top: 10px;'>{tier_name} Plan</h4>
            <h2 style='color: #28a745;'>{price} <span style='font-size:12px;color:#666;'>/year</span></h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("**Plan Benefits:**")
    for f in features:
        st.markdown(f"- {f}")