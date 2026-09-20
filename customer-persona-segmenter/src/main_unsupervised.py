from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib
from pathlib import Path


# --------------------------------------------------
# Initialize FastAPI
# --------------------------------------------------

app = FastAPI(
    title="Customer Persona Segmenter API",
    description="API for customer persona prediction using K-Means clustering",
    version="1.0.0"
)


# --------------------------------------------------
# Model Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_DIR = PROJECT_ROOT / "models"

MODEL_FILES = {
    "scaler": MODEL_DIR / "scaler.pkl",
    "kmeans": MODEL_DIR / "kmeans_model.pkl",
    "personas": MODEL_DIR / "cluster_personas.pkl",
}


def load_model_artifacts():
    missing_files = [path for path in MODEL_FILES.values() if not os.path.exists(path)]

    if missing_files:
        print("Missing model files:")
        for missing in missing_files:
            print(f"- {missing}")
        print("Run: python train_kmeans.py")
        return None, None, None

    try:
        scaler = joblib.load(MODEL_FILES["scaler"])
        kmeans = joblib.load(MODEL_FILES["kmeans"])
        cluster_personas = joblib.load(MODEL_FILES["personas"])
        print("Loaded latest model artifacts from models folder.")
        return scaler, kmeans, cluster_personas
    except Exception as e:
        print(f"Model loading error: {e}")
        return None, None, None


# --------------------------------------------------
# Load Trained Models
# --------------------------------------------------

scaler, kmeans, cluster_personas = load_model_artifacts()


# --------------------------------------------------
# Request Schema
# --------------------------------------------------

class CustomerInput(BaseModel):
    annual_income_k: float = Field(..., gt=0)
    spending_score: float = Field(..., ge=0, le=100)


# --------------------------------------------------
# Root Endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Customer Persona Segmenter API is running",
        "status": "success"
    }


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/health")
def health_check():

    if scaler is None or kmeans is None or cluster_personas is None:
        return {
            "status": "unhealthy",
            "model_loaded": False
        }

    return {
        "status": "healthy",
        "model_loaded": True
    }

# --------------------------------------------------
# Persona Information Endpoint
# --------------------------------------------------

@app.get("/personas")
def get_personas():

    if cluster_personas is None:
        raise HTTPException(
            status_code=500,
            detail="Persona information is not loaded"
        )

    personas = []

    for cluster, details in cluster_personas.items():
        personas.append({
            "cluster": int(cluster),
            "persona": details["persona"],
            "annual_income_k": details["annual_income_k"],
            "spending_score": details["spending_score"]
        })

    personas.sort(key=lambda x: x["cluster"])

    return {
        "count": len(personas),
        "personas": personas
    }


# --------------------------------------------------
# Prediction Endpoint
# --------------------------------------------------

@app.post("/predict")
def predict_persona(customer: CustomerInput):

    if scaler is None or kmeans is None or cluster_personas is None:
        raise HTTPException(
            status_code=500,
            detail="ML model is not loaded"
        )

    # Convert input into DataFrame
    input_data = pd.DataFrame([
        {
            "annual_income_k": customer.annual_income_k,
            "spending_score": customer.spending_score
        }
    ])

    # Apply the same scaler used during training
    input_scaled = scaler.transform(input_data)

    # Predict cluster
    cluster = int(kmeans.predict(input_scaled)[0])

    # Get persona information
    persona_info = cluster_personas.get(cluster)

    if persona_info is None:
        raise HTTPException(
            status_code=500,
            detail="Persona information not found"
        )

    return {
        "annual_income_k": customer.annual_income_k,
        "spending_score": customer.spending_score,
        "cluster": cluster,
        "persona": persona_info["persona"]
    }