import streamlit as st
from send_email import send_email as eml


st.header("Contact me")

submit_message = "No action"

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_msg = st.text_area("Your message")
    button = st.form_submit_button("Send email")

    if button:
        submit_message = "I was pressed."
        eml(sender=user_email ,message=user_msg, subject=f"Email from {user_email}")
        st.info("Your email was sent.")

st.write(submit_message)