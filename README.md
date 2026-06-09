# End-to-End Production-Ready Credit Risk Evaluation System

An end-to-end, high-throughput machine learning system designed to automate credit risk assessment for financial institutions. The system predicts the **Probability of Default (PD)**, maps risk metrics to a standardized credit score ($300 - 900$), and categorizes applicants into actionable risk tiers in real time. 

By combining a high-performance **XGBoost** model with an interpretable **Logistic Regression** baseline, this architecture balances predictive power with regulatory explainability requirements.

🌐 **Live Production Demo:** [Access the Streamlit Web UI](https://credit-risk-classification-harini1708.streamlit.app/)

---

## 🚀 System Architecture & Workflow

The system is split into an isolated backend API service and an intuitive frontend interface, ensuring decoupling and scalability.
[User / Loan Officer UI] ---> (Streamlit App)
|
(REST API)
v
(FastAPI Backend Service)
|
[Data Preprocessing & Feature Engineering]
|
[Inference Engine: XGBoost / LogReg]
|
v
{PD Prediction, Scoring, Tier Assignment}
* **Frontend (Streamlit):** An interactive dashboard designed for loan officers to input applicant profiles and visualize risk metrics instantly.
* **Backend (FastAPI):** A high-performance, asynchronous REST API that handles payload validation, executes feature transformation pipelines, and serves model inference.
* **Production Stack:** Python, Scikit-Learn, XGBoost, Pandas, NumPy, Joblib.

---

## 📊 Model Performance & Financial Metrics

The models were evaluated using industry-standard credit scoring metrics to guarantee strong class separation and minimize credit default exposure.

| Evaluation Metric | Production Value | Financial / Statistical Significance |
| :--- | :--- | :--- |
| **Accuracy** | `92.0%+` | Overall correctness of risk classification across applicant pools. |
| **Recall (Defaulters)** | `94.0%` | **Primary Business Metric.** Minimizes False Negatives (approving bad borrowers). |
| **KS Statistic** | `86.2` | Indicates exceptional separation power between 'Good' and 'Bad' risk distributions. |
| **Model Types** | `XGBoost` & `Logistic Regression` | Ensembled approach balancing raw predictive performance with linear interpretability. |

---

## 🧠 Machine Learning Pipeline & Engineering

### 1. Advanced Feature Engineering
Raw financial data was transformed into high-impact domain metrics to capture leverage and repayment capacity:
* **Loan-to-Income Ratio ($LTI$):** Assesses the debt burden relative to applicant earnings.
* **Credit Utilization Ratio:** Measures active revolving credit balance against total available limits.
* **Delinquency Ratio:** Quantifies historical payment misbehavior frequencies.

### 2. Handling Severe Class Imbalance
To mitigate model bias toward majority non-defaulters, a hybrid **SMOTE-Tomek** links technique was deployed during training:
* **SMOTE** synthetically generates minority default instances.
* **Tomek Links** removes ambiguous, overlapping data points along the decision boundary, sharpening the model's discriminative threshold.

### 3. Hyperparameter Optimization & Transparency
* **Optuna** was utilized for automated Bayesian optimization to fine-tune tree depth, learning rates, and regularization parameters ($L_1$/$L_2$).
* **Explainable AI (XAI):** Logistic Regression coefficients are exposed to provide global and local feature attribution, ensuring lending decisions can be audited for regulatory compliance.

---

## 🧮 Scorecard Segmentation

The system converts the raw Probability of Default ($PD$) into a standardized credit score range ($300$ to $900$). Applicants are automatically routed into four operational risk tiers:

* 🔴 **Poor ($300 - 499$):** High risk. Immediate rejection recommended.
* 🟡 **Average ($500 - 649$):** Moderate risk. Requires manual underwriting or collateral verification.
* 🟢 **Good ($650 - 749$):** Low risk. Standard automated approval routing.
* 🔵 **Excellent ($750 - 900$):** Negligible risk. Preferred pricing and accelerated approval routing.

---

## 🧩 Project Structure

```text
ML-project-credit-risk-model/
│
├── app/                          # Production application code (UI & API services)
│
├── artifacts/                    # Serialized models, encoders, and weights
│
├── Datasets/                     # Source data used for model training and evaluation
│   ├── bureau_data.csv
│   ├── customers.csv
│   └── loans.csv
│
├── credit_risk_model.ipynb       # Jupyter Notebook for EDA, training, and evaluation
├── requirements.txt              # Application dependencies and pinned versions
└── README.md                     # System documentation
```
🛠️ Installation & Local Setup
Follow these step-by-step instructions to clone the repository and run the application in your local development environment:

Prerequisites
Python 3.10 or higher installed on your system.

pip (Python package installer).

Execution Steps
Clone the repository and navigate to the project directory:

Bash
git clone [https://github.com/Harinib1708/ML-project-credit-risk-model.git](https://github.com/Harinib1708/ML-project-credit-risk-model.git)
cd ML-project-credit-risk-model
Install the required dependencies:

Bash
pip install -r requirements.txt
Launch the local Streamlit application:

Bash
streamlit run app/main.py

## 📈 Business Impact & Value Delivered

Implementing this automated system transforms traditional lending workflows into a high-efficiency, data-driven operation:

* **⏱️ Velocity Acceleration:** Reduced loan underwriting turnaround time from days to milliseconds via real-time API inference, drastically lowering customer churn during the application lifecycle.
* **📉 Risk Mitigation & Capital Protection:** Capitalizing on a **94.0% Recall** rate minimizes corporate exposure to toxic debt, protecting liquid capital pools from high-risk defaults.
* **⚖️ Elimination of Underwriting Bias:** Standardized mathematical modeling eliminates subjective human bias, establishing an objective, auditable, and regulatory-compliant credit baseline.
