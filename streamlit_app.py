import streamlit as st
import pandas as pd

st.title("🤖 Machine Learning App")

st.info("This is app builds a machine learning model!")

with st.expander("Data"):
    st.write("***Raw data***")
    df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
    st.write(df)

    st.write("***X***")
    X = df.drop("species", axis=1)
    st.write(X)

    st.write("***y***")
    y = df["species"]
    st.write(y)

with st.expander("Data Visualization"):
    st.scatter_chart(data=df, x="bill_length_mm", y="body_mass_g", color="species")
