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

On Windows with Python 3.14, create a virtual environment and run pip through Python if the standalone `pip` command points to an old installation:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run front-end/streamlit_app.py
```

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
----

# 👥 Customer Persona Segmenter

An end-to-end **Machine Learning web application** that groups customers into meaningful personas based on customer characteristics such as annual income and spending score.

The project combines **Unsupervised Machine Learning, K-Means Clustering, FastAPI, and Streamlit** to provide a complete clustering pipeline from customer data to persona identification.

---

# 📌 Project Overview

Businesses have customers with different income levels and spending behaviors. Identifying groups of customers with similar characteristics can help businesses understand their customer base and create targeted marketing strategies.

This project demonstrates how **unsupervised machine learning** can automatically discover customer groups without requiring predefined labels.

The system analyzes customer information such as:

* Annual Income
* Spending Score

and groups customers into **3 clusters** using the K-Means clustering algorithm.

The resulting clusters are mapped to meaningful marketing personas.

### Project Flow

```text
Customer Input
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
Data Preprocessing
    ↓
StandardScaler
    ↓
Trained K-Means Model
    ↓
Customer Cluster
    ↓
Marketing Persona
    ↓
Result + Visualization
```

---

# 🎯 Objectives

* Build an unsupervised machine learning clustering system.
* Generate customer data for clustering.
* Perform data preprocessing and feature scaling.
* Train a K-Means clustering model.
* Divide customers into three meaningful clusters.
* Map clusters to customer marketing personas.
* Save the trained model and preprocessing components.
* Develop a REST API using FastAPI.
* Create an interactive web interface using Streamlit.
* Visualize customer clusters using a 2D scatter plot.
* Connect the frontend, backend, and ML model into one application.
* Demonstrate collaborative software development using Git and GitHub.

---

# 🧠 Machine Learning

## Problem Type

**Unsupervised Machine Learning – Clustering**

Unlike supervised machine learning, this project does not use a predefined target variable.

The model identifies groups of customers based on similarities in their characteristics.

### Algorithm Used

**K-Means Clustering**

The K-Means algorithm divides customers into a predefined number of clusters.

For this project:

```text
Number of Clusters = 3
```

The K-Means model is trained after normalizing the selected features using `StandardScaler`.

---

# 📊 Input Features

The customer segmentation model uses:

```text
Annual Income
Spending Score
```

These features are used by the clustering algorithm to identify groups of customers with similar characteristics.

---

# 👤 Customer Persona Segmentation

After K-Means clustering, the generated clusters are mapped to meaningful marketing personas.

```text
                    Customers
                        │
                        ▼
                 K-Means Clustering
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
          Cluster 1  Cluster 2  Cluster 3
             │          │          │
             ▼          ▼          ▼
          Persona     Persona     Persona
```

The persona mapping is performed using the cluster centroids generated during model training.

---

# 🤖 Machine Learning Pipeline

```text
Customer Dataset
       ↓
Data Generation
       ↓
Data Loading
       ↓
Feature Selection
       ↓
Feature Scaling
       ↓
StandardScaler
       ↓
K-Means Model Training
       ↓
3 Customer Clusters
       ↓
Centroid Analysis
       ↓
Persona Mapping
       ↓
Save Model Artifacts
       ↓
Customer Prediction
```

The trained model and preprocessing components are saved as reusable files so that the FastAPI backend can load them without retraining the model for every request.

---

# 🏗️ System Architecture

```text
                     ┌──────────────────────┐
                     │        User          │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │   Streamlit UI       │
                     │ app_unsupervised.py  │
                     └──────────┬───────────┘
                                │
                          HTTP Request
                                │
                                ▼
                     ┌──────────────────────┐
                     │      FastAPI         │
                     │ main_unsupervised.py │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ Data Preprocessing   │
                     │   + StandardScaler  │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │    K-Means Model     │
                     │     3 Clusters       │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ Customer Persona     │
                     │      Result          │
                     └──────────┬───────────┘
                                │
                                ▼
                     ┌──────────────────────┐
                     │ Cluster Visualization│
                     └──────────────────────┘
```

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Machine Learning

* Pandas
* NumPy
* Scikit-learn
* StandardScaler
* K-Means
* Joblib

## Backend

* FastAPI
* Uvicorn
* Pydantic

## Frontend

* Streamlit

## Data Visualization

* Matplotlib
* Seaborn

## Development Tools

* Visual Studio Code
* Git
* GitHub
* Python Virtual Environment

---

# 📁 Project Structure

```text
customer-persona-segmenter/
│
├── dataset_unsupervised.py
├── train_kmeans.py
├── main_unsupervised.py
├── app_unsupervised.py
├── requirements.txt
│
├── customers.csv
│
├── scaler.pkl
├── kmeans_model.pkl
└── cluster_personas.pkl
```

### File Responsibilities

```text
requirements.txt
    → Dependency Manifest

dataset_unsupervised.py
    → Synthetic Customer Data Generation

train_kmeans.py
    → K-Means Model Training

main_unsupervised.py
    → FastAPI Backend

app_unsupervised.py
    → Streamlit Dashboard
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

The **Data Dudes team lead** creates the main GitHub repository.

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate into the project:

```bash
cd YOUR_REPOSITORY
```

---

# 2. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

---

# 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 📊 Generate the Customer Dataset

Run:

```bash
python dataset_unsupervised.py
```

This generates:

```text
customers.csv
```

The script programmatically generates synthetic customer records containing annual income and spending score.

---

# 🧪 Train the K-Means Model

Run:

```bash
python train_kmeans.py
```

The training pipeline:

1. Loads the customer dataset.
2. Selects the required features.
3. Normalizes the features using `StandardScaler`.
4. Trains a K-Means model with 3 clusters.
5. Analyzes the cluster centroids.
6. Maps clusters to marketing personas.
7. Saves the trained model and preprocessing components.

Generated model artifacts include the saved `.pkl` files required by the application.

---

# 🚀 Run the FastAPI Backend

Open a terminal and run:

```bash
python -m uvicorn main_unsupervised:app --reload --port 8000
```

The API will be available at:

```text
http://localhost:8000
```

### API Documentation

FastAPI provides interactive API documentation at:

```text
http://localhost:8000/docs
```

The Swagger interface can be used to test the prediction endpoint.

---

# 🖥️ Run the Streamlit Frontend

Open another terminal while the FastAPI server is running.

Run:

```bash
python -m streamlit run app_unsupervised.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

# 🔌 API Workflow

The Streamlit application collects customer information from the user.

Example input:

```text
Annual Income
Spending Score
```

The frontend sends the customer information to the FastAPI backend.

```text
Streamlit
    ↓
HTTP Request
    ↓
FastAPI
    ↓
StandardScaler
    ↓
K-Means Model
    ↓
Cluster Assignment
    ↓
Persona Mapping
    ↓
JSON Response
```


# 👥 Team Contributions

This project is developed collaboratively by the **Data Dudes** team.

The Customer Persona Segmenter project is developed by three members of the team.

---

## 👩‍💻 Aathika Nasreen — Machine Learning / Data

### Responsibilities:

* Customer dataset generation
* Data preprocessing
* Feature selection
* Feature scaling
* StandardScaler implementation
* K-Means model training
* Cluster analysis
* Persona mapping
* Model serialization

### Primary Files:

```text
dataset_unsupervised.py
train_kmeans.py
customers.csv
```

---

## 👩‍💻 Kamalini Rajan — Backend Developer

### Responsibilities:

* FastAPI backend development
* API endpoint development
* Request validation
* Model integration
* Loading trained model artifacts
* Customer cluster prediction
* Persona response
* API testing

### Primary File:

```text
main_unsupervised.py
```

---

## 👩‍💻 Eesha B — Frontend Developer

### Responsibilities:

* Streamlit interface
* Customer input controls
* API integration
* Persona result display
* Cluster visualization
* Scatter plot implementation
* UI design
* Frontend testing

### Primary File:

```text
app_unsupervised.py
```

---

# 🌿 Git Workflow

The project follows a **feature-branch workflow**.

The Data Dudes team lead creates and manages the main repository.

```text
main
 │
 └── Customer Persona Segmenter
       │
       ├── feature/aathika-ml
       │
       ├── feature/kamalini-backend
       │
       └── feature/eesha-frontend
```

Each team member works on their assigned feature branch and submits the completed changes through a Pull Request.


# 📌 How to Run — Quick Version

```bash
# 1. Clone
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

# 2. Enter project
cd YOUR_REPOSITORY

# 3. Create environment
python -m venv venv

# 4. Activate environment (Windows)
.\venv\Scripts\Activate.ps1

# 5. Install dependencies
python -m pip install -r requirements.txt

# 6. Generate customer dataset
python dataset_unsupervised.py

# 7. Train K-Means model
python train_kmeans.py

# 8. Start FastAPI
python -m uvicorn main_unsupervised:app --reload --port 8000

# 9. Start Streamlit in another terminal
python -m streamlit run app_unsupervised.py
```

---

# 📬 Project

**Customer Persona Segmenter — Unsupervised Machine Learning Project**

### Team

**Data Dudes**

### Built Using

**Python • Pandas • NumPy • Scikit-learn • K-Means • FastAPI • Streamlit • Matplotlib • Seaborn • Git • GitHub**

