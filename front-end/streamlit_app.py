from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_FILE = PROJECT_ROOT / "models" / "loan_approval_model.pkl"

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon=":bank:",
    layout="centered",
)

st.title("Loan Approval Predictor")
st.write("Enter applicant details to receive a prediction from the trained model.")


@st.cache_resource
def load_model():
    return joblib.load(MODEL_FILE)


if not MODEL_FILE.exists():
    st.error(f"Model file not found: {MODEL_FILE}")
    st.stop()

model = load_model()

with st.form("loan_application"):
    income = st.number_input("Annual income", min_value=0.0, step=1000.0, value=90000.0)
    credit_score = st.number_input("Credit score", min_value=300, max_value=850, step=1, value=720)
    loan_amount = st.number_input("Loan amount", min_value=0.0, step=500.0, value=25000.0)
    employment_years = st.number_input("Employment years", min_value=0, step=1, value=6)
    submitted = st.form_submit_button("Check eligibility", type="primary")

if submitted:
    applicant = pd.DataFrame(
        {
            "income": [income],
            "credit_score": [credit_score],
            "loan_amount": [loan_amount],
            "employment_years": [employment_years],
        }
    )
    prediction = int(model.predict(applicant)[0])
    probability = float(model.predict_proba(applicant)[0][prediction])
    confidence = f"{probability:.1%}"

    if prediction == 1:
        st.success(f"Loan likely approved ({confidence} model confidence)")
    else:
        st.error(f"Loan likely rejected ({confidence} model confidence)")

    st.caption("This prediction is for decision support and is not a lending commitment.")