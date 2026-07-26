import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1,col2=st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Akarsh Katiyar")
    content="""
My name is Akarsh Katiyar. I have recently completed my B.Tech Computer Science specialization in Artificial Intelligence and Machine Learning.
"""
    st.info(content)

content2="""
Below you can find thwe list of apps that I have build over my education period.
"""
st.write(content2)

col3,col4=st.columns(2)

df=pd.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
