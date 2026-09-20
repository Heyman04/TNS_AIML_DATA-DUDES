# TNS AIML Data Dudes

This repository contains two machine learning applications developed by a six-member team. Each project includes data preparation, model development, and a user-facing application.

## Projects

### 1. Customer Persona Segmenter

An unsupervised machine learning application that groups customers into meaningful personas based on demographic, financial, and behavioral attributes.

**Technologies:** Python, pandas, scikit-learn, K-Means clustering, FastAPI, and Streamlit.

**Flow:**

```text
Customer Data -> Data Cleaning -> K-Means Model -> Persona Segments -> User Interface
```

Folder: `customer-persona-segmenter/`

### 2. Loan Approval Prediction

A supervised machine learning application that predicts whether a loan application is likely to be approved using income, credit score, loan amount, and employment history.

**Technologies:** Python, pandas, scikit-learn, joblib, FastAPI, and Streamlit.

**Flow:**

```text
Applicant Input -> Streamlit Frontend -> FastAPI Backend -> ML Model -> Approval Prediction
```

Folder: `Loan_Approval_Prediction/`

## Team Roles

The work is divided among six team members, with three members assigned to each project.

### Customer Persona Segmenter Team

#### Member 1 - Data and Machine Learning Engineer

- Clean and analyze customer data
- Prepare features for clustering
- Train and evaluate the K-Means model
- Save and document the trained model

#### Member 2 - Backend/API Developer

- Build the FastAPI service
- Create persona prediction endpoints
- Validate incoming data
- Integrate and test the clustering model

#### Member 3 - Frontend and Visualization Developer

- Build the Streamlit interface
- Display persona results and charts
- Connect the frontend to the API
- Test the complete user workflow

### Loan Approval Prediction Team

#### Member 4 - Data and Machine Learning Engineer

- Prepare and analyze loan data
- Perform feature engineering and preprocessing
- Train and compare classification models
- Save the selected model and evaluation reports

#### Member 5 - Backend/API Developer

- Build the FastAPI loan approval service
- Create `/health` and `/predict` endpoints
- Validate loan application requests
- Load and test the trained model

#### Member 6 - Frontend and Integration Developer

- Build the Streamlit loan application interface
- Create input forms and result views
- Connect Streamlit to the FastAPI backend
- Display approval probability and risk factors

Replace `Member 1` through `Member 6` with the team members' names.

## Running the Loan Approval Application

Start the backend:

```powershell
cd Loan_Approval_Prediction
python -m uvicorn backend.main:app --reload
```

Start the frontend in a second terminal:

```powershell
cd Loan_Approval_Prediction
python -m streamlit run front-end/app.py
```

- FastAPI documentation: `http://127.0.0.1:8000/docs`
- Streamlit application: `http://localhost:8501`

## Collaboration

Team members should work on separate feature branches, commit focused changes, and merge their work into `main` through pull requests.

```text
main
├── feature/customer-persona-ml
├── feature/customer-persona-backend
├── feature/customer-persona-frontend
├── feature/loan-approval-ml
├── feature/loan-approval-backend
└── feature/loan-approval-frontend
```
