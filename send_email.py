import smtplib
import ssl

import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = st.secrets["email"]["username"]
    password = st.secrets["email"]["password"]
    receiver = st.secrets["email"]["receiver"]

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        host,
        port,
        context=context,
    ) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
