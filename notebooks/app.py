import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df_carros = pd.read_csv("vehicles_us.csv")

st.header("Análisis de vehículos")

build_histogram = st.checkbox('Histograma')
hist_button = st.button('Construir histograma')
build_disp = st.checkbox('Diagrama de dispersión')
disp_button = st.button("Construir diagrama de dispersión")

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write("Selecciona" + str(" '") + "Construir histograma" + str("' ") +
             "para construir un histograma para la columna odómetro")

    # Lógica a ejecutar cuando se hace clic en el botón
    if hist_button:
        # Escribir un mensaje en la aplicación
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
        fig = go.Figure(data=[go.Histogram(x=df_carros['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
        fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, use_container_width=True)


if build_disp:  # si la casilla de verificación está seleccionada
    st.write(
        "Selecciona" + str(" '") + "Construir diagrama de dispersión" + str("' ") + "para construir un diagrama de dispersión para las columnas odómetro y precio")
    if disp_button:
        # Escribir un mensaje en la aplicación
        st.write(
            'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un diagrama de dispersión utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
        fig = go.Figure(data=[go.Scatter(
            x=df_carros['odometer'], y=df_carros['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
        fig.update_layout(title_text='Distribución del Odómetro vs precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, use_container_width=True)
