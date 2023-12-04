import pandas as pd
import sqlite3
from tabulate import tabulate

# a. Crear una función que permita guardar el contenido del archivo en una tabla de Base de Datos. 
# Debe asumir que existe una Base de Datos llamada Twitter,  la cual contiene
def limpiar_guardar_en_database(archivo_csv):
    try:
        df = pd.read_csv(archivo_csv, skiprows=1, names=['fecha', 'usuario', 'texto', 'likes'], skipinitialspace=True, delimiter=';', quoting=3)
        df = df.drop_duplicates()
        df = df.dropna(subset=['fecha', 'usuario', 'texto', 'likes'])

        df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
        conn = sqlite3.connect('Twitter.db')
        df.to_sql('Twitter_Bitcoins', conn, index=False, if_exists='replace')
        conn.close()
        print("DataFrame leído desde la base de datos:")
        print(tabulate(df, headers='keys', tablefmt='pretty'))

        df_desde_base = leer_desde_database()
        print("\nDataFrame leído desde la base de datos (leer_desde_base_de_datos):")
        print(tabulate(df_desde_base, headers='keys', tablefmt='pretty'))

        top_tweets = obtener_top_likes(3)
        print("\nTop 3 tweets con más likes (obtener_top_likes):")
        print(tabulate(top_tweets, headers='keys', tablefmt='pretty'))

    except pd.errors.ParserError as e:
        print(f"Error al procesar el archivo CSV: {e}")
        with open(archivo_csv, 'r') as file:
            lines = file.readlines()
            problematic_line = lines[7]
            print(f"Línea problemática - Texto del tweet: {problematic_line}")

# b. Crear una función que  se conecte a la base de datos y lea toda la información de la tabla Twitter_Bitcoins 
# y retorne un DataFrame creado a partir de la información de la tabla. (10%)
def leer_desde_database():
    conn = sqlite3.connect('Twitter.db')
    query = "SELECT * FROM Twitter_Bitcoins"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# c. Crear una función que retorne los twitts con más likes. La función debe de tener como parámetro la cantidad
# de twitts a retornar. Si el parámetro es un 3 debe retornar los tres con mayor número de likes. Si es un 5 debe retornar los cinco con mayor número de likes. Validar que el número no sea mayor a la cantidad de datos. NOTA: Debe tomar en cuenta que esta función se conecta a la base de datos, es decir asume que los datos ya se encuentran en la tabla correspondiente. (5%)
def obtener_top_likes(cantidad):
    conn = sqlite3.connect('Twitter.db')
    query = f"SELECT * FROM Twitter_Bitcoins ORDER BY likes DESC LIMIT {cantidad}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

archivo_csv = '/Users/fatimagomezdiaz08/Examen_Programacion/Datasets/bitcoin-tweets.csv'
limpiar_guardar_en_database(archivo_csv)
