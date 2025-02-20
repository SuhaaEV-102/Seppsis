import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
with open("sepsis_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Streamlit UI
st.title("Sepsis Prediction App")
st.write("Enter patient details to predict Sepsis")

# Feature names and input fields with validation and sliders
feature_names = ['PRG', 'PL', 'PR', 'SK', 'TS', 'M11', 'BD2', 'Age', 'Insurance']
user_input = []

for feature in feature_names:
    if feature == "Age":
        value = st.slider(f"Enter {feature}", min_value=0, max_value=120, value=30)
    elif feature in ["PRG", "PL", "PR", "SK", "TS", "M11", "BD2"]:
        value = st.slider(f"Enter {feature}", min_value=0.0, max_value=200.0, value=50.0)
    else:
        value = st.number_input(f"Enter {feature}", value=0.0)
    user_input.append(value)

# Optional file upload for automatic input
uploaded_file = st.file_uploader("Upload Medical Report (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

# Show histogram for user reference
if st.checkbox("Show Data Distribution"):
    df = pd.read_csv("Paitients_Files_Train.csv")  # Load sample dataset
    feature_to_plot = st.selectbox("Select Feature to Visualize", feature_names)
    plt.hist(df[feature_to_plot], bins=20, alpha=0.7)
    st.pyplot(plt)

# Predict button
if st.button("Predict"):
    user_array = np.array(user_input).reshape(1, -1)
    processed_input = scaler.transform(user_array)
    prediction = model.predict(processed_input)
    probs = model.predict_proba(processed_input)[0]
    result = "Positive" if prediction[0] == 1 else "Negative"
    
    st.write(f"### Sepsis Prediction: {result}")
    st.write(f"Sepsis Probability: {probs[1]*100:.2f}%")
