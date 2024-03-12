import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load data
day_df = pd.read_csv("https://github.com/skadex17/proyek-analisis-data-bangkit2024/blob/main/submission/dataset/day.csv?raw=True")
hour_df = pd.read_csv("https://github.com/skadex17/proyek-analisis-data-bangkit2024/blob/main/submission/dataset/hour.csv?raw=True")

# Define functions for plotting
def plot_monthly_rental(day_df):
    monthly_rental = day_df.groupby(by="month", sort=False).agg({"total_rental": "sum"})
    monthly_rental["total_rental"] /= 1000
    
    plt.figure(figsize=(10, 6))
    plt.bar(monthly_rental.index, monthly_rental["total_rental"], color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Total Rental (in thousands)')
    plt.title('Total Rental by Month (in Thousands)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot()

def plot_seasonly_rental(day_df):
    seasonly_rental = day_df.groupby(by="season", sort=False).agg({"total_rental": "sum"})
    seasonly_rental["total_rental"] /= 1000
    
    plt.figure(figsize=(10, 6))
    plt.bar(seasonly_rental.index, seasonly_rental["total_rental"], color='skyblue')
    plt.xlabel('Season')
    plt.ylabel('Total Rental (in thousands)')
    plt.title('Total Rental by Season (in Thousands)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot()

def plot_weatherly_rental(hour_df):
    weatherly_rental = hour_df.groupby(by="weather", sort=False).agg({"total_rental": "sum"})
    weatherly_rental["total_rental"] /= 1000
    
    plt.figure(figsize=(10, 6))
    plt.bar(weatherly_rental.index, weatherly_rental["total_rental"], color='skyblue')
    plt.xlabel('Weather')
    plt.ylabel('Total Rental (in thousands)')
    plt.title('Total Rental by Weather (in Thousands)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot()

def plot_monthly_yearly_rental(day_df):
    monthly_rental = day_df.groupby(by=["month", "year"], sort=False).agg({"total_rental": "sum"})
    monthly_rental["total_rental"] /= 1000
    
    plt.figure(figsize=(10, 6))
    for year in monthly_rental.index.get_level_values('year').unique():
        data_year = monthly_rental.xs(year, level='year')
        plt.plot(data_year.index.get_level_values('month'), data_year["total_rental"], label=str(year))

    plt.xlabel('Month')
    plt.ylabel('Total Rental (in thousands)')
    plt.title('Total Rental by Month and Year (in Thousands)')
    plt.legend(title='Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot()

# Main content
st.title('Bike Rental Dashboard')

st.subheader('Total Rental by Month')
plot_monthly_rental(day_df)

st.subheader('Total Rental by Season')
plot_seasonly_rental(day_df)

st.subheader('Total Rental by Weather')
plot_weatherly_rental(hour_df)

st.subheader('Total Rental by Month and Year')
plot_monthly_yearly_rental(day_df)
