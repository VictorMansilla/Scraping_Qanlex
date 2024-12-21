from Base_de_datos.Conexion_base_datos import conexion_base_de_datos
from mysql.connector import Error

def Tabla_actuaciones(Expediente, Oficina, Fecha, Tipo, Descipcion_detalle, AFS):
    conexion = conexion_base_de_datos()

    #if conexion is None:
        #print("No se pudo establecer la conexión con la base de datos")

    try:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Actuaciones(
                       Expediente VARCHAR(50),
                       Oficina VARCHAR(50) DEFAULT NULL,
                       Fecha VARCHAR(15) DEFAULT NULL,
                       Tipo VARCHAR(500) DEFAULT NULL,
                       Descipcion_detalle VARCHAR(200) DEFAULT NULL,
                       AFS VARCHAR(10) DEFAULT NULL)""")
        
        query_sql = """INSERT INTO Actuaciones(Expediente, Oficina, Fecha, Tipo, Descipcion_detalle, AFS)VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (Expediente, Oficina, Fecha, Tipo, Descipcion_detalle, AFS)

        cursor.execute(query_sql, valores)
        conexion.commit()

    except Error as e:
        print(f"Error durante la operación: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            #print("Conexión cerrada.")



def Tabla_Notas(Expediente, Fecha, Interviniente, Descipcion_detalle):
    conexion = conexion_base_de_datos()

    #if conexion is None:
        #print("No se pudo establecer la conexión con la base de datos")

    try:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Notas(
                       Expediente VARCHAR(50),
                       Fecha VARCHAR(15) DEFAULT NULL,
                       Interviniente VARCHAR(500) DEFAULT NULL,
                       Descipcion_detalle VARCHAR(50) DEFAULT NULL)""")
        
        query_sql = """INSERT INTO Notas(Expediente, Fecha, Interviniente, Descipcion_detalle)VALUES (%s, %s, %s, %s)"""
        valores = (Expediente, Fecha, Interviniente, Descipcion_detalle)

        cursor.execute(query_sql, valores)
        conexion.commit()

    except Error as e:
        print(f"Error durante la operación: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            #print("Conexión cerrada.")