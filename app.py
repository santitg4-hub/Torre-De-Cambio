import streamlit as st
import pandas as pd

# Configuración general de la página
st.set_page_config(page_title="Torre de Cambio - Avianca", layout="wide")

# Estilos CSS personalizados para un aspecto 100% corporativo (Sin emojis)
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    h1, h2, h3 { color: #d32f2f !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    .stButton>button {
        background-color: #d32f2f;
        color: white;
        border-radius: 4px;
        font-weight: 600;
        border: none;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #b71c1c;
        color: white;
    }
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 6px;
        border-left: 4px solid #d32f2f;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Cabecera superior con identidad corporativa
col_logo, col_title = st.columns([1, 8])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/29/Avianca_logo_2013.svg", width=90)
with col_title:
    st.markdown("### CESA & AVIANCA | GESTION OPERATIVA")
    st.title("Torre de Cambio: Tres instrumentos y una regla")

st.markdown("---")

# Pestañas de navegación superiores basadas en la presentación
tab_home, tab_ficha, tab_pulso, tab_tablero = st.tabs([
    "Inicio (Modelo)", 
    "1. Ficha (Compuerta)", 
    "2. Pulso Semanal", 
    "3. Tablero Semanal de Adopción"
])

with tab_home:
    st.subheader("Estructura del Modelo Operativo")
    st.markdown("Asegurando que cada directriz del área corporativa llegue de forma efectiva al mostrador y a la puerta.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: #ffffff; padding: 25px; border-radius: 8px; border-top: 5px solid #d32f2f; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <h3 style="color: #d32f2f; margin-top:0;">1. Ficha</h3>
            <p style="color: #333; font-size: 14px;">Obliga a resolver el margen por escrito antes de liberar cualquier directriz a la red de aeropuertos.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div style="background: #ffffff; padding: 25px; border-radius: 8px; border-top: 5px solid #d32f2f; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <h3 style="color: #d32f2f; margin-top:0;">2. Pulso</h3>
            <p style="color: #333; font-size: 14px;">Medición semanal en el puesto de trabajo (menos de 2 minutos por levantamiento en campo).</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div style="background: #ffffff; padding: 25px; border-radius: 8px; border-top: 5px solid #d32f2f; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
            <h3 style="color: #d32f2f; margin-top:0;">3. Tablero</h3>
            <p style="color: #333; font-size: 14px;">Visibilidad en tiempo real de la adopción, carga activa y nivel de riesgo por estación.</p>
        </div>
        """, unsafe_allow_html=True)

with tab_ficha:
    st.subheader("Instrumento 1: Ficha de Cambio (Compuerta de Capacidad)")
    st.markdown("Ninguna regla con margen sale sin resolver su criterio único por escrito.")
    
    with st.form("form_ficha"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            politica = st.selectbox("¿Qué cambia y desde cuándo?", [
                "Max. 10 kg en cabina, tarifa Light internacional. Vigencia: 27 Ene 2026",
                "Tolerancia de equipaje deportivo y piezas especiales - Tarifa Classic",
                "Lineamiento operativo de dispositivos electrónicos y baterías de litio"
            ])
            razon = st.selectbox("Por qué cambia", [
                "Unificación de política de equipaje en la red de las Americas",
                "Optimización de tiempos de proceso en counter y puerta de embarque",
                "Estandarización regulatoria de seguridad aeroportuaria"
            ])
        with col_f2:
            tipo_regla = st.selectbox("Tipo de regla", ["Regla con margen", "Regla dura"])
            criterio = st.selectbox("Criterio único obligatorio", [
                "11 kg en tarifa que incluye cabina",
                "La maleta excede el medidor por margen menor a 1 cm",
                "Discrepancia entre pasabordo y sistema (Requiere validación escrita)"
            ])
            
        estaciones_ficha = st.multiselect(
            "Estaciones de alcance (Fase Piloto)",
            ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "CTG Cartagena", "MAD Madrid", "MIA Miami"],
            default=["BOG Bogotá El Dorado", "MDE Medellín Rionegro"]
        )
        
        btn_ficha = st.form_submit_button("Validar y Registrar Ficha en Compuerta")
        if btn_ficha:
            st.success(f"Ficha validada y aprobada para {len(estaciones_ficha)} estaciones bajo control de capacidad.")

with tab_pulso:
    st.subheader("Instrumento 2: Registro de Pulso en Puesto de Trabajo")
    st.markdown("Auditoría ágil ejecutada por el instructor en campo (10 minutos por semana por estación).")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        estacion_pulso = st.selectbox("Estación evaluada", ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "MAD Madrid", "MIA Miami"])
        semana = st.selectbox("Periodo de auditoria", ["Semana 45 - 2 Nov 2026", "Semana 46", "Semana 47"])
        cambio_eval = st.selectbox("Politica auditada", ["Equipaje de mano (regla con margen)", "Baterias de litio", "Documentos de viaje"])
        
    with col_p2:
        st.markdown("### Verificacion en Puesto")
        obs_conformes = st.slider("Observaciones conformes en counter (max. 5)", 0, 5, 4)
        
        st.markdown("### Prueba de Consistencia (3 Agentes)")
        resp_a = st.selectbox("Agente Turno A", ["Acepta criterio unificado", "Discrepa criterio"])
        resp_b = st.selectbox("Agente Turno B", ["Acepta criterio unificado", "Discrepa criterio"])
        resp_c = st.selectbox("Agente Turno C", ["Acepta criterio unificado", "Discrepa criterio"])

    if st.button("Registrar Pulso Semanal"):
        st.success(f"Pulso registrado correctamente para {estacion_pulso}. Métricas sincronizadas con el tablero central.")

with tab_tablero:
    st.subheader("Instrumento 3: Tablero Semanal de Adopción por Estación")
    st.markdown("Semana 45 - 2 Nov 2026 | Datos simulados de red")
    
    # Métricas superiores idénticas a la diapositiva 10
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card"><b>Cambios activos</b><br><span style="font-size:24px; font-weight:bold; color:#333;">5</span></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><b>Celdas en riesgo</b><br><span style="font-size:24px; font-weight:bold; color:#d32f2f;">4</span></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><b>Estaciones sobre compuerta</b><br><span style="font-size:24px; font-weight:bold; color:#d32f2f;">3</span> <span style="font-size:12px; color:#666;">max. 3 activos</span></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><b>Calidad de despliegue</b><br><span style="font-size:24px; font-weight:bold; color:#333;">50%</span> <span style="font-size:12px; color:#666;">umbral 40%</span></div>', unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown("### Donde se esta quedando cada cambio, esta semana")
    
    # Matriz detallada exacta a la diapositiva 10
    data_matriz = {
        "Estación": ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "CTG Cartagena", "MIA Miami", "MAD Madrid", "SAL San Salvador", "LET Leticia", "Promedio de red"],
        "Equipaje de mano (Regla con margen)": ["48 - En riesgo", "69 - Adoptado", "52 - En riesgo", "82 - Adoptado", "74 - En verificación", "45 - En riesgo", "85 - Adoptado", "55 - En riesgo", "64"],
        "Baterías de litio (Regla dura)": ["86 - Adoptado", "90 - Adoptado", "84 - Adoptado", "Cerrado", "88 - Adoptado", "80 - Adoptado", "Cerrado", "83 - Adoptado", "85"],
        "Documentos de viaje": ["En despliegue", "No aplica", "En despliegue", "No aplica", "No aplica", "En despliegue", "70", "No aplica", "70"],
        "Plastificado BOG": ["72", "No aplica", "No aplica", "No aplica", "No aplica", "No aplica", "No aplica", "No aplica", "72"],
        "Business Class Américas": ["En despliegue", "En despliegue", "No aplica", "No aplica", "En despliegue", "No aplica", "No aplica", "No aplica", "—"],
        "Carga (Máx. 3)": [5, 3, 4, 1, 3, 4, 3, 2, 3.1]
    }
    
    df_matriz = pd.DataFrame(data_matriz)
    st.dataframe(df_matriz, use_container_width=True)
    
    st.markdown("""
    <div style="background-color: #eef2f7; padding: 10px; border-radius: 5px; font-size: 13px; color: #333;">
        <b>Leyenda de estados:</b> Adoptado (Optimo) | En riesgo (Requiere intervención) | Cerrado (Completado) | En despliegue (Fase inicial) | Índice 0-100 sin ranking.
    </div>
    """, unsafe_allow_html=True)
