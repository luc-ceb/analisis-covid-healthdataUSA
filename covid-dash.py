import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import datetime


df_report = pd.read_csv("Datasets/COVID_19_reported.csv", parse_dates=["date"])

df_mask = df_report['date'] < '2022-01-01'
df_dash = df_report[df_mask]

df_mask = df_dash['date'] >= '2020-01-01'
df_dash = df_dash[df_mask]

df_dash.sort_values(by='date', ascending = True,
                 inplace = True)
df_dash = df_dash.reset_index(drop=True)

df_dash['year'] = df_dash['date'].dt.year
df_dash['date'] = df_dash['date'].apply(lambda x:x.toordinal())

df_dash = df_dash[['date','state','total_adult_patients_hospitalized_confirmed_covid','inpatient_bed_covid_utilization','adult_icu_bed_utilization']]



st.title('Analisis COVID-19 Reported Patient Impact and Hospital')

# Checkbox presentacion de la tabla
if st.checkbox('Mostrar tabla'):
    st.subheader('Vista de los datos contenidos')
    st.table(df_dash.head(10))


st.title('Ranking de Estados con mayor ocupación hospitalaria por COVID')

df_dash_ranking = df_dash.groupby(['state'])['inpatient_bed_covid_utilization'].mean().sort_values(ascending=False)
st.table(df_dash_ranking.head(10))


st.title('Linechart ejemplo')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


st.title('Evolucion de los pacientes hospitalizados con COVID confirmado')
# Filtrar data
option = st.selectbox(
    'Que estado quiere seleccionar?',
     df_dash['state'])

'Seleccionaste: ', option


filtered_data = df_dash[df_dash["state"] == option]
filtered_data = filtered_data[["date",'state','total_adult_patients_hospitalized_confirmed_covid']]
filtered_data['total_adult_patients_hospitalized_confirmed_covid'].fillna(0, inplace=True)
filtered_data = filtered_data.reset_index(drop=True)
st.table(filtered_data.tail(10))

#filtered_data = filtered_data[["date",'total_adult_patients_hospitalized_confirmed_covid']]
#st.line_chart(filtered_data)
