# Loan Approval App

A lightweight loan eligibility calculator built with plain HTML, CSS, and JavaScript.

## Features

- Annual income and monthly debt inputs
- Credit score and loan amount evaluation
- Estimated debt-to-income ratio
- Monthly payment estimate based on a risk-adjusted rate
- Decision status with a clear approval/review/decline result

## Run locally

From the project folder, start a local web server for the frontend:

```bash
python -m http.server 8000 --directory front-end
```

Then open:

```text
http://localhost:8000
```

To run the Streamlit model frontend:

```bash
streamlit run front-end/streamlit_app.py
```

### Windows setup

If the `pip` command is unavailable or points to an old Python installation, use a virtual environment and run pip through Python:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run front-end/streamlit_app.py
```

## Project structure

- `data/loans.csv` – source loan dataset
- `scripts/train_model.py` – trains and evaluates the ML models
- `scripts/analyze_loans.py` – creates reports and visualizations
- `models/` – saved model artifacts
- `graphs/` – confusion matrices, comparisons, and data charts
- `reports/` – classification report, data report, and model flow
- `front-end/` – HTML, CSS, and JavaScript application

## Train the model

```bash
python scripts/train_model.py
```

The final preprocessing and Logistic Regression pipeline is saved to:

```text
models/loan_approval_model.pkl
```

## Generate analysis outputs

```bash
python scripts/analyze_loans.py
```
