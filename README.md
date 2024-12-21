Proyecto Scraping para Qanlex

Pasos para utilizar el programa:

Clonar el repositorio:
Ejecuta el siguiente comando en tu terminal:
git clone https://github.com/VictorMansilla/Scraping_Qanlex

Crear un entorno virtual:
Ejecuta:
python -m venv venv

Activar el entorno virtual:
venv\Scripts\activate

Instalar los requerimientos:
pip install -r requirements.txt

Instalar MySQL:
Descarga e instala MySQL desde este enlace, ya que es la base de datos requerida.

Configurar la conexión a la base de datos:

Abre el archivo Conexion_base_datos.py ubicado en la carpeta Base_de_datos.
Reemplaza los asteriscos con tu información:
Contraseña de MySQL: Líneas 10, 27 y 41.
Nombre de la base de datos: Líneas 11 y 42.
(Alternativamente, puedes usar un archivo .env para mayor seguridad y flexibilidad.)

Ejecutar el programa:
Corre el archivo Scraping.py:
python Scraping.py

Puntos a tener en cuenta
Captcha manual:
Al abrir la ventana, los campos disponibles se autocompletarán, pero el captcha debe resolverse manualmente.

Para ajustar el tiempo disponible para resolverlo, modifica la línea 26 del archivo Scraping.py. Ajusta el valor según tu preferencia.
Jurisdicción:
Si deseas cambiar la jurisdicción, modifica la línea 23 del archivo Acceder.py con una jurisdicción disponible.

Palabras clave:
Para usar una palabra clave distinta a "residuos", edita la línea 33 del archivo Acceder.py.

Tiempos de carga:
El tiempo para cargar las secciones puede personalizarse en las líneas 18, 28, 38 y 45 del archivo Acceder_a_elementos.py.

Estructura de la base de datos
Toda la información extraída se almacena en una base de datos MySQL, organizada en las siguientes tablas:

Tabla	Descripción
actuaciones :	Contiene las actuaciones relacionadas con los expedientes.
expedientes	: Contiene todos los expedientes, con el campo id_exp como clave primaria.
fiscales : Almacena los fiscales asociados a cada expediente.
notas : Incluye las notas correspondientes a los expedientes.
partes : Almacena las partes involucradas en cada expediente.
recursos : Contiene los recursos presentados en los expedientes.
vinculados : Almacena los datos de los vinculados a los expedientes.
En la tabla expedientes, se almacenan todos los expedientes con id como clave primaria.
Las tablas restantes contienen datos de las secciones asociadas a cada expediente, usando el id como clave foránea.
Si alguna sección no contiene datos, no se almacenará.
