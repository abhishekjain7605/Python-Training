import pandas as pd 
import streamlit as st

df = pd.read_csv("US_honey_dataset_updated.csv")

total_production = df["production"].sum()
total_state = df["state"].nunique()
avg_production = int(df["production"].mean())

max_state = df.groupby("state")["production"].sum().idxmax()
max_value = df.groupby("state")["production"].sum().max()
min_value = df.groupby("state")["production"].sum().min()

# row 1

col1, col2, col3 = st.columns(3)
col1.metric("Total Production", f"{total_production}")
col2.metric("Total States", total_state)
col3.metric("Average Production", f"{avg_production}")

# row 2
col4, col5, col6 = st.columns(3)
col4.metric("State with Highest Production", max_state)
col5.metric("Highest Production", f"{max_value}")
col6.metric("Lowest Production", f"{min_value}")

# sidebar
st.sidebar.header("Filter by State")
state_options = df["state"].unique()
selected_state = st.sidebar.selectbox("Select a state", state_options)
