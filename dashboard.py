import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency


st.set_page_config(page_title="Dashboard E-commerce by Yohana", page_icon=":bar_chart", layout="wide")
st.title(" :bar_chart: Dashboard E-commerce by Yohana :bar_chart:")
st.header("Dashboard E-Commerce")
st.subheader("Yohana Beatrice Nainggolan, yohanabeatrice1263@gmail.com")
st.subheader("ID: yohanabeatrice")
all_df = pd.read_csv('all_data.csv')

st.title("Sales Dashboard")

# Display the DataFrame
st.subheader("Data Overview")
st.dataframe(all_df)

# Bar chart for customer_state
st.subheader("Customer State Distribution")
state_counts = all_df['customer_state'].value_counts()
st.bar_chart(state_counts)

# Bar chart for customer_city
st.subheader("Customer City Distribution")
city_counts = all_df['customer_city'].value_counts()
st.bar_chart(city_counts)

