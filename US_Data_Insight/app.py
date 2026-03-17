import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('US_honey_dataset_updated.csv')

if "pages" not in st.session_state:
    st.session_state.pages = "Home"

st.header('US Honey Production Data Insights')
st.write(" ")


st.sidebar.header("Menu")
if st.sidebar.button("Home"):
    st.session_state.pages = "Home"
if st.sidebar.button("Filtered Data"):
    st.session_state.pages = "Filtered Data"
if st.sidebar.button("Insights"):
    st.session_state.pages = "Insights"
if st.sidebar.button("Visualizations"):
    st.session_state.pages = "Visualizations"


# Home Page
if st.session_state.pages == "Home":
    st.subheader('Dataset Overview')
    st.write(" ")

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


# Filtered Data Page
if st.session_state.pages == "Filtered Data":

    st.subheader("Filtered Data")
    st.write(" ")

    col1, col2 = st.columns(2)

    with col1:
        state_option = st.selectbox(
            "Select State",
            options=["All"] + sorted(df["state"].unique())
        )

    with col2:
        year_option = st.selectbox(
            "Select Year",
            options=["All"] + sorted(df["year"].unique())
        )

    filtered_df = df.copy()

    if state_option != "All":
        filtered_df = filtered_df[filtered_df["state"] == state_option]

    if year_option != "All":
        filtered_df = filtered_df[filtered_df["year"] == year_option]

    st.write("### Filtered Dataset")
    st.dataframe(filtered_df[["state", "year", "production"]])
    
    
# Visualizations Page
if st.session_state.pages == "Visualizations":
    st.subheader("Visualizations")
    st.write(" ")

    col1, col2 = st.columns(2)

    with col1:
        state_option = st.multiselect(
            "Select State",
            options=["All"] + sorted(df["state"].unique())
        )
    pivot = pd.pivot_table(df, values='production', index='year', columns='state', aggfunc='sum')
    data = pivot[state_option] if state_option else pivot[["Alabama"]]
    data.plot(kind='bar', figsize=(16, 10))
    plt.title("Production by Year for Selected States")
    plt.xlabel("Year")
    plt.ylabel("Production")
    plt.grid(True)
    st.pyplot(plt)