# INFORME PERSONAL DE LA GUARDIA

Aplicación web desarrollada con [Streamlit](https://streamlit.io) que permite generar informes personales de guardia en formato `.docx`, siguiendo una estructura formal y personalizada similar a los modelos usados en contextos militares o académicos.

---

## 📝 ¿Qué permite hacer esta app?

- Rellenar un formulario con los siguientes datos:
  - Informante
  - Fecha (con selector de calendario)
  - Alumno
  - Puesto
- Evaluar 11 categorías de comportamiento/aptitudes mediante 6 preguntas tipo checklist cada una.
- Calcular automáticamente la nota numérica y en letra por categoría y una nota media final.
- Añadir observaciones por categoría y generales.
- Generar un archivo `.docx` con toda la información formateada de forma limpia y profesional.

---

## 📷 Interfaz de usuario

La interfaz es limpia y sencilla. Todas las categorías están visibles en pantalla sin necesidad de desplegarlas.

---

## 🚀 Cómo usar

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python instalado.
3. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:

```bash
streamlit run app.py
```

5. Rellena el formulario y descarga el documento generado.

---

## 🌐 Acceso en línea

Si has desplegado la app en Streamlit Cloud, puedes acceder aquí:  
👉 [https://tu-nombre.streamlit.app](https://tu-nombre.streamlit.app) *(actualiza esta URL si es necesario)*

---

## 📄 Formato del documento generado

- Fuente: **Verdana**, tamaño 10 pt.
- Alineación centrada en encabezados y notas, alineación izquierda en observaciones.
- Tabla con columnas: Categoría | A | B | C | D | Observaciones.
- Nota media y observaciones finales al pie del documento.

---

## 📁 Estructura del proyecto

```
📦 informe-personal-de-la-guardia
├── app.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## 👤 Autor

Desarrollado por [Tu nombre o usuario de GitHub].

---

