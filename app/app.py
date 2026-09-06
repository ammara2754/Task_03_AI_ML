import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("best_gradient_boosting_model.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Customer Churn Prediction System")

st.write(
    "Enter the customer information below and the trained Gradient Boosting model "
    "will predict whether the customer is likely to leave the bank."
)

st.markdown("---")

# Customer input fields
credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=900,
    value=650
)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=40
)

tenure = st.number_input(
    "Tenure",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.number_input(
    "Balance",
    min_value=0.0,
    value=50000.0
)

num_products = st.number_input(
    "Number of Products",
    min_value=1,
    max_value=4,
    value=1
)

has_cr_card = st.selectbox(
    "Has Credit Card",
    ["Yes", "No"]
)

is_active_member = st.selectbox(
    "Is Active Member",
    ["Yes", "No"]
)

estimated_salary = st.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=50000.0
)

# Feature Engineering
balance_salary_ratio = balance / (estimated_salary + 1)

# Age Group
if age <= 30:
    age_group = "Young"
elif age <= 40:
    age_group = "Adult"
elif age <= 50:
    age_group = "Middle_Age"
else:
    age_group = "Senior"

# Categorical Encoding
geography_germany = 1 if geography == "Germany" else 0
geography_spain = 1 if geography == "Spain" else 0

gender_male = 1 if gender == "Male" else 0

agegroup_adult = 1 if age_group == "Adult" else 0
agegroup_middle_age = 1 if age_group == "Middle_Age" else 0
agegroup_senior = 1 if age_group == "Senior" else 0

# Create the final input data with the exact 15 features
input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_products],
    "HasCrCard": [1 if has_cr_card == "Yes" else 0],
    "IsActiveMember": [1 if is_active_member == "Yes" else 0],
    "EstimatedSalary": [estimated_salary],
    "BalanceSalaryRatio": [balance_salary_ratio],
    "Geography_Germany": [geography_germany],
    "Geography_Spain": [geography_spain],
    "Gender_Male": [gender_male],
    "AgeGroup_Adult": [agegroup_adult],
    "AgeGroup_Middle_Age": [agegroup_middle_age],
    "AgeGroup_Senior": [agegroup_senior]
})

# Prediction button
if st.button("Predict Churn"):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ The customer is likely to churn.")
    else:
        st.success("✅ The customer is likely to stay.")

st.markdown("---")
st.caption("Developed as part of the Devixo Solutions AI/ML Internship Project.")