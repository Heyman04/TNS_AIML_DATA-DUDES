# TNS AIML Data Dudes

<p align="center">
	<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&pause=900&color=0F766E&center=true&vCenter=true&width=700&lines=Turning+data+into+decisions;Customer+personas+%7C+Loan+approval;Machine+Learning+%2B+FastAPI+%2B+Streamlit" alt="Animated project introduction" />
</p>

This repository contains two machine learning applications developed by a six-member team. Each project includes data preparation, model development, and a user-facing application.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

> Two practical ML products. One collaborative team. Data becomes decisions.

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

## Tech Stack

| Layer | Technologies |
| --- | --- |
| Programming language | Python 3.x |
| Data processing | pandas, NumPy |
| Machine learning | scikit-learn |
| Customer segmentation | K-Means clustering, StandardScaler |
| Loan prediction | Logistic Regression, Decision Tree, Random Forest |
| Backend API | FastAPI, Uvicorn, Pydantic |
| Frontend | Streamlit |
| API integration | Requests, REST/JSON |
| Model persistence | Joblib, Pickle |
| Data visualization | Matplotlib, Seaborn |
| Testing | Pytest, FastAPI TestClient |
| Collaboration | Git, GitHub, feature branches, pull requests |

## Project Workflows

<p align="center">
	<img src="https://capsule-render.vercel.app/api?type=rect&color=0F766E&height=3&section=header" alt="Animated section divider" width="85%" />
</p>

### Customer Persona Segmenter

```mermaid
flowchart LR
	A[Customer Data] --> B[Clean and Explore]
	B --> C[Scale Features]
	C --> D((K-Means Clustering))
	D --> E[Persona Mapping]
	E --> F[FastAPI Service]
	F --> G[Streamlit Dashboard]

	classDef data fill:#e8f5f2,stroke:#00796b,color:#123;
	classDef model fill:#fff1d6,stroke:#ef8b00,color:#321;
	classDef app fill:#e8efff,stroke:#3457d5,color:#123;
	class A,B,C data;
	class D,E model;
	class F,G app;
```

### Loan Approval Prediction

```mermaid
flowchart LR
	A[Applicant Details] --> B[Streamlit Form]
	B --> C[FastAPI /predict]
	C --> D[Preprocessing Pipeline]
	D --> E((Classification Model))
	E --> F[Approval Probability]
	F --> G[Risk Summary]

	classDef input fill:#e8f5f2,stroke:#00796b,color:#123;
	classDef service fill:#e8efff,stroke:#3457d5,color:#123;
	classDef model fill:#fff1d6,stroke:#ef8b00,color:#321;
	classDef output fill:#fce8ef,stroke:#c2185b,color:#321;
	class A,B input;
	class C,D service;
	class E model;
	class F,G output;
```

## Project Structure

```text
TNS_AIML_DATA-DUDES/
├── README.md
├── customer-persona-segmenter/
│   ├── assets/personas/          # Persona images
│   ├── data/
│   │   ├── raw/                  # Original customer data
│   │   └── processed/            # Cleaned customer data
│   ├── models/                   # K-Means and scaler artifacts
│   ├── src/                      # Backend, dataset, and training modules
│   ├── tests/                    # Model tests
│   ├── app_unsupervised.py      # Streamlit application
│   ├── main_unsupervised.py     # FastAPI service
│   ├── dataset_unsupervised.py  # Dataset preparation
│   ├── train_kmeans.py          # K-Means training
│   └── requirements.txt
└── Loan_Approval_Prediction/
	├── backend/
	│   └── main.py              # FastAPI loan prediction API
	├── front-end/
	│   ├── app.py               # Streamlit application
	│   └── assets/               # Approved/rejected images
	├── data/                     # Loan dataset
	├── graphs/                   # Evaluation charts and metrics
	├── models/                   # Trained loan models
	├── reports/                  # Evaluation and analysis reports
	├── scripts/                  # Training and analysis scripts
	└── requirements.txt
```

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

### 🤖 HEYMAALOCHAN - Data and Machine Learning Engineer

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
