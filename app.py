import streamlit as st
import pickle
import numpy as np

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #1a1a2e;
            color: white;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align: center;
            color: #f1c40f;
            font-size: 36px;
            font-weight: bold;
        }
        .subheader {
            text-align: center;
            font-size: 20px;
            margin-bottom: 20px;
        }
        .feature-box {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s;
        }
        .feature-box:hover {
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Load the trained model and scaler
@st.cache_resource
def load_model():
    with open("sepsis_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_model()

# Navigation Menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Signup", "Login", "Prediction", "About"])

if page == "Home":
    st.markdown("<h1 class='title'>Sepsis Foresee</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subheader'>Your AI-powered solution for early sepsis detection.</p>", unsafe_allow_html=True)

elif page == "About":
    st.markdown("<h1 class='title'>Why Sepsis Foresee?</h1>", unsafe_allow_html=True)
    st.write("Sepsis Foresee is an AI-based platform designed to predict sepsis at an early stage, providing life-saving insights.")

    # Features Section
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='feature-box'><h3>Early Detection</h3><p>Quick and accurate predictions to help doctors take immediate action.</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='feature-box'><h3>AI-Powered Analysis</h3><p>Advanced machine learning algorithms ensure precision and reliability.</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='feature-box'><h3>Easy to Use</h3><p>User-friendly interface with a seamless experience.</p></div>", unsafe_allow_html=True)

    st.markdown("<h2 style='color: #f1c40f;'>Our Mission</h2>", unsafe_allow_html=True)
    st.write("We strive to reduce sepsis-related deaths by providing a powerful and efficient AI-driven detection tool for healthcare professionals.")

    st.markdown("<a href='#' style='color: #f1c40f; text-decoration: none; font-size: 16px;'>← Back to Home</a>", unsafe_allow_html=True)

elif page == "Signup":
    st.title("Signup Page")
    st.write("Coming soon...")

elif page == "Login":
    st.title("Login Page")
    st.write("Coming soon...")

elif page == "Prediction":
    st.title("Sepsis Prediction")
    st.write("Enter patient details below for sepsis prediction.")

    # Input fields
    feature_names = ['PRG', 'PL', 'PR', 'SK', 'TS', 'M11', 'BD2', 'Age', 'Insurance']
    user_input = []
    for feature in feature_names:
        user_input.append(st.number_input(f"Enter {feature}", value=0.0))

    # Predict button
    if st.button("Predict"):
        input_array = np.array(user_input).reshape(1, -1)
        scaled_input = scaler.transform(input_array)
        prediction = model.predict(scaled_input)
        result = "Positive Sepsis" if prediction[0] == 1 else "Negative Sepsis"
        st.write(f"### Prediction: {result}")
