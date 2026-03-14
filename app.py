import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
pipeline = joblib.load('smartpremium_pipeline.pkl')

st.title("Smart Premium Insurance Prediction")
st.write("Enter customer details to predict insurance premium:")

# -----------------------------
# Input fields for user
# -----------------------------
age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
annual_income = st.number_input("Annual Income", min_value=0, value=30000)
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
num_dependents = st.number_input("Number of Dependents", min_value=0, value=0)
education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
occupation = st.selectbox("Occupation", ["Employed", "Self-Employed", "Unemployed"])
health_score = st.number_input("Health Score", min_value=0.0, max_value=100.0, value=50.0)
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
policy_type = st.selectbox("Policy Type", ["Basic", "Comprehensive", "Premium"])

# Default/filler fields for missing columns in pipeline
previous_claims = st.number_input("Previous Claims", min_value=0, value=0)
vehicle_age = st.number_input("Vehicle Age", min_value=0, value=5)
credit_score = st.number_input("Credit Score", min_value=0, max_value=850, value=600)
insurance_duration = st.number_input("Insurance Duration (Years)", min_value=1, max_value=10, value=1)
policy_start_date = st.text_input("Policy Start Date (YYYY-MM-DD)", "2023-01-01")
customer_feedback = st.selectbox("Customer Feedback", ["Poor", "Average", "Good"])
smoking_status = st.selectbox("Smoking Status", ["Yes", "No"])
exercise_frequency = st.selectbox("Exercise Frequency", ["Daily", "Weekly", "Monthly", "Rarely"])
property_type = st.selectbox("Property Type", ["House", "Apartment", "Condo"])

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict Premium"):
    # Create DataFrame with all columns in the same order as pipeline
    input_df = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Annual Income": [annual_income],
        "Marital Status": [marital_status],
        "Number of Dependents": [num_dependents],
        "Education Level": [education_level],
        "Occupation": [occupation],
        "Health Score": [health_score],
        "Location": [location],
        "Policy Type": [policy_type],
        "Previous Claims": [previous_claims],
        "Vehicle Age": [vehicle_age],
        "Credit Score": [credit_score],
        "Insurance Duration": [insurance_duration],
        "Policy Start Date": [policy_start_date],
        "Customer Feedback": [customer_feedback],
        "Smoking Status": [smoking_status],
        "Exercise Frequency": [exercise_frequency],
        "Property Type": [property_type]
    })
    
    # Predict using the pipeline
    predicted_premium = pipeline.predict(input_df)[0]
    
    st.success(f"Predicted Insurance Premium: ₹{predicted_premium:.2f}")
