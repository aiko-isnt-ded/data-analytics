import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

# Title of the page
st.title("Titanic Data Visualization")
df = pd.read_csv("train.csv")
st.dataframe(df)

# General Statistical Data
st.header("General Statistical Measures of the Data")
st.write(df[df.columns[[5,6,7,9]]].describe())
p = (f"There were {df.shape[0]} passengers aboard: {df['Pclass'].value_counts()[1]} of them were upper class, {df['Pclass'].value_counts()[2]} middle class, and {df['Pclass'].value_counts()[3]} lower class.")
a = (f"The average passenger aged {round(df['Age'].mean())}, and their ages ranged from {math.floor(df['Age'].min())} to {round(df['Age'].max())} years-old.")
t = (f"The average ticket fare was £{df['Fare'].mean():.2f} pounds, and the maximum amount paid was £{df['Fare'].max():.2f}.")
st.write(p)
st.write(a)
st.write(t)

# General Data Analysis
st.header("General Data Analysis")
# Class
st.subheader("Passengers by Class")
fig, ax = plt.subplots()
ax.hist(df["Pclass"], bins=20)
st.pyplot(fig)
st.markdown("The passengers travelling in the Titanic were mostly from the lower class, twice the amount as the other groups.")
# Sex
st.subheader("Passengers by Sex")
fig, ax = plt.subplots()
ax.hist(df["Sex"])
st.pyplot(fig)
st.markdown("The passengers aboard the Titanic were mostly men, almost doubling the amount of women in the ship.")
# Age
st.subheader("Passengers by Age")
fig, ax = plt.subplots()
ax.hist(df["Age"], bins=20)
st.pyplot(fig)
st.markdown("Most of the passengers travelling in the Titanic aged 20 to 30 years-old. There were also more children than elderly.")
# Sibs to Spouses
st.subheader("Siblings to Spouses Ratio")
fig, ax = plt.subplots()
ax.hist(df["SibSp"], bins=20)
st.pyplot(fig)
st.markdown("There were more spouses than siblings aboard the Titanic ship, as shown by the data concentration in the range 0 to 1.")
st.markdown("If the opposite were true (more siblings than spouses), the numerator would overwhelm the denominator, resulting in bigger values.")
# Parents to Children Ratio
st.subheader("Parents to Children Ratio")
fig, ax = plt.subplots()
ax.hist(df["Parch"], bins=20)
st.pyplot(fig)
st.markdown("The value of 0 in this graphs stands for those children who were not accompanied by their parents. The large concentration of data in this range shows that most of the children aboard the ship travelled with nannys or other people.")
st.markdown("Thus, there were more children than parents aboard the ship.")
# Fare
st.subheader("Ticket Fare")
fig, ax = plt.subplots()
ax.hist(df["Fare"], bins=20)
st.pyplot(fig)
st.markdown("Most of the passengers aboard the Titanic purchased their tickets below £100 pounds. This represents more than 700 people.")

# Data Analysis by Class
st.header("Data Analysis by Class")
upper = df[df["Pclass"] == 1]
middle = df[df["Pclass"] == 2]
lower = df[df["Pclass"] == 3]
# Ticket Fare by upper class
st.subheader("Ticket Fare Paid by Upper Class")
fig, ax = plt.subplots()
ax.hist(upper["Fare"], bins=20)
st.pyplot(fig)
st.markdown("As shown by the graph above, most of the passengers travelling in upper class paid around £25 to £75 for their tickets in the Titanic.")
st.markdown("There’s also a possible outlier, who paid £500 for their ticket.")

#st.markdown("")