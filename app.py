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

# Inicializar Base de Datos con variables dinámicas detalladas para cada cambio
if 'cambios_db' not in st.session_state:
    st.session_state.cambios_db = [
        {
            "id": "FC-014", 
            "titulo": "Equipaje de mano en vuelos internacionales", 
            "categoria": "Equipaje", 
            "estaciones": ["BOG Bogotá", "MAD Madrid"], 
            "estado": "En riesgo 🔴", 
            "criterio": "Máx 10 kg en tarifa Light. Si excede los 11 kg, cobro obligatorio en counter.",
            "hacer": ["Verificar peso exacto en báscula de mostrador.", "Aplicar cobro automático si supera los 11 kg.", "Exigir ingreso al medidor metálico si hay duda."],
            "no_hacer": ["No aceptar tolerancias verbales subjetivas ('déjalo pasar por esta vez').", "No discutir con el pasajero; remitir a la regla escrita."]
        },
        {
            "id": "FC-015", 
            "titulo": "Política de baterías de litio en cabina", 
            "categoria": "Operaciones", 
            "estaciones": ["MIA Miami", "MDE Medellín"], 
            "estado": "Adoptado 🔵", 
            "criterio": "Prohibido en equipaje de bodega. Permitido máx. 2 unidades portátiles en cabina.",
            "hacer": ["Preguntar directamente al pasajero por dispositivos con litio.", "Revisar potencia (Wh) si la batería es de alta capacidad."],
            "no_hacer": ["No permitir baterías sueltas en maletas documentadas a bodega.", "No ignorar la alerta de seguridad del escáner."]
        },
        {
            "id": "FC-016", 
            "titulo": "Flexibilidad en documentos de viaje y visas", 
            "categoria": "Servicios", 
            "estaciones": ["BOG Bogotá", "CLO Cali"], 
            "estado": "En despliegue 🟡", 
            "criterio": "Pasaporte con vigencia mínima de 6 meses para vuelos a EE.UU. Alerta amarilla = escalar a supervisor.",
            "hacer": ["Validar fecha de expiración mes a mes con el lector óptico.", "Escalar inmediatamente al supervisor de turno si el sistema arroja alerta."],
            "no_hacer": ["No embarcar pasajeros con pasaportes vencidos o próximos a vencer sin la autorización del supervisor.", "No omitir el sello digital."]
        }
    ]

if 'estaciones_estado' not in st.session_state:
    st.session_state.estaciones_estado = {
        "BOG Bogotá El Dorado": {"capacidad": 3, "activos": 4, "alineacion": 78, "estado": "ALTO 🔴"},
        "MDE Medellín Rionegro": {"capacidad": 4, "activos": 3, "alineacion": 85, "estado": "ESTABLE 🟢"},
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
    
    st.info("💡 **Tip para la presentación:** Crea un cambio en la pestaña 1 y luego ven a la pestaña 5 para ver cómo las variables cambian de forma única e interactiva.")

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
        criterio_f = st.text_area("Criterio único oficial", "Se permite 1 pieza adicional de 5kg sin costo si porta membresía Elite activa.")
        hacer_input = st.text_area("Qué SÍ toca hacer (separado por comas)", "Verificar tarjeta Elite física o digital, Registrar la pieza en el sistema de abordaje")
        no_hacer_input = st.text_area("Qué NO se debe hacer (separado por comas)", "No aplicar excepciones a tarifas Light, No aceptar códigos vencidos")
        
        if st.button("Validar y Lanzar Cambio a la Red", type="primary"):
            if titulo_f and criterio_f:
                nuevo_cambio = {
                    "id": nuevo_id,
                    "titulo": titulo_f,
                    "categoria": categoria_f,
                    "estaciones": estacion_f,
                    "estado": "En despliegue 🟡",
                    "criterio": criterio_f,
                    "hacer": [x.strip() for x in hacer_input.split(",")],
                    "no_hacer": [x.strip() for x in no_hacer_input.split(",")]
                }
                st.session_state.cambios_db.append(nuevo_cambio)
                st.success(f"✅ Ficha {nuevo_id} aprobada con sus variables de ejecución y lista en el mostrador.")
            else:
                st.warning("Por favor completa los campos obligatorios.")
    
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
    
    df_cambios = pd.DataFrame(st.session_state.cambios_db)[["id", "titulo", "categoria", "estado", "criterio"]]
    st.dataframe(df_cambios, use_container_width=True)
    
    st.markdown("#### Estado de Estaciones")
    df_estaciones = pd.DataFrame.from_dict(st.session_state.estaciones_estado, orient='index')
    st.dataframe(df_estaciones, use_container_width=True)

# -------------------------------------------------------------------------
# PESTAÑA 4: QUÉ HACER / QUÉ NO (Guía Dinámica por Variable)
# -------------------------------------------------------------------------
with tab_guia:
    st.markdown("##### ESPACIO DE REGISTRO Y CONSULTA RÁPIDA")
    st.subheader("Manual de Ejecución en Mostrador: Qué hacer y Qué no por Cambio")
    st.markdown("Selecciona un cambio normativo específico para ver sus directrices operativas únicas.")
    
    # Selector dinámico de cambios
    nombres_cambios = [f"[{c['id']}] {c['titulo']}" for c in st.session_state.cambios_db]
    cambio_elegido_str = st.selectbox("Seleccione la directriz a consultar", nombres_cambios)
    
    # Encontrar el cambio seleccionado
    cambio_activo = next(c for c in st.session_state.cambios_db if f"[{c['id']}] {c['titulo']}" == cambio_elegido_str)
    
    st.markdown(f"### 📌 Detalle operativo para: **{cambio_activo['titulo']}**")
    st.info(f"🏷️ **Categoría:** {cambio_activo['categoria']} | 📊 **Estado en red:** {cambio_activo['estado']}")
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        hacer_html = "".join([f"<li>{item}</li>" for item in cambio_activo['hacer']])
        st.markdown(f"""
            <div style="background-color: #e8f5e9; padding: 20px; border-radius: 8px; border-left: 5px solid #4CAF50; min-height: 180px;">
                <h4 style="color: #2e7d32; margin-top:0;">✅ LO QUE SÍ TOCA HACER</h4>
                <ul style="padding-left: 20px; color: #1b5e20; font-size: 15px;">
                    {hacer_html}
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col_g2:
        no_hacer_html = "".join([f"<li>{item}</li>" for item in cambio_activo['no_hacer']])
        st.markdown(f"""
            <div style="background-color: #ffebee; padding: 20px; border-radius: 8px; border-left: 5px solid #E30613; min-height: 180px;">
                <h4 style="color: #c62828; margin-top:0;">❌ LO QUE NO SE DEBE HACER</h4>
                <ul style="padding-left: 20px; color: #b71c1c; font-size: 15px;">
                    {no_hacer_html}
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown(f"**📝 Criterio Único Oficial Registrado en Ficha:** *{cambio_activo['criterio']}*")
