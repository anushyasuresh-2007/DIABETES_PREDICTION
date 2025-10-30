import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# ---------------------------
# Load Dataset & Train Model (only once)
# ---------------------------
@st.cache_resource
def load_model():
    df = pd.read_csv("diabetes.csv")

    # Only select important features
    X = df[["Glucose", "BMI", "Age"]]
    y = df["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_scaled, y)

    return model, scaler

model, scaler = load_model()

# ---------------------------
# App Title
# ---------------------------
st.title("🏥 Diabetes Prediction System")

st.markdown("""
A hospital wants to **predict whether a patient has diabetes**  
based on key health indicators: **Glucose levels, BMI, and Age**.
""")

# ---------------------------
# User Input for Prediction
# ---------------------------
def user_input():
    glucose = st.number_input("Glucose Level", 0, 200, 120)
    bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
    age = st.number_input("Age", 0, 120, 30)

    data = np.array([[glucose, bmi, age]])
    return data

input_data = user_input()

if st.button("🔍 Predict Diabetes"):
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.error("🚨 Prediction: The patient **has Diabetes**")
    else:
        st.success("✅ Prediction: The patient **does not have Diabetes**")
