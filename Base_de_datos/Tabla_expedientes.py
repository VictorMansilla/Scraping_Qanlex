from Base_de_datos.Conexion_base_datos import conexion_base_de_datos
from mysql.connector import Error

def Tabla_expedientes(Expediente, Dependencia, Caratula, Situacion, Ultima_actualizacion):
    conexion = conexion_base_de_datos()

    #if conexion is None:
        #print("No se pudo establecer la conexión con la base de datos")

    try:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Expedientes(
                       Expediente VARCHAR(50) PRIMARY KEY,
                       Dependencia VARCHAR(100) DEFAULT NULL,
                       Caratula VARCHAR(500) DEFAULT NULL,
                       Situacion VARCHAR(100) DEFAULT NULL,
                       Ultima_actualizacion VARCHAR(100) DEFAULT NULL)""")
        
        query_sql = """INSERT INTO Expedientes(Expediente, Dependencia, Caratula, Situacion, Ultima_actualizacion)VALUES (%s, %s, %s, %s, %s)"""
        valores = (Expediente, Dependencia, Caratula, Situacion, Ultima_actualizacion)

        cursor.execute(query_sql, valores)
        conexion.commit()

    except Error as e:
        print(f"Error durante la operación: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            #print("Conexión cerrada.")
