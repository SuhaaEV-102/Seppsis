import streamlit as st

# Navigation Bar
st.markdown("""
<nav style="background-color:#1a1a2e; padding:10px; text-align:center;">
    <a style="color:#f1c40f; font-size:20px; margin-right:20px;" href='#home'>Home</a>
    <a style="color:#f1c40f; font-size:20px; margin-right:20px;" href='#signup'>Signup</a>
    <a style="color:#f1c40f; font-size:20px; margin-right:20px;" href='#login'>Login</a>
    <a style="color:#f1c40f; font-size:20px;" href='#prediction'>Prediction</a>
</nav>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("<h1 style='color:#f1c40f; text-align:center;'>Sepsis Foresee</h1>", unsafe_allow_html=True)
st.write("Your AI-powered solution for early sepsis detection.")

# About Section
st.subheader("Why Sepsis Foresee?")
st.write("Sepsis Foresee is an AI-based platform designed to predict sepsis at an early stage, providing life-saving insights.")

# Features
st.markdown("### Features")
st.write("- **Early Detection**: Quick and accurate predictions.")
st.write("- **AI-Powered Analysis**: Advanced ML algorithms ensure precision.")
st.write("- **User-Friendly**: Simple and easy-to-use interface.")
