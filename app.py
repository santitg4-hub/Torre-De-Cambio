import streamlit as st
import pandas as pd

# Configuración general de la página
st.set_page_config(page_title="Torre de Cambio - Avianca", page_icon="✈️", layout="wide")

# Estilos visuales personalizados (Estética corporativa rojo Avianca)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1, h2, h3 { color: #d32f2f !important; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button {
        background-color: #d32f2f;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #b71c1c;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal inspirado en la diapositiva 7
st.markdown("### LA SOLUCIÓN")
st.title("✈️ Torre de Cambio: tres instrumentos y una regla")
st.markdown("---")

# Pestañas de navegación superiores (Igual que en tus diapositivas)
tab_home, tab_ficha, tab_pulso, tab_tablero = st.tabs([
    "🏠 Inicio (Los 3 Instrumentos)", 
    "1️⃣ Ficha (Compuerta)", 
    "2️⃣ Pulso Semanal", 
    "3️⃣ Tablero de Red"
])

with tab_home:
    st.subheader("Estructura del Modelo Operativo")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #d32f2f 0%, #c2185b 100%); padding: 25px; border-radius: 10px; color: white; text-align: center;">
            <h3>1 Ficha</h3>
            <p>Obliga a resolver el margen por escrito antes de salir a la red.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #d32f2f 0%, #c2185b 100%); padding: 25px; border-radius: 10px; color: white; text-align: center;">
            <h3>2 Pulso</h3>
            <p>Mide en el puesto de trabajo, de forma semanal y ágil.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #d32f2f 0%, #c2185b 100%); padding: 25px; border-radius: 10px; color: white; text-align: center;">
            <h3>3 Tablero</h3>
            <p>Adopción y carga visibles en tiempo real por estación.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.info("💡 **Navega por las pestañas superiores** para interactuar con cada instrumento del sistema en tiempo real durante tu presentación.")

with tab_ficha:
    st.subheader("Instrumento 1: Ficha de Cambio (Compuerta de Capacidad)")
    st.markdown("Ninguna regla con margen sale sin resolverlo por escrito[cite: 11].")
    
    with st.form("form_ficha"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            # Opciones estructuradas en lugar de texto libre
            politica = st.selectbox("¿Qué cambia y desde cuándo?", [
                "Máx. 10 kg en cabina, tarifa Light internacional. Desde 27 ene 2026",
                "Tolerancia de equipaje deportivo y maletas de mano - Tarifa Classic",
                "Lineamiento de baterías de litio y dispositivos en bodega"
            ])
            razon = st.selectbox("Por qué cambia", [
                "Nueva política de equipaje unificada en las Américas",
                "Optimización de tiempos de embarque en puerta",
                "Estandarización regulatoria internacional"
            ])
        with col_f2:
            tipo_regla = st.radio("Tipo de regla", ["Regla dura", "Regla con margen"])
            criterio = st.selectbox("Criterio único obligatorio", [
                "11 kg en tarifa que incluye cabina",
                "La maleta no entra en el medidor por poco",
                "Pasabordo y sistema no coinciden (Decisión por escrito)"
            ])
            
        estaciones_ficha = st.multiselect(
            "Estaciones alcancé (Piloto)",
            ["BOG Bogotá", "MDE Medellín", "CLO Cali", "CTG Cartagena", "MAD Madrid", "MIA Miami"],
            default=["BOG Bogotá", "MDE Medellín"]
        )
        
        btn_ficha = st.form_submit_button("Validar y Registrar Ficha en Compuerta")
        if btn_ficha:
            st.success(f"✅ Ficha aprobada y validada para {len(estaciones_ficha)} estaciones. Compuerta superada sin saturar la red.")

with tab_pulso:
    st.subheader("Instrumento 2: Registro de Pulso en Puesto de Trabajo")
    st.markdown("Menos de 2 minutos por levantamiento en el celular del instructor (10 min por semana/estación)[cite: 12].")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        estacion_pulso = st.selectbox("Estación a auditar", ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "MAD Madrid"])
        semana = st.selectbox("Semana de evaluación", ["Semana 45 - 2 nov 2026", "Semana 46", "Semana 47"])
        cambio_eval = st.selectbox("Política evaluada", ["Equipaje de mano (regla con margen)", "Baterías de litio", "Documentos de viaje"])
        
    with col_p2:
        st.markdown("### Verificación en Puesto (5 observaciones)")
        obs_conformes = st.slider("Observaciones conformes en counter (de 5)", 0, 5, 4)
        
        st.markdown("### Prueba de Consistencia (3 Agentes)")
        resp_a = st.selectbox("Agente Turno A", ["Acepta / Coincide", "No coincide"])
        resp_b = st.selectbox("Agente Turno B", ["Acepta / Coincide", "No coincide"])
        resp_c = st.selectbox("Agente Turno C", ["Acepta / Coincide", "No coincide"])

    if st.button("Registrar Pulso Semanal"):
        st.success(f"📊 Pulso registrado para {estacion_pulso}. Los datos se han sincronizado con el Tablero de Red.")

with tab_tablero:
    st.subheader("Instrumento 3: Tablero Semanal de Adopción por Estación")
    st.markdown("Dónde se está quedando cada cambio, esta semana (Datos simulados).")
    
    # Métricas superiores inspiradas en la diapositiva 10
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Cambios activos", "5", "Estándar red")
    m2.metric("Celdas en riesgo", "4", "🔴 Alerta", delta_color="inverse")
    m3.metric("Estaciones en compuerta", "3", "Máx. 3 activos")
    m4.metric("Calidad de despliegue", "50%", "Umbral 40%")
    
    st.markdown("---")
    
    # Matriz interactiva de red basada en tu diapositiva 10
    data_matriz = {
        "Estación": ["BOG Bogotá", "MDE Medellín", "CLO Cali", "CTG Cartagena", "MAD Madrid"],
        "Equipaje (Regla con margen)": ["48 🔴 En riesgo", "69 🔵 Adoptado", "52 🔴 En riesgo", "82 🔵 Adoptado", "45 🔴 En riesgo"],
        "Baterías de litio": ["86 🔵 Adoptado", "90 🔵 Adoptado", "84 🔵 Adoptado", "Cerrado ⬛", "80 🔵 Adoptado"],
        "Documentos de viaje": ["En despliegue", "—", "En despliegue", "—", "En despliegue"],
        "Carga Activa": [5, 3, 4, 1, 4]
    }
    
    df_matriz = pd.DataFrame(data_matriz)
    st.dataframe(df_matriz, use_container_width=True)
    
    st.info("Leyenda: 🔵 Adoptado | 🔴 En riesgo | ⬛ Cerrado | — No aplica")
