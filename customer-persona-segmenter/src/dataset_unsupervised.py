import numpy as np
import pandas as pd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# For reproducible results
np.random.seed(42)

# Number of customers
n_customers = 600

# Generate three types of customer groups
n_per_cluster = n_customers // 3

# Cluster 1: Lower income, lower spending
income_1 = np.random.normal(30, 8, n_per_cluster)
spending_1 = np.random.normal(30, 10, n_per_cluster)

# Cluster 2: Higher income, higher spending
income_2 = np.random.normal(75, 12, n_per_cluster)
spending_2 = np.random.normal(75, 10, n_per_cluster)

# Cluster 3: Higher income, lower spending
income_3 = np.random.normal(70, 12, n_per_cluster)
spending_3 = np.random.normal(30, 10, n_per_cluster)

# Combine the data
annual_income = np.concatenate([
    income_1,
    income_2,
    income_3
])

spending_score = np.concatenate([
    spending_1,
    spending_2,
    spending_3
])

# Keep values within reasonable ranges
annual_income = np.clip(annual_income, 10, 120)
spending_score = np.clip(spending_score, 1, 100)

# Create DataFrame
customers = pd.DataFrame({
    "annual_income_k": annual_income.round(2),
    "spending_score": spending_score.round(2)
})

# Save original generated dataset
customers.to_csv(RAW_DATA_DIR / "customers.csv", index=False)

# ----------------------------
# Data cleaning
# ----------------------------
cleaned = customers.copy()

# Remove duplicate rows
cleaned = cleaned.drop_duplicates().reset_index(drop=True)

# Convert columns to numeric and handle invalid values
for col in ["annual_income_k", "spending_score"]:
    cleaned[col] = pd.to_numeric(cleaned[col], errors="coerce")

# Remove rows with missing values
cleaned = cleaned.dropna(subset=["annual_income_k", "spending_score"]).reset_index(drop=True)

# Keep realistic customer ranges
cleaned = cleaned[
    cleaned["annual_income_k"].between(10, 120)
    & cleaned["spending_score"].between(1, 100)
].reset_index(drop=True)

# Sort to make output consistent
cleaned = cleaned.sort_values(["annual_income_k", "spending_score"]).reset_index(drop=True)

# Save cleaned dataset to a new file
cleaned.to_csv(PROCESSED_DATA_DIR / "customers_cleaned.csv", index=False)

print("Customer dataset generated successfully!")
print(f"Original rows: {len(customers)}")
print(f"Cleaned rows: {len(cleaned)}")
print("\nFirst 5 cleaned records:")
print(cleaned.head())