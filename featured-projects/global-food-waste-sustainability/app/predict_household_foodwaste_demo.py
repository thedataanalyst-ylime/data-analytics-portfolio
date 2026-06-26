import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ------------------------------------------------------------
# Load trained model
# ------------------------------------------------------------

model = joblib.load("random_forest_food_waste_model.pkl")

# ------------------------------------------------------------
# App title and description
# ------------------------------------------------------------

st.set_page_config(
    page_title="Global Household Food Waste Predictor",
    layout="centered"
)

st.title("Global Household Food Waste Predictor")

st.write(
    """
    This demo estimates household food waste in kg/capita/year using the 
    Random Forest Regression model developed for the Global Food Waste Analysis.
    """
)

# ------------------------------------------------------------
# User inputs
# ------------------------------------------------------------

st.header("Input Country-Level Indicators")

average_temperature = st.number_input(
    "Average Temperature (°C)",
    min_value=-20.0,
    max_value=40.0,
    value=25.0,
    step=0.5
)

gdp_per_capita = st.number_input(
    "GDP per Capita (US$)",
    min_value=0.0,
    value=10000.0,
    step=500.0
)

population_density = st.number_input(
    "Population Density (# of people per square km)",
    min_value=0.0,
    value=100.0,
    step=10.0
)

food_service_kg_per_capita_year = st.number_input(
    "Food Service Waste (kg/capita/year)",
    min_value=0.0,
    value=20.0,
    step=1.0
)

income_group = st.selectbox(
    "Income Group",
    [
        "High Income",
        "Upper Middle Income",
        "Lower Middle Income",
        "Low Income"
    ]
)

# ------------------------------------------------------------
# Prepare input dataframe
# ------------------------------------------------------------

input_data = pd.DataFrame({
    "average_temperature": [average_temperature],
    "log_gdp_per_capita": [np.log1p(gdp_per_capita)],
    "log_population_density": [np.log1p(population_density)],
    "food_service_kg_per_capita_year": [food_service_kg_per_capita_year],
    "income_group": [income_group]
})

# ------------------------------------------------------------
# Predict
# ------------------------------------------------------------

if st.button("Predict Household Food Waste"):

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    st.metric(
        label="Estimated Household Food Waste",
        value=f"{prediction:.2f} kg/capita/year"
    )

    st.write(
        """
        This prediction should be interpreted as an estimate based on available
        country-level indicators. It does not prove causality and may be less
        accurate for countries with unusually high or low household food waste.
        """
    )

# ------------------------------------------------------------
# Model information
# ------------------------------------------------------------

st.header("Model Summary")

st.write(
    """
    Final model: Random Forest Regression - Round 1  
    n_estimators: 300  
    max_depth: 5  
    min_samples_leaf: 5  
    random_state: 27
    """
)