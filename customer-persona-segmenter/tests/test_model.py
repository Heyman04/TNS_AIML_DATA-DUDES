import requests

API_URL = "http://127.0.0.1:8011/predict"

samples = [
    {"annual_income_k": 25, "spending_score": 20},
    {"annual_income_k": 40, "spending_score": 35},
    {"annual_income_k": 60, "spending_score": 55},
    {"annual_income_k": 75, "spending_score": 80},
    {"annual_income_k": 90, "spending_score": 30},
]

for payload in samples:
    response = requests.post(API_URL, json=payload, timeout=10)
    print(f"Input: {payload}")
    print(f"Status: {response.status_code}")
    print(response.json())
    print("-" * 60)
