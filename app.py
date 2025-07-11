import streamlit as st
from auth import create_users_table, add_user, login_user
from ai_module import get_solution
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

# Setup DB
create_users_table()

# Theme toggle
theme = st.sidebar.radio("Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
        .stApp { background-color: #121212; color: white; }
        </style>
    """, unsafe_allow_html=True)

st.title("🧠 AI Disease Diagnosis System")

# Authentication system
menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Account", menu)

if choice == "Sign Up":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    if st.button("Sign Up"):
        add_user(new_user, new_password)
        st.success("You have successfully created an account")
        st.info("Go to Login to access your account")

elif choice == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    if st.button("Login"):
        user = login_user(username, password)
        if user:
            st.success(f"Welcome {username}")

            # Disease Diagnosis
            st.subheader("Enter your disease to get AI advice:")
            disease = st.text_input("Enter Disease")
            if st.button("Get AI Solution"):
                if disease.strip() == "":
                    st.warning("⚠️ Please enter a disease name.")
                else:
                    solution = get_solution(disease)
                    if solution:
                        st.info(f"💡 AI Suggestion:\n\n{solution}")
                    else:
                        st.error("⚠️ No response from AI. Check your API key or network.")
        else:
            st.error("Incorrect Username/Password")
