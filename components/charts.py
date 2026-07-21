import streamlit as st
import plotly.express as px

def render_insurance_chart(df):
    """Example function to render a chart for your dashboard"""
    fig = px.bar(df, x="Category", y="Premium", title="Premium Distribution")
    st.plotly_chart(fig, use_container_width=True)