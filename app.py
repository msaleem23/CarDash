import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('vehicles_us.csv')
df.head()
df.describe()

fig_price = px.histogram(df, x='price', title='Distribution of Vehicle Prices')
fig_price.show()
fig_mileage = px.histogram(df, x='odometer', title='Distribution of Vehicle Mileage')
fig_mileage.show()

scatter_price_mileage = px.scatter(df, x='odometer', y='price', color='condition',
                                   title='Price vs. Mileage by Vehicle Condition')
scatter_price_mileage.show()

scatter_year_price = px.scatter(df, x='model_year', y='price', color='condition',
                                title='Year vs. Price by Vehicle Condition')
scatter_year_price.show()
