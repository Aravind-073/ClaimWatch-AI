# 🛡️ ClaimWatch AI  
### Insurance Fraud Detection using Machine Learning

ClaimWatch AI is a machine-learning–based system designed to **detect fraudulent insurance claims** by analyzing customer, policy, incident, and claim data.  
The system provides **fraud risk scores (0–100)** along with **explainable insights**, helping insurance investigators prioritize high-risk claims efficiently.

---

## 🚨 Problem Statement
Insurance fraud causes **significant financial losses** and increases operational costs.  
Traditional rule-based systems are:
- Time-consuming  
- Difficult to scale  
- Inefficient for complex fraud patterns  

**ClaimWatch AI** solves this problem using data-driven machine learning and explainable AI.

---

## 🎯 Key Features
- ✅ Fraud classification (Fraud / Non-Fraud)
- 📊 Fraud **risk scoring** (0–100)
- 🧠 **Explainable AI** (key factors behind predictions)
- ⚖️ Class imbalance handled using **SMOTE**
- 🌐 Interactive **Streamlit web application**

---

## 🧠 Machine Learning Approach
- **Algorithm Used:** Random Forest Classifier  
- **Why Random Forest?**
  - Handles mixed numerical & categorical data
  - Robust against overfitting
  - Supports feature importance for explainability  

### Data Preprocessing
- Label encoding for categorical features  
- Log transformation for skewed numerical features  
- Removal of irrelevant columns  
- Feature scaling  
- Class balancing using **SMOTE**

---

## 🔍 Explainable AI
The model identifies important fraud indicators such as:
- Incident severity  
- Total claim amount  
- Authority involvement  
- Policy and geographical patterns  

This ensures the model is **transparent and trustworthy**, not a black box.

---

## 🌐 Web Application (Demo)
A Streamlit-based web app allows users to:
1. Enter insurance claim details  
2. View fraud risk score  
3. Understand reasons behind the prediction  

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn, Imbalanced-learn  
- **Visualization:** Matplotlib, Seaborn  
- **Web Framework:** Streamlit  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure
ClaimWatch-AI/
│
├── app/ # Streamlit web application
├── data/ # Dataset
├── notebooks/ # EDA & ML notebook
├── models/ # Trained model (generated locally)
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
git clone https://github.com/Aravind-073/ClaimWatch-AI.git
cd ClaimWatch-AI
##2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

##3️⃣ Install dependencies
pip install -r requirements.txt

##4️⃣ Train the model

Run all cells in:

notebooks/fraud_detection.ipynb


This will generate the trained model inside the models/ folder.

##5️⃣ Run the web application
streamlit run app/app.py
