import streamlit as st

from send_email import send_email

st.set_page_config(
    page_title="Contact Me | Akarsh Katiyar",
    page_icon="📩",
    layout="wide",
)


# -----------------------------
# CONTACT PAGE
# -----------------------------

st.title("📩 Let's Connect")

st.write(
    "Have a question, want to discuss a project, or interested in "
    "working together? Feel free to get in touch."
)

st.markdown("---")


# -----------------------------
# CONTACT INFORMATION
# -----------------------------

contact_col1, contact_col2 = st.columns(
    2,
    gap="large",
)


with contact_col1:
    st.markdown("### Get in Touch")

    st.write("""
        I'm always interested in connecting with people who are working on
        interesting projects, exploring technology, or looking for
        opportunities in software development, data, and AI/ML.
        """)

    st.markdown("**📧 Email**")

    st.write("Send me a message using the form and I'll get back to you.")


with contact_col2:
    st.markdown("### Find Me Online")

    st.write(
        "You can also find me on LinkedIn and GitHub, "
        "where I share my professional journey and projects."
    )

    social_col1, social_col2 = st.columns(
        2,
        gap="medium",
    )

    with social_col1:
        st.link_button(
            "💼 LinkedIn",
            "https://www.linkedin.com/in/akarsh-katiyar-145992347",
            use_container_width=True,
        )

    with social_col2:
        st.link_button(
            "💻 GitHub",
            "https://github.com/AKatheFlame",
            use_container_width=True,
        )


# -----------------------------
# RESUME
# -----------------------------

st.markdown("---")

st.markdown("### 📄 Resume")

st.write(
    "Interested in learning more about my background, projects, "
    "skills, and experience?"
)

with open("resume/Akarsh_Katiyar_Resume.pdf", "rb") as file:
    resume_data = file.read()

st.download_button(
    "📄 Download Resume",
    data=resume_data,
    file_name="Akarsh_Katiyar_Resume.pdf",
    mime="application/pdf",
    use_container_width=True,
)


# -----------------------------
# CONTACT FORM
# -----------------------------

st.markdown("---")

st.markdown("### Send Me a Message")

with st.form(key="email_form"):

    user_email = st.text_input(
        "Your Email Address",
        placeholder="example@email.com",
    )

    raw_message = st.text_area(
        "Your Message",
        placeholder="Write your message here...",
        height=180,
    )

    button = st.form_submit_button(
        "📩 Send Message",
        use_container_width=True,
    )

    if button:

        if not user_email.strip():
            st.error("Please enter your email address.")

        elif "@" not in user_email or "." not in user_email:
            st.error("Please enter a valid email address.")

        elif not raw_message.strip():
            st.error("Please enter a message.")

        else:

            message = f"""Subject: New Portfolio Contact

Visitor Email: {user_email}

Message:
{raw_message}
"""

            try:
                send_email(message)

                st.success(
                    "Your message has been sent successfully. "
                    "Thank you for reaching out!"
                )

            except Exception:
                st.error(
                    "Something went wrong while sending your message. "
                    "Please try again later."
                )
