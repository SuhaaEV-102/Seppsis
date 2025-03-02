import streamlit as st
import streamlit.components.v1 as components

# Navigation Menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Signup", "Login", "Prediction"])

def load_html(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return f.read()

if page == "Home":
    st.title("Sepsis Foresee - Home")
    home_html = load_html("index.html")
    components.html(home_html, height=700, scrolling=True)

elif page == "About":
    st.title("About Sepsis Foresee")
    about_html = load_html("about.html")
    components.html(about_html, height=700, scrolling=True)

elif page == "Signup":
    st.title("Signup Page")
    signup_html = load_html("signup.html")
    components.html(signup_html, height=700, scrolling=True)

elif page == "Login":
    st.title("Login Page")
    login_html = load_html("login.html")
    components.html(login_html, height=700, scrolling=True)

elif page == "Prediction":
    st.title("Sepsis Prediction")
    prediction_html = load_html("Prediction.html")
    components.html(prediction_html, height=800, scrolling=True)
