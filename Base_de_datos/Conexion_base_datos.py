import mysql.connector
from mysql.connector import Error

# Configuración de conexión
def conexion_base_de_datos():
    try:
        conexion = mysql.connector.connect(
            host="localhost",       # Servidor MySQL (usa 'localhost' para tu computadora local)
            user="root",            # Usuario (generalmente 'root' para el administrador)
            password="*",  # Contraseña del usuario
            database="*"    # Nombre de la base de datos existente
        )

        # Verificar conexión
        #if conexion.is_connected():
            #print("Conexión exitosa a la base de datos")

        return conexion        

    #Si no existe la base de datos la crea
    except Error as e:
        try:
            #print("Conexión muy fallida a la base de datos, entonces creamos la base de datos")
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="*")

            cursor = conexion.cursor()

            #Crear una base de datos
            cursor.execute("CREATE DATABASE IF NOT EXISTS Scraping")
            cursor.close()
            conexion.close()
            
            #print("Base de datos creada")

            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="*",
                database="*")
        
        #Si no se pudo crear la base de datos
        except Error as e:
            print(f"No se pudo crear la base de datos: {e}")
            return None
