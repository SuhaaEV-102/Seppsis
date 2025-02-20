import streamlit as st
import pickle
import numpy as np

# Load trained model and scaler
with open("sepsis_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Streamlit UI
st.title("Sepsis Prediction App")
st.write("Enter patient details to predict Sepsis")

# Input fields
feature_names = ['PRG', 'PL', 'PR', 'SK', 'TS', 'M11', 'BD2', 'Age', 'Insurance']
user_input = []
for feature in feature_names:
    user_input.append(st.number_input(f"Enter {feature}", value=0.0))

# Predict button
if st.button("Predict"):
    user_array = np.array(user_input).reshape(1, -1)
    processed_input = scaler.transform(user_array)
    prediction = model.predict(processed_input)
    result = "Positive" if prediction[0] == 1 else "Negative"
    st.write(f"### Sepsis Prediction: {result}")
