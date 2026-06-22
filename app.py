import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Ensure these paths are correct relative to your app.py
from inferences.predict_freight import predict_freight_cost
from inferences.predict_invoice_flag import predict_invoice_flag

# -----------------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide"
)

# -----------------------------------------------------------------------------
# Header Section
# -----------------------------------------------------------------------------
st.markdown("""
# 📦 Vendor Invoice Intelligence Portal
### AI-Driven Freight Cost Prediction & Invoice Risk Flagging

This internal analytics portal leverages machine learning to:
- **Forecast freight costs accurately**
- **Detect risky or abnormal vendor invoices**
- **Reduce financial leakage and manual workload**
""")

st.divider()

# -----------------------------------------------------------------------------
# Sidebar
# -----------------------------------------------------------------------------
st.sidebar.title("🔍 Model Selection")
selected_model = st.sidebar.radio(
    "Choose Prediction Module",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Business Impact**
- 📊 Improved cost forecasting
- 🛡️ Reduced invoice fraud & anomalies
- ⚙️ Faster finance operations
""")

# -----------------------------------------------------------------------------
# Module 1: Freight Cost Prediction
# -----------------------------------------------------------------------------
if selected_model == "Freight Cost Prediction":
    st.subheader("🚚 Freight Cost Prediction")

    st.markdown("""
    **Objective:**
    Predict freight cost for a vendor invoice using **Quantity** and **Invoice Dollars** 
    to support budgeting and forecasting.
    """)

    with st.form("freight_form"):
        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "📦 Quantity",
                min_value=1,
                value=1200
            )

        with col2:
            dollars = st.number_input(
                "💰 Invoice Dollars",
                min_value=1.0,
                value=18500.0
            )
        
        submit_freight = st.form_submit_button("🔮 Predict Freight Cost")

    if submit_freight:
        # Prepare input for the model
        input_df = pd.DataFrame({
            "Quantity": [quantity],
            "Dollars": [dollars]
        })

        # Calling the inference function
        result = predict_freight_cost(input_df)
        prediction = result['Predicted_Freight']

        st.success("Prediction completed successfully.")
        st.metric(
            label="📊 Estimated Freight Cost",
            value=f"${prediction:,.2f}"
        )

# -----------------------------------------------------------------------------
# Module 2: Invoice Flag Prediction
# -----------------------------------------------------------------------------
else:
    st.subheader("🚨 Invoice Manual Approval Prediction")

    st.markdown("""
    **Objective:**
    Predict whether a vendor invoice should be **flagged for manual approval** 
    based on abnormal cost, freight, or delivery patterns.
    """)

    with st.form("invoice_flag_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            invoice_quantity = st.number_input(
                "Invoice Quantity",
                min_value=1,
                value=50
            )
            
            freight = st.number_input(
                "Freight Cost",
                min_value=0.0,
                value=1.73
            )

        with col2:
            invoice_dollars = st.number_input(
                "Invoice Dollars",
                min_value=1.0,
                value=352.95
            )
            total_item_quantity = st.number_input(
                "Total Item Quantity",
                min_value=1,
                value=162
            )

        with col3:
            total_item_dollars = st.number_input(
                "Total Item Dollars",
                min_value=1.0,
                value=2476.0
            )

        submit_flag = st.form_submit_button("🧠 Evaluate Invoice Risk")

    if submit_flag:
        # Prepare input for the model
        input_df = pd.DataFrame({
            "invoice_quantity": [invoice_quantity],
            "invoice_dollars": [invoice_dollars],
            "Freight": [freight],
            "total_item_quantity": [total_item_quantity],
            "total_item_dollars": [total_item_dollars]
        })

        # Calling the inference function
        flag_result = predict_invoice_flag(input_df)
        flag_prediction = flag_result['Predicted_Flag']

        # Evaluation of result
        if bool(flag_prediction[0]):
            st.error("🚨 Invoice requires **MANUAL APPROVAL**")
            st.warning("Reason: The system detected patterns consistent with high-risk or abnormal invoices.")
        else:
            st.success("✅ Invoice is **SAFE for Auto-Approval**")
            st.info("The invoice parameters fall within normal operational ranges.")