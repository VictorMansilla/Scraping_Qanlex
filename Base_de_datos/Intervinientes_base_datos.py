from Base_de_datos.Conexion_base_datos import conexion_base_de_datos
from mysql.connector import Error

def Tabla_partes(Expediente, Tipo, Nombre, Tomo_folio, IEJ):
    conexion = conexion_base_de_datos()

    #if conexion is None:
        #print("No se pudo establecer la conexión con la base de datos")

    try:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Partes(
                       Expediente VARCHAR(50),
                       Tipo VARCHAR(50),
                       Nombre VARCHAR(100),
                       Tomo_folio VARCHAR(30) DEFAULT NULL,
                       IEJ VARCHAR(30))""")
        
        query_sql = """INSERT INTO Partes(Expediente, Tipo, Nombre, Tomo_folio, IEJ)VALUES (%s, %s, %s, %s, %s)"""
        valores = (Expediente, Tipo, Nombre, Tomo_folio, IEJ)

        cursor.execute(query_sql, valores)
        conexion.commit()

    except Error as e:
        print(f"Error durante la operación: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            #print("Conexión cerrada.")



def Tabla_fiscales(Expediente, Fiscalia, Fiscal, IEJ):
    conexion = conexion_base_de_datos()

    #if conexion is None:
        #print("No se pudo establecer la conexión con la base de datos")

    try:
        cursor = conexion.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS Fiscales(
                       Expediente VARCHAR(50),
                       Fiscalia VARCHAR(150) DEFAULT NULL,
                       Fiscal VARCHAR(100) DEFAULT NULL,
                       IEJ VARCHAR(70) DEFAULT NULL)""")
        
        query_sql = """INSERT INTO Fiscales(Expediente, Fiscalia, Fiscal, IEJ)VALUES (%s, %s, %s, %s)"""
        valores = (Expediente, Fiscalia, Fiscal, IEJ)

        cursor.execute(query_sql, valores)
        conexion.commit()

    except Error as e:
        print(f"Error durante la operación: {e}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            #print("Conexión cerrada.")