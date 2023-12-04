import pandas as pd
import numpy as np
from datetime import datetime


def cargar_emisiones():
    archivos = [
        "/Users/fatimagomezdiaz08/Examen_Programacion/Datasets/emisiones-2017.csv",
        "/Users/fatimagomezdiaz08/Examen_Programacion/Datasets/emisiones-2018.csv",
        "/Users/fatimagomezdiaz08/Examen_Programacion/Datasets/emisiones-2019.csv"
    ]
    df = pd.DataFrame()

    for archivo in archivos:
        temp_df = pd.read_csv(archivo, delimiter=';')
        print(temp_df.columns)
        df = pd.concat([df, temp_df])

    # i. Solo tener las siguientes columnas: Estación, Magnitud, Año, Mes y las correspondientes a los días 
    # D01, D02, D03, etc. (5%)
    columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + [f'D{i:02d}' for i in range(1, 32)]
    df = df[columnas]

    # ii. Debe reestructurar el DataFrame para que los valores de los contaminantes de las columnas de los días 
    # aparezcan en una única columna. NOTA: Investigar función melt
    df = pd.melt(df, id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name='Día', value_name='Valor')

    # iii. Añadir una columna con la fecha a partir de la concatenación del año, el mes y el día 
    # (usar el módulo datetime) (5%)
    df['Fecha'] = pd.to_datetime(
        df['ANO'].astype(str) + df['MES'].astype(str).str.zfill(2) + df['Día'].str.extract('(\d+)')[0].str.zfill(2),
        errors='coerce')

    # iv. Eliminar los renglones con fechas no válidas (puede utilizar la función isnat del módulo numpy) y 
    # ordenar el DataFrame por estaciones contaminantes y fecha. (5%)
    df = df.dropna(subset=['Fecha'])
    df = df.sort_values(by=['ESTACION', 'MAGNITUD', 'Fecha'])
    return df


# b. Crear una función que reciba una estación, una magnitud (contaminante) y un rango de fechas. 
# Debe retornar una serie con las emisiones de la magnitud(contaminante) dado en la estación y 
# rango de fechas dado. (5%)
def obtener_emisiones(df, estacion, magnitud, fecha_inicio, fecha_fin):
    filtro = (df['ESTACION'] == estacion) & (df['MAGNITUD'] == magnitud) & (df['Fecha'] >= fecha_inicio) & (
                df['Fecha'] <= fecha_fin)
    return df[filtro][['Fecha', 'Valor']].set_index('Fecha')['Valor']


df_emisiones = cargar_emisiones()
estacion_ejemplo = 'Estacion1'
magnitud_ejemplo = 4
fecha_inicio_ejemplo = pd.to_datetime('2018-01-01')
fecha_fin_ejemplo = pd.to_datetime('2018-12-31')

serie_emisiones = obtener_emisiones(df_emisiones, estacion_ejemplo, magnitud_ejemplo, fecha_inicio_ejemplo,
                                    fecha_fin_ejemplo)
print(df_emisiones.head())
print(serie_emisiones.head())
