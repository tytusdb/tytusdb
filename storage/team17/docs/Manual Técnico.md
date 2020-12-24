 MANUAL TECNICO
===================

## Indice

#### • [Descripción de la solución](#descipcion-de-la-solucion) ####

#### • [Requerimientos Funcionales del Sistema](#requerimientos-funcionales-del-sistema) ####

#### • [Requerimientos del Entorno de Desarrollo](#requerimientos-del-entorno-de-desarrollo) ####

#### • [Diccionario de Clases](#diccionario-de-clases) ####

#### • [Diccionario de Funciones](#diccionario-de-funciones) ####

#### • [Diagramas de Flujo](#diagramas-de-flujo) ####

Descripción de la solución 
-----------------------
#### Almacenamiento ####

Para el almacenamiento de las bases de datos se utilizó un diccionario en el cual se utiliza de índice el nombre de la base de datos; no importando si lo escriben en minúsculas o mayúsculas, al igual que se utilizarón diccionarios para las tablas; donde el índice es el nombre de la tabla, y el valor es el arbol correspondiente.

Para la estructura del arbol B se utilizó un grado 5, para almacenar la información en el arbol, se inserta una tupla con 2 posiciones, en la primera posicion se almacena la llave primaria de la información, y en la segunda posición se guarda la información que se desea almacenar, el arbol ordena dependiendo el número, en caso de que la llave primaria sea un string entonces se utilizará una funcion para sumar todos sus caracteres para comparar su tamaño en ASCII, dando prioridad a los números.

#### Serialización ####

Para preservar la información almacenada en la base de datos y evitar que se cargue información innecesaria en memoria se optó por serializar 2 cosas; la base de datos la cual almacena cada tabla con su configuración de llaves primarias y número de columnas a excepción del arbol de cada tabla, ¿por que? se tomó esta decisión debido funcionalidades de las bases de datos porque al querer llamar a la función showTables() o showDatabases() habria que iterar cada archivo guardado haciendo menos eficiente la busqueda de información, por ello se serializa cada arbol por separado debido a que son independientes de los otros, al hacer cualquier función en una base de datos y tabla especificada esta trae la información almacenada en un arbol, la utiliza para realizar los cambios necesarios, los guarda de nuevo, y cuando termina de utilizarlo lo elimina de la tabla para evitar ocupar demasiado espacio.

Requerimientos Funcionales del Sistema
-----------------------
• Existe un paquete el cual es el encargado de gestionar el almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para ingresar, modificar extraer y eliminar la información.

• Cada registro que corresponde a una tupla de una tabla será almacenado en cada nodo que corresponden a un Arbol B. Estos registros seran débilmente tipados.

• Se proporcionan funciones relacionadas al CRUD de bases de datos, tablas y registros.

• El paquete cuenta con una interfaz gráfica que facilita el manejo de la información, para ello se requiere tener instalado [graphviz](https://graphviz.org/download/)


Requerimientos del Entorno de Desarrollo
-----------------------
• Versión de Python: Python 3.9.0 [MSC v.1927 64 bit (AMD64)] on win32

• IDE utilizada: PyChram 2020.2.3

• Espacio en memoria: 1 MB como mínimo

• Versión de Graphviz: graphviz version 2.38.0 (20140413.2041)

• Liberia Pillow de Python

Diccionario de Clases 
-----------------------
Clase |  Definición 
------------ | -------------
`ArbolB` | Contiene todas la funciones que le rellenan y dan la forma al arbol B, instanciando nodos.
`DB` | Inicializa y contiene todas las funciones con respecto a crear, editar, leer y eliminar de las bases de datos, tablas y registros.
`NodoB` | Inicializa y contiene la estructura de los nodos que se conforman el arbol B.
`PP` | Contiene todas las funciones de la interfaz gráfica.

Diccionario de Funciones 
-----------------------

### Funciones CRUD de las bases de datos ###

Función |  Definición 
------------ | -------------
`alterDatabase` | Renombra la base de datos seleccionada.
`createDatabase` | Crea una base de datos.
`dropDatabase` | Elimina por completo la base de datos seleccionada.
`showDatabase` | Devuelve una lista de los nombres de las bases de datos.

### Funciones CRUD de las tablas ###

Función |  Definición 
------------ | -------------
`alterAddColumn` | Agrega una columna al final de cada registro de la tabla y base de datos especificada.
`alterAddPK` | Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas.
`alterDropColumn` | Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias.
`alterDropPK` | Elimina la llave primaria actual en la información de la tabla, manteniendo el índice actual de la estructura.
`alterTable` | Renombra el nombre de la tabla de una base de datos especificada.
`createTable` | Crea una tabla en una base de datos especificada recibiendo una lista de índices referentes a la llave primaria.
`dropTable` | Elimina por completo una tabla de una base de datos especificada.
`extractRangeTable` | Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabla. 
`extractTable` | Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla.
`showTables` | Devuelve una lista de los nombres de las tablas almacenadas en una base de datos.

### Funciones CRUD de los registros ###

Función |  Definición 
------------ | -------------
`delete` | Elimina un registro de una tabla y base de datos especificados por la llave primaria.
`extractRow` | Extrae y devuelve un registro especificado por su llave primaria.
`insert` | Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.
`loadCSV` | Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado.
`truncate` | Elimina todos los registros de una tabla y base de datos.
`update` | Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.

### Funciones de utilidad ###

Función |  Definición 
------------ | -------------
`identify` | Valida que los nombres de bases de datos y tablas sean identificadores de SQL.
`searchDB` | Verifica si una base de datos especifica ya se encuentra almacenada.
`searchTB` | Verifica si una tabla de una base de datos ya se encuentra almacenada.
`searchRepeat` | Verifica si en el arreglo indicado existen datos repetidos.
`updateTree` |  Actualiza el arbol B de datos cuando se realizan cambios.
`verifyPk` | Crea y verifica si las llaves primarias estan repetidas.

### Funciones de serializacion ###

Función |  Definición 
------------ | -------------
`commit` | Genera el archivo binario.
`initCheck` | Verifica si esta creada la carpeta que almacena archivos binarios.
`rollback` | Decodifica el archivo binario.

### Funciones del nodo ###

Función |  Definición 
------------ | -------------
`buscar_llave` | Verifica la existencia de una llave dentro de un nodo.
`comparar` | Compara las llaves dentro de los nodos.
`insertar` | Guarda la tupla dentro del nodo.
`ordenar_llave` | Ordena las llaves dentro del nodo, ascendentemente.
`posicionNodo` | Obtiene la posicion del nodo dentro del arbol
`toASCII` | Obtiene la sumatoria del codigo asi de los caracteres de una cadena.

### Funciones del arbol B ###

Función |  Definición 
------------ | -------------
`agregarValor` | Agrega un dato en la ultima posicion de cada registro.
`buscar` | Encuentra y devuelve el nodo al que pertenece una llave.
`del` | Elimina un registro de la estructura.
`eliminarValor` | Eliminar un dato en especifico de cada registro.
`estructurar` | Ordena el arbol luego de una inserción.
`graficar` | Genera el archivo del arbol en forma visual.
`insertar` | Ingresa una llave en el nodo correcto.
`Keys` | Obtiene todas las llaves primarias de los registros almacenados.
`posicion` | Obtiene la posición de la llave a eliminar.
`registros` | Obtiene todos los registros almacenados en cada nodo del arbol B.
`rotar` | Determina la posición en la que se insertará una llave.
`separar_nodo` | Rompe una página del árbol.
`unir` | Une dos páginas separadas y forma una sola.
`valor_buscar` | Obtiene la posición de un valor dado en los nodos.

Diagramas de flujo
-----------------------

![](https://github.com/tytusdb/tytus/blob/main/storage/team17/docs/img/clases.png)

Diagramas de flujo
-----------------------

### Función Insertar ###

![](https://github.com/tytusdb/tytus/blob/main/storage/team17/docs/img/Insertar.png)

### Función Eliminar ###

![](https://github.com/tytusdb/tytus/blob/main/storage/team17/docs/img/Eliminar.png)
