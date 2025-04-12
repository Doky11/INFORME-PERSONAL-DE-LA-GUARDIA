import streamlit as st
from utils import rellenar_docx, calcular_nota

st.set_page_config(page_title="Informe Guardia", layout="centered")

st.title("INFORME PERSONAL DE LA GUARDIA")

st.subheader("Datos del informe")
informante = st.text_input("Informante")
fecha = st.text_input("Fecha (dd.mm.aaaa)")
alumno = st.text_input("Alumno")
puesto = st.text_input("Puesto")

categorias = [
    "POLICÍA", "DISCIPLINA", "INTERES", "RESPONSABILIDAD", "INICIATIVA",
    "CONFIANZA EN SI MISMO", "ACTITUD CON LOS SUBORDINADOS", "ACTITUD CON EL MANDO",
    "COMPETENCIA / EFICACIA", "TRATO", "RESISTENCIA A LA FATIGA"
]

conceptos = []
st.subheader("Evaluación por categorías")
for cat in categorias:
    with st.expander(cat):
        tics = 0
        for i in range(1, 7):
            if st.checkbox(f"{cat} - Pregunta {i}", key=f"{cat}_q{i}"):
                tics += 1
        nota, letra = calcular_nota(tics)
        st.markdown(f"**Nota:** {nota} ({letra})")
        obs = st.text_area(f"Observaciones ({cat})", key=f"obs_{cat}")
        conceptos.append({"categoria": cat, "ticks": tics, "observacion": obs})

st.subheader("Observaciones generales")
observaciones_generales = st.text_area("Observaciones generales / justificación")

if st.button("Generar Informe"):
    datos = {
        "informante": informante,
        "fecha": fecha,
        "alumno": alumno,
        "puesto": puesto,
    }
    path = rellenar_docx(datos, conceptos, observaciones_generales)
    with open(path, "rb") as f:
        st.download_button("Descargar informe .docx", f, file_name="Informe_Personal_Guardia.docx")
