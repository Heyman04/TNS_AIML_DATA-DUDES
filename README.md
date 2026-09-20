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

