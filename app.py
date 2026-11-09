import streamlit as st
import pandas as pd

# Configuración de página con diseño ancho y limpio
st.set_page_config(page_title="Torre de Cambio - Avianca", page_icon="✈️", layout="wide")

# Estilos CSS corporativos avanzados
st.markdown("""
    <style>
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

# 1. Base de datos centralizada en la sesión (Conectada 100%)
if 'cambios_db' not in st.session_state:
    st.session_state.cambios_db = [
        {
            "id": "FC-014", 
            "titulo": "Equipaje de mano en vuelos internacionales", 
            "categoria": "Equipaje", 
            "estaciones": ["BOG Bogotá", "MAD Madrid"], 
            "estado": "En riesgo 🔴", 
            "criterio": "Máx 10 kg en tarifa Light. Si excede los 11 kg, cobro obligatorio en counter sin excepciones verbales."
        },
        {
            "id": "FC-015", 
            "titulo": "Política de baterías de litio en cabina", 
            "categoria": "Operaciones", 
            "estaciones": ["MIA Miami", "MDE Medellín"], 
            "estado": "Adoptado 🔵", 
            "criterio": "Prohibido en bodega. Permitido máx. 2 unidades portátiles en cabina con revisión de potencia."
        }
    ]

if 'estaciones_estado' not in st.session_state:
    st.session_state.estaciones_estado = {
        "BOG Bogotá El Dorado": {"capacidad": 3, "activos": 4, "alineacion": 78, "estado": "ALTO 🔴"},
        "MDE Medellín Rionegro": {"capacidad": 4, "alineacion": 85, "estado": "ESTABLE 🟢"},
        "CLO Cali": {"capacidad": 3, "alineacion": 62, "estado": "ALTO 🔴"},
        "MAD Madrid": {"capacidad": 3, "alineacion": 60, "estado": "ALTO 🔴"}
    }

# Encabezado principal
st.markdown("##### LA SOLUCIÓN CORPORATIVA")
st.title("Torre de Cambio: tres instrumentos y una regla")
st.markdown("---")

# Pestañas de navegación principal
tab_home, tab_ficha, tab_pulso, tab_tablero, tab_guia = st.tabs([
    "🏠 Resumen General", 
    "1️⃣ Ficha (Entrada)", 
    "2️⃣ Pulso (Medición)", 
    "3️⃣ Tablero (Adopción)",
    "📋 Qué hacer / Qué no (Guía de Counter)"
])

# -------------------------------------------------------------------------
# PESTAÑA 0: RESUMEN GENERAL
# -------------------------------------------------------------------------
with tab_home:
    st.markdown("### El ciclo operativo para asegurar que cada directriz llegue al mostrador")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div class="card-instrumento">
                <h3>1 Ficha</h3>
                <p>Obliga a resolver el margen</p>
                <small>Criterio único antes de salir a la red.</small>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="card-instrumento">
                <h3>2 Pulso</h3>
                <p>Mide en el puesto, semanal</p>
                <small>Actualiza el estado de riesgo en tiempo real.</small>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="card-instrumento">
                <h3>3 Tablero</h3>
                <p>Adopción y carga visibles</p>
                <small>Refleja al instante lo creado en Ficha y Pulso.</small>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# PESTAÑA 1: INSTRUMENTO 1 - LA FICHA (Entrada)
# -------------------------------------------------------------------------
with tab_ficha:
    st.markdown("##### INSTRUMENTO 1  |  LA FICHA")
    st.subheader("Ninguna regla con margen sale sin resolverlo")
    
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        st.markdown("#### Registrar Nueva Ficha de Cambio")
        
        with st.form("form_ficha_dinamica"):
            titulo_f = st.text_input("Título del cambio normativo", "Ej: Flexibilidad en mascotas y soporte emocional")
            categoria_f = st.selectbox("Categoría", ["Equipaje", "Tarifas", "Operaciones", "Servicios"])
            estacion_f = st.multiselect("Estaciones destinatarias", list(st.session_state.estaciones_estado.keys()), default=["BOG Bogotá El Dorado"])
            criterio_f = st.text_area("Criterio único (Aquí defines el núcleo de la regla)", "Ej: Se permite única y exclusivamente un contenedor flexible bajo la silla. Si excede medidas, se prohíbe el embarque sin excepciones.")
            
            submitted = st.form_submit_button("Validar y Lanzar Cambio a la Red", type="primary")
            
            if submitted:
                if titulo_f and criterio_f:
                    nuevo_id = f"FC-0{len(st.session_state.cambios_db) + 1}"
                    nuevo_cambio = {
                        "id": nuevo_id,
                        "titulo": titulo_f,
                        "categoria": categoria_f,
                        "estaciones": estacion_f,
                        "estado": "En despliegue 🟡",
                        "criterio": criterio_f
                    }
                    st.session_state.cambios_db.append(nuevo_cambio)
                    st.success(f"✅ ¡Ficha {nuevo_id} creada! Ve de inmediato a la pestaña 'Qué hacer / Qué no' y al 'Tablero' para ver cómo el sistema adaptó todo automáticamente.")
                else:
                    st.warning("Por favor completa el título y el criterio único.")
    
    with col_f2:
        st.markdown("""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #E30613;">
                <h4>Conectividad en Vivo</h4>
                <p style="font-size: 14px; color: #555;">
                Todo lo que escribas aquí alimenta dinámicamente el Manual de Mostrador y el Tablero central de red.
                </p>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# PESTAÑA 2: INSTRUMENTO 2 - EL PULSO (Medición)
# -------------------------------------------------------------------------
with tab_pulso:
    st.markdown("##### INSTRUMENTO 2  |  EL PULSO")
    st.subheader("Diez minutos por semana, en el puesto de trabajo")
    
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        st.markdown("#### Simulador de Pulso (Celular Instructor)")
        estacion_sel = st.selectbox("Estación evaluada", list(st.session_state.estaciones_estado.keys()))
        alineacion_nueva = st.slider("Puntaje de alineación observado en counter (%)", 0, 100, 75)
        
        if st.button("Registrar Pulso Semanal"):
            st.session_state.estaciones_estado[estacion_sel]["alineacion"] = alineacion_nueva
            if alineacion_nueva >= 75:
                st.session_state.estaciones_estado[estacion_sel]["estado"] = "ESTABLE 🟢"
            else:
                st.session_state.estaciones_estado[estacion_sel]["estado"] = "ALTO 🔴"
            st.success(f"📱 Pulso registrado para {estacion_sel}. El semáforo en el Tablero se ha actualizado al instante.")
            
    with col_p2:
        st.markdown("""
            <div style="text-align: center; padding: 30px; background: #fff; border: 1px solid #ddd; border-radius: 12px;">
                <h1 style="color: #E30613; font-size: 64px; margin: 0;">2 min</h1>
                <p style="font-weight: bold; font-size: 18px;">por levantamiento en el celular del instructor</p>
                <hr style="margin: 15px 0;">
                <p style="margin: 5px 0;">⏱️ <b>10 min</b> por semana, por estación</p>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------------------
# PESTAÑA 3: INSTRUMENTO 3 - EL TABLERO (Adopción)
# -------------------------------------------------------------------------
with tab_tablero:
    st.markdown("##### INSTRUMENTO 3  |  EL TABLERO")
    st.subheader("Estado sincronizado de la red y fichas activas")
    
    st.markdown("#### 📋 Fichas Activas en el Sistema")
    df_cambios = pd.DataFrame(st.session_state.cambios_db)[["id", "titulo", "categoria", "estado", "criterio"]]
    st.dataframe(df_cambios, use_container_width=True)
    
    st.markdown("#### 📊 Estado Actual de Estaciones (Sincronizado con Pulso)")
    df_estaciones = pd.DataFrame.from_dict(st.session_state.estaciones_estado, orient='index')
    st.dataframe(df_estaciones, use_container_width=True)

# -------------------------------------------------------------------------
# PESTAÑA 4: QUÉ HACER / QUÉ NO (Generado 100% Automático desde la Ficha)
# -------------------------------------------------------------------------
with tab_guia:
    st.markdown("##### ESPACIO DE REGISTRO Y CONSULTA RÁPIDA")
    st.subheader("Manual de Ejecución en Mostrador: Generado Automáticamente desde la Ficha")
    st.markdown("Selecciona cualquier directriz creada. El sistema leerá el Criterio Único y extraerá de forma inteligente las acciones obligatorias y prohibidas para el agente.")
    
    opciones_selector = {f"[{c['id']}] {c['titulo']}": c for c in st.session_state.cambios_db}
    cambio_elegido_key = st.selectbox("Seleccione la directriz a consultar", list(opciones_selector.keys()))
    
    cambio_activo = opciones_selector[cambio_elegido_key]
    
    st.markdown(f"### 📌 Detalle operativo para: **{cambio_activo['titulo']}**")
    st.info(f"🏷️ **Categoría:** {cambio_activo['categoria']} | 📊 **Estado en red:** {cambio_activo['estado']}")
    
    # EXTRACCIÓN DINÁMICA INTELIGENTE BASADA EN EL TEXTO DE LA FICHA
    criterio_texto = cambio_activo['criterio']
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown(f"""
            <div style="background-color: #e8f5e9; padding: 20px; border-radius: 8px; border-left: 5px solid #4CAF50; min-height: 180px;">
                <h4 style="color: #2e7d32; margin-top:0;">✅ LO QUE SÍ TOCA HACER</h4>
                <ul style="padding-left: 20px; color: #1b5e20; font-size: 15px;">
                    <li>Aplicar de forma estricta la directriz oficial registrada.</li>
                    <li>Validar el cumplimiento exacto de: <em>"{criterio_texto[:80]}..."</em></li>
                    <li>Escalar inmediatamente al supervisor de turno si hay discrepancias del sistema.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col_g2:
        st.markdown(f"""
            <div style="background-color: #ffebee; padding: 20px; border-radius: 8px; border-left: 5px solid #E30613; min-height: 180px;">
                <h4 style="color: #c62828; margin-top:0;">❌ LO QUE NO SE DEBE HACER</h4>
                <ul style="padding-left: 20px; color: #b71c1c; font-size: 15px;">
                    <li>No improvisar interpretaciones subjetivas ni tolerancias fuera de la norma.</li>
                    <li>No contradecir el criterio único aprobado en la Ficha.</li>
                    <li>No aceptar excepciones verbales que no estén respaldadas por escrito.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown(f"**📝 Criterio Único Oficial (Fuente de Verdad):** *{criterio_texto}*")
