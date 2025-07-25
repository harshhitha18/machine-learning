import streamlit as st
import pandas as pd

st.title("🤖 Machine Learning app")

st.write("This app builds a Machine Learning model")

with st.expander('Data'):
    st.write('**Raw data**')
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
    st.write(df)
