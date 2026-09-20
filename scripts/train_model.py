from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "loans.csv"
MODEL_FILE = PROJECT_ROOT / "models" / "loan_approval_model.pkl"
GRAPH_DIR = PROJECT_ROOT / "graphs"
TARGET = "loan_status"


def build_preprocessor(data):
    categorical_features = data.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    numerical_features = data.select_dtypes(exclude=["object", "category", "bool"]).columns.tolist()

    return ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
                categorical_features,
            ),
            ("numerical", StandardScaler(), numerical_features),
        ],
        remainder="drop",
    )


def build_pipeline(data, classifier):
    return Pipeline(
        steps=[
            ("preprocessing", build_preprocessor(data)),
            ("classifier", classifier),
        ]
    )


data = pd.read_csv(DATA_FILE)
X = data.drop(columns=[TARGET])
y = data[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

models = {
    "Logistic Regression": build_pipeline(
        X_train,
        LogisticRegression(max_iter=1000, random_state=42),
    ),
    "Decision Tree": build_pipeline(
        X_train,
        DecisionTreeClassifier(random_state=42),
    ),
    "Random Forest": build_pipeline(
        X_train,
        RandomForestClassifier(n_estimators=100, random_state=42),
    ),
}

GRAPH_DIR.mkdir(exist_ok=True)
MODEL_FILE.parent.mkdir(exist_ok=True)
metrics = []
reports = []

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions, zero_division=0)
    report_name = name.lower().replace(" ", "_")

    metrics.append(
        {
            "model": name,
            "accuracy": accuracy_score(y_test, predictions),
            "precision": precision_score(y_test, predictions, zero_division=0),
            "recall": recall_score(y_test, predictions, zero_division=0),
            "f1_score": f1_score(y_test, predictions, zero_division=0),
        }
    )
    reports.append(f"{name}\n{'=' * len(name)}\n{report}")

    display = ConfusionMatrixDisplay.from_predictions(
        y_test,
        predictions,
        display_labels=["Rejected", "Approved"],
        cmap="Blues",
        values_format="d",
    )
    display.ax_.set_title(f"{name} Confusion Matrix")
    display.figure_.tight_layout()
    display.figure_.savefig(GRAPH_DIR / f"{report_name}_confusion_matrix.png", dpi=160)
    plt.close(display.figure_)

metrics_frame = pd.DataFrame(metrics)
metrics_frame.to_csv(GRAPH_DIR / "model_comparison_metrics.csv", index=False)
REPORT_FILE = PROJECT_ROOT / "reports" / "classification_report.txt"
REPORT_FILE.parent.mkdir(exist_ok=True)
REPORT_FILE.write_text("\n\n".join(reports), encoding="utf-8")

print("Model comparison:")
print(metrics_frame.to_string(index=False, float_format=lambda value: f"{value:.3f}"))
print("\nLogistic Regression selected as the final model based on the current test results.")
joblib.dump(models["Logistic Regression"], MODEL_FILE)
print(f"Saved complete preprocessing + ML pipeline to {MODEL_FILE}")