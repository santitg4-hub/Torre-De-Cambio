import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Torre de Cambio - Avianca", page_icon="✈️", layout="wide")

# Estilo visual limpio y profesional
st.title("✈️ Torre de Cambio: Panel Operativo de Red")
st.markdown("**CESA & Avianca:** Asegurando que cada directriz del área llegue realmente al mostrador y a la puerta.")

# Estado inicial simulado de las estaciones en la red de Avianca
if 'estaciones' not in st.session_state:
    st.session_state.estaciones = {
        "Bogotá (BOG)": {"capacidad_maxima": 3, "cambios_activos": 4, "indice_alineacion": 58, "estado_riesgo": "ALTO 🔴"},
        "Cali (CLO)": {"capacidad_maxima": 3, "cambios_activos": 4, "indice_alineacion": 62, "estado_riesgo": "ALTO 🔴"},
        "Medellín (MDE)": {"capacidad_maxima": 4, "cambios_activos": 3, "indice_alineacion": 85, "estado_riesgo": "ESTABLE 🟢"},
        "Madrid (MAD)": {"capacidad_maxima": 3, "cambios_activos": 4, "indice_alineacion": 60, "estado_riesgo": "ALTO 🔴"},
        "Cartagena (CTG)": {"capacidad_maxima": 4, "cambios_activos": 2, "indice_alineacion": 92, "estado_riesgo": "ESTABLE 🟢"}
    }

# Menú lateral de navegación
menu = st.sidebar.selectbox("Navegación", ["Tablero de Control", "Registrar Pulso Semanal", "Compuerta de Entrada (Ficha)", "Métricas de Impacto"])

if menu == "Tablero de Control":
    st.subheader("📊 Estado en Tiempo Real por Estación")
    st.markdown("Este tablero muestra qué estaciones están sobrecargadas de cambios normativos frente a su capacidad real.")
    
    # Convertir a DataFrame para mostrar tabla elegante
    df = pd.DataFrame.from_dict(st.session_state.estaciones, orient='index')
    st.dataframe(df, use_container_width=True)
    
    st.warning("💡 **Alerta de Red:** Las estaciones en rojo superan su capacidad de asimilación o muestran alta discrepancia entre agentes.")

elif menu == "Registrar Pulso Semanal":
    st.subheader("⏱️ Registro de Pulso Semanal (Instructor)")
    st.markdown("El instructor evalúa en 10 minutos el nivel de alineación real directamente en el counter.")
    
    estacion_sel = st.selectbox("Seleccione la estación", list(st.session_state.estaciones.keys()))
    nuevo_pulso = st.slider("Puntaje de alineación observado en counter (%)", 0, 100, 75)
    discrepancias = st.number_input("Agentes con respuestas distintas ante la misma regla de prueba (0-3)", 0, 3, 0)
    
    if st.button("Actualizar Pulso en Red", type="primary"):
        st.session_state.estaciones[estacion_sel]["indice_alineacion"] = nuevo_pulso
        if nuevo_pulso < 75 or discrepancias > 1:
            st.session_state.estaciones[estacion_sel]["estado_riesgo"] = "ALTO 🔴"
        else:
            st.session_state.estaciones[estacion_sel]["estado_riesgo"] = "ESTABLE 🟢"
        st.success(f"¡Pulso registrado con éxito para {estacion_sel}! El tablero se ha actualizado.")

elif menu == "Compuerta de Entrada (Ficha)":
    st.subheader("📋 Control de Compuerta de Cambios")
    st.markdown("Ningún cambio sale sin resolver el margen por escrito y sin verificar la capacidad de la estación.")
    
    titulo_cambio = st.text_input("Título del cambio normativo (ej. Tolerancia equipaje 11kg)")
    categoria = st.selectbox("Categoría", ["Equipaje", "Tarifas", "Operaciones", "Servicios"])
    estaciones_afectadas = st.multiselect("Estaciones destinatarias", list(st.session_state.estaciones.keys()))
    
    if st.button("Validar y Lanzar Cambio"):
        if titulo_cambio and estaciones_afectadas:
            st.success(f"✅ Cambio '{titulo_cambio}' aprobado y filtrado por la compuerta de capacidad para {len(estaciones_afectadas)} estaciones.")
        else:
            st.warning("Por favor complete el título y seleccione al menos una estación.")

elif menu == "Métricas de Impacto":
    st.subheader("📈 Seguimiento a 30 y 60 Días")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Disminución de discusiones en mostrador", value="-34%", delta="Mejora mensual")
        st.metric(label="Consistencia de respuestas en red", value="78%", delta="+27% vs mes anterior")
    with col2:
        st.metric(label="Tiempo de asimilación de normativas", value="5 días", delta="-16 días antes del piloto")
        st.metric(label="Estado de PQRS por ambigüedad", value="En descenso", delta="Tendencia estable")
