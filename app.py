import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="CarDash", page_icon=":car:")

st.header('CarDash: Interactive Car Sales Insights')
st.subheader('Explore trends and insights into car sales data, focusing on different vehicle types and their features.')

df = pd.read_csv('vehicles_us.csv')

# Sidebar for filters
st.sidebar.header('Filter Options')
selected_year = st.sidebar.slider('Select Model Year', int(df['model_year'].min()), int(df['model_year'].max()), int(df['model_year'].median()))
selected_type = st.sidebar.multiselect('Select Vehicle Type', options=df['type'].unique(), default=df['type'].unique())
selected_fuel = st.sidebar.multiselect('Select Fuel Type', options=df['fuel'].unique(), default=df['fuel'].unique())
selected_transmission = st.sidebar.multiselect('Select Transmission Type', options=df['transmission'].unique(), default=df['transmission'].unique())

# Filtering data based on sidebar selection
filtered_data = df[
    (df['model_year'] == selected_year) & 
    (df['type'].isin(selected_type)) & 
    (df['fuel'].isin(selected_fuel)) & 
    (df['transmission'].isin(selected_transmission))
]

# Layout with columns for histograms and scatter plots
col1, col2 = st.columns(2)

with col1:
    fig_price = px.histogram(filtered_data, x='price', title='Price Distribution for Selected Vehicles')
    st.plotly_chart(fig_price, use_container_width=True)

with col2:
    fig_mileage = px.scatter(filtered_data, x='odometer', y='price', color='condition', title='Price vs. Mileage Analysis')
    st.plotly_chart(fig_mileage, use_container_width=True)

# Display statistical summaries
st.sidebar.header("Statistical Summary:")
st.sidebar.metric("Average Price", f"${filtered_data['price'].mean():,.2f}")
st.sidebar.metric("Average Mileage", f"{filtered_data['odometer'].mean():,.0f} miles")
st.sidebar.metric("Max Price", f"${filtered_data['price'].max():,.2f}")
st.sidebar.metric("Min Price", f"${filtered_data['price'].min():,.2f}")

# Interactive checkbox to toggle additional analysis
if st.checkbox('Show Detailed Statistical Analysis'):
    st.subheader('Detailed Statistics')
    st.write(filtered_data.describe())