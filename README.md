##📊 Customer Churn Prediction using Machine Learning

Predict whether a customer is likely to churn based on billing and contract information.

This project uses Logistic Regression and is deployed with Streamlit for real-time interactive predictions.


---


##🚀 Project Objective

Customer churn prediction is a critical business problem in telecom and subscription-based industries. Retaining customers is significantly more cost-effective than acquiring new ones.
This model identifies high-risk customers so businesses can take proactive retention actions.

---

## 🌐 Live Demo

🚀 Try the deployed application here:

[Customer Churn Prediction App](https://customer-churn-prediction-ml-snsradfqmbpcgf9n63uqso.streamlit.app/)

> ⚠️ Note: The application is hosted on Streamlit Community Cloud free tier and may take a few seconds to wake up after inactivity.
---

##📁 Dataset Features

The model uses the following input features:

Tenure (Months) – Duration of customer relationship

Monthly Charges – Current monthly billing amount

Total Charges – Lifetime spending by the customer

Contract Type – Month-to-Month, One Year, Two Year

Target Variable:

Churn (0 = No, 1 = Yes)


---


##🔎 Exploratory Data Analysis (EDA) Insights

Customers with month-to-month contracts show higher churn rates.

Customers with low tenure are more likely to churn.

Higher monthly charges increase churn probability.

Dataset shows moderate class imbalance.

---



##🧠 Model Details

Algorithm: Logistic Regression

Custom Threshold Used: 0.4

Reason: To improve churn recall while maintaining reasonable precision

##📊 Model Performance
Metric	Value
Accuracy	~79%
Precision (Churn)	58%
Recall (Churn)	71%
ROC-AUC Score	0.86

The threshold was tuned to balance business impact between false positives and false negatives.


---


##📌 Confusion Matrix
[[423  95]
 [ 54 133]]

✅ True Positives (Correctly predicted churners): 133

❌ False Negatives (Missed churners): 54

✅ True Negatives: 423

❌ False Positives: 95

The model captures 71% of actual churners, which is valuable for retention strategies.


---


##💻 Deployment (Streamlit App)

The project includes a simple interactive web app built using Streamlit.

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py
📦 Project Structure
customer-churn-prediction-ml/
│
├── model.ipynb          # EDA + Model Training
├── app.py               # Streamlit Web Application
├── churn_model.pkl      # Trained Model
├── requirements.txt
└── README.md

---


##📈 Business Value

Helps businesses identify high-risk customers

Enables targeted retention campaigns

Reduces revenue loss due to churn

Improves customer lifetime value (CLV)


---



##🔮 Future Improvements

Implement Random Forest / XGBoost

Perform K-Fold Cross Validation

Advanced Feature Engineering

Deploy on Cloud (Streamlit Cloud / Render / AWS)

Add Feature Importance Visualization


---


👨‍💻 Author

Anuj
B.Tech CSE (AI & ML)
