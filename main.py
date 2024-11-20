import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('data/air_quality.csv')

# Display data in the app
st.title('Air Quality Analytics')
st.write(df)

geo_place= st.selectbox('Place Name', df['Geo Place Name'].unique())
filtered_data = df[df['Geo Place Name'] == geo_place]

fig = px.bar(filtered_data, x='Geo Place Name', y='Data Value', title=f"Air Quality in {geo_place}")
st.plotly_chart(fig)
