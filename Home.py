import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Akarsh Katiyar | Portfolio",
    page_icon="🖥️",
    layout="wide",
)


# -----------------------------
# CUSTOM STYLING
# -----------------------------

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    p {
        line-height: 1.7;
    }

    [data-testid="stImage"] img {
        max-width: 350px;
        margin-left: auto;
        margin-right: auto;
    }

    .stLinkButton a,
    .stDownloadButton button,
    .stFormSubmitButton button {
        border-radius: 8px;
    }

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
            padding-top: 1rem;
        }

        h1 {
            font-size: 2rem !important;
        }

        h2 {
            font-size: 1.6rem !important;
        }

        h3 {
            font-size: 1.3rem !important;
        }

        p {
            font-size: 0.95rem;
        }

        [data-testid="stImage"] img {
            max-width: 100%;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------


def display_project(row, featured=False):
    """
    Display a project card using information from data.csv.
    """

    with st.container(border=True):

        st.image(
            "Images/" + row["image"],
            use_container_width=True,
        )

        if featured:
            st.markdown(f"### {row['title']}")
        else:
            st.markdown(f"#### {row['title']}")

        st.write(row["description"])

        st.caption(f"📂 {row['category']}")

        st.caption(f"🛠️ {row['technologies']}")

        github_url = row["github"]
        demo_url = row["demo"]

        # Treat empty CSV cells as unavailable links
        has_github = pd.notna(github_url) and str(github_url).strip() != ""

        has_demo = pd.notna(demo_url) and str(demo_url).strip() != ""

        if has_github and has_demo:

            button_col1, button_col2 = st.columns(2)

            with button_col1:
                st.link_button(
                    "💻 GitHub",
                    github_url,
                    use_container_width=True,
                )

            with button_col2:
                st.link_button(
                    "🚀 Live Demo",
                    demo_url,
                    use_container_width=True,
                )

        elif has_github:

            st.link_button(
                "💻 GitHub",
                github_url,
                use_container_width=True,
            )

        elif has_demo:

            st.link_button(
                "🚀 Live Demo",
                demo_url,
                use_container_width=True,
            )


# -----------------------------
# HERO SECTION
# -----------------------------

col1, col2 = st.columns(
    [1.5, 1],
    gap="large",
)

with col1:

    st.markdown("# Hi, I'm Akarsh Katiyar 👋")

    st.markdown("""
        ### Computer Science Student | Python Developer | Data & AI/ML

        I build practical projects to turn ideas into working solutions,
        while continuously learning and exploring new technologies.
        """)

    st.write("")

    button_col1, button_col2 = st.columns(2)

    with button_col1:
        st.link_button(
            "📝 View My Projects",
            "#projects",
            use_container_width=True,
        )

    with button_col2:
        st.link_button(
            "📩 Contact Me",
            "/Contact_Me",
            use_container_width=True,
        )


with col2:

    st.image(
        "Images/photo.jpg",
        use_container_width=True,
    )


# -----------------------------
# ABOUT SECTION
# -----------------------------

st.markdown("---")

st.markdown("## About Me")

about_col1, about_col2 = st.columns(
    [1.5, 1],
    gap="large",
)

with about_col1:

    st.markdown("""
        I'm currently pursuing my **Computer Science degree** and have been
        exploring different areas of technology through hands-on projects.

        Rather than limiting myself to a single area, I've worked across
        **software development, data analytics, automation, web scraping,
        machine learning, and deep learning**. Working on these projects has
        helped me understand how different technologies can come together to
        solve practical problems.

        I enjoy the process of taking an idea, figuring out how to implement it,
        debugging the things that don't work, and eventually turning it into
        something useful.

        I'm currently focused on strengthening my technical foundation,
        building more real-world projects, and growing toward a career in
        **Software Development, Data Analytics, and AI/ML**.
        """)


with about_col2:

    st.markdown("### What I enjoy")

    st.markdown("""
        -  Building software and applications
        -  Working with data and finding insights
        -  Exploring AI and Machine Learning
        -  Solving technical problems
        -  Turning ideas into practical projects
        -  Learning new technologies
        """)


# -----------------------------
# SKILLS SECTION
# -----------------------------

st.markdown("---")

st.markdown("## Skills")

st.write(
    "Technologies and tools I've worked with while building projects "
    "and developing my technical skills."
)

skill_col1, skill_col2, skill_col3 = st.columns(
    3,
    gap="large",
)


with skill_col1:

    st.markdown("### 💻 Programming")

    st.markdown("""
        - **Python**
        - **Java**
        - **SQL**
        - **HTML & CSS**
        - **JavaScript**
        """)


with skill_col2:

    st.markdown("### 📊 Data & AI")

    st.markdown("""
        - **Pandas**
        - **NumPy**
        - **Matplotlib**
        - **Plotly**
        - **Scikit-learn**
        - **Machine Learning**
        - **Deep Learning**
        """)


with skill_col3:

    st.markdown("### 🛠️ Tools & Development")

    st.markdown("""
        - **Streamlit**
        - **Git & GitHub**
        - **Jupyter**
        - **VS Code**
        - **Web Scraping**
        - **Data Visualization**
        - **Virtual Environments**
        """)


# -----------------------------
# PROJECTS SECTION
# -----------------------------

st.markdown("---")

st.markdown(
    '<h2 id="projects">Projects</h2>',
    unsafe_allow_html=True,
)

st.write(
    "A selection of projects I've built while learning, "
    "experimenting, and applying my technical skills."
)


# -----------------------------
# LOAD PROJECT DATA
# -----------------------------

df = pd.read_csv(
    "data.csv",
    sep=";",
)


# -----------------------------
# FEATURED PROJECTS
# -----------------------------

st.markdown("### ⭐ Featured Projects")

st.write(
    "Some of the projects that best represent my experience "
    "with software development, data, Python, and AI/ML."
)


featured_projects = df[df["featured"].astype(str).str.lower() == "true"]


featured_col1, featured_col2 = st.columns(
    2,
    gap="large",
)


for position, (_, row) in enumerate(featured_projects.iterrows()):

    current_col = featured_col1 if position % 2 == 0 else featured_col2

    with current_col:
        display_project(
            row,
            featured=True,
        )


# -----------------------------
# OTHER PROJECTS
# -----------------------------

st.markdown("---")

st.markdown("### Other Projects")

st.write("More projects and experiments from my development journey.")


other_projects = df[df["featured"].astype(str).str.lower() != "true"]


project_col1, project_col2, project_col3 = st.columns(
    3,
    gap="medium",
)


for position, (_, row) in enumerate(other_projects.iterrows()):

    if position % 3 == 0:
        current_col = project_col1

    elif position % 3 == 1:
        current_col = project_col2

    else:
        current_col = project_col3

    with current_col:
        display_project(
            row,
            featured=False,
        )


# -----------------------------
# CONNECT SECTION
# -----------------------------

st.markdown("---")

st.markdown("## Let's Connect")

st.write(
    "Interested in my work, have an opportunity, or just want to connect? "
    "Feel free to reach out."
)


connect_col1, connect_col2, connect_col3, connect_col4 = st.columns(
    4,
    gap="medium",
)


with connect_col1:

    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/akarsh-katiyar-145992347",
        use_container_width=True,
    )


with connect_col2:

    st.link_button(
        "💻 GitHub",
        "https://github.com/AKatheFlame",
        use_container_width=True,
    )


with connect_col3:

    with open(
        "resume/Akarsh_Katiyar_Resume.pdf",
        "rb",
    ) as file:
        resume_data = file.read()

    st.download_button(
        "📄 Download Resume",
        data=resume_data,
        file_name="Akarsh_Katiyar_Resume.pdf",
        mime="application/pdf",
        use_container_width=True,
    )


with connect_col4:

    st.link_button(
        "📩 Contact Me",
        "/Contact_Me",
        use_container_width=True,
    )
