# Customer Churn Prediction – End-to-End Machine Learning Project

## 📌 Overview

This project is an end-to-end **Customer Churn Prediction** system developed as part of the **Devixo Solutions AI/ML Internship**.

The project uses machine learning to predict whether a bank customer is likely to **churn (leave)** or **stay**.

## 📊 Dataset

* Dataset: Customer Churn / Churn Modelling
* Rows: **10,000**
* Features: Customer demographic and banking information
* Target: **Exited**

## ⚙️ Machine Learning Workflow

1. Data loading and inspection
2. Data cleaning
3. Feature engineering
4. Categorical encoding
5. Feature importance analysis
6. Train-test split
7. Model training
8. Cross-validation
9. Hyperparameter tuning
10. Final model evaluation
11. Model saving using Joblib

## 🤖 Models Tested

| Model             |  Accuracy |
| ----------------- | --------: |
| Gradient Boosting | **87.1%** |
| Random Forest     |     86.1% |
| SVM               |     86.1% |
| Decision Tree     |     77.9% |

**Best Model:** Gradient Boosting Classifier
**Final Accuracy:** **87.1%**

## 🔑 Important Features

The most important features identified by the final Gradient Boosting model were:

* Age
* Number of Products
* Is Active Member
* Balance
* Geography

## 💾 Saved Model

The trained model was saved using Joblib:

```text
best_gradient_boosting_model.pkl
```

A scaler was also saved:

```text
scaler.pkl
```

## 🌐 Streamlit Application

A simple Streamlit interface was developed to allow users to enter customer information and receive a churn prediction.

The application predicts:

* ✅ Customer is likely to stay
* ⚠️ Customer is likely to churn

### Run the Application

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Matplotlib

## 👩‍💻 Internship Project

**Devixo Solutions – AI/ML Internship**
**Task 03: End-to-End Machine Learning Project**
