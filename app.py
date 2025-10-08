import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')
st.header('Gráficos de vehiculos')
st.subheader('Click al botón para Gráficar - Histogramas')
hist_button = st.button('Graficar')

if hist_button:
    st.write('Creacion de un histograma para el conjunto de datos anuncios de ventas de coches')

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)

st.subheader('Click al botón para Gráficar - Dispersión')
dis_button = st.button('Gráficar')

if dis_button:
    st.write('Creación de grafico de dispersion')

    fig2 = px.scatter(car_data, x='odometer',y='price')

    st.plotly_chart(fig2, use_container_width=True)