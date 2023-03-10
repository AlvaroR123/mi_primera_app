import streamlit as st
import pandas as pd
st.image("p.png")

##Al momento que salgan las nuevas bases oficom se deben actualizar las fechas, el AÑO debe ir en formato año_anterior - año_actual, 
# y MES enero-mes_actual
MES = "Enero-Diciembre"
mes_inicio = "Enero"
mes_actual = "Diciembre"
año_anterior = "2021"
año_actual = "2022"
AÑO = "2021-2022" 
titulo1 = "Visualización Datos Estadísticos Exportaciones Colombia {}".format(AÑO)
st.title(titulo1)
SUBTITULO = "{}".format(MES)
st.title(SUBTITULO)

@st.cache
def load_data():
    data = pd.read_excel("OFICOM2022.xlsx")
    return data

df = load_data()

#st.write("Muestra de los datos:")

st.subheader("Estatísticas descriptivas exportaciones totales:")
st.write(df[['AÑO_ACTUAL_CORRIDO_FOB', "AÑO_ACTUAL_CORRIDO_PESO" ,'AÑO_ANTERIOR_CORRIDO_FOB', "AÑO_ANTERIOR_CORRIDO_PESO" ]].describe())
subheader1 = "Las exportaciones de Colombia entre los meses de {} se han comportado de la siguiente manera:".format(MES)
st.subheader(subheader1)

total_sum = df['AÑO_ACTUAL_CORRIDO_FOB'].sum()
last_total_sum = df['AÑO_ANTERIOR_CORRIDO_FOB'].sum()
variacion = (total_sum - last_total_sum) / last_total_sum
Variacion = round(variacion, 3)
if variacion > 0:
    result1 = "Las exportaciones totales de Colombia de {} a {} para el {} fue de USD {}Millones, mientras que las exportaciones totales para el año inmediatamente anterior USD {}Millones, esto quiere decir hubo un con un crecimiento del {}'%' frente al mismo periodo".format(mes_inicio, mes_actual,año_actual,total_sum,last_total_sum, Variacion) 
    st.write(result1)
elif variacion < 0: 
    result2 = "Las exportaciones totales de Colombia de {} a {} para el {} fue de USD {}Millones, mientras que las exportaciones totales para el año inmediatamente anterior USD {}Millones, esto quiere decir hubo un con una disminución del {}'%' frente al mismo periodo".format(mes_inicio, mes_actual,año_actual,total_sum,last_total_sum, Variacion)
    st.write(result2)
elif variacion == 0:
    result3 = "Las exportaciones totales de Colombia de {} a {} para el {} fue de USD {}Millones, mientras que las exportaciones totales para el año inmediatamente anterior USD {}Millones, esto quiere decir hubo una varaición considerable".format(mes_inicio, mes_actual,año_actual,total_sum,last_total_sum)
    st.write(result3)



st.title("Exportaciones no minero energeticas")
df_nominero = df[df["TIPO"]== "No Mineras"]
st.subheader("Estatísticas descriptivas exportaciones NO mineras:")
st.write(df_nominero[['AÑO_ACTUAL_CORRIDO_FOB', "AÑO_ACTUAL_CORRIDO_PESO" ,'AÑO_ANTERIOR_CORRIDO_FOB', "AÑO_ANTERIOR_CORRIDO_PESO" ]].describe())
nm_total_sum = round(df_nominero['AÑO_ACTUAL_CORRIDO_FOB'].sum(), 2)
nm_last_total_sum = round(df_nominero['AÑO_ANTERIOR_CORRIDO_FOB'].sum(), 2)
nm_variacion = (nm_total_sum - nm_last_total_sum) / nm_last_total_sum
nm_Variacion = round(nm_variacion, 3)
if nm_variacion > 0:
    nm_result1 = "Entre {} de {}, las exportaciones no minero energéticas de Colombia fueron de USD {}millones mientras que en {} las exportaciones no minero energeticos fue de USD {}millones, lo que significa un aumento del {}'%' respecto al {}".format(MES, año_actual,nm_total_sum,año_anterior,nm_last_total_sum, nm_Variacion, año_anterior) 
    st.write(nm_result1)   
elif nm_variacion < 0: 
     nm_result2 = "Entre {} de {}, las exportaciones no minero energéticas de Colombia fueron de USD {}millones mientras que en {} las exportaciones no minero energeticos fue de USD {}millones, lo que significa una disminución del {}'%' respecto al {}".format(MES, año_actual,nm_total_sum,año_anterior,nm_last_total_sum, nm_Variacion, año_anterior) 
     st.write(nm_result2)
elif nm_variacion == 0:
    nm_result3 = "Entre {} de {}, las exportaciones no minero energéticas de Colombia fueron de USD {}millones mientras que en {} las exportaciones no minero energeticos fue de USD {}millones, lo que significa no hubo variación".format(MES, año_actual,nm_total_sum,año_anterior,nm_last_total_sum) 
    st.write(nm_result3)


