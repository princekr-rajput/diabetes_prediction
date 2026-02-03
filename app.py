import streamlit as st
import numpy as np
import joblib

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout="centered"
)

# ------------------ LOAD MODEL ------------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("diabetes_scaler.pkl")
    return model, scaler

model, scaler = load_artifacts()

# ------------------ PREDICTION FUNCTION ------------------
def predict_diabetes_with_confidence(model, scaler, user_input):
    user_input = np.array(user_input, dtype=float).reshape(1, -1)
    user_input_scaled = scaler.transform(user_input)

    prob = model.predict_proba(user_input_scaled)[0][1]

    if prob >= 0.6:
        label = "High Diabetes Risk"
        color = "🔴"
    elif prob >= 0.4:
        label = "Moderate Diabetes Risk"
        color = "🟠"
    else:
        label = "Low Diabetes Risk"
        color = "🟢"

    return label, round(prob * 100, 2), color

# ------------------ UI ------------------
st.title("🩺 Diabetes Risk Prediction")
st.write("Enter medical values to estimate diabetes risk.")

with st.form("diabetes_form"):
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose Level", 50, 300, 120)
    bp = st.number_input("Blood Pressure", 40, 200, 80)
    skin = st.number_input("Skin Thickness", 5, 100, 20)
    insulin = st.number_input("Insulin", 10, 900, 80)
    bmi = st.number_input("BMI", 10.0, 70.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.05, 3.0, 0.5)
    age = st.number_input("Age", 1, 120, 30)

    submit = st.form_submit_button("Predict Risk")

if submit:
    inputs = [pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]

    label, probability, color = predict_diabetes_with_confidence(
        model, scaler, inputs
    )

    st.subheader("Result")
    st.markdown(f"### {color} {label}")
    st.metric("Probability (%)", probability)

    st.info("⚠️ This tool is for educational purposes only and not a medical diagnosis.")

