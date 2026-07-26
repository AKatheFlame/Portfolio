import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="Email_form"):
    user_email = st.text_input("Your E-Mail Address")
    raw_message = st.text_area("Your Message")
    message = f"""Subject: A user contacted

    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button()
    if button:
        send_email(message)
        st.info("Email send successfully.")
