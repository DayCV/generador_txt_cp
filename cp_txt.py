import streamlit as st
import pandas as pd

# =========================
# Listas de códigos postales
# =========================
listas_cp = {
    "Tlaxcala":[90000,90006,90010,90013,90014,90019,90020,90030,90040,90050,90060],
    "Puebla":[72000,72010,72013,72014,72015,72016,72017,72019,72020,72023],
    "Hidalgo":[42000,42004,42010,42014,42015,42018,42020,42026,42027,42029],
    "CDMX":[1000,1010,1020,1030,1040,1049,1050,1060,1070,1080],
    "EdoMex":[50000,50010,50016,50017,50020,50026,50040,50050,50060,50070],
    "Michoacan":[58011,58111,58241,58882,58461,58361,58405,58421,61601,58482]
}

# =========================
# Interfaz
# =========================
st.set_page_config(page_title="Generador de TXT por Estado", page_icon="📄")
st.title("Generador de TXT por Estado")

# Selección de estado
estado = st.selectbox("Selecciona un estado", list(listas_cp.keys()))

# Ingreso de RFC y nombre
rfc = st.text_input("RFC").upper()
nombre = st.text_input("Nombre").upper()

# Botón para generar TXT
if st.button("Generar TXT"):
    if not estado or not rfc or not nombre:
        st.error("Todos los campos son obligatorios")
    else:
        codigos = listas_cp[estado]

        # Crear DataFrame
        df = pd.DataFrame({
            "num": range(1, len(codigos)+1),
            "rfc": rfc,
            "nombre": nombre,
            "cp": codigos
        })

        # Convertir a TXT con separador | y sin índice ni encabezado
        txt_data = df.to_csv(sep="|", index=False, header=False)

        # Botón para descargar
        st.download_button(
            label="Descargar TXT",
            data=txt_data,
            file_name=f"{estado}_{rfc}.txt",
            mime="text/plain"
        )

        st.success(f"Archivo listo para descargar: {estado}_{rfc}.txt")
