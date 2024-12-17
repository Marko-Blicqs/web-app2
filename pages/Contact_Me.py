import streamlit as st
from send_email import send_email as eml
import pandas


st.header("Contact me")

submit_message = "No action"
topics = pandas.read_csv("data/topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
        "What's the topic of your email",
        topics
    )
    user_msg = st.text_area("Your message")
    button = st.form_submit_button("Send email")

    if button:
        submit_message = "I was pressed."
        subject = f"{option} from {user_email}"
        eml(sender=user_email ,message=user_msg, subject=subject)
        st.info("Your email was sent.")

#st.write(submit_message)