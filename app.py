import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("sleep_model.pkl")

st.title("Smart Sleep Predictor")

age = st.number_input("Age", 18, 100)
sleep_duration = st.number_input("Sleep Duration (Hours)", 0.0, 12.0, step=0.1)
stress_level = st.slider("Stress Level (0 - No Stress, 10 - High Stress)", 0, 10)
bmi = st.number_input("BMI Value", 10.0, 50.0, step=0.1)

if st.button("Predict"):
    data = pd.DataFrame([{
        "Age": age,
        "Sleep Duration": sleep_duration,
        "Stress Level": stress_level,
        "BMI": bmi
    }])
    
    result = model.predict(data)[0]
    st.success(f"Prediction: {result}")

