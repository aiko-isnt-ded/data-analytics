import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Titanic Data Visualization")
st.header("This is a header")
st.markdown("*italic*")

df = pd.read_csv("train.csv")
st.dataframe(df)

st.header("General Statistical Measures of the Data")
df.describe()

st.markdown(f"There were {df.value_counts} passengers aboard: 
            {df['Pclass'].value_counts()[1]} of them were upper class, 
            {df['Pclass'].value_counts()[2]} middle class, and 
            {df['Pclass'].value_counts()[3]} of them were lower class")
st.markdown(f"")
st.markdown(f"")