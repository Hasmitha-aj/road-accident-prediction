import streamlit as st

st.title("🌍 Smart Traffic Risk Prediction System")

# User Inputs
speed = st.number_input("Enter Speed Limit", min_value=0.0)
vehicles = st.number_input("Enter Traffic Density (Number of Vehicles)", min_value=0.0)

weather = st.selectbox(
    "Weather Condition",
    ["Clear", "Rain", "Fog", "Snow"]
)

road_condition = st.selectbox(
    "Road Condition",
    ["Good", "Moderate", "Bad"]
)

driver_behavior = st.selectbox(
    "Driver Behaviour",
    ["Calm", "Normal", "Aggressive"]
)

if st.button("Predict Risk"):

    risk_score = 0

    # Speed Risk
    if speed >= 75:
        risk_score += 2
    elif 55 <= speed < 75:
        risk_score += 1

    # Traffic Risk
    if vehicles >= 5:
        risk_score += 2
    elif 3 <= vehicles < 5:
        risk_score += 1

    # Weather Risk
    if weather in ["Rain","Fog","Snow"]:
        risk_score += 2

    # Road Risk
    if road_condition == "Bad":
        risk_score += 2
    elif road_condition == "Moderate":
        risk_score += 1

    # Driver Risk
    if driver_behavior == "Aggressive":
        risk_score += 2
    elif driver_behavior == "Normal":
        risk_score += 1

    max_risk_score = 8
    risk_index = (risk_score / max_risk_score) * 100
    confidence_level = 100 - risk_index

    st.subheader("🚦 Prediction Result")

    if risk_score >= 6:
        st.error("🔴 HIGH RISK ZONE - Slow Down Immediately")

    elif risk_score >= 3:
        st.warning("🟠 MODERATE RISK ZONE - Drive Carefully")

    else:
        st.success("🟢 SAFE ZONE - Normal Driving Allowed")

    st.write(f"Risk Index: {risk_index:.2f}%")
    st.write(f"System Confidence Level: {confidence_level:.2f}%")
