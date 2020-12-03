# Enunciado del Proyecto

Universidad de San Carlos de Guatemala  
Facultad de Ingeniería  
Cursos: 772 Estructuras de Datos | 774 Sistemas de Bases de Datos 1 | 781 Organización de Lenguajes y Compiladores 2  
Diciembre 2020


## 1. Objetivo

Poner en práctica los conocimientos teóricos adquiridos durante cada curso y aplicarlo a un proyecto real de código abierto fortaleciendo las competencias de administración de equipos de desarrollo.

## 2. Condiciones

### Equipos de desarrollo

Se deben formar equipos de 3 a 5 personas por curso y por afinidad con la restricción de que en cada equipo no hayan estudiantes del mismo año (por ejemplo, en un equipo de tres estudiantes puede haber un carné 2014, un 2015 y un 2017).

Cada curso tendrá una hoja de cálculo, en la carpeta compartida correspondiente, para especificar los integrantes de cada equipo y así asignarles el tema de implementación. Además deben decidir quién será el coordinador de cada equipo.

### Lenguaje de programación

El lenguaje seleccionado es Python, y no deben utilizarse biliotecas adicionales si no hacen falta, por ejemplo, para compiladores 2 si deben utilizar PLY. Cualquier otra biblioteca debe ser autorizada por el catedrático.

### Licencias

El proyecto está diseñado por el catedrático bajo una licencia Open Source, específicamente MIT. Los estudiantes aparecerán como contribuidores junto con el copyright. Además cualquier biblioteca autorizada también se debe colocar la licencia y el copyright en el archivo LICENSE.md en su carpeta respectiva.

## 3. TytusDB

Es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres elementos interralicionados: el almacenamiento de la base de datos, que estará a cargo del curso de Estructuras de Datos; el administrador de la base de datos, que estará a cargo del curso de Sistemas de Bases de Datos 1; y el traductor de SQL, que estará a cargo del curso de Organización de Lenguajes y Compiladores 2.

## 4. Almacenamiento de la base de datos

### Fase 1

Construir el almacenamiento de un servidor de bases de datos proporcionando un conjunto de funciones para extraer la información.

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

createTable(mode, database, tableName, numberColumns): crea una tabla según el modo de almacenamiento, la base de datos debe de existir, y solo se define el número de columnas.

dropTable(mode, database, tableName): elimina por completo la tabla indicada.

dropDatabase(mode, database): elimina por completo la base de datos indicada.

deleteTable(mode, database, tableName, id): elimina un nodo o elemento de página indicado de una tabla y base de datos especificada.

alterAdd(mode, database, tableName): agrega una columna a cada registro de la tabla.

alterDrop(mode, database, tableName, columnNumber): elimina una n-esima columna de cada registro de la tabla.

truncate(mode, database, tableName): vacía la tabla de todos los registros.


### Fase 2

## 5. Administrador de la base de datos

### Fase 1

### Fase 2

## 6. Traductor de SQL

### Fase 1

### Fase 2









llamado TytusDB relacionado con un administrador de base de datos licencia MIT fortaleciendo las competencias de administración de equipos de desarrollo.

Universidad de San Carlos de Guatemala
Facultad de Ingeniería
Estructuras de Datos
Sistemas de Bases de Datos 1
Organización de Lenguajes y Compiladores 2


