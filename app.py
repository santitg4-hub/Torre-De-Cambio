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
            st.success(f"Ficha validada y aprobada mediante compuerta de capacidad para {len(estaciones_ficha)} estaciones.")

with tab_pulso:
    st.subheader("Instrumento 2: Registro de Pulso Semanal en Puesto de Trabajo")
    st.markdown("Menos de 2 minutos por levantamiento en el celular del instructor (10 min por semana por estación).")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.form("form_pulso_realtime"):
        col_p1, col_p2 = st.columns(2)
        with col_p1:
            estacion_pulso = st.selectbox("Estacion evaluada", ["BOG Bogotá El Dorado", "MDE Medellín Rionegro", "CLO Cali", "CTG Cartagena", "MIA Miami", "MAD Madrid", "SAL San Salvador", "LET Leticia"])
            semana = st.selectbox("Periodo de auditoria actual", ["Semana 45 - 2 Nov 2026", "Semana 46 - 9 Nov 2026", "Semana 47 - 16 Nov 2026"])
            cambio_eval = st.selectbox("Politica auditada", ["Equipaje de mano (regla con margen)", "Baterías de litio (regla dura)", "Documentos de viaje"])
            
        with col_p2:
            st.markdown("<b>Verificacion en Puesto (5 observaciones)</b>", unsafe_allow_html=True)
            obs_conformes = st.slider("Observaciones conformes detectadas", 0, 5, 4)
            
            st.markdown("<b>Prueba de Consistencia (3 Agentes)</b>", unsafe_allow_html=True)
            resp_a = st.selectbox("Agente Turno A", ["Acepta criterio unificado", "Discrepa criterio"])
            resp_b = st.selectbox("Agente Turno B", ["Acepta criterio unificado", "Discrepa criterio"])
            resp_c = st.selectbox("Agente Turno C", ["Acepta criterio unificado", "Discrepa criterio"])

        st.markdown("<br>", unsafe_allow_html=True)
        btn_registrar_pulso = st.form_submit_button("Registrar Pulso en Tiempo Real")

    if btn_registrar_pulso:
        puntaje_calculado = int((obs_conformes / 5.0) * 80 + (20 if (resp_a == resp_b == resp_c) else 5))
        estado_texto = f"{puntaje_calculado} - Adoptado" if puntaje_calculado >= 75 else f"{puntaje_calculado} - En riesgo"
        
        columna_politica = "Equipaje de mano (regla con margen)"
        if "Baterías" in cambio_eval:
            columna_politica = "Baterías de litio (regla dura)"
        elif "Documentos" in cambio_eval:
            columna_politica = "Documentos de viaje"

        df_temp = st.session_state.matriz_red
        idx_estacion = df_temp.index[df_temp["Estación"] == estacion_pulso].tolist()
        
        if idx_estacion and columna_politica in df_temp.columns:
            df_temp.at[idx_estacion[0], columna_politica] = estado_texto
            st.session_state.matriz_red = df_temp

        nuevo_id = max([item['id'] for item in st.session_state.historial_pulsos], default=0) + 1
        nuevo_historial = {
            "id": nuevo_id,
            "estacion": estacion_pulso,
            "periodo": semana,
            "politica": cambio_eval,
            "resultado": f"Indice de alineación calculado: {puntaje_calculado}% (Actualizado en tiempo real)",
            "color": "#2e7d32" if puntaje_calculado >= 75 else "#d32f2f"
        }
        st.session_state.historial_pulsos.insert(0, nuevo_historial)
        
        st.success(f"Pulso registrado para {estacion_pulso}. Tablero y matriz actualizados en tiempo real.")

    # SECCIÓN HISTÓRICA CON GESTIÓN Y BOTÓN DE ELIMINAR
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.subheader("Historial Cronológico y Gestión de Auditorías")
    st.markdown("Seleccione un registro histórico para eliminarlo y mantener limpia la trazabilidad:")
    
    if len(st.session_state.historial_pulsos) > 0:
        # Formulario para eliminar registros de forma interactiva
        with st.form("form_eliminar_historial"):
            opciones_historial = {f"ID {item['id']} | {item['estacion']} - {item['politica']} ({item['periodo'])"} : item['id'] for item in st.session_state.historial_pulsos}
            
            registro_a_borrar = st.selectbox("Seleccione el registro de auditoría a eliminar", options=list(opciones_historial.keys()))
            btn_eliminar = st.form_submit_button("Eliminar Registro Seleccionado")
            
            if btn_eliminar and registro_a_borrar:
                id_a_quitar = opciones_historial[registro_a_borrar]
                st.session_state.historial_pulsos = [item for item in st.session_state.historial_pulsos if item['id'] != id_a_quitar]
                st.success(f"Registro eliminado correctamente de la base de datos histórica.")
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        for item in st.session_state.historial_pulsos:
            st.markdown(f"""
            <div class="card-historial">
                <b>ID Registro: {item['id']} | Estación: {item['estacion']}</b> | <b>Periodo:</b> {item['periodo']} | <b>Política:</b> {item['politica']}<br>
                <span style="color: {item['color']}; font-weight: 600;">Resultado: {item['resultado']}</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No hay registros históricos en este momento.")

with tab_tablero:
    st.subheader("Instrumento 3: Tablero Semanal de Adopción por Estación")
    st.markdown("Semana 45 - 2 Nov 2026 | Dónde se está quedando cada cambio, esta semana (Actualizado en tiempo real).")
    st.markdown("<br>", unsafe_allow_html=True)
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card"><b>Cambios activos</b><br><span style="font-size:24px; font-weight:bold; color:#222;">5</span></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><b>Celdas en riesgo</b><br><span style="font-size:24px; font-weight:bold; color:#d32f2f;">4</span></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><b>Estaciones sobre compuerta</b><br><span style="font-size:24px; font-weight:bold; color:#d32f2f;">3</span> <span style="font-size:11px; color:#666;">max. 3 activos</span></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><b>Calidad de despliegue</b><br><span style="font-size:24px; font-weight:bold; color:#222;">50%</span> <span style="font-size:11px; color:#666;">umbral 40%</span></div>', unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.dataframe(st.session_state.matriz_red, use_container_width=True)
    
    st.markdown("""
    <div style="background-color: #eef2f7; padding: 14px; border-radius: 6px; font-size: 12px; color: #333; margin-top: 15px;">
        <b>Convenciones de estados:</b> Adoptado | En riesgo | Cerrado | En despliegue | No aplica | Índice 0-100 sin ranking. (Los valores se actualizan en vivo al registrar o eliminar pulsos).
    </div>
    """, unsafe_allow_html=True)

with tab_fases:
    st.subheader("Medición y Arranque: Plan de Despliegue por Fases")
    st.markdown("Un índice por celda, un piloto antes de escalar a toda la red.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_fase1, col_fase2, col_fase3, col_fase4 = st.columns(4)
    with col_fase1:
        st.markdown("""
        <div style="background:white; padding:20px; border-radius:8px; border-top:4px solid #666; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
            <b>FASE 0: Diseño</b><br><span style="color:#666; font-size:12px;">2 a 3 semanas</span>
            <p style="font-size:12px; margin-top:10px; color:#444;">Estructuración de fichas y validación de indicadores base.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_fase2:
        st.markdown("""
        <div style="background:white; padding:20px; border-radius:8px; border-top:4px solid #d32f2f; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
            <b>FASE 1: Piloto</b><br><span style="color:#d32f2f; font-size:12px; font-weight:600;">6 a 8 semanas</span>
            <p style="font-size:12px; margin-top:10px; color:#444;">Validación de equipaje de mano en 3 a 5 estaciones piloto.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_fase3:
        st.markdown("""
        <div style="background:white; padding:20px; border-radius:8px; border-top:4px solid #666; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
            <b>FASE 2: Segunda ola</b><br><span style="color:#666; font-size:12px;">4 a 6 semanas</span>
            <p style="font-size:12px; margin-top:10px; color:#444;">Expansión controlada a 2 estaciones adicionales.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_fase4:
        st.markdown("""
        <div style="background:white; padding:20px; border-radius:8px; border-top:4px solid #666; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
            <b>FASE 3: Red completa</b><br><span style="color:#666; font-size:12px;">Operación continua</span>
            <p style="font-size:12px; margin-top:10px; color:#444;">Cadencia de seguimiento semanal institucionalizada.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("### Composición Ponderada del Índice Operativo")
    st.markdown("<br>", unsafe_allow_html=True)
    c_i1, c_i2, c_i3, c_i4 = st.columns(4)
    c_i1.metric("Cobertura", "20%")
    c_i2.metric("Ejecución observada", "40%")
    c_i3.metric("Respuesta única", "20%")
    c_i4.metric("Persistencia", "20%")
