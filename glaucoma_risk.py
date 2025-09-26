import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open("log_reg_model.pkl", "rb"))

st.title("Glaucoma Prediction App")
st.write("Fill in the patient details below and click **Predict** to check for glaucoma.")

# Sidebar input fields
st.sidebar.header("Patient Information")

# Input fields based on dataset
age = st.sidebar.slider("Age", min_value=20, max_value=90, value=40)
cdr = st.sidebar.slider("CDR (Cup-to-Disc Ratio)", min_value=0.3, max_value=0.9, value=0.5, step=0.01)
iop = st.sidebar.slider("IOP (Intraocular Pressure)", min_value=10, max_value=40, value=20)
rnfl = st.sidebar.slider("RNFL Thickness", min_value=70, max_value=120, value=95)

gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
diabetes = st.sidebar.selectbox("Diabetes", ("Yes", "No"))
hypertension = st.sidebar.selectbox("Hypertension", ("Yes", "No"))

# Encode categorical variables
gender_encoded = 1 if gender == "Male" else 0
diabetes_encoded = 1 if diabetes == "Yes" else 0
hypertension_encoded = 1 if hypertension == "Yes" else 0

# Collect inputs into dataframe
input_data = pd.DataFrame({
    "Age": [age],
    "CDR": [cdr],
    "IOP": [iop],
    "RNFL": [rnfl],
    "Gender": [gender_encoded],
    "Diabetes": [diabetes_encoded],
    "Hypertension": [hypertension_encoded]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.write("The predicted diagnosis: **Glaucoma**")
    else:
        st.write("The predicted diagnosis: **No Glaucoma**")

# Instructions at the bottom
st.write("""
### Instructions
1. Use the sidebar to enter the patient's details.
2. Adjust the sliders for Age, CDR (Cup-to-Disc Ratio), IOP (Intraocular Pressure), and RNFL Thickness.
3. Select appropriate options for Gender, Diabetes, and Hypertension.
4. Click the **Predict** button to see the predicted diagnosis.
""")

