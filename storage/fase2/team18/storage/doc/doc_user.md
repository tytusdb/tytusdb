Manual de usuario
=============
## Indice
- [Introducción](#requerimientos)
- [Glosario](#glosario)
- [Requerimientos del sistema](#req)
- [Aplicación y capacidad del sistema](#app)
- [Descripción general del sistema](#descripcion)
- [Explicación del funcionamiento](#explicacion)
- [Solución de problemas](#solucionP)

<div id='introduccion'/>

## Introducción
TytusDB es un proyecto Open Source para desarrollar un administrador de bases de datos. Este manual tiene como propósito brindar soporte al usuario de la aplicación respecto a las bases funcionales de la parte del almacenamiento de las bases de datos.

Es programa reúne distintos algoritmos que se ejecutan para almacenar información, estructuras de datos que actúan como motores de bases de datos, con finalidad de ofrecer una mayor flexibilidad y preferencia en cuanto a nivel de eficiencia y complejidad.

<div id='glosario'/>

## Glosario

| Termino   | Descripción   |
| ----- | ----- |
| Archivo CSV | Archivo simple que se utiliza para almacenar datos tabulares, como una hoja de cálculo o una base de datos. |
| Checksum | Una suma de verificación o Checksum en telecomunicación e informática, es una función de redundancia que tiene como propósito principal detectar cambios accidentales en una secuencia de datos para proteger la integridad de estos, verificando que no haya discrepancias entre los valores obtenidos al hacer una comprobación inicial y otra final tras la transmisión.|
| CRUD | Es el acrónimo de "Crear, Leer, Actualizar y Borrar" (del original en inglés: Create, Read, Update and Delete), que se usa para referirse a las funciones básicas en bases de datos o la capa de persistencia en un software.|
| Eficiencia | Es la relación entre los recursos utilizados en un proyecto y los logros conseguidos con el mismo. |
| Estructura de datos | Es una colección de valores, la relación que existe entre estos valores y las operaciones que podemos hacer sobre ellos; se refiere a cómo los datos están organizados y cómo se pueden administrar. |
| Interfaz | Se conoce como la interfaz de usuario al medio que permite a una persona comunicarse con una máquina. |
| Licencia MIT | Esta licencia es una Licencia de software libre permisiva lo que significa que impone muy pocas limitaciones en la reutilización y por tanto posee una excelente Compatibilidad de licencia. La licencia MIT permite reutilizar software dentro de Software propietario. |
| Llave Foránea – FK(Foreign Key)| Es llamada clave Externa, es uno o más campos de un tabla que hacen referencia al campo o campos de clave principal de otra tabla, una clave externa indica como esta relacionadas las tablas. Los datos en los campos de clave externa y clave principal deben coincidir, aunque los nombres de los campos no sean los mismos. |
| Llave Primaria – PK(Primary Key) | Es un conjunto de uno o más atributos de una tabla, que tomados colectivamente nos permiten identificar un registro como único, es decir, en una tabla podemos saber cuál es un registro en específico sólo con conocer la llave primaria.|
| Método |Un método es una subrutina cuyo código es definido en una clase y puede pertenecer tanto a una clase, como es el caso de los métodos de clase o estáticos, como a un objeto, como es el caso de los métodos de instancia. |
| Nodo | De forma muy general, un nodo es un punto de intersección, conexión o unión de varios elementos que confluyen en el mismo lugar. En estructuras de datos dinámicas un nodo es un registro que contiene un dato de interés y al menos un puntero para referenciar (apuntar) a otro nodo. |
| Parámetro | Es una variable utilizada para recibir valores de entrada en una rutina, subrutina o método. |
| PEP 8 | Es una guía de estilo única descrita íntegramente en el Python (Enhancement Proposal) numero 8. En esta se define al pie de la letra, como debería estar escrito el código python.|
| Registro | También llamado fila o tupla, representa un objeto único de datos implícitamente estructurados en una tabla. |
| Tupla |Registro. |


<div id='req'/>

## Requerimientos del sistema
•	Microsoft Windows XP o superior, 32 o 64 bits.
•	Python 2.7o superior.
•	Graphviz
•	Cryptography


<div id='app'/>

## Aplicación y capacidad del sistema

El programa dedicado al almacenamiento puede ser utilizado como un motor de bases de datos que maneja la parte funcional del almacenamiento con distintas estructuras de datos basado en un sistema de archivos.

<div id='descripcion'/>

## Descripción general del sistema
Este componente es el encargado de gestionar el almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para extraer la información.
##### Modo de almacenamiento
TytusDB consta de distintos modos de almacenamiento, que corresponden a un motor de la base de datos y cada estructura almacena una tabla. Dichos modos son: B, Tabla Hash, ISAM, B+, jsonMode y Dictionaries.

##### Administrador del modo de almacenamiento
El storageManager debe permitir cambiar el modo de almacenamiento de una base de datos o de una tabla en cualquier momento. Se construye la estructura de datos asociada al modo y eliminar la anterior. De manera que se hace un “transferencia” de datos a una estructura diferente a la actual.

#### Metodos:
-  ###### alterDatabaseMode(database, mode)
Cambia el modo de almacenamiento de una base de datos, reestructurando los datos. 
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| mode | El modo de almacenamiento de la nueva base de datos. |
-  ###### alterTableMode(database, table,  mode)
Cambia el modo de almacenamiento de una tabla.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |
| mode | El modo de almacenamiento de la nueva base de datos. |

-  ###### alterTableAddUnique(database, table, indexName, columns)
Agrega un índice único a una o más columnas de una tabla.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |
| indexName | Nombre dl índice único. |
| columns | Columnas de la tabla donde se agregará el índice|

-  ###### alterTableDropUnique(database, table, indexName)
Elimina un índice único existente.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |
| indexName | Nombre del índice. |



##### Registros de almacenamiento
Cada registro que corresponde a una tupla de una tabla es almacenado en cada nodo. Cada atributo es débilmente tipado.
##### Bases de datos
•	Una base de datos es un conjunto de tablas, para este diseño, es un conjunto de estructuras arbóreas.
•	Se manejan los archivos de manera binaria para no exponer la información.
##### Funciones
Estas están disponibles para que un componente SQL Parser pueda hacer uso de estas.

##### Administración de índices
Mediante funciones se administran los diferentes índices de una base de datos, entre los cuales figuran: creación y eliminación de llaves foráneas, creación y eliminación de índices únicos y creación - eliminación de índices.

-  ###### alterTableAddFK(database, table, indexName, columns, tableRef, columnsRef)
Agrega una llave foránea a una o más columnas de una tabla.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |
| indexName | Nombre de la llave foránea. |
| columns | Columnas de la tabla donde agregará la llave foránea |
| tableRef | Tabla a la que la llave foránea hace referencia. |
| columnsRef | Columnas de la tabla a la que la llave foránea hace referencia. |


-  ###### alterTableDropFK(database, table, indexName)
Elimina una llave foránea existente.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |
| indexName | Nombre de la llave foránea. |



##### Administración de la codificación
Mediante funciones se puede seleccionar cualquiera de las siguientes codificaciones para una base de datos y poder modificarse: ASCII, ISO 8859-1 y UTF8.

-  ###### alterDatabaseEncoding(database, encoding)
Verifica cada una de las tuplas de la base de datos específica, de acuerdo al encoding seleccionado.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| encoding | Tipo de encoding a utilizar. |


##### Generación del Checksum
Mediante una función se calcula el Checksum de la base de datos, conforme lo hace SQL. Los dos algoritmos a utilizar son: MD5 y SHA256.

-  ###### checksumDatabase(database, mode)
Obtiene el valor hash de toda la base de datos seleccionada.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| mode | El nombre del algoritmo al cual se le calculara el valor hash.. |


-  ###### checksumTable(database, table, mode)
Obtiene el valor hash de una sola tabla.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |
| mode | El nombre del algoritmo al cual se le calculara el valor hash. |


##### Compresión de datos

Mediante funciones se debe ejecutar las operaciones de comprimir y descomprimir.

-  ###### alterDatabaseCompress(database, level)
El método se encarga de comprimir cada una de las tablas que contenga una base de datos.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| level | Nivel de compresión (1 al 9). |

-  ###### alterDatabaseDecompress(database)
El método se encarga de descomprimir cada una de las tablas que contenga una base de datos comprimida.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |

-  ###### alterTableCompress(database, table, level)
El método se encarga de comprimir una de las tablas que contenga una base de datos.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |
| level | Nivel de compresión (1 al 9). |

-  ###### alterTableDecompress(database, table)
El método se encarga de descomprimir una de las tablas que contenga una base de datos comprimida.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |


##### Seguridad
Los conceptos de seguridad se aplicarán en dos sub componentes:

-  Criptografía: el storageManager debe proveer la manera de cifrar y descifrar ya sea una base de datos completa o también cifrar o descifrar una backup de una base de datos.

-  ###### encrypt(backup, password)
Encripta un texto, devuelve el texto encriptado como una cadena de texto.
| Parámetro | Descripción |
| ------ | ------ |
| backup | Es el string que se desea encriptar. |
| password | Cadena que se usará para la encriptación del texto. La contraseña es necesaria para desencriptar. |

-  ###### decrypt(cipherbackup, password)
Descrifra el texto cipherBackup con la llave password y devuelve el texto plano.
| Parámetro | Descripción |
| ------ | ------ |
| cipherbackup| Es el string que se desea desencriptar. |


-  BlockChain:el storageManager debe proveer un mecanismo para trabajar en modo seguro una tabla. Es decir, al activar el modo seguro de una tabla, cuando se realicen operaciones de inserción se debe ir creando bloques con sus respectivos valores Hash (esto almacenado en un archivo JSON), cuando algún bloque sea modificado o eliminado la cadena quedará incosistente y debe mostrarse de manera gráfica.

-  ###### SafeModeOn(database, table)
Activa el modo seguro para una tabla.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |

-  ###### SafeModeOff(database, table)
Desactiva el modo seguro para una tabla.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a utilizar. |

-  ###### GraphSafeTable(database, table)
Grafica el los bloques de BlockChain de una tabla en modo seguro.
| Parámetro | Descripción |
| ------ | ------ |
| database | El nombre de la base de datos a utilizar. |
| table | El nombre de la tabla a graficar. |

##### Grafos
El storageManager debe tener un paquete de generación de diagramas de estructuras de datos basado en GraphViz. Para esto se deben crear los siguientes grafos de dependencias:

- diagrama de estructura de datos: para mayor detalle ver este enlace. def graphDSD(database: str) -> str:
- diagrama de dependencias: este grafo muestra las dependencias funcionales que existen en una tabla específica. def graphDF(database: str, table: str) -> str:

<div id='explicacion'/>

## Explicación del funcionamiento

## Interfaz gráfica / GUI
Tytus DB cuenta con una interfaz grafica que facilita la creación y manejo de bases de datos. Por medio de ésta, el usuario es capaz de visualizar las bases de datos por medio de imagenes que representan las estructuras implementadas y la navegacion de la misma consta de presionar botones.

### Ventana Inicial
![](https://i.imgur.com/K1ZfKs1.png)

La ventana inicial muestra el nombre del programa y el boton de "Reportes" que cuando es presionado pasa a la ventana de bases de datos, en donde ya se podran gestionar las bases de datos

### Ventana Bases de datos
![](https://i.imgur.com/2HPBvRb.png)


##### Parte superior
|Boton | Descripcion |
|------| ------------|
|Regresar|Regresa a la ventana inicial del programa|

#### Parte central
Se puede visualizar botones con las nombres de las bases de datos almacenadas. Al presionar alguna, se abre la ventana para visualizar sus tablas.

### Ventana Tablas
![](https://i.imgur.com/iioChcg.png)

#### Parte superior

|Botón| Descripción|
|-----| -----------|
|Regresar| Regresa a la ventana de las bases de datos|
|GraphDSD| Genera un diagrama de estructura de datos|

#### Parte central
Se puede visualizar botones con las nombres de las tablas almacenadas. Al presionar alguna, se abre la ventana para visualizar sus registros.

### Ventana Tuplas
![](https://i.imgur.com/nsOIGlz.png)


#### Parte Superior
Existe una lista despegable para visualizar los registros de la tabla.
|Botón |Descripción|
|------|-----------|
|GraphDF| Genera un diagrama acerca de las dependencias funcionales de una tabla especificada de una base de datos
|Candado| Permite visualizar la estructura del blockchain|


#### Parte central
Se puede visualizar la estructura utilizada para el almacenamiento de los registros.

## Funciones CRUD - (Existentes para cada modo)
### CRUD para las bases de datos
- #### createDatabase(database: str) -> int:
Crea una base de datos. (CREATE)
Parámetro database: es el nombre de la base de datos, debe cumplir con las reglas de identificadores de SQL.
| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos existente |


- #### showDatabases() -> list:

Devuelve una lista de los nombres de las bases de datos. (READ)
| Valor de retorno | Definición |
| ------ | ------ |
| <lista> | Operación exitosa |
| <lista vacía> | No hay bases de datos almacenadas |


- #### alterDatabase(databaseOld, databaseNew) -> int:

Renombra la base de datos databaseOld por databaseNew. (UPDATE)
Parámetro databaseOld: es el nombre actual de la base de datos, debe cumplir con las reglas de identificadores de SQL.
Parámetro databaseNew: es el nuevo nombre que tendrá de la base de datos databaseOld, debe cumplir con las reglas de identificadores de SQL.
| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Nombre de base de datos origen inexistente |
| 3 | Nuevo nombre de la base de datos existente |

- #### dropDatabase(database: str) -> int: 

Elimina por completo la base de datos indicada en database. (DELETE)
Parámetro database: es el nombre de la base de datos que se desea eliminar, debe cumplir con las reglas de identificadores de SQL.
| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |

## CRUD de las tablas

- ### createTable(database: str, table: str, numberColumns: int) -> int:

Crea una tabla en una base de datos especificada recibiendo una lista de índices referentes a la llave primaria y llave foránea. (CREATE)
| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar.|
| table | es el nombre de la tabla que se desea crear.|
| numberColumns | es el número de columnas que tendrá cada registro de la tabla.|

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla existente |
 
- ### showTables(database: str) -> list:
Devuelve una lista de los nombres de las tablas de una base de datos. (READ)
| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |


| Valor de retorno | Definición |
| ------ | ------ |
| <Lista> | Operación exitosa |
| <Lista vacía> | La base de datos no contiene tablas |
| None | Base de datos inexistente |

- ### extractTable(database: str, table: str) -> list:

Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla. (READ)
| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |

| Valor de retorno | Definición |
| ------ | ------ |
| <Lista> | Operación exitosa |
| <Lista vacía> | La tabla no contiene registros |
| None | Error en la operación |


- ### extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabla. (READ)
| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |
| columnNumber | es el número de índice de columna a restringir o verificar con los valores upper y lower. |
| lower | es el límite inferior (inclusive) del rango a extraer de la columna indicada de la tabla. |
| upper | es el límite superior (inclusive) del rango a extraer de la columna indicada de la tabla. |

| Valor de retorno | Definición |
| ------ | ------ |
| <Lista> | Operación exitosa |
| <Lista vacía> | La tabla no contiene registros |
| None | Error en la operación |


- ### alterAddPK(database: str, table: str, columns: list) -> int:

Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas, esto para anticipar el índice de la estructura de la tabla cuando se inserten registros.
| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |
| columns | es el listado de números de columnas que formarán parte de la llave primaria. |

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |
| 4 | Llave primaria existente |
| 5 | Columnas fuera de límites |

- ### alterDropPK(database: str, table: str) -> int:
Elimina la llave primaria actual en la información de la tabla, manteniendo el índice actual de la estructura del árbol hasta que se invoque de nuevo el alterAddPK().

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |
| 4 | Llave primaria inexistente |
 
- ### alterTable(database: str, tableOld: str, tableNew: str) -> int:

Renombra el nombre de la tabla de una base de datos especificada.

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| tableOld | es el nombre de la tabla a renombrar. |
| tableNew | es el nuevo nombre con que renombrará la tableOld. |


| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla a modificar inexistente |
| 4 | Nuevo nombre de tabla existente |

- ### alterAddColumn(database: str, table: str, default: any) -> int:

Agrega una columna al final de cada registro de la tabla y base de datos especificada.

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a modificar. |
| default | es el valor que se establecerá en a la nueva columna para los registros existentes. |

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |

- ### alterDropColumn(database: str, table: str, columnNumber: int) -> int:

Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias. (DELETE)

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a modificar. |
| columnNumber | numero de columna que se quiere eliminar en los registros. |

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |
| 4 | Es llave primaria o la tabla no puede quedarse sin columnas |
| 5 | Columna fuera de límites |

- ### dropTable(database: str, table: str) -> int: 

Elimina por completo una tabla de una base de datos especificada. (DELETE)

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a eliminar. |

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |

## CRUD de tuplas

- ### insert(database: str, table: str, register: list) -> int:

Inserta un registro en la estructura de datos asociada a la tabla y la base de datos. (CREATE)
| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |
| register | es una lista de elementos que representan un registro. |

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla existente |
| 4 | Llave primaria duplicada |
| 5 | Numero de columnas no coinciden |


- ### loadCSV(file: str, database: str, table: str) -> list:

Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado. La base de datos y la tabla deben existir, y coincidir con el número de columnas. Si hay llaves primarias duplicadas se ignoran. No se utilizan títulos de columnas y la separación es por comas. (CREATE)
| Parámetro | Descripción |
| ------ | ------ |
| file | dirección o path del archivo CSV. |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |

| Valor de retorno | Definición |
| ------ | ------ |
| Lista  | lista con los valores enteros que devuelve el insert por cada fila del CSV. |
| <Lista vacía> | Error en la operación / Base de datos inexistente / Tabla inexistente |

- ### extractRow(database: str, table: str, columns: list) -> list:

Extrae y devuelve un registro especificado por su llave primaria. (READ)

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |
| columns | es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...]. (si no hay pk se debe enviar la hiddenPK). |


| Valor de retorno | Definición |
| ------ | ------ |
| Lista de datos | Operación exitosa |
| <Lista vacía> | Error en la operación |

- ### update(database: str, table: str, register: dict, columns: list) -> int:

Permite actualizar los datos de un registro en específico, especificando su llave primaria, es posible modificar las propias llaves primarias, sin embargo, se verificará que la nueva primaria no esté repetida, esto para mantener la consistencia de los datos, si la nueva primaria se repite se forma un error.

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |
| register | es una lista de elementos llave: valor que representa los elementos a actualizar del registro. La llave el número de coluna y el valor el contenido del campo. |
| columns | es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...]. (si no hay llave primaria PK se debe enviar la hiddenPK). |

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla existente |
| 4 | Llave primaria no existe |

- ### delete(database: str, table: str, columns: list) -> int:

Elimina un registro de una tabla y base de datos especificados por la llave primaria. (DELETE)

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |
| columns | es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...]. (si no hay pk se debe enviar la hiddenPK). |

| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla existente |
| 4 | Llave primaria no existe |

- ### truncate(database: str, table: str) -> int:

Elimina todos los registros de una tabla y base de datos. (DELETE)

| Parámetro | Descripción |
| ------ | ------ |
| database | es el nombre de la base de datos a utilizar. |
| table | es el nombre de la tabla a utilizar. |


| Valor de retorno | Definición |
| ------ | ------ |
| 0 | Operación exitosa |
| 1 | Error en la operación |
| 2 | Base de datos inexistente |
| 3 | Tabla inexistente |


<div id='solucionP'/>


## Preguntas frecuentes - FAQ
| Pregunta | Solución |
| ------ | ------ |
| ¿En donde se almacenan las bases de datos e informacion perteneciente? | En la carpeta </Data> del directorio de archivos |
| ¿El archivo CSV debe estar estructurado? | Si. Debe estructurarse de acuerdo a la estructura tipa de registros, separados por línea y datos separados por una coma |
| ¿Están los registros limitados en cuanto al tipo de dato?| En los registros se puede ingresar cadenas de texto y datos numéricos. |
| ¿Es lo mismo delete row y truncate? | El delete row sirve para eliminar una sola tupla de una tabla. Truncate sirve para eliminar todos los registros que posee la tabla. |
| ¿Por qué se usan archivos binarios para guardar información? | Para mantener la información no legible. |
| ¿Toda información guardada permanece aún después de reiniciar el equipo en donde corre? | Si. La información se guarda en archivos, que permanecen en la unidad de almacenamiento a menos que intencionalmente se borren dichos archivos. |
| ¿Qué factor puede limitar la cantidad de datos que puedo almacenar? | El espacio en disco disponible del equipo servidor |