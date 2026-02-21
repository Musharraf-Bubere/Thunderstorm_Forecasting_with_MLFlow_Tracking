import streamlit as st  # frontend UI
import requests

API_URL = "http://localhost:8000/predict" # fast api runs



st.title("🌦 Weather Thunderstorm Prediction App")
st.write("Enter atmospheric parameters to predict TH (Thunderstorm Occurrence)")

# Input fields
SWEAT_index = st.number_input("SWEAT index")
K_index = st.number_input("K index")
Totals_totals_index = st.number_input("Totals totals index")
Environmental_Stability = st.number_input("Environmental_Stability")
Moisture_Indices = st.number_input("Moisture_Indices")
Convective_Potential = st.number_input("Convective_Potential")
Temperature_Pressure = st.number_input("Temperature_Pressure")
Moisture_Temperature_Profiles = st.number_input("Moisture_Temperature_Profiles")

if st.button("Predict"):
    payload = {
        "SWEAT_index": SWEAT_index,
        "K_index": K_index,
        "Totals_totals_index": Totals_totals_index,
        "Environmental_Stability": Environmental_Stability,
        "Moisture_Indices": Moisture_Indices,
        "Convective_Potential": Convective_Potential,
        "Temperature_Pressure": Temperature_Pressure,
        "Moisture_Temperature_Profiles": Moisture_Temperature_Profiles,
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
        st.info(f"Probability: {result['probability']}")
    else:
        st.error("API error. Check FastAPI backend.")
