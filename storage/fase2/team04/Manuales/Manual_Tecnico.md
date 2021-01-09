# Tytus - Manual Tecnico
---
##Objetivos

General:
Proporcionar una guía útil y entendible para el usuario, explicando detalladamente el programa, métodos etc. 			

Específicos:
•	Brindar al usuario una concepción técnica de la funcionalidad de los principales procesos del sistema incluyendo los conceptos de entrada y salida de datos.

•	Proporcionar información de manera clara para que el usuario no represente mayor dificultad al momento de querer realizar cambios en el programa.
Objetivos

General:
• Proporcionar una guía útil y entendible para el usuario, explicando detalladamente el programa, métodos etc. 			

Específicos:
•	Brindar al usuario una concepción técnica de la funcionalidad de los principales procesos del sistema incluyendo los conceptos de entrada y salida de datos.

•	Proporcionar información de manera clara para que el usuario no represente mayor dificultad al momento de querer realizar cambios en el programa.

## Descripción de La Solución
Para la solución de este proyecto se realizó un análisis del problema y una serie de procesos para resolverlo de manera optima y llegar a un resultado satisfactorio
Para realizar este proyecto se utilizó el lenguaje de programación “Python” el cual es un lenguaje de propósito general, orientado a objetos, que también puede utilizarse para el desarrollo web.
forma sencilla para interactuar con la solución y se pueda observar el comportamiento de las 
estructuras de datos y como funcionan estas mismas dentro de la solución. Las estructuras de datos utilizadas fueron árboles en su mayoria, en específico árboles AVL y árboles B+, esto para mejorar el rendimiento de ejecución de la solución.

##Requisitos del sistema operativo
•	MS Windows XP o superior.
•	Apple OSX 10.4.x o superior.
•	GNU/Linux 2.6.x o superior.
•	Python 2.6 (opcionalmente Python 2.7, para Plone 4.2 y superior).

##Metodos
•	Método:  dropDatabas (database: str) -> int:
 Descripción: Elimina por completo la base de datos indicada en database           Parámetros.

•	Método:  __drop_database_sp (database: str, mode: str) -> int:
 Descripción: Elimina por la base de datos con el nombre y modo 
Indicados.


•	Método:  createTable (database: str, table: str, numberColumns: int) -> int:
 Descripción:   Crea una nueva tabla en la base de datos indicada


•	Método:  __create_table_sp (database: str, table: str, numberColumns: int, mode: str) -> int:
 Descripción:   Crea una nueva tabla en la base de datos indicada con el modo indicado.

•	Método:  showTables (database: str) -> list:
Descripción:  Devuelve una lista con los nombres de todas las tablas de la base de datos.

•	Método:  alterDropPK (database: str, table: str) -> int: 
Descripción:  Elimina la llave primaria actual en la información de la tabla, manteniendo el índice actual de la estructura del árbol hasta que se invoque de nuevo el alterAddPK().


•	Método:  alterAddColumn (database: str, table: str, default: any) -> int:
Descripción: Agrega una columna al final de cada registro de la tabla y base de datos especificada.

•	Método:  alterDropColumn (database: str, table: str, columnNumber: int) -> int:
Descripción:   Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias.

•	Método:  codificar (text, encoding):
Descripción: Convierte un string en bytes utilizando la codificación especificada.

•	Método: insert (database: str, table: str, register: list):
Descripción: Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.

•	Método:  __insert_sp (database: str, table: str, register: list, mode: str):
Descripción: Inserta un registro en la estructura de datos asociada a la tabla y la base de datos con el modo indicado.

•	Método:  loadCSV (file: str, database: str, table: str) -> list:
Descripción: Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado


•	Método:  get_routes (database: str) -> list:
Descripción: Devuelve una lista con las rutas de todos los archivos binarios relacionados a la base de datos indicada.

•	Método:  get_route_table (database: str, table: str) -> list:
Descripción: Devuelve una ruta del archivo binario correspondiente a la tabla indicada.

•	Método: extractTable (database,table):
Descripción: Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla.

•	Método: __drop_table_sp(database, table, mode):
Descripción: Elimina una tabla especificada en una base de datos con el nombre y modo especificados.

•	Método: __drop_table_sp(database, table, mode):
Descripción: Elimina una tabla especificada en una base de datos con el nombre y modo especificados.

Métodos de TBList.py:
•	Método: create(self, name, columns):
Descripción: Elimina una tabla especificada en una base de datos con el nombre y modo especificados.

•	Método: show(self):
•	Descripción; Imprime en consola la información de todos los nodos en la lista.


•	Método: search(self, name):
•	Descripción: Busca un nodo en la lista utilizando su nombre como parámetro de búsqueda.


Métodos de DBList.py:
•	Método: create(self, name, mode, encoding):
•	Descripción: Crea un nuevo nodo con la información de la base de datos

•	Método: show(self):
Descripción: Imprime en consola la información de todos los nodos en la lista.

•	Método: search(self, name):
•	Descripción: Busca un nodo en la lista utilizando su nombre como parámetro de búsqueda.

•	Método: find_all(self, name):
Descripción: Devuelve una lista con todos los nodos correspondientes a una misma base de datos.

•	Método: list_databases_diff(self):
Descripción: Devuelve una lista con los nombres de todas las bases de datos sin repetición.

•	Método: delete(self, name):
Descripción: Elimina de la lista el nodo que tenga el nombre indicado.

•	Método: modify(self, name, new_mode, new_encoding):
Descripción: Modifica la información contenida en un nodo

•	Método: find_table(self, database, table):
Descripción: Devuelve el TBNode cuyo nombre coincida con el indicado.





•	Método: delete(self, name):
Descripción: Elimina de la lista el nodo que tenga el nombre indicado.

•	Método: modify(self, name, new_pk, new_columns):
Descripción: Modifica la información contenida en un nodo.
Nodos de TBList (TBNode):

