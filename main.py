import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Load Dataset
st.title("Streamlit Assessment Project - Bank Churn Data")

#data_path = "C:\\Users\\user\\OneDrive\\Dokumen\\GitHub\\clone\\streamlit_inceptionv3\\bank_churn_data.csv"
data_path = "bank_churn_data.csv" if os.path.exists("bank_churn_data.csv") else "/mnt/data/bank_churn_data.csv"
df = pd.read_csv(data_path)
df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces in column names

# Display Data Overview
st.header("Dataset Overview")
st.write(df.head())
st.write("Shape of the dataset:", df.shape)
#st.write("Columns in dataset:", df.columns.tolist())

# Basic Components
st.header("Basic Components")
if 'user_id' in df.columns:
    user_id = st.selectbox("Select User ID:", df['user_id'].unique())
else:
    st.error("Column 'user_id' not found in dataset. Please check column names.")
    st.stop()

age = st.slider("Filter by Age:", int(df['customer_age'].min()), int(df['customer_age'].max()), (20, 60))
credit_limit = st.slider("Filter by Credit Limit:", int(df['credit_limit'].min()), int(df['credit_limit'].max()), (500, 20000))

filtered_df = df[(df['customer_age'].between(*age)) & (df['credit_limit'].between(*credit_limit))]

st.write("Filtered Data:", filtered_df.head())

# Interactive Visualization
st.header("Interactive Visualization")
fig = px.histogram(filtered_df, x='customer_age', nbins=30, title='Age Distribution of Customers')
st.plotly_chart(fig)

fig2 = px.scatter(filtered_df, x='credit_limit', y='total_trans_amt', color='attrition_flag', 
                  title='Credit Limit vs Total Transaction Amount')
st.plotly_chart(fig2)

# Deployment Message
st.header("Deployment")
st.write("This app is deployed on Streamlit Cloud.")
st.markdown("[GitHub Repository](https://github.com/MuhammadRivaldiAsyhari/streamlit_projek)")