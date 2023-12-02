import pandas as pd
from tabulate import tabulate

#a. Crear una función que retorne un DataFrame indexado, con la siguiente Información: (5%)
def crear_dataframe():
    data = {'Calorías': [420, 380, 390, 490, 300],
            'Tiempo': [60, 40, 75, 55, 45]}
    index = ['L', 'M', 'X', 'J', 'V']
    df = pd.DataFrame(data, index=index)
    return df

#b. Crear una función que reciba como parámetro el Data Frame anterior, y retorne la media, mediana y desviación estándar de ambas columnas. (5%)
def calcular_estadisticas(dataframe):
    estadisticas = {
        'Media_Calorías': dataframe['Calorías'].mean(),
        'Mediana_Calorías': dataframe['Calorías'].median(),
        'Desviación_Calorías': dataframe['Calorías'].std(),
        'Media_Tiempo': dataframe['Tiempo'].mean(),
        'Mediana_Tiempo': dataframe['Tiempo'].median(),
        'Desviación_Tiempo': dataframe['Tiempo'].std()
    }
    return estadisticas

# c. Desarrollar una función que agregue otra columna al Data Frame para ver si se ha cumplido el reto de quemar más de 400 calorías por hora (Calorías/Tiempo > 400/60). El Data Frame resultante debe ser el siguiente: (5%)
def agregar_columna_reto(dataframe):
    dataframe['Reto'] = dataframe.apply(lambda row: row['Calorías'] / row['Tiempo'] > 400/60, axis=1)
    return dataframe

# d. Crear una función que retorne el porcentaje de días que se ha conseguido el reto y los que no. (10%)
def calcular_porcentaje_cumplimiento(dataframe):
    total_dias = len(dataframe)
    cumplidos = dataframe['Reto'].sum()
    porcentaje_cumplimiento = (cumplidos / total_dias) * 100
    porcentaje_no_cumplimiento = 100 - porcentaje_cumplimiento
    return porcentaje_cumplimiento, porcentaje_no_cumplimiento

# DataFrame como una tabla
def imprimir_tabla(dataframe):
    tabla = tabulate(dataframe, headers='keys', tablefmt='pipe', showindex=True)
    print(tabla)

df = crear_dataframe()
print("DataFrame Original:")
imprimir_tabla(df)

estadisticas = calcular_estadisticas(df)
print("\nEstadísticas:")
print(estadisticas)

df_con_reto = agregar_columna_reto(df.copy())
print("\nDataFrame con columna de Reto:")
imprimir_tabla(df_con_reto)

porcentaje_cumplimiento, porcentaje_no_cumplimiento = calcular_porcentaje_cumplimiento(df_con_reto)
print(f"\nPorcentaje de días que se ha cumplido el reto: {porcentaje_cumplimiento}%")
print(f"Porcentaje de días que no se ha cumplido el reto: {porcentaje_no_cumplimiento}%")
