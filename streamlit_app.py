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

# Data preparations
with st.sidebar:
    st.header('Input features')
   
    island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
    bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
    bill_depth_mm = st.slider('Bill_depth (mm)', 13.1, 21.5, 17.2)
    flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
    body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
    gender = st.selectbox('Gender', ('male', 'female'))

# Create a DataFrame for the input features
data = {
    'island': island,
    'bill_length_mm': bill_length_mm,
    'bill_depth_mm': bill_depth_mm,
    'flipper_length_mm': flipper_length_mm,
    'body_mass_g': body_mass_g,
    'gender': gender
}
input_df = pd.DataFrame(data, index=[0])

# Concatenate with existing DataFrame X
input_penguins = pd.concat([input_df, X], axis=0)

# Optional: Display the updated DataFrame
with st.expander("Updated Data with New Input"):
    st.write("***Input Penguins***")
    st.write(input_penguins)
