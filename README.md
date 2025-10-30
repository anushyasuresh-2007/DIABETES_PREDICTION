
## 🏥 Diabetes Prediction System
A hospital wants to predict whether a patient has diabetes based on health indicators like Glucose levels, BMI, and Age. This project provides:

## App:

A Streamlit web app for easy predictions:https://xgboostdiabetes.streamlit.app/ image

## 🚀 Features

📊 Machine Learning Models (Logistic Regression & XGBoost)

🧾 Input patient details (Glucose, BMI, Age)

🔍 Predicts outcome (Diabetic / Not Diabetic)

## 📈 Model evaluation with Confusion Matrix, ROC Curve, AUC
⚡ Interactive Streamlit interface for hospital staff

## 📂 Project Structure
├── diabetes.csv              # Dataset

├── app.py                    # Streamlit app (Logistic Regression)

├── train_model.py            # (Optional) script to train Logistic Regression and save model.pkl

├── model.pkl                 # Saved trained model (generated)

├── scaler.pkl                # Saved scaler (generated)

├── requirements.txt          # Python dependencies

└── README.md                 # Project documentation

## 📊 Dataset
We use the Pima Indians Diabetes Dataset:
Features: Glucose, BMI, Age
Target: Outcome (0 = No Diabetes, 1 = Diabetes)

## 📦 Requirements

Python 3.8+

Streamlit

Pandas

NumPy

scikit-learn

XGBoost

Matplotlib

Seaborn
