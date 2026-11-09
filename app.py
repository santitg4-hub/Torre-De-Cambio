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
    .instruction-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid #E30613;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializar Base de Datos en la sesión para que los cambios persistan en vivo durante la demo
if 'cambios_db' not in st.session_state:
    st.session_state.cambios_db = [
        {"id": "FC-014", "titulo": "Equipaje de mano en vuelos internacionales", "categoria": "Equipaje", "estaciones": ["BOG Bogotá", "MAD Madrid"], "estado": "En riesgo 🔴", "criterio": "Máx 10 kg en tarifa Light. Si excede, aplicar cobro en counter."},
        {"id": "FC-015", "titulo": "Política de baterías de litio en cabina", "categoria": "Operaciones", "estaciones": ["MIA Miami", "MDE Medellín"], "estado": "Adoptado 🔵", "criterio": "Regla dura: prohibido en bodega, permitido máx 2 unidades en cabina."},
        {"id": "FC-016", "titulo": "Flexibilidad en documentos de viaje", "categoria": "Servicios", "estaciones": ["BOG Bogotá", "CLO Cali"], "estado": "En despliegue 🟡", "criterio": "Validación biométrica obligatoria en pre-embarque."}
    ]

if 'estaciones_estado' not in st.session_state:
    st.session_state.estaciones_estado = {
        "BOG Bogotá El Dorado": {"capacidad": 3, "activos": 4, "alineacion": 78, "estado": "ALTO 🔴"},
        "MDE Medellín Rionegro": {"capacidad": 4, "alineacion": 85, "estado": "ESTABLE 🟢"},
        "CLO Cali": {"capacidad": 3, "activos": 4, "alineacion": 62, "estado": "ALTO 🔴"},
        "MAD Madrid": {"capacidad": 3, "activos": 4, "alineacion": 60, "estado": "ALTO 🔴"}
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
    
    st.info("💡 **Listo para la presentación:** Usa la pestaña **'Qué hacer / Qué no'** para mostrarle al jurado cómo el agente del counter consulta las reglas sin espacio a la improvisación.")

# -------------------------------------------------------------------------
# PESTAÑA 1: INSTRUMENTO 1 - LA FICHA (Entrada)
# -------------------------------------------------------------------------
with tab_ficha:
    st.markdown("##### INSTRUMENTO 1  |  LA FICHA")
    st.subheader("Ninguna regla con margen sale sin resolverlo")
    
    col_f1, col_f2 = st.columns([2, 1])
    with col_f1:
        st.markdown("#### Registrar Nueva Ficha de Cambio")
        nuevo_id = f"FC-0{len(st.session_state.cambios_db) + 1}"
        titulo_f = st.text_input("Título del cambio normativo", "Tolerancia en equipaje deportivo especial")
        categoria_f = st.selectbox("Categoría", ["Equipaje", "Tarifas", "Operaciones", "Servicios"])
        estacion_f = st.multiselect("Estaciones destinatarias", ["BOG Bogotá", "MDE Medellín", "CLO Cali", "MAD Madrid"], default=["BOG Bogotá"])
        criterio_f = st.text_area("Criterio único (El campo que hoy no existe)", "Se permite 1 pieza adicional de 5kg sin costo si porta membresía Elite.")
        
        if st.button("Validar y Lanzar Cambio a la Red", type="primary"):
            if titulo_f and criterio_f:
                nuevo_cambio = {
                    "id": nuevo_id,
                    "titulo": titulo_f,
                    "categoria": categoria_f,
                    "estaciones": estacion_f,
                    "estado": "En despliegue 🟡",
                    "criterio": criterio_f
                }
                st.session_state.cambios_db.append(nuevo_cambio)
                st.success(f"✅ Ficha {nuevo_id} aprobada por la compuerta y registrada en el sistema de red.")
            else:
                st.warning("Por favor completa el título y el criterio único.")
    
    with col_f2:
        st.markdown("""
            <div style="background-color: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 4px solid #E30613;">
                <h4>Criterio Único</h4>
                <p style="font-size: 14px; color: #555;">
                O hay tolerancia oficial y se dice cuál, o no la hay y se dice que no. Se eliminan los grises operativos.
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
            st.success(f"📱 Pulso registrado para {estacion_sel}. El tablero de red se ha actualizado.")
            
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
# PESTAÑA 3: INSTRUMENTO 3 - EL TABLERO (Adopción)
# -------------------------------------------------------------------------
with tab_tablero:
    st.markdown("##### INSTRUMENTO 3  |  EL TABLERO")
    st.subheader("Estado actual de los cambios registrados en la red")
    
    # Mostrar tabla interactiva basada en los registros reales añadidos
    df_cambios = pd.DataFrame(st.session_state.cambios_db)
    st.dataframe(df_cambios, use_container_width=True)
    
    st.markdown("#### Estado de Estaciones")
    df_estaciones = pd.DataFrame.from_dict(st.session_state.estaciones_estado, orient='index')
    st.dataframe(df_estaciones, use_container_width=True)

# -------------------------------------------------------------------------
# PESTAÑA 4: QUÉ HACER / QUÉ NO (Guía Operativa para el Counter)
# -------------------------------------------------------------------------
with tab_guia:
    st.markdown("##### ESPACIO DE REGISTRO Y CONSULTA RÁPIDA")
    st.subheader("Manual de Ejecución en Mostrador: Qué hacer y Qué no")
    st.markdown("Consulta en tiempo real las reglas vigentes aprobadas por la Ficha para evitar desacuerdos con pasajeros.")
    
    estacion_consulta = st.selectbox("Seleccione su estación de trabajo", list(st.session_state.estaciones_estado.keys()))
    
    st.markdown(f"### 📍 Directrices activas para: **{estacion_consulta}**")
    
    # Mostrar dinámicamente los cambios aplicables
    for c in st.session_state.cambios_db:
        with st.expander(f"📌 [{c['id']}] {c['titulo']} ({c['categoria']}) - Estado: {c['estado']}"):
            col_g1, col_g2 = st.columns(2)
            with col_g1:
                st.markdown("""
                    <div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; border-left: 4px solid #4CAF50;">
                        <h4 style="color: #2e7d32; margin-top:0;">✅ LO QUE SÍ TOCA HACER</h4>
                        <ul style="padding-left: 15px; margin-bottom: 0;">
                            <li>Aplicar estrictamente el criterio único oficial.</li>
                            <li>Verificar el peso/medida según la Ficha aprobada.</li>
                            <li>Escalar al supervisor de turno si hay discrepancia de sistema.</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
            with col_g2:
                st.markdown("""
                    <div style="background-color: #ffebee; padding: 15px; border-radius: 8px; border-left: 4px solid #E30613;">
                        <h4 style="color: #c62828; margin-top:0;">❌ LO QUE NO SE DEBE HACER</h4>
                        <ul style="padding-left: 15px; margin-bottom: 0;">
                            <li>No improvisar tolerancias subjetivas en el counter.</li>
                            <li>No aceptar excepciones verbales sin respaldo en la Ficha.</li>
                            <li>No contradecir al pasajero sin validar el código del tiquete.</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown(f"**📝 Criterio Oficial Registrado:** {c['criterio']}")
