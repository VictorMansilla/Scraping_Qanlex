from Base_de_datos.Conexion_base_datos import conexion_base_de_datos
from mysql.connector import Error

def Tabla_vinculados(Expediente, Expediente_vinculado, Dependencia, Situacion, Caratula, Ultima_actualizacion):
    conexion = conexion_base_de_datos()

    #if conexion is None:
        #print("No se pudo establecer la conexión con la base de datos")

    try:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Vinculados(
                       Expediente VARCHAR(50),
                       Expediente_vinculado VARCHAR(50) DEFAULT NULL,
                       Dependencia VARCHAR(70) DEFAULT NULL,
                       Situacion VARCHAR(100) DEFAULT NULL,
                       Caratula VARCHAR(500) DEFAULT NULL,
                       Ultima_actualizacion VARCHAR(15) DEFAULT NULL)""")
        
        query_sql = """INSERT INTO Vinculados(Expediente, Expediente_vinculado, Dependencia, Situacion, Caratula, Ultima_actualizacion)VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (Expediente, Expediente_vinculado, Dependencia, Situacion, Caratula, Ultima_actualizacion)

        cursor.execute(query_sql, valores)
        conexion.commit()

    except Error as e:
        print(f"Error durante la operación: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            #print("Conexión cerrada.")

