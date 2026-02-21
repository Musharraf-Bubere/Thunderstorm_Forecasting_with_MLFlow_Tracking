# ⚡ Thunderstorm Forecasting with MLflow Tracking

A production-ready Machine Learning project to predict **Thunderstorm Occurrence** using atmospheric indices and weather parameters.  
This project demonstrates **end-to-end ML pipeline development**, **experiment tracking with MLflow**, and **deployment using Streamlit**.

---

## 🚀 Project Highlights

✔ End-to-End ML Pipeline  
✔ Multi-Model Benchmarking  
✔ Hyperparameter Tuning  
✔ MLflow Experiment Tracking  
✔ Model Versioning & Artifact Logging  
✔ Streamlit Deployment  
✔ Production-style Project Structure  

---

## 📌 Problem Statement

Thunderstorms can cause severe weather disruptions.  
This project builds a classification model that predicts the likelihood of a thunderstorm using meteorological indices such as:

- SWEAT Index  
- K Index  
- Totals Totals Index  
- Convective Potential  
- Environmental Stability  
- Moisture Indices  
- Temperature & related atmospheric features  

---

## 🏗️ Project Architecture

```
Thunderstorm_Forecasting_with_MLFlow_Tracking/
│
├── api/                          # FastAPI backend (if applicable)
├── app/                          # Core ML logic
├── data/                         # Raw & processed datasets
├── models/                       # Saved trained models
├── streamlit_app/                # Streamlit frontend
│
├── app.py                        # Main training + MLflow logging script
├── mlflow.db                     # MLflow SQLite tracking database
├── requirements.txt              # Production dependencies
├── local-requirements.txt        # Local dev dependencies
├── pyproject.toml                # Project configuration
├── Thunderstorm_Forecasting_Handwritten_Notes.pdf
└── README.md
```

---

## 🧠 Machine Learning Workflow

### 1️⃣ Data Processing
- Cleaning missing values
- Feature engineering
- Train-Test split
- Scaling / preprocessing

### 2️⃣ Model Training
Multiple models are trained and compared:

- Logistic Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting  
- SVM  
- KNN  
- XGBoost  

### 3️⃣ Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Cross Validation

### 4️⃣ Experiment Tracking (MLflow)

Each run logs:
- Model name
- Hyperparameters
- Metrics
- Artifacts
- Best model selection

---

## 📊 MLflow Tracking

Start MLflow UI:

```bash
mlflow ui
```

Open in browser:
```
http://localhost:5000
```

You can:
- Compare experiments
- View parameters & metrics
- Download artifacts
- Register best model

---

## 🛠 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Musharraf-Bubere/Thunderstorm_Forecasting_with_MLFlow_Tracking.git
cd Thunderstorm_Forecasting_with_MLFlow_Tracking
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Training Pipeline

```bash
python app.py
```

This will:
- Train models
- Log experiments in MLflow
- Save best model locally

---

## 🌐 Run Streamlit App

```bash
streamlit run streamlit_app/app.py
```

Features:
- Input weather parameters
- Get real-time thunderstorm prediction
- Interactive UI for demonstration

---

## 📦 Tech Stack

- Python  
- Pandas & NumPy  
- Scikit-Learn  
- XGBoost  
- MLflow  
- Streamlit  
- FastAPI (if API enabled)

---

## 📈 Why This Project Matters

This project demonstrates:

- Real-world ML experimentation workflow
- Model comparison & tuning
- Experiment reproducibility
- Deployment readiness
- Portfolio-level project structure

It reflects strong understanding of:
- Machine Learning fundamentals
- MLOps basics
- Tracking & model management
- End-to-end project implementation

---

## 🔮 Future Improvements

- Docker containerization  
- CI/CD integration  
- Cloud deployment (AWS / GCP / Azure)  
- Automated retraining pipeline  
- Advanced ensemble stacking  

---

## 👨‍💻 Author

**Musharraf Bubare**  
Aspiring Data Scientist | ML Engineer  
Commerce Background → Transitioning into AI & Data Science  

GitHub: https://github.com/Musharraf-Bubere  

---

## ⭐ If You Like This Project

Give it a ⭐ on GitHub and feel free to fork & improve it!

---
