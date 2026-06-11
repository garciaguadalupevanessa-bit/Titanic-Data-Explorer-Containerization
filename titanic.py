import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la pestaña del navegador
st.set_page_config(page_title="Titanic Explorer", page_icon="🚢", layout="wide")

# 2. Carga inteligente de datos (usamos la URL oficial del dataset)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    data = pd.read_csv(url)
    # Creamos la columna del tamaño familiar que analizamos en el cuaderno
    data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
    return data

df = load_data()

# 3. Menú lateral de navegación
st.sidebar.title("Navigation")
opcion_menu = st.sidebar.radio(
    "Ir a:",
    ["Inicio", "Explorador", "Gráficos", "Acerca de"]
)

# ==========================================
# SECCIÓN 1: INICIO (Tu pantalla actual)
# ==========================================
if opcion_menu == "Inicio":
    
    # Título e introducción con el emoji del barco
    st.title("🚢 Titanic Explorer")
    st.markdown("""
    Bienvenido al explorador interactivo del dataset del **RMS Titanic**.  
    Usa el menú lateral izquierdo para navegar entre las secciones.
    """)
    
    st.markdown("---")
    
    # Título del bloque de tarjetas
    st.subheader("Resumen global del dataset")
    
    # Cálculos matemáticos en tiempo real basados en el DataFrame
    total_pasajeros = len(df)
    supervivientes = int(df['Survived'].sum())
    no_supervivientes = total_pasajeros - supervivientes
    tasa_supervivencia = (supervivientes / total_pasajeros) * 100
    
    # Creamos 4 columnas para pintar las tarjetas numéricas gigantes
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total de pasajeros", f"{total_pasajeros}")
    m2.metric("Supervivientes", f"{supervivientes}")
    m3.metric("No supervivientes", f"{no_supervivientes}")
    m4.metric("Tasa de supervivencia", f"{tasa_supervivencia:.1f}%")
    
    st.markdown("---")
    
    # Sección inferior de información
    st.subheader("¿Qué encontrarás en esta app?")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.info("**🔍 Explorador**\n\nFiltra los pasajeros por clase, sexo, edad y puerto de embarque. Revisa los datos en tiempo real.")
        
    with c2:
        st.success("**📊 Gráficos**\n\nVisualizaciones interactivas sobre supervivencia, distribución de edades, tarifas y correlaciones.")
        
    with c3:
        st.warning("**ℹ️ Acerca de**\n\nContexto histórico del Titanic, descripción de las variables y fuente del dataset.")

# ==========================================
# SECCIÓN 2: GRÁFICOS (Tus 3 gráficas dinámicas)
# ==========================================
elif opcion_menu == "Gráficos":
    st.title("📊 Visualizaciones Dinámicas del Titanic")
    st.markdown("Usa los filtros de aquí abajo para cambiar las 3 gráficas simultáneamente en tiempo real.")
    
    # Filtros interactivos en la parte superior
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        sex_filter = st.multiselect("Filtrar por Género:", df['Sex'].unique(), default=list(df['Sex'].unique()))
    with col_f2:
        class_filter = st.multiselect("Filtrar por Clase:", sorted(df['Pclass'].unique()), default=list(df['Pclass'].unique()))
        
    # Aplicamos los filtros al dataframe que usarán los gráficos
    df_filtered = df[df['Sex'].isin(sex_filter) & df['Pclass'].isin(class_filter)]
    
    # Distribución en rejilla (Fila 1: Dos columnas)
    g1, g2 = st.columns(2)
    
    with g1:
        st.markdown("#### 1. Supervivencia por Clase Social")
        fig1 = px.histogram(df_filtered, x="Pclass", color="Survived", barmode="group",
                            color_discrete_map={0: '#e63946', 1: '#4a90e2'},
                            labels={"Pclass": "Clase", "Survived": "Destino"},
                            category_orders={"Pclass": [1, 2, 3]})
        fig1.update_layout(xaxis={'type': 'category'})
        st.plotly_chart(fig1, width='stretch')
        
    with g2:
        st.markdown("#### 2. Distribución de Edades y Supervivencia")
        fig2 = px.histogram(df_filtered, x="Age", color="Survived", marginal="box",
                            color_discrete_map={0: '#e63946', 1: '#4a90e2'},
                            labels={"Age": "Edad", "Survived": "Destino"}, nbins=30)
        st.plotly_chart(fig2, width='stretch')
        
    st.markdown("---")
    
    # Fila 2: Gráfica horizontal completa para la curva familiar
    st.markdown("#### 3. Tasa de Supervivencia por Tamaño de Familia")
    if not df_filtered.empty:
        fam_df = df_filtered.groupby('FamilySize')['Survived'].mean().reset_index()
        fig3 = px.line(fam_df, x="FamilySize", y="Survived", markers=True, 
                       color_discrete_sequence=['purple'],
                       labels={"FamilySize": "Miembros de la familia", "Survived": "Probabilidad de salvarse"})
        fig3.update_yaxes(tickformat=".0%")
        st.plotly_chart(fig3, width='stretch')
    else:
        st.error("No hay datos para mostrar con la combinación de filtros seleccionada.")

# ==========================================
# SECCIONES RESTANTES (Estructura vacía para rellenar después)
# ==========================================
elif opcion_menu == "Explorador":
    st.title("🔍 Explorador de Datos")
    st.markdown("Aquí colocaremos la tabla interactiva para buscar pasajeros.")
    st.dataframe(df)

elif opcion_menu == "Acerca de":
    st.title("ℹ️ Acerca de la investigación")
    st.markdown("Aquí pondremos el contexto histórico y la documentación de las variables.")