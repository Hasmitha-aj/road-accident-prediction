
import streamlit as st
import numpy as np

print("\n Smart Traffic Risk Prediction System (Final Version)")

try:

    # User Inputs
    speed = float(input("Enter Speed Limit: "))
    vehicles = float(input("Enter Traffic Density (Number of Vehicles): "))

    print("\nWeather Options:")
    print("1 → Clear")
    print("2 → Rain")
    print("3 → Fog")
    print("4 → Snow")

    weather_map = {"1":"Clear","2":"Rain","3":"Fog","4":"Snow"}
    weather = weather_map.get(input("Choose Weather Condition (1/2/3/4): "),"Clear")

    print("\nRoad Condition Options:")
    print("1 → Good Road")
    print("2 → Moderate Road")
    print("3 → Bad Road")

    road_map = {"1":"Good","2":"Moderate","3":"Bad"}
    road_condition = road_map.get(input("Choose Road Condition (1/2/3): "),"Good")

    print("\nDriver Behaviour Options:")
    print("1 → Calm Driver")
    print("2 → Normal Driver")
    print("3 → Aggressive Driver")

    driver_map = {"1":"Calm","2":"Normal","3":"Aggressive"}
    driver_behavior = driver_map.get(input("Choose Driver Behaviour (1/2/3): "),"Normal")


    # Risk Score Calculation (Rule Based)


    risk_score = 0

    if speed >= 75:
        risk_score += 2
    elif 55 <= speed < 75:
        risk_score += 1

    if vehicles >= 5:
        risk_score += 2
    elif 3 <= vehicles < 5:
        risk_score += 1

    if weather in ["Rain","Fog","Snow"]:
        risk_score += 2

    if road_condition == "Bad":
        risk_score += 2
    elif road_condition == "Moderate":
        risk_score += 1

    if driver_behavior == "Aggressive":
        risk_score += 2
    elif driver_behavior == "Normal":
        risk_score += 1


    #  Advanced Feature (Non-AI)
    # Risk Index Normalization


    max_risk_score = 8
    risk_index = (risk_score / max_risk_score) * 100
    risk_index = min(risk_index, 100)

    confidence_level = 100 - risk_index


    # Final Output


    print("\n--- FINAL SMART ALERT RESULT ---")

    if risk_score >= 6:
        print(" HIGH RISK ZONE")
        print(" Slow Down Immediately")

    elif risk_score >= 3:
        print(" MODERATE RISK ZONE")
        print(" Drive Carefully")

    else:
        print(" SAFE ZONE")
        print(" Normal Driving Allowed")

    print(f"\nRisk Index = {risk_index:.2f}%")
    print(f"System Confidence Level = {confidence_level:.2f}%")

except Exception as e:
    print("Prediction Error:", e)
