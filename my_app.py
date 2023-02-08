import streamlit as st
import pandas as pd
st.image("Procolombia.png")
@st.cache
def load_data():
    data = pd.read_excel("OFICOM2022.xlsx")
    return data

df = load_data()

#st.write("Muestra de los datos:")

st.subheader("Estatísticas descriptivas exportaciones totales:")
st.write(df[['AÑO_ACTUAL_CORRIDO_FOB', "AÑO_ACTUAL_CORRIDO_PESO" ,'AÑO_ANTERIOR_CORRIDO_FOB', "AÑO_ANTERIOR_CORRIDO_PESO" ]].describe())
