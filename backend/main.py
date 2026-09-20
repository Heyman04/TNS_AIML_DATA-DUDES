from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "loan_approval_model.pkl"

app = FastAPI(title="Loan Approval API")


class LoanApplication(BaseModel):
    income: float
    credit_score: int
    loan_amount: float
    employment_years: int


model = joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return {
        "message": "Loan Approval API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }


@app.post("/predict")
def predict(application: LoanApplication):
    applicant = pd.DataFrame(
        [[
            application.income,
            application.credit_score,
            application.loan_amount,
            application.employment_years,
        ]],
        columns=[
            "income",
            "credit_score",
            "loan_amount",
            "employment_years",
        ],
    )

    prediction = model.predict(applicant)[0]

    probability = None
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(applicant)[0][1])

    return {
        "approved": bool(prediction),
        "probability": probability,
    }
