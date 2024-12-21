from Base_de_datos.Conexion_base_datos import conexion_base_de_datos
from mysql.connector import Error

def Tabla_recursos(Expediente, Recurso, Oficina_de_evaluacion, Fecha_de_presentacion, Tipo_de_recurso, Estado_actual):
    conexion = conexion_base_de_datos()

    #if conexion is None:
        #print("No se pudo establecer la conexión con la base de datos")

    try:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Recursos(
                       Expediente VARCHAR(50),
                       Recurso VARCHAR(50) DEFAULT NULL,
                       Oficina_de_evaluacion VARCHAR(10) DEFAULT NULL,
                       Fecha_de_presentacion VARCHAR(20) DEFAULT NULL,
                       Tipo_de_recurso VARCHAR(30) DEFAULT NULL,
                       Estado_actual VARCHAR(20) DEFAULT NULL)""")
        
        query_sql = """INSERT INTO Recursos(Expediente, Recurso, Oficina_de_evaluacion, Fecha_de_presentacion, Tipo_de_recurso, Estado_actual)VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (Expediente, Recurso, Oficina_de_evaluacion, Fecha_de_presentacion, Tipo_de_recurso, Estado_actual)

        cursor.execute(query_sql, valores)
        conexion.commit()

    except Error as e:
        print(f"Error durante la operación: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            #print("Conexión cerrada.")
