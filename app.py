import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="SoBe Pools", page_icon="🌊")
st.title("🌊 Control de Piscinas South Beach")

# Formulario
with st.form("registro"):
    tecnico = st.selectbox("Técnico", ["Juan", "Carlos", "Luis"])
    cliente = st.text_input("Dirección del Cliente")
    ph = st.number_input("Nivel de pH", 6.0, 8.5, 7.2)
    cloro = st.number_input("Cloro (ppm)", 0.0, 5.0, 2.0)
    notas = st.text_area("Notas / Observaciones")
    boton = st.form_submit_button("ENVIAR REPORTE")

if boton:
    st.success(f"✅ Reporte enviado para {cliente}. ¡Certeza total!")
    st.balloons()
