# 🏦 Loan Approval Predictor

An end-to-end **Machine Learning web application** that predicts whether a loan application is likely to be approved based on applicant information such as income, credit score, employment history, and loan details.

The project combines **Supervised Machine Learning, FastAPI, and Streamlit** to provide a complete prediction pipeline from user input to ML-based decision output.

---

## 📌 Project Overview

Loan approval is generally influenced by several applicant-related factors such as:

* Annual income
* Credit score
* Employment history
* Loan amount
* Existing financial obligations
* Other applicant information

This project demonstrates how supervised machine learning can be used to learn patterns from historical/synthetic loan application data and generate a prediction for a new applicant.

### Project Flow

```text
User Input
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
Data Preprocessing
    ↓
Trained ML Model
    ↓
Loan Approval Prediction
    ↓
Result Displayed to User
```

---

## 🎯 Objectives

* Build a supervised machine learning classification system.
* Generate and preprocess loan application data.
* Train and evaluate a classification model.
* Save the trained model for reuse.
* Develop a REST API using FastAPI.
* Create an interactive web interface using Streamlit.
* Connect the frontend, backend, and ML model into one application.
* Demonstrate collaborative software development using Git and GitHub.

---

## 🧠 Machine Learning

### Problem Type

**Supervised Machine Learning – Binary Classification**

The model predicts two possible outcomes:

```text
1 → Loan Approved
0 → Loan Rejected
```

### Input Features

The model can use applicant information such as:

* Annual Income
* Credit Score
* Employment Years
* Loan Amount
* Existing Loans
* Debt-to-Income Ratio
* Age
* Other relevant applicant attributes

### Target Variable

```text
Loan_Approved
```

---

## 🤖 Machine Learning Pipeline

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Selection
   ↓
Train / Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Save Model
   ↓
Prediction
```

The trained model and preprocessing components are saved as reusable files so that the FastAPI server can load them without retraining the model for every request.

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │        User          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit UI       │
                    │       app.py         │
                    └──────────┬───────────┘
                               │
                         HTTP Request
                               │
                               ▼
                    ┌──────────────────────┐
                    │     FastAPI          │
                    │      main.py         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Data Preprocessing  │
                    │      + Scaler        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   ML Classification  │
                    │       Model          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Prediction Result    │
                    │ Approved / Rejected  │
                    └──────────────────────┘
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Pandas
* NumPy
* Scikit-learn
* Joblib

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* Streamlit

### Development Tools

* Visual Studio Code
* Git
* GitHub
* Python Virtual Environment

---

## 📁 Project Structure

```text
loan-approval-app/
│
├── dataset.py
├── train_model.py
├── main.py
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── loans.csv
│
├── models/
│   ├── loan_model.pkl
│   └── scaler.pkl
│
├── tests/
│   ├── test_model.py
│   └── test_api.py
│
└── screenshots/
    ├── frontend.png
    ├── api.png
    └── prediction.png
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/loan-approval-app.git
```

Navigate into the project:

```bash
cd loan-approval-app
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 📊 Generate the Dataset

Run:

```bash
python dataset.py
```

This generates the loan dataset:

```text
data/loans.csv
```

The dataset contains applicant information and the corresponding loan approval target.

---

# 🧪 Train the Machine Learning Model

Run:

```bash
python train_model.py
```

The training pipeline:

1. Loads the dataset.
2. Performs preprocessing.
3. Selects relevant features.
4. Splits the dataset into training and testing sets.
5. Scales numerical features where required.
6. Trains the classification model.
7. Evaluates model performance.
8. Saves the trained model and preprocessing objects.

Generated files:

```text
models/
├── loan_model.pkl
└── scaler.pkl
```

---

# 🚀 Run the FastAPI Backend

Open a terminal and run:

```bash
python -m uvicorn main:app --reload --port 8000
```

The API will be available at:

```text
http://localhost:8000
```

### API Documentation

FastAPI provides interactive Swagger documentation at:

```text
http://localhost:8000/docs
```

You can use the Swagger interface to test the prediction endpoint.

---

# 🖥️ Run the Streamlit Frontend

Open another terminal while the FastAPI server is running.

Activate the virtual environment if necessary:

```powershell
.\venv\Scripts\Activate.ps1
```

Run:

```bash
python -m streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

# 🔌 API Workflow

The frontend sends applicant information to the FastAPI backend.

Example request:

```json
{
    "income": 60000,
    "credit_score": 750,
    "employment_years": 5,
    "loan_amount": 200000
}
```

The backend processes the request and sends a prediction response.

Example:

```json
{
    "prediction": "Approved",
    "probability": 0.91
}
```

The Streamlit application then displays the result to the user.

---

# 📈 Model Evaluation

The model can be evaluated using standard classification metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

Example output:

```text
Model Evaluation
----------------
Accuracy  : XX.XX%
Precision : XX.XX%
Recall    : XX.XX%
F1 Score  : XX.XX%
```

> The actual values depend on the dataset and trained model. Evaluation values should be updated with the results generated by `train_model.py`.

---

# 👥 Team Contributions

This project is developed collaboratively by a team of three members.

### 👨‍💻 HEYMAALOCHAN — Machine Learning / Data

Responsibilities:

* Dataset generation
* Data preprocessing
* Feature engineering
* Model training
* Model evaluation
* Model serialization

Primary files:

```text
dataset.py
train_model.py
```

---

### 👨‍💻 Prakash — Backend Developer

Responsibilities:

* FastAPI backend
* API endpoint development
* Request validation
* Model integration
* Prediction service
* API testing

Primary file:

```text
main.py
```

---

### 👨‍💻 Santhosh — Frontend Developer

Responsibilities:

* Streamlit interface
* User input form
* API integration
* Prediction result display
* UI design
* Frontend testing

Primary file:

```text
app.py
```

---

# 🌿 Git Workflow

The project follows a feature-branch workflow.

```text
main
 │
 ├── feature/ml-model
 │
 ├── feature/backend-api
 │
 └── feature/frontend
```

Each team member works on their assigned branch and submits changes through a Pull Request.

### Example

```bash
git checkout -b feature/ml-model
```

Make changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Add machine learning training pipeline"
```

Push:

```bash
git push -u origin feature/ml-model
```

Then create a Pull Request and merge it into `main` after review.

---

# 🔐 Environment Variables

If the project later requires API keys or credentials, store them in a `.env` file.

Example:

```text
API_KEY=your_api_key
```

Do **not** commit `.env` files to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
*.pyc
```

---

# 🧪 Testing

The application should be tested at three levels:

### Machine Learning

* Dataset loading
* Preprocessing
* Model training
* Prediction
* Evaluation metrics

### Backend

* API request validation
* Prediction endpoint
* Invalid input handling
* Model loading

### Frontend

* Form validation
* API communication
* Prediction display
* Error handling

---

# 🔮 Future Enhancements

Possible improvements include:

* Use a real-world loan approval dataset.
* Compare multiple ML algorithms.
* Add cross-validation.
* Add hyperparameter tuning.
* Add feature importance visualization.
* Add model explainability using SHAP.
* Add user authentication.
* Store prediction history in a database.
* Deploy the FastAPI backend.
* Deploy the Streamlit frontend.
* Add Docker support.
* Add automated CI/CD using GitHub Actions.
* Add monitoring for model performance.

---

# ⚠️ Disclaimer

This project is developed for **educational and demonstration purposes**.

The prediction produced by this application should not be treated as an actual financial or lending decision. Real-world loan approval involves additional financial, regulatory, institutional, and applicant-specific considerations.

---

# 📚 Learning Outcomes

Through this project, the team gains practical experience in:

* Supervised Machine Learning
* Binary Classification
* Data Preprocessing
* Feature Scaling
* Model Evaluation
* Python
* REST API Development
* FastAPI
* Streamlit
* Git and GitHub
* Branching and Pull Requests
* Full-stack ML application development
* Team-based software development

---

# ⭐ Project Highlights

```text
✔ Supervised Machine Learning
✔ End-to-End ML Pipeline
✔ FastAPI REST API
✔ Interactive Streamlit UI
✔ Model Serialization
✔ Git/GitHub Collaboration
✔ Modular Architecture
✔ API Documentation
```

---

## 📌 How to Run — Quick Version

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/loan-approval-app.git

# 2. Enter project
cd loan-approval-app

# 3. Create environment
python -m venv venv

# 4. Activate environment (Windows)
.\venv\Scripts\Activate.ps1

# 5. Install dependencies
python -m pip install -r requirements.txt

# 6. Generate dataset
python dataset.py

# 7. Train model
python train_model.py

# 8. Start FastAPI
python -m uvicorn main:app --reload --port 8000

# 9. Start Streamlit in another terminal
python -m streamlit run app.py
```

---

## 📬 Project

**Loan Approval Predictor — Supervised Machine Learning Project**

Built using:

**Python • Scikit-learn • FastAPI • Streamlit • Git • GitHub**
