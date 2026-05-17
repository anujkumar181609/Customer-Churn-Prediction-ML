import streamlit as st
import pickle
import pandas as pd
from pathlib import Path

# Page config
st.set_page_config(page_title="Churn Predictor", page_icon="📊", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>📊 Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict whether a customer is likely to churn</p>", unsafe_allow_html=True)
st.markdown("---")

# Load model
BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / "churn_model.pkl"
model = pickle.load(open(model_path, 'rb'))

# Create two columns
col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (Months)", min_value=0)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

with col2:
    total_charges = st.number_input("Total Charges", min_value=0.0)
    contract = st.selectbox("Contract Type", 
                            ["Month to Month", "One year", "Two year"])

st.markdown("---")

# Prediction
if st.button("🔍 Predict Churn"):

    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthly_charges],
        "TotalCharges": [total_charges],
        "Contract": [contract]
    })

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    # Threshold = 0.4
    if probability > 0.7:
        st.error(f"🚨 High Risk of Churn ({probability:.2f})")
    elif probability > 0.4:
        st.warning(f"⚠ Medium Risk of Churn ({probability:.2f})")
    else:
        st.success(f"✅ Low Risk of Churn ({probability:.2f})")

    # Progress bar
    st.progress(float(probability))
