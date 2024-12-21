import mysql.connector

# Configuración de conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pysqlthon"
)

cursor = conexion.cursor()

# Eliminar la base de datos si existe
cursor.execute("DROP DATABASE IF EXISTS Scraping")

# Crear la base de datos desde cero
cursor.execute("CREATE DATABASE Scraping")

#print("Base de datos Scraping recreada exitosamente.")

# Cerrar la conexión
cursor.close()
conexion.close()
