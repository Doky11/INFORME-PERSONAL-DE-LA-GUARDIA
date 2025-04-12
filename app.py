import streamlit as st
from utils import generar_informe, calcular_nota
from datetime import date

st.set_page_config(page_title="Informe Guardia", layout="centered")
st.title("INFORME PERSONAL DE LA GUARDIA")

st.subheader("Datos del informe")
informante = st.text_input("Informante")
fecha = st.date_input("Fecha", value=date.today(), format="DD.MM.YYYY").strftime("%d.%m.%Y")
alumno = st.text_input("Alumno")
puesto = st.text_input("Puesto")

st.subheader("Evaluación por categorías")

categorias = [
    "POLICÍA", "DISCIPLINA", "INTERES", "RESPONSABILIDAD", "INICIATIVA",
    "CONFIANZA EN SÍ MISMO", "ACTITUD CON LOS SUBORDINADOS", "ACTITUD CON EL MANDO",
    "COMPETENCIA / EFICACIA", "TRATO", "RESISTENCIA A LA FATIGA"
]

conceptos = []
for cat in categorias:
    st.markdown(f"### {cat}")
    tics = sum([1 for i in range(1, 7) if st.checkbox(f"{cat} - Pregunta {i}", key=f"{cat}_{i}")])
    nota, letra = calcular_nota(tics)
    st.markdown(f"**Nota provisional:** {nota} ({letra})")
    observacion = st.text_area(f"Observaciones ({cat})", key=f"obs_{cat}")
    conceptos.append({"categoria": cat, "ticks": tics, "observacion": observacion})

st.subheader("Observaciones generales")
observaciones_generales = st.text_area("Observaciones generales / justificación")

if st.button("Generar Informe"):
    datos = {
        "informante": informante,
        "fecha": fecha,
        "alumno": alumno,
        "puesto": puesto
    }
    docx_file = generar_informe(datos, conceptos, observaciones_generales)
    with open(docx_file, "rb") as f:
        st.download_button("📥 Descargar informe .docx", f, file_name="Informe_Personal_Guardia.docx")
