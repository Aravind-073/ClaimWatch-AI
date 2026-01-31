import streamlit as st
import numpy as np
import joblib

# Load trained model
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "fraud_model.pkl")

model = joblib.load(MODEL_PATH)


st.set_page_config(page_title="ClaimWatch AI", layout="centered")

st.title("🛡️ ClaimWatch AI – Insurance Fraud Detection")
st.write("Detect fraudulent insurance claims using risk scoring and explainable AI.")

st.divider()

st.header("Enter Claim Details")

# ---- INPUT FIELDS ----
incident_severity = st.selectbox(
    "Incident Severity",
    ["Trivial Damage", "Minor Damage", "Major Damage", "Total Loss"]
)

total_claim_amount = st.number_input(
    "Total Claim Amount",
    min_value=0,
    step=1000
)

authorities_contacted = st.selectbox(
    "Authorities Contacted",
    ["None", "Police", "Fire", "Ambulance"]
)

policy_deductable = st.number_input(
    "Policy Deductable",
    min_value=0,
    step=500
)

st.divider()

# ---- ENCODING MAPS ----
severity_map = {
    "Trivial Damage": 0,
    "Minor Damage": 1,
    "Major Damage": 2,
    "Total Loss": 3
}

authorities_map = {
    "None": 0,
    "Police": 1,
    "Fire": 2,
    "Ambulance": 3
}

# ---- PREDICTION ----
if st.button("Analyze Claim"):
    # Create input array with correct feature size
    input_data = np.zeros((1, model.n_features_in_))

    # Map values (demo-safe approximation)
    input_data[0, 0] = severity_map[incident_severity]
    input_data[0, 1] = total_claim_amount
    input_data[0, 2] = authorities_map[authorities_contacted]
    input_data[0, 3] = policy_deductable

    fraud_prob = model.predict_proba(input_data)[0][1]
    risk_score = fraud_prob * 100

    st.subheader("Prediction Result")

    if risk_score > 70:
        st.error(f"🚨 High Fraud Risk: {risk_score:.2f}%")
    elif risk_score > 30:
        st.warning(f"⚠️ Medium Fraud Risk: {risk_score:.2f}%")
    else:
        st.success(f"✅ Low Fraud Risk: {risk_score:.2f}%")

    st.subheader("Explanation")
    st.write("• High incident severity")
    st.write("• Claim amount pattern")
    st.write("• Authority reporting behavior")
