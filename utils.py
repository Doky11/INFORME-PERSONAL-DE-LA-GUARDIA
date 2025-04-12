from docx import Document
from docx.shared import Pt

def calcular_nota(tics):
    puntuacion = (tics / 6) * 10
    if puntuacion >= 9:
        letra = 'A'
    elif puntuacion >= 7:
        letra = 'B'
    elif puntuacion >= 5:
        letra = 'C'
    else:
        letra = 'D'
    return round(puntuacion, 1), letra

def rellenar_docx(datos, conceptos, observaciones_generales):
    doc = Document("informe_blanco.docx")

    tabla = doc.tables[0]

    tabla.cell(0, 1).text = datos['informante']
    tabla.cell(1, 1).text = datos['fecha']
    tabla.cell(2, 1).text = datos['alumno']
    tabla.cell(3, 1).text = datos['puesto']

    notas = []
    fila_inicio = 6
    for i, concepto in enumerate(conceptos):
        nota_num, nota_letra = calcular_nota(concepto["ticks"])
        notas.append(nota_num)
        fila = fila_inicio + i
        col_nota = ['A', 'B', 'C', 'D'].index(nota_letra)
        tabla.cell(fila, 1 + col_nota).text = 'X'
        tabla.cell(fila, 5).text = f"({nota_num}) {concepto['observacion']}"

    media = sum(notas) / len(notas)
    if media >= 9:
        letra = 'A'
    elif media >= 7:
        letra = 'B'
    elif media >= 5:
        letra = 'C'
    else:
        letra = 'D'

    doc.paragraphs[-3].text = f"Nota media: {round(media, 1)} ({letra})"
    doc.paragraphs[-1].text = observaciones_generales

    output_path = "informe_generado.docx"
    doc.save(output_path)
    return output_path
