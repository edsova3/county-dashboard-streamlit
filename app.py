# Streamlit dashboard for county-level socioeconomic analysis
# Covers Southern Ohio counties and Greenup County, KY

# Import required libraries
import streamlit as st
import pandas as pd

st.markdown("### Reigonal Economic Overview: Southern Ohio + Greenup County, KY")

# import excel data sheet
df = pd.read_excel("2.0 county data for tableau.xlsx")

df = df.set_index("County")

avg_income = df["median_income"].mean()

# abbreviates names to make shorter
df.index = df.index.str.replace(" County", "", regex=False)
df.index = df.index.str.replace(", Ohio", " (OH)", regex=False)
df.index = df.index.str.replace(", Kentucky", " (KY)", regex=False)

st.title("5 County Dashboard")

county = st.selectbox(
	"Select a county",
	df.index)


st.write("You selected:", county)

st.subheader("County Data")

# Compare selected county median income to regional average
if df.loc[county, "median_income"] > avg_income:
	st.success(f"{county} has ABOVE average median income for the region.")
else:
	st.warning(f"{county} has BELOW average median income for the region.")

st.write("Population (2025):", f"{df.loc[county, 'population_2025']:,}")
st.write("Median Income:", f"${df.loc[county, 'median_income']:,}")
st.write("Unemployment (2022):", f"{df.loc[county, 'unemployment_2022']}%")

# sets up bar charts
st.subheader("Comparison Across Counties")

st.subheader("Population by County")
st.bar_chart(df["population_2025"])

st.subheader("Median Income by County")
st.bar_chart(df["median_income"])

st.subheader("Population Change (%)")
st.bar_chart(df["population_change_pct"])

st.subheader("Unemployment Rate by County")
st.bar_chart(df["unemployment_2022"])






