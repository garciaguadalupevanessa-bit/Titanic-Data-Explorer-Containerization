# 🚢 Titanic Data Explorer & Containerization

Selector de idioma / Language selector:  
👉 [Castellano / Spanish](#castellano) | [English](#english)

---

<a name="castellano"></a>
## 🇪🇸 Castellano

¡Bienvenido/a a mi proyecto de exploración y análisis de datos del Titanic! Esta es una aplicación interactiva construida con Streamlit para analizar los factores clave que determinaron la supervivencia de los pasajeros. Además, el proyecto está completamente contenerizado con Docker para asegurar su portabilidad absoluta.

### 📊 El Proyecto y la Limpieza de Datos
Para lograr un análisis preciso, realicé un proceso exhaustivo de Análisis Exploratorio de Datos (EDA) con Python y Pandas:
* Gestión de Valores Nulos: Identificación y tratamiento de datos faltantes en columnas críticas como la edad (imputación basada en medianas).
* Transformación de Variables: Conversión de variables categóricas (como el género y puerto de embarque) a formatos óptimos.
* Visualización Interactiva: Utilizando Plotly, desarrollé 3 gráficos dinámicos que permiten filtrar la información por clase, género y edad en tiempo real.

### 🛠️ Tecnologías Utilizadas
* Python 3.11
* Streamlit
* Pandas & Plotly
* Docker & WSL Ubuntu
* Git & GitHub

### 🐳 Contenerización con Docker
El proyecto incluye una configuración optimizada de Docker:
1. .dockerignore: Excluye carpetas pesadas como el entorno virtual (venv/), garantizando una construcción ligera de la imagen.
2. Dockerfile: Estructurado siguiendo las mejores prácticas de optimización de capas para aprovechar al máximo la caché.

Como ejecutar localmente con Docker:
- Para construir la imagen: docker build -t titanic-explorer .
- Para ejecutar el contenedor: docker run -p 8501:8501 titanic-explorer

Navega en tu explorador a http://localhost:8501.

### 🌐 Despliegue en Docker Hub
La imagen está publicada de forma pública en Docker Hub. Puedes descargarla directamente con el comando: docker pull vanessagg/titanic-explorer:v1.0

---

<a name="english"></a>
## 🇬🇧 English

Interactive Titanic Data Explorer built with Streamlit, Pandas, and Plotly. Fully containerized using Docker and deployed on Docker Hub for seamless portability and real-time data analysis.

### 📊 Project & Data Cleaning
To ensure accurate insights, I performed a thorough Exploratory Data Analysis (EDA) using Python and Pandas:
* Handling Missing Values: Identified and treated missing data in critical columns such as age (using median imputation).
* Variable Transformation: Converted categorical variables (like gender and embarkation port) into optimal visualization formats.
* Interactive Visualization: Developed 3 dynamic charts using Plotly, allowing real-time filtering by passenger class, gender, and age.

### 🛠️ Technologies Used
* Python 3.11
* Streamlit
* Pandas & Plotly
* Docker & WSL Ubuntu
* Git & GitHub

### 🐳 Containerization with Docker
The project includes an optimized Docker environment setup:
1. .dockerignore: Configured to exclude heavy directories like the virtual environment (venv/), keeping the build light.
2. Dockerfile: Structured following best practices for layer optimization to maximize Docker caching mechanisms.

How to run locally with Docker:
- To build the image: docker build -t titanic-explorer .
- To run the container: docker run -p 8501:8501 titanic-explorer

Open your browser and navigate to http://localhost:8501.

### 🌐 Docker Hub Deployment
The production-ready image is publicly available on Docker Hub. You can pull it using the command: docker pull vanessagg/titanic-explorer:v1.0
