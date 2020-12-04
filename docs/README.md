# Enunciado del Proyecto (FASE I)

Universidad de San Carlos de Guatemala  
Facultad de Ingeniería  
Cursos: 772 Estructuras de Datos | 774 Sistemas de Bases de Datos 1 | 781 Organización de Lenguajes y Compiladores 2  
Diciembre 2020

## 1. Objetivo

Poner en práctica los conocimientos teóricos adquiridos durante cada curso y aplicarlo a un proyecto real de código abierto fortaleciendo las competencias de administración de equipos de desarrollo.


## 2. Condiciones

### Equipos de desarrollo

Se formarán equipos de estudiantes con carné continuos por curso.

Cada curso tendrá una hoja de cálculo, en la carpeta compartida correspondiente, para informar acerca de los integrantes de cada equipo y así asignarles el tema de implementación. Además deben decidir quién será el coordinador de cada equipo.

### Lenguaje de programación

El lenguaje seleccionado es Python, y no deben utilizarse biliotecas adicionales si no hacen falta, por ejemplo, para compiladores 2 si deben utilizar PLY. Cualquier otra biblioteca debe ser autorizada por el catedrático.

### Licencias

El proyecto está diseñado por el catedrático bajo una licencia Open Source, específicamente MIT. Los estudiantes aparecerán como contribuidores junto con el copyright. Además cualquier biblioteca autorizada también se debe colocar la licencia y el copyright en el archivo LICENSE.md en su carpeta respectiva.

## 3. TytusDB

Es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres elementos interralicionados: el almacenamiento de la base de datos, que estará a cargo del curso de Estructuras de Datos; el administrador de la base de datos, que estará a cargo del curso de Sistemas de Bases de Datos 1; y el traductor de SQL, que estará a cargo del curso de Organización de Lenguajes y Compiladores 2.

## 4. Almacenamiento de la base de datos

Este módulo forma parte del sevidor, la finalidad es tener el almacenamiento de las bases de datos, proporcionando un conjunto de funciones para extraer la información.

#### Modo de almacenamiento 

TytusDB tendrá cinco modos de almacenamiento, cada uno corresponde a un motor de la base de datos y cada estructura almacena una tabla. Cada modo será asignado a un equipo diferente para que lo desarrolle. Los modos de almacenamiento son los siguientes: 
1. Mediante un árbol AVL
2. Mediante un árbol B
3. Mediante un árbol B+
4. Mediante ISAM
5. Mediante tablas Hash.

#### Registros de almacenamiento

Cada nodo o cada elemento de una página de cada estructura del modo de almacenamiento guardará el registro correpondiente a una tupla de una tabla.

#### Bases de datos

Una base de datos es un conjunto de tablas, para este diseño, es un conjunto de estructuras arbóreas. El servidor de la base de datos podrá contener n bases de datos. Se deja a discreción de los estudiantes cómo manejar el conjunto de tablas de una base de datos y el conjunto de bases de datos. Se sugiere manejar los archivos de manera binaria para no exponer la información. 

#### Funciones

loadCSV(mode, filecsv, database, table): carga un archivo csv de un ruta especificada indicando la ruta de la base de datos y en qué tabla será guardada. Si la tabla existe verifica la cantidad de columnas, si no corresponde da error. Si la tabla no existe, la crea. Si la base de datos no existe, la crea.

showDatabase(): devuelve una lista de los nombres de las bases de datos, el nombre es único.

showTables(database): devuelve una lista de los nombre de las tablas de una base de datos, los nombre de tablas son únicos.

createDatabase(mode, database): crea una base de datos con cierto modo de almacenamiento.

createTable(mode, database, tableName, numberColumns): crea una tabla según el modo de almacenamiento, la base de datos debe de existir, y solo se define el número de columnas.

dropTable(mode, database, tableName): elimina por completo la tabla indicada.

dropDatabase(mode, database): elimina por completo la base de datos indicada.

deleteTable(mode, database, tableName, id): elimina un nodo o elemento de página indicado de una tabla y base de datos especificada.

alterAdd(mode, database, tableName): agrega una columna a cada registro de la tabla.

alterDrop(mode, database, tableName, columnNumber): elimina una n-esima columna de cada registro de la tabla.

alterDatabase(mode, databaseOld, databaseNew): cambia el nombre de una base de datos.

truncate(mode, database, tableName): vacía la tabla de todos los registros.

insert(database, table, columns): inserta un registro en la estructura de datos persistente, database es el nombre de la base de datos, table es el nombre de la tabla y columns es una lista de campos a insertar. Devuelve un True si no hubo problema, y un False si no se logró insertar.

update(database, table, id, columnNumber, value): actualiza el valor de una columna x en un registro id de una tabla de una base de datos. Devuelve True si se actualizó correctamente y False si no se logró actualizar.


## 5. Administrador de la base de datos

El administrador de la base de datos se compone de dos elementos:
- server: es un servidor http, se debe seleccionar un puerto adecuado que no tenga conflictos. El servidor debe instalarse para algunos equipos en Windows y para otros equipos en Linux. La carpeta donde se almacena debe tener una carpeta llamada /data donde se almacenarán las bases de datos. Se debe crear un usuario admin y su contraseña. Además de crear n usuarios configurando el acceso a las bases de datos.

- client: es un cliente de escritorio que se conectará al servidor y podrá hacer la mayoría de operaciones que hace pgadmin de PostgreSQL, considerando las funciones básicas.


## 6. Traductor de SQL

Construir un intérprete del subconjunto del lenguaje SQL especificado en la siguiente [documentación](https://github.com/tytusdb/tytus/tree/main/docs/sql_syntax). 

El intérprete debe ser capaz de:
- invocar las [Funciones](#funciones) proporcionadas por el almacenamiento, para realizar operaciones sobre la base de datos.
- proporcionar la función parser(database, queries): esta función ejecuta y devuelve el resultado de la(s) consulta(s) sobre una base de datos, debe retornar una lista de listas con el resultado de la consulta. Si hay más de una consulta considerar la ejecución de consultas en PostgreSQL.



