import streamlit as st
from prediction_helper import predict  # Linked to prediction_helper.py

# Set the page configuration and title
st.set_page_config(page_title="CredSecure AI: Credit Risk Classification", page_icon="📊", layout="wide")

# Custom CSS to inject the exact UI design details from your screenshots
st.markdown("""
    <style>
    /* 1. Base Application Background Gradient (Matching original screenshots) */
    .stApp {
        background: radial-gradient(circle at top right, #1d4ed8 0%, #0c192e 60%, #09101e 100%) !important;
        color: #f0f4f8;
    }

    /* Ensure clean typography colors */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* 2. Styling for Input Fields & Dropdowns */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: #1a2238 !important;
        border: 1px solid #283655 !important;
        border-radius: 4px !important;
    }

    /* 3. Highlighting the + and - Number Step Buttons with Blue Background */
    button[data-testid="stNumberInputStepUp"], 
    button[data-testid="stNumberInputStepDown"] {
        background-color: #1d4ed8 !important;
        color: #ffffff !important;
        border: none !important;
    }
    button[data-testid="stNumberInputStepUp"]:hover, 
    button[data-testid="stNumberInputStepDown"]:hover {
        background-color: #2563eb !important;
    }

    /* 4. Styling for custom card metric boxes (Loan to Income & Risk Assessment Results) */
    .metric-card {
        background-color: #111a2e;
        border: 1px solid #1e3a8a;
        border-radius: 8px;
        padding: 20px;
        margin-top: 10px;
    }
    .metric-label {
        font-size: 14px;
        color: #94a3b8;
        font-weight: 500;
        margin-bottom: 6px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: bold;
        color: #3b82f6;
    }

    /* 5. Styling the Risk Calculation Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        color: white;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(90deg, #4338ca 0%, #6d28d9 100%);
        color: white;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Centered Title & Subtitle
st.markdown("<h1 style='text-align: center; color: white;'>CredSecure AI: Credit Risk Classification</h1>",
            unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size: 16px; margin-top: -10px;'>AI-driven credit risk scoring for smarter lending decisions</p>",
    unsafe_allow_html=True)
st.write("---")

# ----------------------------------------------------
# 1. Borrower Profile Section
# ----------------------------------------------------
st.markdown("### 🎯 Borrower Profile")
col1_1, col1_2, col1_3 = st.columns(3)

with col1_1:
    age = st.number_input('Age', min_value=18, step=1, max_value=100, value=25)
with col1_2:
    income = st.number_input('Income', min_value=0, value=1000000)
with col1_3:
    loan_amount = st.number_input('Loan Amount', min_value=0, value=2000000)

st.write("")

# ----------------------------------------------------
# 2. Financial Metrics Section
# ----------------------------------------------------
st.markdown("### 💳 Financial Metrics")
col2_1, col2_2, col2_3 = st.columns(3)

# Calculate Loan to Income Ratio dynamically
loan_to_income_ratio = loan_amount / income if income > 0 else 0

with col2_1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Loan to Income Ratio</div>
            <div class="metric-value">{loan_to_income_ratio:.2f}</div>
        </div>
    """, unsafe_allow_html=True)
with col2_2:
    loan_tenure_months = st.number_input('Loan Tenure (months)', min_value=0, step=1, value=12)
with col2_3:
    avg_dpd_per_delinquency = st.number_input('Avg DPD', min_value=0, value=0)

st.write("")

# ----------------------------------------------------
# 3. Credit Behavior Section
# ----------------------------------------------------
st.markdown("### 📊 Credit Behavior")
col3_1, col3_2, col3_3 = st.columns(3)

with col3_1:
    delinquency_ratio = st.number_input('Delinquency Ratio (%)', min_value=0, max_value=100, step=1, value=0)
with col3_2:
    credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%)', min_value=0, max_value=100, step=1,
                                               value=50)
with col3_3:
    num_open_accounts = st.number_input('Open Loan Accounts', min_value=1, max_value=4, step=1, value=1)

st.write("")

# ----------------------------------------------------
# 4. Loan Details Section
# ----------------------------------------------------
st.markdown("### 🏡 Loan Details")
col4_1, col4_2, col4_3 = st.columns(3)

with col4_1:
    residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
with col4_2:
    loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
with col4_3:
    loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])

st.write("")
st.write("")

# ----------------------------------------------------
# Risk Assessment Trigger and Boxed Output Display
# ----------------------------------------------------
if st.button('CALCULATE RISK'):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.write("---")
    st.markdown("### 📝 Risk Assessment Results")

    res_col1, res_col2, res_col3 = st.columns(3)

    # Each output parameter is explicitly boxed with a metric-card block boundary
    with res_col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Default Probability</div>
                <div class="metric-value">{probability:.2%}</div>
            </div>
        """, unsafe_allow_html=True)

    with res_col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Credit Score</div>
                <div class="metric-value">{credit_score}</div>
            </div>
        """, unsafe_allow_html=True)

    with res_col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Rating</div>
                <div class="metric-value">{rating}</div>
            </div>
        """, unsafe_allow_html=True)