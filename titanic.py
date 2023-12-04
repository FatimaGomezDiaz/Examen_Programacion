import pandas as pd


def limpiar_datos(archivo):
    # a. Generar un dataframe con los datos del archivo.
    df = pd.read_csv(archivo)

    # b. Imprimir el porcentaje de valores nulos de la columna Age(Edad).
    porcentaje_nulos_age = df['Age'].isnull().mean() * 100
    print(f"Porcentaje de valores nulos en la columna Age: {porcentaje_nulos_age:.2f}%")

    # c. Eliminar del DataFrame los pasajeros con edad desconocida.
    df = df.dropna(subset=['Age'])

    # d. Imprimir el porcentaje de valores nulos de la columna Cabin.
    porcentaje_nulos_cabin = df['Cabin'].isnull().mean() * 100
    print(f"Porcentaje de valores nulos en la columna Cabin: {porcentaje_nulos_cabin:.2f}%")

    # e. Sustituir en el DataFrame los valores desconocidos de la columna Cabin por la frase “Sin especificar”.
    df['Cabin'].fillna('Sin especificar', inplace=True)

    # f. Retornar el DataFrame con los cambios realizados.
    return df


archivo_titanic = '/Users/fatimagomezdiaz08/Examen_Programacion/Datasets/titanic.csv'
titanic_limpio = limpiar_datos(archivo_titanic)

# Guardar el DataFrame limpio
archivo_salida = '/Users/fatimagomezdiaz08/Examen_Programacion/Datasets/titanic_limpio.csv'
titanic_limpio.to_csv(archivo_salida, index=False)
print(f"DataFrame limpio guardado en {archivo_salida}")
