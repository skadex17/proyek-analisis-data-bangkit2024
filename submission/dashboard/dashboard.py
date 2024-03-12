import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load data
day_df = pd.read_csv("day_mod.csv")
hour_df = pd.read_csv("hour_mod.csv")

# Define functions for plotting
def plot_monthly_rental(day_df):
    monthly_rental = day_df.groupby(by="month", sort=False).agg({"total_rental": "sum"}).reset_index()
    monthly_rental["total_rental"] /= 1000
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="month", y="total_rental", data=monthly_rental, ax=ax, color='skyblue')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Rental (in thousands)')
    ax.set_title('Total Rental by Month (in Thousands)', fontsize=16)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig)

def plot_seasonly_rental(day_df):
    seasonly_rental = day_df.groupby(by="season", sort=False).agg({"total_rental": "sum"}).reset_index()
    seasonly_rental["total_rental"] /= 1000
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="season", y="total_rental", data=seasonly_rental, ax=ax, color='skyblue')
    ax.set_xlabel('Season')
    ax.set_ylabel('Total Rental (in thousands)')
    ax.set_title('Total Rental by Season (in Thousands)', fontsize=16)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig)

def plot_weatherly_rental(hour_df):
    weatherly_rental = hour_df.groupby(by="weather", sort=False).agg({"total_rental": "sum"}).reset_index()
    weatherly_rental["total_rental"] /= 1000
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x="weather", y="total_rental", data=weatherly_rental, ax=ax, color='skyblue')
    ax.set_xlabel('Weather')
    ax.set_ylabel('Total Rental (in thousands)')
    ax.set_title('Total Rental by Weather (in Thousands)', fontsize=16)
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig)

def plot_monthly_yearly_rental(day_df):
    monthly_rental = day_df.groupby(by=["month", "year"], sort=False).agg({"total_rental": "sum"}).reset_index()
    monthly_rental["total_rental"] /= 1000
    
    fig, ax = plt.subplots(figsize=(10, 6))
    for year in monthly_rental['year'].unique():
        data_year = monthly_rental[monthly_rental['year'] == year]
        sns.lineplot(data=data_year, x='month', y='total_rental', label=str(year), ax=ax)
    
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Rental (in thousands)')
    ax.set_title('Total Rental by Month and Year (in Thousands)', fontsize=16)
    ax.legend(title='Year')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(fig)

# Sidebar
st.sidebar.title("Date Range Selector")
min_date = pd.to_datetime(day_df['date']).min().date()
max_date = pd.to_datetime(day_df['date']).max().date()
start_date = st.sidebar.date_input("Start Date", min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input("End Date", min_value=min_date, max_value=max_date, value=max_date)

# Filter data based on selected date range
filtered_day_df = day_df[(pd.to_datetime(day_df['date']).dt.date >= start_date) & 
                         (pd.to_datetime(day_df['date']).dt.date <= end_date)]
filtered_hour_df = hour_df[(pd.to_datetime(hour_df['date']).dt.date >= start_date) & 
                           (pd.to_datetime(hour_df['date']).dt.date <= end_date)]

# Main content
st.title('Bike Rental Dashboard')

st.subheader('Total Rental by Month')
plot_monthly_rental(filtered_day_df)

st.subheader('Total Rental by Season')
plot_seasonly_rental(filtered_day_df)

st.subheader('Total Rental by Weather')
plot_weatherly_rental(filtered_hour_df)

st.subheader('Total Rental by Month and Year')
plot_monthly_yearly_rental(filtered_day_df)