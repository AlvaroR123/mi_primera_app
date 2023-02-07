import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
st.image("Procolombia.png")

st.title("Visualización de la base de datos Dane_Oficom.csv")
st.session_state['answer'] = ''!

st.write(st.session_state)

realans = ['', 'abc', 'edf']

if  st.session_state['answer'] in realans:
    answerStat = "correct"
elif st.session_state['answer'] not in realans:
    answerStat = "incorrect"

st.write(st.session_state)
st.write(answerStat)

@st.cache
def load_data():
    data = pd.read_excel("OFICOM2022.xlsx")
    return data

df = load_data()

st.write("Muestra de los datos:")
st.write(df.head())

st.write("Estatísticas descriptivas:")
st.write(df.describe())

st.title("Suma Total de la Columna 'AÑO_ACTUAL_CORRIDO_FOB'")

total_sum = df['AÑO_ACTUAL_CORRIDO_FOB'].sum()

st.write("La suma total de la columna de las exportaciones totales de Colombia en 2023 es: ", total_sum)

st.write("La siguiente gráfica muestra la distribución de los valores en la columna 'AÑO_ACTUAL_CORRIDO_FOB':")

st.sidebar.subheader("histograma")
plt.hist(df['AÑO_ACTUAL_CORRIDO_FOB'], 15, color = "blue", ec ="black")
plt.show()
