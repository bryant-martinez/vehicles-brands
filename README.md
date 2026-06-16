## Vehicles-brands analysis by streamline

#Aplicación web interactiva desarrollada con Python y Streamlit para visualizar y analizar datos de anuncios de venta de vehículos en Estados Unidos.

Descripción del proyecto

Este proyecto permite explorar un conjunto de datos de vehículos mediante visualizaciones interactivas creadas con Plotly.
La aplicación ofrece:

Histograma de distribución del odómetro.
Diagrama de dispersión entre odómetro y precio.
Interfaz interactiva usando Streamlit.

El objetivo principal es practicar análisis exploratorio de datos (EDA) y desarrollo de aplicaciones web para ciencia de datos.

Tecnologías utilizadas
Python
Pandas
Streamlit
Plotly
Estructura del proyecto
vehicles-brands/
│
├── app.py
├── vehicles_us.csv
├── notebooks/
└── README.md
Instalación
Clona este repositorio:
git clone https://github.com/bryant-martinez/vehicles-brands.git
Accede al directorio del proyecto:
cd vehicles-brands
Instala las dependencias:
pip install -r requirements.txt
Ejecución de la aplicación

Ejecuta el siguiente comando en la terminal:

streamlit run app.py
Funcionalidades
Histograma

Permite visualizar la distribución del kilometraje (odómetro) de los vehículos registrados en el conjunto de datos.

Diagrama de dispersión

Muestra la relación entre el precio y el odómetro de los vehículos.

Dataset

El proyecto utiliza un conjunto de datos de anuncios de venta de vehículos en Estados Unidos, almacenado en el archivo:

vehicles_us.csv
Objetivos de aprendizaje
Manipulación de datos con Pandas.
Visualización de datos con Plotly.
Desarrollo de aplicaciones web con Streamlit.
Implementación de interfaces interactivas para análisis de datos.
Autor

Bryant Martinez

Proyecto desarrollado como parte de prácticas de análisis de datos y ciencia de datos.