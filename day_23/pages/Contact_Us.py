import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("your email address")
    text_message = st.text_area("Your message")
    button = st.form_submit_button()
    if button:
        print("asfasfg")