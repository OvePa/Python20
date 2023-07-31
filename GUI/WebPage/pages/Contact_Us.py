import streamlit as st
from send_email import send_email
import pandas as pd

st.header("Contact Us")

df = pd.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Email:")
    option = st.selectbox("What topic do you want to discuss?", df["topic"])
    message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {option}
{message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")
