import mysql.connector

from src.core.config import DATABASE_CONFIG

def create_mysql():
    try:
        connection = mysql.connector.connect(**DATABASE_CONFIG) 
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        raise