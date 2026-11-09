import streamlit as st
import pandas as pd

# Configuración general de la página
st.set_page_config(
    page_title="Torre de Cambio | CESA & Avianca",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS ejecutivos y creativos (Branding Avianca, sin emojis)
st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    h1, h2, h3 { color: #d32f2f !important; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: 700; }
    
    .stButton>button {
        background-color: #d32f2f;
        color: white;
        border-radius: 4px;
        font-weight: 600;
        border: none;
        padding: 0.6rem 1.4rem;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #b71c1c;
        color: white;
        box-shadow: 0 4px 12px rgba(211, 47, 47, 0.3);
    }
    
    .card-instrumento {
        background: linear-gradient(145deg, #ffffff 0%, #fcfcfc 100%);
        padding: 28px;
        border-radius: 8px;
        border-top: 5px solid #d32f2f;
        border-left: 1px solid #e0e0e0;
        border-right: 1px solid #e0e0e0;
        border-bottom: 1px solid #e0e0e0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        height: 100%;
    }
    
    .card-instructivo {
        background: #ffffff;
        padding: 22px;
        border-radius: 8px;
        border-left: 5px solid #d32f2f;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 16px;
        border-top: 1px solid #f0f0f0;
        border-right: 1px solid #f0f0f0;
        border-bottom: 1px solid #f0f0f0;
    }
    
    .card-historial {
        background: #ffffff;
        padding: 18px;
        border-radius: 6px;
        border-left: 4px solid #1976d2;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        margin-bottom: 10px;
        font-size: 13px;
        color: #333;
    }
    
    .metric-card {
        background-color: white;
        padding: 18px;
        border-radius: 8px;
        border-left: 5px solid #d32f2f;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    }
    
    .header-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 18px;
        border-bottom: 2px solid #e8ecef;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# INICIALIZACIÓN DE ESTADOS EN TIEMPO REAL (SESSION STATE)
if 'matriz_red' not in st.session_state:
    st.session_state.matriz_red = pd.DataFrame({
        "Estación": ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "CTG Cartagena", "MIA Miami", "MAD Madrid", "SAL San Salvador", "LET Leticia", "Promedio de red"],
        "Equipaje de mano (regla con margen)": ["48 - En riesgo", "69 - Adoptado", "52 - En riesgo", "82 - Adoptado", "74 - En verificación", "45 - En riesgo", "85 - Adoptado", "55 - En riesgo", "64"],
        "Baterías de litio (regla dura)": ["86 - Adoptado", "90 - Adoptado", "84 - Adoptado", "Cerrado", "88 - Adoptado", "80 - Adoptado", "Cerrado", "83 - Adoptado", "85"],
        "Documentos de viaje": ["En despliegue", "No aplica", "En despliegue", "No aplica", "No aplica", "En despliegue", "70", "No aplica", "70"],
        "Plastificado BOG": ["72", "No aplica", "No aplica", "No aplica", "No aplica", "No aplica", "No aplica", "No aplica", "72"],
        "Business Class Américas": ["En despliegue", "En despliegue", "No aplica", "No aplica", "En despliegue", "No aplica", "No aplica", "No aplica", "—"],
        "Carga (máx. 3)": [5, 3, 4, 1, 3, 4, 3, 2, 3.1]
    })

if 'historial_pulsos' not in st.session_state:
    st.session_state.historial_pulsos = [
        {"id": 1, "estacion": "BOG Bogotá El Dorado", "periodo": "Semana 44 (26 Oct 2026)", "politica": "Equipaje de mano", "resultado": "Indice de alineación 58% (Alerta roja - Brecha de criterio en mostrador)", "color": "#d32f2f"},
        {"id": 2, "estacion": "MDE Medellín Rionegro", "periodo": "Semana 44 (26 Oct 2026)", "politica": "Baterías de litio", "resultado": "Indice de alineación 90% (Adoptado satisfactoriamente)", "color": "#2e7d32"},
        {"id": 3, "estacion": "CLO Cali", "periodo": "Semana 43 (19 Oct 2026)", "politica": "Equipaje de mano", "resultado": "Indice de alineación 62% (Intervención de instructor asignada)", "color": "#d32f2f"},
        {"id": 4, "estacion": "MAD Madrid", "periodo": "Semana 43 (19 Oct 2026)", "politica": "Documentos de viaje", "resultado": "Fase de despliegue inicial completada (70%)", "color": "#1976d2"}
    ]

# Encabezado institucional superior con logotipo oficial
st.markdown("""
    <div class="header-container">
        <div>
            <span style="font-size: 11px; font-weight: 700; color: #555; letter-spacing: 1.5px; text-transform: uppercase;">CESA & AVIANCA | RETO OPERATIVO</span>
            <h1 style="margin: 2px 0 0 0; font-size: 30px; color: #d32f2f;">Torre de Cambio</h1>
            <p style="margin: 4px 0 0 0; font-size: 14px; color: #555;">Un sistema para saber si cada cambio entró en cada estación, y si se quedó.</p>
        </div>
        <div>
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/29/Avianca_logo_2013.svg" width="150">
        </div>
    </div>
""", unsafe_allow_html=True)

# Pestañas de navegación superiores
tab_home, tab_ficha, tab_pulso, tab_tablero, tab_fases = st.tabs([
    "Modelo e Instructivo", 
    "1. Ficha (Compuerta)", 
    "2. Pulso Semanal", 
    "3. Tablero de Adopción",
    "Despliegue por Fases"
])

with tab_home:
    st.subheader("Tres instrumentos y una regla")
    st.markdown("Solución integral para cerrar la brecha entre el anuncio corporativo y la ejecución en el mostrador.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card-instrumento">
            <h3 style="color: #d32f2f; margin-top:0; font-size:20px;">1. Ficha</h3>
            <p style="font-weight: 700; color: #222; font-size:14px;">Obliga a resolver el margen</p>
            <p style="color: #555; font-size:13px; line-height: 1.5;">Ninguna regla con margen sale al mostrador sin definir formalmente su criterio único por escrito.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="card-instrumento">
            <h3 style="color: #d32f2f; margin-top:0; font-size:20px;">2. Pulso</h3>
            <p style="font-weight: 700; color: #222; font-size:14px;">Mide en el puesto de trabajo</p>
            <p style="color: #555; font-size:13px; line-height: 1.5;">Auditoría semanal de 10 minutos por estación ejecutada por el instructor directamente en campo.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="card-instrumento">
            <h3 style="color: #d32f2f; margin-top:0; font-size:20px;">3. Tablero</h3>
            <p style="font-weight: 700; color: #222; font-size:14px;">Adopción y carga visibles</p>
            <p style="color: #555; font-size:13px; line-height: 1.5;">Matriz centralizada de control semanal por estación para evitar la saturación operativa.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### Instructivo Operativo de la Plataforma")
    st.markdown("Guía rápida para la sustentación y demostración en vivo ante el comité:")

    st.markdown("""
    <div class="card-instructivo">
        <h4 style="margin:0 0 6px 0; color:#d32f2f; font-size:16px;">Sección 1: Ficha (Compuerta de Capacidad)</h4>
        <p style="margin:0; font-size:13px; color:#444; line-height: 1.5;"><b>Objetivo:</b> Simular el registro formal de directrices normativas.</p>
    </div>
    
    <div class="card-instructivo">
        <h4 style="margin:0 0 6px 0; color:#d32f2f; font-size:16px;">Sección 2: Pulso Semanal (Gestión e Historial con Eliminación)</h4>
        <p style="margin:0; font-size:13px; color:#444; line-height: 1.5;"><b>Objetivo:</b> Permite registrar nuevos pulsos en tiempo real y <b>gestionar/eliminar registros históricos</b> de la base de datos de auditorías para total control durante la demo.</p>
    </div>
    
    <div class="card-instructivo">
        <h4 style="margin:0 0 6px 0; color:#d32f2f; font-size:16px;">Sección 3: Tablero de Adopción</h4>
        <p style="margin:0; font-size:13px; color:#444; line-height: 1.5;"><b>Objetivo:</b> Refleja de forma centralizada el estado operativo actual de la red.</p>
    </div>
    """, unsafe_allow_html=True)

with tab_ficha:
    st.subheader("Instrumento 1: Ficha de Cambio (Compuerta de Capacidad)")
    st.markdown("FC-014 - Version 1 | Ninguna regla con margen sale sin resolver su criterio único.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.form("form_ficha"):
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            politica = st.selectbox("Que cambia y desde cuando", [
                "Max. 10 kg en cabina, tarifa Light internacional. Vigencia: 27 Ene 2026",
                "Tolerancia de equipaje deportivo y piezas especiales - Tarifa Classic",
                "Lineamiento operativo de dispositivos electrónicos y baterías de litio"
            ])
            razon = st.selectbox("Por que cambia", [
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
            "Estaciones alcanzadas (Fase Piloto)",
            ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "CTG Cartagena", "MAD Madrid", "MIA Miami", "SAL San Salvador", "LET Leticia"],
            default=["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali"]
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        btn_ficha = st.form_submit_button("Validar y Registrar Ficha en Compuerta")
        if btn_ficha:
            st.success(f"Ficha validada y aprobada mediante compuerta de capacidad para {len
