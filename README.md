# 🤖 Vendor Invoice Intelligence System | SQL + Python + Machine Learning

## 🚀 Project Overview

Vendor Invoice Intelligence System is an end-to-end Machine Learning and Analytics platform designed to automate vendor invoice review processes and improve procurement decision-making.

The system combines predictive analytics, anomaly detection, and business intelligence techniques to:

* Predict freight costs before invoice approval
* Automatically flag potentially risky invoices
* Reduce manual invoice verification effort
* Improve procurement efficiency
* Support data-driven vendor management

The solution includes data preprocessing pipelines, machine learning model training, model deployment, and an interactive Streamlit dashboard for real-time predictions.

---

## 🎯 Business Problem

Organizations process thousands of vendor invoices every month.

Manual invoice verification often results in:

* Delayed approvals
* Human errors
* Financial leakage
* High operational costs
* Difficulty identifying suspicious invoices

This project addresses these challenges using Machine Learning and Automation.

---

## 🏗️ Solution Architecture

```text
Vendor Invoice Data
        │
        ▼
Data Cleaning & Feature Engineering
        │
        ▼
SQLite Database
        │
        ▼
Machine Learning Models
        │
 ┌──────┴────────┐
 ▼               ▼
Freight Cost     Invoice Risk
Prediction       Flagging
        │
        ▼
Streamlit Dashboard
        │
        ▼
Business Decision Support
```

---

## 📂 Project Components

### 1️⃣ Freight Cost Prediction

A Regression-based Machine Learning model predicts expected freight charges based on invoice values and purchasing behavior.

#### Objective

Predict transportation costs before invoice approval.

#### Benefits

* Better budgeting
* Cost forecasting
* Procurement planning
* Expense optimization

---

### 2️⃣ Intelligent Invoice Flagging

A Classification-based Machine Learning model identifies invoices that may require additional review or approval.

#### Objective

Automatically detect potentially risky invoices.

#### Benefits

* Reduce manual effort
* Improve audit efficiency
* Minimize approval errors
* Detect unusual invoice patterns

---

## ⚙️ Technologies Used

### Programming Languages

* Python
* SQL

### Machine Learning

* Scikit-Learn
* Random Forest
* Decision Tree
* Linear Regression
* Grid Search CV

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib
* Seaborn

### Database

* SQLite
* SQLAlchemy

### Deployment

* Streamlit

### Model Storage

* Joblib

---

## 🔄 Machine Learning Workflow

### Data Collection

Vendor invoice data was collected and stored inside SQLite databases.

### Data Preprocessing

* Missing value handling
* Feature selection
* Data transformation
* Label creation
* Feature scaling

### Model Training

#### Freight Prediction Models

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

Best-performing model selected based on evaluation metrics.

#### Invoice Flagging Models

* Random Forest Classifier
* Hyperparameter Tuning using GridSearchCV

---

## 📊 Features Used

### Freight Cost Prediction

Input Features:

* Invoice Dollars

Output:

* Predicted Freight Cost

---

### Invoice Risk Flagging

Input Features:

* Invoice Quantity
* Invoice Dollars
* Freight Cost
* Total Item Quantity
* Total Item Dollars

Output:

* Invoice Flag (0 = Normal, 1 = Review Required)

---

## 📈 Model Evaluation

### Regression Metrics

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score

### Classification Metrics

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🌐 Interactive Dashboard

A Streamlit-based dashboard was developed to provide real-time predictions.

### Dashboard Features

✅ Freight Cost Prediction

✅ Invoice Risk Classification

✅ Interactive User Interface

✅ Real-Time Machine Learning Inference

✅ Business-Friendly Analytics Portal

---

## 📋 Business Impact

The system helps organizations:

* Automate invoice screening
* Improve procurement efficiency
* Predict logistics expenses
* Detect potentially risky invoices
* Reduce operational costs
* Improve financial control processes

---

## 📁 Project Structure

```text
vendor_invoice_intelligent_system/
│
├── app.py
│
├── data/
│   └── inventory.db
│
├── notebooks/
│   ├── invoice_Flagging.ipynb
│   └── Predicting_Freight_cost.ipynb
│
├── Freight_cost_prediction/
│   ├── train.py
│   ├── data_preprocessing.py
│   ├── model_evaluation.py
│   └── models/
│
├── invoice_flagging/
│   ├── train.py
│   ├── data_preprocessing.py
│   ├── modelling_evaluation.py
│   └── models/
│
├── inferences/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── models/
│   └── predict_freight_model.pkl
│
├── README.md
└── requirements.txt
```

---

## 🎓 Skills Demonstrated

* Machine Learning
* Classification Modeling
* Regression Modeling
* Feature Engineering
* Hyperparameter Tuning
* SQL Database Integration
* Data Analytics
* Model Deployment
* Streamlit Development
* Business Intelligence

---

## 🏆 Project Highlights

✔ End-to-End Machine Learning Pipeline

✔ Real-World Procurement Analytics Use Case

✔ Interactive Streamlit Dashboard

✔ Automated Invoice Intelligence System

✔ SQL + Python + ML Integration

✔ Business-Oriented Predictive Analytics

---

## 👨‍💻 Author

**Yash Maheshwari**

Aspiring Data Analyst | Machine Learning Enthusiast | SQL | Python | Data Science

📧 Open to Data Analyst, Machine Learning Engineer, Business Analyst, and Data Science opportunities.

⭐ If you found this project useful, consider giving the repository a star.

