# 1. IMAGEN BASE: Partimos de Python 3.11 ligero
FROM python:3.11-slim

# 2. DIRECTORIO DE TRABAJO: Nos movemos a la carpeta /app del contenedor
WORKDIR /app

# 3. COPIAR DEPENDENCIAS: Llevamos el archivo requirements antes para usar la caché
COPY requirements.txt .

# 4. INSTALAR DEPENDENCIAS: Descarga e instala las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# 5. COPIAR EL RESTO DEL PROYECTO: Llevamos tu código y páginas al contenedor
COPY . .

# 6. EXPONER EL PUERTO: El puerto por defecto que usa Streamlit
EXPOSE 8501

# 7. COMANDO DE ARRANQUE: Arranca tu archivo original expuesto hacia afuera
CMD ["streamlit", "run", "titanic.py", "--server.address=0.0.0.0", "--server.port=8501"]
