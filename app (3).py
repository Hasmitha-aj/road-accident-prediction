
import streamlit as st
import numpy as np

st.title("🚦 Road Accident Risk Prediction")

location = st.text_input("Enter Location")
weather = st.selectbox("Weather Condition", ["Clear", "Rain", "Fog", "Snow"])

risk_score = np.random.uniform(1,10)

st.write("Risk Score:", round(risk_score,2))

if risk_score >= 7:
    st.error("⚠ HIGH RISK ZONE! Slow down!")
elif risk_score >= 4:
    st.warning("⚠ Moderate Risk Area. Drive carefully.")
else:
    st.success("✅ Safe Zone. Drive safely.")
