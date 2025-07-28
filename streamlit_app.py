import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🤖 Machine Learning app")

st.write("This app builds a Machine Learning model")

with st.expander('Data'):
    st.write('**Raw data**')
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
    st.write(df)

    # X-axis selection
    st.write("**Select X-Axis Column**")
    x_axis = st.selectbox("Choose a column for the X-axis:", options=df.columns, index=2)  # Default to 'bill_length_mm'
    st.write(f"Selected X-axis: {x_axis}")

    # Y-axis selection
    st.write("**Select Y-Axis Column**")
    y_axis = st.selectbox("Choose a column for the Y-axis:", options=df.columns, index=5)  # Default to 'body_mass_g'
    st.write(f"Selected Y-axis: {y_axis}")

    # Scatter plot visualization with Plotly
    if x_axis and y_axis:
        st.write("**Scatter Plot**")
        fig = px.scatter(df, x=x_axis, y=y_axis, color="species", title=f"{y_axis} vs {x_axis}")
        st.plotly_chart(fig)

with st.expander('Data Visualization'):
    st.write("**Additional Scatter Plot**")
    st.scatter_chart(data=df, x="bill_length_mm", y="bill_depth_mm", color="species")
