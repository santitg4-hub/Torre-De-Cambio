import streamlit as st
import pandas as pd

# Configuración de página con diseño ancho y limpio estilo corporativo
st.set_page_config(page_title="Torre de Cambio - Avianca", page_icon="✈️", layout="wide")

# Estilos CSS personalizados para replicar la identidad visual de las diapositivas (Rojo/Fucsia Avianca)
st.markdown("""
    <style>
    /* Barra superior corporativa */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 6px;
        background: linear-gradient(90deg, #E30613 0%, #C8102E 50%, #98002E 100%);
        z-index: 99999;
    }
    /* Estilo de títulos principales */
    h1, h2, h3 {
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        color: #111111;
    }
    /* Tarjetas de instrumentos */
    .card-instrumento {
        background: linear-gradient(135deg, #E30613 0%, #A00034 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .card-instrumento h3 {
        color: white !important;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal idéntico al concepto de la diapositiva 7
st.markdown("##### LA SOLUCIÓN")
st.title("Torre de Cambio: tres instrumentos y una regla")
st.markdown("---")

# Navegación superior con Pestañas (Tabs) idénticas a las de las diapositivas 8, 9 y 10
tab_home, tab_ficha, tab_pulso, tab_tablero = st.tabs([
    "🏠 Resumen General", 
    "1️⃣ Ficha (Entrada)", 
    "2️⃣ Pulso (Medición)", 
    "3️⃣ Tablero (Adopción)"
])

# -------------------------------------------------------------------------
# PESTAÑA 0: RESUMEN GENERAL (Estilo Diapositiva 7)
# -------------------------------------------------------------------------
with tab_home:
    st.markdown("### El ciclo operativo para asegurar que cada directriz llegue al mostrador")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="card-instrumento">
                <h3>1 Ficha</h3>
                <p>Obliga a resolver el margen</p>
                <small>Criterio único y excepciones claras antes de salir a la red.</small>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="card-instrumento">
                <h3>2 Pulso</h3>
                <p>Mide en el puesto, semanal</p>
                <small>Menos de 2 minutos por levantamiento en el celular del instructor.</small>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="card-instrumento">
                <h3>3 Tablero</h3>
                <p>Adopción y carga visibles</p>
                <small>Monitoreo en tiempo real de celdas en riesgo y capacidad de estación.</small>
            </div>
        """, unsafe_allow_html=True)
    
    st.info("💡 **Cómo navegar:** Usa las pestañas superiores (Ficha, Pulso, Tablero) para simular cada herramienta en vivo frente al jurado del CESA.")

# -------------------------------------------------------------------------
# PESTAÑA 1: INSTRUMENTO 1 - LA FICHA (Estilo Diapositiva 8)
# -------------------------------------------------------------------------
with tab_ficha:
    st.markdown("##### INSTRUMENTO 1  |  LA FICHA")
    st.subheader("Ninguna regla con margen sale sin resolverlo")
    
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        st.markdown("#### Ficha de Cambio (FC-014 · v1)")
        titulo_f = st.text_input("Qué cambia y desde cuándo", "Equipaje de mano en vuelos internacionales - Máx. 10 kg")
        porque = st.text_input("Por qué cambia", "Nueva política de equipaje para vuelos en las Américas")
        criterio = st.text_input("Criterio único (El campo que hoy no existe)", "11 kg en tarifa que incluye cabina / Si no entra en medidor: supervisor")
        
        if st.button("Validar y Registrar Ficha en Compuerta", type="primary"):
            st.success("✅ Ficha validada con criterio único. El margen ha quedado por escrito y no depende de la improvisación del agente.")
    
    with col_f2:
        st.markdown("""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #E30613;">
                <h4>Criterio Único</h4>
                <p style="font-size: 14px; color: #555;">
                O hay tolerancia oficial y se dice cuál, o no la hay y se dice que no. Se eliminan los grises en el counter.
                </p>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# PESTAÑA 2: INSTRUMENTO 2 - EL PULSO (Estilo Diapositiva 9)
# -------------------------------------------------------------------------
with tab_pulso:
    st.markdown("##### INSTRUMENTO 2  |  EL PULSO")
    st.subheader("Diez minutos por semana, en el puesto de trabajo")
    
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        st.markdown("#### Simulador de Pulso (Celular Instructor)")
        estacion_pulso = st.selectbox("Estación evaluada", ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "MAD Madrid"])
        observaciones = st.slider("Observaciones conformes en counter (sobre 5)", 0, 5, 4)
        prueba_consistencia = st.radio("¿Qué hace con 11 kg en tarifa con cabina?", ["Acepta unificado", "No coinciden criterios"])
        
        if st.button("Enviar Pulso Semanal"):
            st.success(f"📱 Pulso registrado para {estacion_pulso}. Datos actualizados en el tablero central de red.")
            
    with col_p2:
        st.markdown("""
            <div style="text-align: center; padding: 30px; background: #fff; border: 1px solid #ddd; border-radius: 12px;">
                <h1 style="color: #E30613; font-size: 64px; margin: 0;">2 min</h1>
                <p style="font-weight: bold; font-size: 18px;">por levantamiento en el celular del instructor</p>
                <hr style="margin: 15px 0;">
                <p style="margin: 5px 0;">⏱️ <b>10 min</b> por semana, por estación</p>
                <p style="margin: 5px 0;">📋 <b>< 10</b> campos en el formulario</p>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# PESTAÑA 3: INSTRUMENTO 3 - EL TABLERO (Estilo Diapositiva 10)
# -------------------------------------------------------------------------
with tab_tablero:
    st.markdown("##### INSTRUMENTO 3  |  EL TABLERO")
    st.subheader("Dónde se está quedando cada cambio, esta semana")
    
    # Métricas superiores idénticas a la diapositiva 10
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.metric(label="Cambios activos", value="5")
    with col_m2:
        st.metric(label="Celdas en riesgo", value="4", delta="🔴 Crítico", delta_color="inverse")
    with col_m3:
        st.metric(label="Estaciones sobre compuerta", value="3", delta="máx. 3 activos")
    with col_m4:
        st.metric(label="Calidad del despliegue", value="50%", delta="umbral 40%")

    st.markdown("#### Tablero Semanal de Adopción (Datos Simulados)")
    
    # Tabla interactiva simulando la diapositiva 10
    data_tablero = {
        "Estación": ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "CTG Cartagena", "MIA Miami", "MAD Madrid"],
        "Equipaje de mano (regla con margen)": ["48 🔴 En riesgo", "69 Adopto", "52 🔴 En riesgo", "82 Adopto", "74 En verificación", "45 🔴 En riesgo"],
        "Baterías de litio (regla dura)": ["86 Adopto", "90 Adopto", "84 Adopto", "Cerrado", "88 Adopto", "80 Adopto"],
        "Documentos de viaje (retrospectivo)": ["En despliegue", "—", "En despliegue", "—", "—", "En despliegue"],
        "Carga Actual": [5, 3, 4, 1, 3, 4]
    }
    
    df_t = pd.DataFrame(data_tablero)
    st.dataframe(df_t, use_container_width=True)
    
    st.markdown("""
        <div style="font-size: 13px; color: #666; margin-top: 10px;">
        🔴 <b>En riesgo:</b> Requiere intervención del instructor · 🔵 <b>Adoptado:</b> Operación estandarizada · ⚫ <b>Cerrado:</b> Ciclo concluido.
        </div>
    """, unsafe_allow_html=True)
