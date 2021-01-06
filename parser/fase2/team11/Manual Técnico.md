# Manual Técnico Proyecto , fase 2: *TytusDB*
<p align="center">
  <img src="img/tytus.png" width="100" alt="Presentación">
</p>

---

        Universidad de San Carlos de Guatemala
        Facultad de ingeniería
        Escuela de Ciencias y Sistemas 
        781 Organización de lenguajes y compiladores 2
        Manual de usuario proyecto , fase 2

                                                   Perteneciente a: Grupo 11
                                                  

***
## Índice
- [Competencias del proyecto](#competencias-del-proyecto)
- [Descripcion de TytusDB](#descripcion-de-tytusdb)
- [Flujo del programa](#flujo-del-programa)
- [Plataforma de Desarrollo](#plataforma-de-desarrollo)
- [Gramatica utilizada](#gramatica-utilizada)
    - [Analisis Léxico](#Analisis-Léxico)
    - [Analisis Sintáctico](#Analisis-Sintáctico)
***
## Competencias del proyecto:
### *General:*
- Poner en práctica los conocimientos teóricos adquiridos durante cada curso y aplicarlo a un proyecto real de código abierto fortaleciendo las competencias de administración de equipos de desarrollo.
### *Específico:*
- El estudiante construye un intérprete para el subconjunto del lenguaje SQL mediante la traducción dirigida por la sintaxis.
- El estudiante utiliza la herramienta PLY o SLY de Python para la traducción.

 
***
## Descripcion de TytusDB:
Es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos, que estará a cargo del curso de Estructuras de Datos; el administrador de la base de datos, que estará a cargo del curso de Sistemas de Bases de Datos 1, este administrador se compone a su vez de un servidor y de un cliente; y el SQL Parser, que estará a cargo del curso de Organización de Lenguajes y Compiladores 2.

### Utilización de funciones CRUD de las bases de datos:
```
def createDatabase(database: str) -> int:
```
Crea una base de datos.  (CREATE)  
Parámetro database: es el nombre de la base de datos, debe cumplir con las reglas de identificadores de SQL.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos existente  

```
def showDatabases() -> list:
```
Devuelve una lista de los nombres de las bases de datos. (READ)  
Valor de retorno: lista de strings con los nombres de las bases de datos, si ocurrió un error o no hay bases de datos devuelve una lista vacía [].  

```
def alterDatabase(databaseOld, databaseNew) -> int:
```
Renombra la base de datos databaseOld por databaseNew.  (UPDATE)  
Parámetro databaseOld: es el nombre actual de la base de datos, debe cumplir con las reglas de identificadores de SQL.  
Parámetro databaseNew: es el nuevo nombre que tendrá de la base de datos databaseOld, debe cumplir con las reglas de identificadores de SQL.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 databaseOld no existente, 3 databaseNew existente.  

```
def dropDatabase(database: str) -> int: 
```
Elimina por completo la base de datos indicada en database.  (DELETE)  
Parámetro database: es el nombre de la base de datos que se desea eliminar, debe cumplir con las reglas de identificadores de SQL.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos no existente.  


### Utilización de funciones CRUD de las tablas:

```
def createTable(database: str, table: str, numberColumns: int) -> int:
```
Crea una tabla en una base de datos especificada recibiendo una lista de índices referentes a la llave primaria y llave foránea.  (CREATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla que se desea crear.  
Parámetro numberColumns: es el número de columnas que tendrá cada registro de la tabla.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos inexistente, 3 tabla existente.  

```
def showTables(database: str) -> list:
```
Devuelve una lista de los nombres de las tablas de una bases de datos.  (READ)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Valor de retorno: si existen la base de datos y las tablas devuelve una lista de nombres de tablas, si existe la base de datos pero no existen tablas devuelve una lista vacía, y si no existe la base de datos devuelve None.  

```
def extractTable(database: str, table: str) -> list:
```
Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla.  (READ)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: si existen la base de datos, la tabla y los registros devuelve una lista con los registros, si existen las base de datos, la tablas pero no registros devuelve una lista vacía, y si no existe la base de datos o la tabla devuelve None.  

```
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
```
Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabala.  (READ)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámetro columnNumber: es el número de índice de columna a restringir o verificar con los valores upper y lower.
Parámetro lower: es el limite inferior (inclusive) del rango a extraer de la columna indicada de la tabla.  
Parámetro upper: es el limite superior (inclusive) del rango a extraer de la columna indicada de la tabla.  
Valor de retorno: si existen la base de datos, la tabla y los registros devuelve una lista con los registros(lista), si existen las base de datos, la tablas pero no registros devuelve una lista vacía, y si no existe la base de datos o la tabla o cualquier error devuelve None.  
Consideraciones:
- Para la comparación de lower y upper se puede hacer cast a str cuando las llaves sean compuestas o en general para reducir complejidad.
- Ver el submódulo Any del paquete typing.  

```
def alterAddPK(database: str, table: str, columns: list) -> int:
```
Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas, esto para anticipar el índice de la estructura de la tabla cuando se inserten registros. (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámetro columns: es el listado de números de columnas que formarán parte de la llave primaria. 
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria existente, 5 columnas fuera de limites.  

Considerar:
- Si no se define al menos una llave primaria, cuando ocurre el primer insert se debe utilizar una llave primaria escondida (numérica).  
- Si ya existían datos sin llave primaria explícita se recalcula el índice de la estructura de índices con la actual llave primaria.  
- Si la llave primaria es compuesta, se sugiere concatener en cualqueir estilo las columnas, para manternas intactas (sería como llave primaria escondida).
- El error 42P16 de PostgreSQL invalid_table_definition, entre algunas causas no permite definir múltiples llaves primarias (nótese de la diferencia de una llave primaria compuesta). Si ya existe una llave primaria y se desea agregar otro campo, entonces se debe eliminar la llave actual recalculado el índice cuando sea modificado, si no hay modificación se queda con el llave anterior.
- El error 23505 de PostgreSQL unique_violation, cuando se ejecuta esta función se debe recalcular el índice, si hay un valor duplicado en una parte de la llave primaria debe dar error y dejar el índice como estaba.

```
def alterDropPK(database: str, table: str) -> int:
```
Elimina la llave primaria actual en la información de la tabla, manteniendo el índice actual de la estructura del árbol hasta que se invoque de nuevo el alterAddPK().  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 pk no existente.  

```
def alterAddFK(database: str, table: str, references: dict) -> int:
```
Asocia la integridad referencial entre llaves foráneas y llaves primarias, para efectos de la fase 1 se ignora esta petición. Debido a que será parte de la fase 2 en la construcción de índices secundarios.  (UPDATE PENDIENTE)  

```
def alterAddIndex(database: str, table: str, references: dict) -> int:
```
Asocia un índice, para efectos de la fase 1 se ignora esta petición. Debido a que será parte de la fase 2 en la construcción de índices secundarios.  (UPDATE PENDIENTE)  

```
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
```
Renombra el nombre de la tabla de una base de datos especificada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro tableOld: es el nombre de la tabla a renombrar.  
Parámetro tableNew: es el nuevo nombre con que renombrará la tableOld.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 tableOld no existente, 4 tableNew existente.  

```
def alterAddColumn(database: str, table: str, default: any) -> int:
```
Agrega una columna al final de cada registro de la tabla y base de datos especificada.  (UPDATE) 
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a modificar.  
Parámetro default: es el valor que se establecerá en al nueva columna para los registros existentes.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.  

```
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
```
Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias.  (DELETE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a modificar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave no puede elimnarse o tabla quedarse sin columnas, 5 columna fuera de limites.  

```
def dropTable(database: str, table: str) -> int: 
```
Elimina por completo una tabla de una base de datos especificada.  (DELETE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a eliminar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.  

### Utilización de las funciones CRUD de las tuplas:

```
def insert(database: str, table: str, register: list) -> int:
```
Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.  (CREATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámetro register: es una lista de elementos que representan un registro.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primari  a duplicada, 5 columnas fuera de limites.  

```
def loadCSV(file: str, database: str, table: str) -> list:
```
Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado. La base de datos y la tabla deben existir, y coincidir con el número de columnas. Si hay llaves primarias duplicadas se ignoran. No se utilizan títulos de columnas y la separación es por comas.  (CREATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno, una lista con el resultado de insertar cada línea del CSV: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primari  a duplicada, 5 columnas fuera de limites.  

```
def extractRow(database: str, table: str, columns: list) -> list:
```
Extrae y devuelve un registro especificado por su llave primaria.  (READ)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámeto columns: es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...].  (si no hay pk se debe enviar la hiddenPK)  
Valor de retorno: lista con los valores del registro, si ocurrió un error o no hay registro que mostrar devuelve una lista vacía [].  

```
def update(database: str, table: str, register: dict, columns: list) -> int:
``` 
Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámetro register: es una lista de elementos llave:valor que representa los elementos a actualizar del registro. La llave el número de coluna y el valor el contenido del campo.  
Parámeto columns: es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...].  (si no hay pk se debe enviar la hiddenPK)
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria no existe.

```
def delete(database: str, table: str, columns: list) -> int:
```
Elimina un registro de una tabla y base de datos especificados por la llave primaria.  (DELETE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Parámeto columns: es la llave primaria, si es simple [llave], si es compuesta [llaveatr1, llaveatr2...].  (si no hay pk se debe enviar la hiddenPK)  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 llave primaria no existe.  

```
def truncate(database: str, table: str) -> int:
```
Elimina todos los registros de una tabla y base de datos.  (DELETE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente.  

---
## Fase2:

### 1. Unificación de modos de almacenamiento

En cuanto se haya calificado la fase 1, algunos grupos serán seleccionados para formar parte de los modos de almacenamiento o motores de las bases de datos TytusDB. Cada equipo en su carpeta asignada debe unificar los modos de los proyectos seleccionados para formar un solo storageManager que maneje los diferentes modos de almacenamiento (sin agregar de manera redundante los paquetes).

Los proyectos seleccionados son:
Grupo 17-> B
Grupo 15-> Tabla Hash
Grupo 14-> ISAM
Grupo 18-> B+
Grupo 16-> AVL
storageManager -> jsonMode
DictMode -> Dictionaries

#### Estructura del paquete

Cada coordinador de los equipos seleccionados debe copiar solamente los archivos de código fuente en la carpeta correspondiente del modo, cumpliendo con la guía PEP 8.

```
storage/
    __init__.py
    avl/
        __init__.py
        avl_mode.py
        otros.py
    b/
        __init__.py
        b_mode.py
        otros.py
    bplus/
        __init__.py
        bplus_mode.py
        otros.py
    dict/
        __init__.py
        dict_mode.py
        otros.py
    isam/
        __init__.py
        isam_mode.py
        otros.py
    json/
        __init__.py
        json_mode.py
        otros.py
    hash/
        __init__.py
        mode.py
        otros.py    
```

#### Funciones relativas al modo

La función createDatabase está relacionada con el requerimiento 1, pero también está relacionada con el requerimiento 4.

```
def createDatabase(database: str, mode: string, encoding: string) -> int:
```
Crea una base de datos.  (CREATE)  
Parámetro database: es el nombre de la base de datos, debe cumplir con las reglas de identificadores de SQL.  
Parámetro mode: es un string indicando el modo 'avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash'.  
Parámetro encoding: es un string indicando el modo 'ascii', 'iso-8859-1', 'utf8'.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 base de datos existente, 3 modo incorrecto, 4 codificación incorrecta.  

### 2. Administrador del modo de almacenamiento

El storageManager debe permitir cambiar el modo de almacenamiento de una base de datos o de una tabla en cualquier momento. Al suceder, si no hay ningun error, se debe construir la estructura de datos asociada al modo y eliminar la anterior.

```
def alterDatabaseMode(database: str, mode: str) -> int:
```
Cambia el modo de almacenamiento de una base de datos.  (UPDATE)  
Parámetro database: es el nombre de la base de datos que se desea modificar, debe cumplir con las reglas de identificadores de SQL.  
Parámetro mode: es un string indicando el modo 'avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash'.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 4 modo incorrecto.  

```
def alterTableMode(database: str, table: str, mode: str) -> int:
```
Cambia el modo de almacenamiento de una tabla de una base de datos especificada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro mode: es un string indicando el modo 'avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash'.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 modo incorrecto.  


### 3. Administración de índices

Mediante funciones se debe administrar los diferentes índices de una base de datos, entre los cuales figuran:
- creación y eliminación de llaves foráneas

```
def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
```
Agrega un índice de llave foránea, creando una estructura adicional con el modo indicado para la base de datos.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro table: es el nombre de la tabla donde está(n) la(s) llave(s) foránea(s).  
Parámetro indexName: es el nombre único del índice manejado como metadato de la tabla para ubicarlo fácilmente.
Parámetro columns: es el conjunto de índices de columnas que forman parte de la llave foránea, mínimo debe ser una columna.  
Parámetro tableRef: es el nombre de la tabla que hace referencia, donde está(n) la(s) llave(s) primarias(s).  
Parámetro columnsRef: es el conjunto de índices de columnas que forman parte de la llave primaria, mínimo debe ser una columna.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table o tableRef no existente, 4 cantidad no exacta entre columns y columnsRef, 5 no se cumple la integridad referencial (es decir, algún valor de las llaves foráneas no existe en la tabla de referencia).  
No es necesario que las llaves foráneas en la tabla de referencia sean primarias.  
Se aceptan llaves foráneas nulas (None), en estás no se verifica la integridad referencial.
A este nivel no se debe manejar las restricciones de delete o update de llaves, será manejado a nivel lógico del parser.

```
def alterTableDropFK(database: str, table: str, indexName: str) -> int:
```
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro table: es el nombre de la tabla donde está(n) la(s) llave(s) foránea(s).  
Parámetro indexName: es el nombre del índice manejado como metadato de la tabla para ubicarlo fácilmente.
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 nombre de índice no existente.  


- creación y eliminación de índices únicos

```
def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
```
Agrega un índice único, creando una estructura adicional con el modo indicado para la base de datos.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro table: es el nombre de la tabla donde está(n) la(s) llave(s) foránea(s).  
Parámetro indexName: es el nombre único del índice manejado como metadato de la tabla para ubicarlo fácilmente.
Parámetro columns: es el conjunto de índices de columnas que forman parte de la llave foránea, mínimo debe ser una columna.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table o tableRef no existente, 4 cantidad no exacta entre columns y columnsRef, 5 no se cumple la integridad de unicidad (es decir, algún valor de las llaves está duplicado).  
La restricción de unicidad en los insert se debe verificar.  

```
def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
```
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro table: es el nombre de la tabla donde está(n) la(s) llave(s) foránea(s).  
Parámetro indexName: es el nombre del índice manejado como metadato de la tabla para ubicarlo fácilmente.
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 nombre de índice no existente.  

- creación y eliminación de índices

```
def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
```
Agrega un índice, creando una estructura adicional con el modo indicado para la base de datos.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro table: es el nombre de la tabla donde está(n) la(s) llave(s) foránea(s).  
Parámetro indexName: es el nombre único del índice manejado como metadato de la tabla para ubicarlo fácilmente.
Parámetro columns: es el conjunto de índices de columnas que forman parte de la llave foránea, mínimo debe ser una columna.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table o tableRef no existente, 4 cantidad no exacta entre columns y columnsRef.  

```
def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
```
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro table: es el nombre de la tabla donde está(n) la(s) llave(s) foránea(s).  
Parámetro indexName: es el nombre del índice manejado como metadato de la tabla para ubicarlo fácilmente.
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 nombre de índice no existente.  


### 4. Administración de la codificación

Mediante funciones se debe seleccionar cualquiera de las siguientes codificaciones para una base de datos y poder modificarse:
- ASCII
- ISO 8859-1
- UTF8

Considerar que la codificación por default es 'ASCII', aunque no se ejecute esta función se debe utilizar la codificación ASCII.

```
def alterDatabaseEncoding(database: str, encoding: str) -> int:
```
Asociada una codificación a una base de datos por completo.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro enconding: es la codificación a utilizar puede ser 'ASCII', 'ISO-8859-1' o 'UTF8'.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 nombre de codificación no existente.  


### 5. Generación del Checksum

Mediante una función se debe calcular el Checksum de la base de datos, conforme lo hace SQL. Los dos algoritmos a utilizar son:
- MD5
- SHA256

```
def checksumDatabase(database: str, mode: str) -> str:
```
Genera un diggest a partir del contenido de la base de datos incluyendo sus tablas.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro mode: es el algoritmo de hash, puede ser 'MD5' o 'SHA256'.  
Valor de retorno: cadena que devuelva o None si hay algún error.  

```
def checksumTable(database: str, table:str, mode: str) -> str:
```
Genera un diggest a partir del contenido de la tabla de una base de datos.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar. 
Parámetro table: es el nombre de la tabla que se desea calcular el checksum.  
Parámetro mode: es el algoritmo de hash, puede ser 'MD5' o 'SHA256'.  
Valor de retorno: cadena que devuelva o None si hay algún error.  


### 6. Compresión de datos

Mediante funciones se debe ejecutar las operaciones de comprimir y descomprimir bajo las siguientes condiciones:

```
def alterDatabaseCompress(database: str, level: int) -> int:
```
Agregue compresión utilizando la biblioteca zlib de python y las funciones compress y decompress. Se debe agregar a columna tipo varchar o text de cada tabla de la base de datos. De igual manera, al extraer la información se debe descomprimir.  (UPDATE)  
Parámetro database: es el nombre de la base de datos que se desea modificar, debe cumplir con las reglas de identificadores de SQL.  
Parámetro level: es el nivel de compressión definido por la función compress de la bilbioteca zlib de Python.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 4 level incorrecto.  

```
def alterDatabaseDecompress(database: str) -> int:
```
Quita la compresión de una base de datos especificada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 no había compresión.  

```
def alterTableCompress(database: str, table: str, level: int) -> int:
```
Agregue compresión utilizando la biblioteca zlib de python y las funciones compress y decompress. Se debe agregar a columna tipo varchar o text de cada tabla de la base de datos. De igual manera, al extraer la información se debe descomprimir. De igual manera, al extraer la información se debe descomprimir.  (UPDATE)  
Parámetro database: es el nombre de la base de datos que se desea modificar, debe cumplir con las reglas de identificadores de SQL.  
Parámetro table: es el nombre de la tabla.  
Parámetro level: es el nivel de compressión definido por la función compress de la bilbioteca zlib de Python.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 4 level incorrecto.  

```
def alterTableDecompress(database: str, table: str) -> int:
```
Quita la compresión de una base de datos especificada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 no había compresión.  


### 7. Seguridad

Los conceptos de seguridad se aplicarán en dos sub componentes:
- Criptografía: el storageManager debe proveer la manera de cifrar y descifrar ya sea una base de datos completa o también cifrar o descifrar una backup de una base de datos.

```
def encrypt(backup: str, password: str) -> str:
```
Crifra el texto backup con la llave password y devuelve el criptograma. Se puede utilizar cualquier método y biblioteca.  (UPDATE)  
Parámetro backup: es el nombre de la base de datos a utilizar.  
Parámetro password: es la llave para cifrar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación.  

```
def decrypt(cipherBackup: str, password: str) -> str:
```
Descrifra el texto cipherBackup con la llave password y devuelve el texto plano. Se puede utilizar cualquier método y biblioteca.  (UPDATE)  
Parámetro cipherBackup: es el nombre de la base de datos a utilizar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación.  

- BlockChain: el storageManager debe proveer un mecanismo para trabajar en modo seguro una tabla. Es decir, al activar el modo seguro de una tabla, cuando se realicen operaciones de inserción se debe ir creando bloques con sus respectivos valores Hash (esto almacenado en un archivo JSON), cuando algún bloque sea modificado o eliminado la cadena quedará incosistente y debe mostrarse de manera gráfica.

```
def safeModeOn(database: str, table: str): -> int
```
Activa el modo seguro para una tabla de una base de datos.  
Parámetro database: nombre de la base de datos. 
Parámetro table: nombre de la tabla.  
Valor de retorno: 0 operación exitora, 1 error en la operación, 2 database inexistente, 3 table inexistente, 4 modo seguro existente.  

```
def safeModeOff(database: str, table: str): -> int
```
Desactiva el modo seguro en la tabla especificada de la base de datos.  
Parámetro database: nombre de la base de datos.  
Parámetro table: nombre de la tabla.  
Valor de retorno: 0 operación exitora, 1 error en la operación, 2 database inexistente, 3 table inexistente, 4 modo seguro no existente.  


### 8. Grafos

El storageManager debe tener un paquete de generación de diagramas de estructuras de datos basado en GraphViz. Para esto se deben crear los siguientes grafos de dependencias:

- diagrama de estructura de datos: para mayor detalle ver este [enlace](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.172.3370&rep=rep1&type=pdf).
- diagrama de dependencias: este grafo muestra las dependencias funcionales que existen en una tabla específica.

El resultado será gráfico, sin embargo se deben crear dos funciones para generar dichos diagramas.

```
def graphDSD(database: str) -> str:
```
Genera un gráfico mediante Graphviz acerca de la base de datos especificada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Valor de retorno: archivo en formato Graphviz para dibujar, None si hay un error.  

```
def graphDF(database: str, table: str) -> str:
```
Genera un gráfico mediante Graphviz acerca de las dependencias funcionales de una tabla especificada de una base de datos.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: archivo en formato Graphviz para dibujar, None si hay un error.  


## Flujo del programa:
<p align="center">
  <img src="img/flujo.png" width="700" alt="Presentación">
</p>
TytusDB ha sido creado para los desarroladores tanto como principiantes como avanzados en el lenguaje SQL (especificamente POSTGRES SQL) Dado que puede recibir toda las instrucciones SQL, este programa puede brindar al usuario una serie de reportes en los cuales se pueden analizar todas las instrucciones ingresadas asi como su salida de resultados con sus respectivos errores tanto léxicos, sintácticos y semánticos. Reporte AST mostrando las instrucciones ingresadas de una forma ascendente. 
Este programa ha sido desarrollado en Python, bajo licencia MIT.

---
## Plataforma de Desarrollo
El programa se ha desarrollado en el IDE Visual Studio Code:
* Versión: 1.52.1 (user setup)
* Confirmación: ea3859d4ba2f3e577a159bc91e3074c5d85c0523
* Fecha: 2020-12-16T16:34:46.910Z
* Electron: 9.3.5
* Chrome: 83.0.4103.122
* Node.js: 12.14.1
* V8: 8.3.110.13-electron.0
* Sistema Operativo: Windows_NT x64 10.0.19041
---
## Gramatica utilizada

### Analisis Léxico
#### *Palabras Reservadas*
    reservadas = {
    'smallint': 'SMALLINT',          'integer': 'INTEGER',
    'bigint': 'BIGINT',            'numeric': 'NUMERIC',
    'real': 'REAL',              'mode': 'MODE',
    'double': 'DOUBLE',            'precision': 'PRECISION',
    'money': 'MONEY',             'character': 'CHARACTER',
    'varying': 'VARYING',           'varchar': 'VARCHAR',
    'char': 'CHAR',              'text': 'TEXT',
    'date': 'DATE',              'time': 'TIME',
    'timestamp': 'TIMESTAMP',    'float': 'FLOAT',
    'int': 'INT',                'inherits': 'INHERITS',
    'boolean': 'BOOLEAN',           'create': 'CREATE',
    'or': 'OR',                'replace': 'REPLACE',
    'database': 'DATABASE',          'if': 'IF',
    'not': 'NOT',               'exists': 'EXISTS',
    'owner': 'OWNER',             'show': 'SHOW',
    'like': 'LIKE',              'regex': 'REGEX',
    'alter': 'ALTER',             'rename': 'RENAME',
    'to': 'TO',                'current_user': 'CURRENT_USER',
    'session_user': 'SESSION_USER',    'drop': 'DROP',
    'table': 'TABLE',             'default': 'DEFAULT',
    'null': 'NULL',               'unique': 'UNIQUE',
    'and': 'AND',                'constraint': 'CONSTRAINT',
    'check': 'CHECK',             'primary': 'PRIMARY',
    'key': 'KEY',               'references': 'REFERENCES',
    'foreign': 'FOREIGN',           'add': 'ADD',
    'column': 'COLUMN',            'insert': 'INSERT',
    'into': 'INTO',              'values': 'VALUES',
    'update': 'UPDATE',             'set': 'SET',
    'where': 'WHERE',             'delete': 'DELETE',
    'from': 'FROM',              'truncate': 'TRUNCATE',
    'cascade': 'CASCADE',           'year': 'YEAR',
    'month': 'MONTH',              'day': 'DAY',
    'minute': 'MINUTE',             'second': 'SECOND',
    'enum': 'ENUM',               'type': 'TYPE',
    'interval': 'INTERVAL',           'zone': 'ZONE',
    'databases': 'DATABASES',         'without': 'WITHOUT',
    'with': 'WITH',               'hour': 'HOUR',
    'select': 'SELECT',
    'as': 'AS',                'distinct': 'DISTINCT',
    'count': 'COUNT',             'sum': 'SUM',
    'avg': 'AVG',               'max': 'MAX',
    'min': 'MIN',               'in': 'IN',
    'group': 'GROUP',             'by': 'BY',
    'order': 'ORDER',             'having': 'HAVING',
    'asc': 'ASC',               'desc': 'DESC',
    'nulls': 'NULLS',             'first': 'FIRST',
    'last': 'LAST',              'limit': 'LIMIT',
    'all': 'ALL',               'offset': 'OFFSET',
    'abs': 'ABS',                'cbrt': 'CBRT',
    'ceil': 'CEIL',               'ceiling': 'CEILING',
    'degrees': 'DEGREES',            'div': 'DIV',
    'exp': 'EXP',                'factorial': 'FACTORIAL',
    'floor': 'FLOOR',              'gcd': 'GCD',
    'ln': 'LN',                 'log': 'LOG',
    'mod': 'MOD',                'pi': 'PI',
    'power': 'POWER',              'radians': 'RADIANS',
    'round': 'ROUND',
    'acos': 'ACOS',               'acosd': 'ACOSD',
    'asin': 'ASIN',               'asind': 'ASIND',
    'atan': 'ATAN',               'atand': 'ATAND',
    'atan2': 'ATAN2',              'atan2d': 'ATAN2D',
    'cos': 'COS',                'cosd': 'COSD',
    'cot': 'COT',                'cotd': 'COTD',
    'sin': 'SIN',                'sind': 'SIND',
    'tan': 'TAN',                'tand': 'TAND',
    'sinh': 'SINH',               'cosh': 'COSH',
    'tanh': 'TANH',               'asinh': 'ASINH',
    'acosh': 'ACOSH',              'atanh': 'ATANH',
    'length': 'LENGTH',             'substring': 'SUBSTRING',
    'trim': 'TRIM',               'get_byte': 'GET_BYTE',
    'md5': 'MD5',                'set_byte': 'SET_BYTE',
    'sha256': 'SHA256',             'substr': 'SUBSTR',
    'convert': 'CONVERT',            'encode': 'ENCODE',
    'decode': 'DECODE',             'for': 'FOR',
    'between': 'BETWEEN',           'isnull' : 'ISNULL',
    'notnull' : 'NOTNULL',          'case' : 'CASE',
    'end' : 'END',                  'when' : 'WHEN',
    'then' : 'THEN'   ,              'else' : 'ELSE',
    'is' : 'IS',
    'sign': 'SIGN',                 'sqrt': 'SQRT',
    'width_bucket': 'WBUCKET',      'trunc': 'TRUNC',
    'random': 'RANDOM',             'true': 'TRUE',
    'false': 'FALSE',               'use' : 'USE'


}


#### *Simbolos*
    tokens = [
        'DOSPUNTOS',   'COMA',      'PTCOMA',
        'LLAVIZQ',     'LLAVDER',   'PARIZQ',
        'PARDER',      'CORCHIZQ',  'CORCHDER',
        'IGUAL',       'MAS',       'MENOS',
        'ASTERISCO',   'DIVIDIDO',  'EXPONENTE',
        'MENQUE',      'MAYQUE',
        'NIGUALQUE',   'DIFERENTE', 'MODULO',
        'DECIMAL',     'ENTERO',    'CADENADOBLE',
        'CADENASIMPLE', 'ID',        'MENIGUAL',
        'MAYIGUAL',    'PUNTO',     'CADENALIKE',
        'CONCAT', 'BITWAND', 'BITWOR', 'BITWXOR',
        'BITWNOT', 'BITWSHIFTL', 'BITWSHIFTR', 'CSIMPLE'
    ] + list(reservadas.values())


#### *Expresiones regulares, Precedencia de operadores, terminación de analisis léxico*
    t_PUNTO = r'\.'
    t_DOSPUNTOS = r':'
    t_COMA = r','
    t_PTCOMA = r';'
    t_LLAVIZQ = r'{'
    t_LLAVDER = r'}'
    t_PARIZQ = r'\('
    t_PARDER = r'\)'
    t_CORCHIZQ = r'\['
    t_CORCHDER = r'\]'
    t_IGUAL = r'='
    t_MAS = r'\+'
    t_MENOS = r'-'
    t_ASTERISCO = r'\*'
    t_DIVIDIDO = r'/'
    t_EXPONENTE = r'\^'
    t_MENQUE = r'<'
    t_MAYQUE = r'>'
    t_MENIGUAL = r'<='
    t_MAYIGUAL = r'>='
    t_DIFERENTE = r'<>'
    t_MODULO = r'\%'
    t_BITWOR = r'\|'
    t_CONCAT = r'\|\|'
    t_BITWAND = r'&'
    t_BITWXOR = r'\#'
    t_BITWNOT = r'~'
    t_BITWSHIFTL = r'<<'
    t_BITWSHIFTR = r'>>'
    t_CSIMPLE = r'\''

---

    def t_DECIMAL(t):
        r'\d+\.\d+'
        try:
            t.value = float(t.value)
        except ValueError:
            print("Float value too large %d", t.value)
            t.value = 0
        return t

---
    def t_ENTERO(t):
      r'\d+'
      try:
          t.value = int(t.value)
      except ValueError:
          print("Integer value too large %d", t.value)
          t.value = 0
      return t
---
    def t_ID(t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = reservadas.get(t.value.lower(), 'ID')
        return t
---
#### Cadenas

    def t_CADENADOBLE(t):
        r'\".*?\"'
        t.value = t.value[1:-1]
        return t
---

    def t_CADENALIKE(t):
        r'\'%.*?%\''
        t.value = t.value[1:-1]
        return t
---

    def t_CADENASIMPLE(t):
        r'\'.*?\''
        t.value = t.value[1:-1]
        return t
---
#### Comentarios
    def t_COMENTARIO_MULTILINEA(t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')

    def t_COMENTARIO_SIMPLE(t):
        r'--.*\n'
        t.lexer.lineno += 1
---
#### Caracteres ignorados
    t_ignore = " \t"

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")


    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
---
##### Asociación de operadores y precedencia
      precedence = (

        ('left', 'CONCAT'),
        ('left', 'BITWOR'),
        ('left', 'BITWXOR'),
        ('left', 'BITWAND'),
        ('left', 'BITWSHIFTL', 'BITWSHIFTR'),
        ('left', 'BITWNOT'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'MENQUE', 'MAYQUE', 'MENIGUAL', 'MAYIGUAL', 'IGUAL', 'DIFERENTE'),
        ('left', 'MAS', 'MENOS'),
        ('left', 'ASTERISCO', 'DIVIDIDO', 'MODULO'),
        ('left', 'EXPONENTE'),
        ('right', 'UMENOS')
      )
### Analisis Sintáctico

#### *Definición de la gramática*
##### Bloque instrucciones principales, estado inicial.
    init : instrucciones

    instrucciones : instrucciones instruccion
                    | instruccion

    instruccion   : createDB_instr
                    | replaceDB_instr
                    | alterDB_instr
                    | dropDB_instr
                    | showDB_instr
                    | insert_instr
                    | update_instr
                    | alter_instr PTCOMA
                    | delete_instr
                    | truncate_instr
                    | create_instr
                    | select_instr
                    | use_instr
                    | indexinstr
                    | plsql_instr
                    | llamadafunciones
                    | llamadaprocedimiento
##### DATABASE
###### CREATE AND REPLACE DATABASE
    createDB_instr    : CREATE DATABASE existencia
                        | CREATE DATABASE ID state_owner

    replaceDB_instr   : REPLACE DATABASE existencia
                        | REPLACE DATABASE ID state_owner
    
    existencia        : IF NOT EXISTS ID state_owner

    state_owner       : OWNER IGUAL ID state_mode
                        | OWNER IGUAL CADENASIMPLE state_mode
                        | OWNER ID state_mode
                        | OWNER CADENASIMPLE state_mode
                        | state_mode
    
    state_mode        : MODE IGUAL ENTERO PTCOMA
                        | MODE ENTERO PTCOMA
                        | PTCOMA

###### ALTER DATABASE

    alterDB_instr     : ALTER DATABASE ID RENAME TO ID PTCOMA
                        | ALTER DATABASE ID OWNER TO owner_users PTCOMA

    owner_users       : ID
                        | CURRENT_USER
                        | SESSION_USER
###### DROP DATABASE
    dropDB_instr      : DROP DATABASE ID PTCOMA
                        | DROP DATABASE IF EXISTS ID PTCOMA
###### SHOW DATABASES
    showDB_instr      : SHOW DATABASES PTCOMA
                        | SHOW DATABASES LIKE regexpr PTCOMA

    regexpr           :  MODULO ID
                        | MODULO ID MODULO
                        | MODULO ENTERO
                        | MODULO ENTERO MODULO
                        | ID MODULO
                        | ENTERO MODULO
###### USE DATABASE
    use_instr         :  USE DATABASE ID PTCOMA


##### INSERT INTO
    insert_instr      : INSERT INTO ID VALUES PARIZQ parametros PARDER PTCOMA
                        | INSERT INTO ID PARIZQ columnas PARDER VALUES PARIZQ parametros PARDER PTCOMA

    parametros        :  parametros COMA parametroinsert
                        | parametroinsert

    parametroinsert   : DEFAULT
                        | expresion

    columnas          : columnas COMA ID
                        | ID
##### UPDATE
    update_instr      : UPDATE ID SET asignaciones PTCOMA
                        | UPDATE ID SET asignaciones WHERE condiciones PTCOMA

    asignaciones      : asignaciones COMA asignacion
                        | asignacion

    asignacion        : ID IGUAL expresion

##### DELETE, TRUNCATE
    delete_instr      : DELETE FROM ID PTCOMA
                        | DELETE FROM ID WHERE condiciones PTCOMA

    truncate_instr    : TRUNCATE listtablas PTCOMA
                        | TRUNCATE listtablas CASCADE PTCOMA
                        | TRUNCATE TABLE listtablas PTCOMA  
                        | TRUNCATE TABLE listtablas CASCADE PTCOMA

    listtablas        : listtablas COMA ID
                        | ID

##### ALTER TABLE
    alter_instr       : ALTER TABLE ID ADD COLUMN list_columns
                        | ALTER TABLE ID ADD CHECK PARIZQ condicion PARDER
                        | ALTER TABLE ID ADD CONSTRAINT ID UNIQUE PARIZQ ID PARDER
                        | ALTER TABLE ID ADD FOREIGN KEY PARIZQ ID PARDER REFERENCES ID
                        | ALTER TABLE ID ALTER COLUMN ID SET NOT NULL
                        | ALTER TABLE ID DROP CONSTRAINT ID
                        | ALTER TABLE ID RENAME COLUMN ID TO ID
                        | ALTER TABLE ID DROP COLUMN listtablas
                        | ALTER TABLE ID list_alter_column

    list_alter_column : list_alter_column COMA ALTER COLUMN ID TYPE type_column
                        | ALTER COLUMN ID TYPE type_column

    list_columns      : list_columns COMA ID type_column
                        | ID type_column

    type_column       : SMALLINT
                        | INTEGER
                        | BIGINT
                        | decimal
                        | NUMERIC
                        | REAL
                        | FLOAT
                        | INT
                        | DOUBLE
                        | MONEY
                        | VARCHAR PARIZQ ENTERO PARDER
                        | CHARACTER VARYING PARIZQ ENTERO PARDER
                        | CHARACTER PARIZQ ENTERO PARDER
                        | CHAR PARIZQ ENTERO PARDER
                        | TEXT
                        | TIMESTAMP 
                        | TIMESTAMP PARIZQ ENTERO PARDER
                        | DATE
                        | TIME
                        | TIME PARIZQ ENTERO PARDER
                        | INTERVAL field

    field             : YEAR
                        | MONTH
                        | DAY
                        | HOUR
                        | MINUTE
                        | SECOND
##### CREATE TABLE
    create_instr      : CREATE lista_crear create_final

    create_final      : PTCOMA
                        | INHERITS PARIZQ ID PARDER PTCOMA

    lista_crear       : DATABASE lista_owner
                        | OR REPLACE DATABASE lista_owner
                        | TABLE ID PARIZQ lista_campos PARDER 

    lista_campos      : lista_campos COMA campo
                        | campo
                    
    campo             :  ID type_column
                        | ID type_column PRIMARY KEY
                        | PRIMARY KEY PARIZQ columnas PARDER 
                        | FOREIGN KEY PARIZQ columnas PARDER REFERENCES ID PARIZQ columnas PARDER

    lista_owner       : IF NOT EXISTS ID
                        | ID


#### QUERIES
##### SELECT
    select_instr      : select_instr1 PTCOMA

    select_instr1     : SELECT termdistinct selectlist selectfrom

    selectfrom        : FROM listatablasselect whereselect groupby orderby
                        | empty

    termdistinct      : DISTINCT
                        | empty

    selectlist        : ASTERISCO
                        | listaselect

    listaselect       : listaselect COMA valselect
                        | valselect

    valselect         : ID alias
                        | ID PUNTO ASTERISCO
                        | ID PUNTO ID alias
                        | funcion_matematica_ws alias
                        | funcion_matematica_s alias
                        | funcion_trigonometrica alias
                        | PARIZQ select_instr1 PARDER alias
                        | agregacion PARIZQ cualquieridentificador PARDER alias
                        | COUNT PARIZQ ASTERISCO PARDER alias
                        | COUNT PARIZQ cualquieridentificador PARDER alias
                        | func_bin_strings_1 alias
                        | func_bin_strings_2 alias
                        | func_bin_strings_4 alias

    agregacion        : SUM
                        | AVG
                        | MAX
                        | MIN

    listatablasselect : listatablasselect COMA tablaselect
                        | tablaselect
    
    tablaselect       : ID alias
                        | PARIZQ select_instr1 PARDER alias

    alias             : ID
                        | CADENASIMPLE
                        | CADENADOBLE
                        | AS ID
                        | AS CADENASIMPLE
                        | AS CADENADOBLE
                        | empty
##### WHERE
    whereselect       : WHERE condicioneswhere
                        | empty

    condicioneswhere  : condicioneswhere OR  condicionwhere
                        | condicioneswhere AND condicionwhere
                        | condicionwhere
    
    condicionwhere    : whereexists
                        | notwhereexists
                        | wherenotin
                        | wherein
                        | wherenotlike
                        | wherelike
                        | wheresubstring
                        | between_state
                        | not_between_state
                        | predicates_state
                        | is_distinct_state
                        | condicion

    whereexists       : EXISTS PARIZQ select_instr1 PARDER

    notwhereexists    : NOT EXISTS PARIZQ select_instr1 PARDER

    wherein           : cualquiernumero IN PARIZQ select_instr1 PARDER
                        | cadenastodas IN PARIZQ select_instr1 PARDER
    
    wherenotin        : cualquiernumero NOT IN PARIZQ select_instr1 PARDER
                        | cadenastodas NOT IN PARIZQ select_instr1 PARDER

    wherenotlike      : cadenastodas NOT LIKE CADENALIKE

    wherelike         : cadenastodas LIKE CADENALIKE

    wheresubstring    : SUBSTRING PARIZQ cadenastodas COMA ENTERO COMA ENTERO PARDER IGUAL CADENASIMPLE

    cadenastodas      : cualquiercadena
                        | cualquieridentificador

##### GROUP BY, HAVING, ORDER BY . . .
    groupby           : GROUP BY listagroupby
                        | GROUP BY listagroupby HAVING condicioneshaving
                        | empty

    listagroupby      : listagroupby COMA valgroupby
                        | valgroupby

    valgroupby        : cualquieridentificador
                        | cualquiernumero
    
    condicioneshaving : condicioneshaving OR condicionhaving
                        | condicioneshaving AND condicionhaving
                        | condicionhaving

    condicionhaving   : expresionhaving MENQUE expresionhaving
                        | expresionhaving MAYQUE expresionhaving
                        | expresionhaving MENIGUAL expresionhaving
                        | expresionhaving MAYIGUAL expresionhaving
                        | expresionhaving IGUAL expresionhaving
                        | expresionhaving DIFERENTE expresionhaving

    expresionhaving   : cualquiercadena
                        | expresionaritmetica
                        | condicionhavingagregacion
                        | funcion_matematica_ws

    condicionhavingagregacion     : agregacion PARIZQ cualquieridentificador PARDER

    orderby           : ORDER BY listarorderby
                        | ORDER BY listarorderby instrlimit
                        | empty

    listarorderby     : listarorderby COMA valororderby
                        | valororderby

    valororderby      : cualquieridentificador ascdesc anular
                        | cualquiernumero ascdesc anular

    ascdesc           : DESC
                        | ASC
                        | empty

    anular            : NULLS LAST
                        | NULLS FIRST
                        | empty

    instrlimit        : LIMIT ENTERO instroffset
                        | LIMIT ALL instroffset

    instroffset       : OFFSET ENTERO
                        | empty

    condiciones       : condiciones AND condicion
                        | condiciones OR condicion
                        | condicion
    
    condicion         : expresion MENQUE expresion
                        | expresion MAYQUE expresion
                        | expresion MENIGUAL expresion
                        | expresion MAYIGUAL expresion
                        | expresion IGUAL expresion 
                        | expresion DIFERENTE expresion

    expresion         : cualquiercadena
                        | funcion_matematica_ws
                        | expresionaritmetica
                        | func_bin_strings_1
                        | func_bin_strings_2
                        | vallogico
                        | PARIZQ select_instr1 PARDER

    expresionaritmetica   : expresionaritmetica MAS expresionaritmetica 
                            | expresionaritmetica MENOS expresionaritmetica 
                            | expresionaritmetica ASTERISCO expresionaritmetica
                            | expresionaritmetica DIVIDIDO expresionaritmetica 
                            | expresionaritmetica MODULO expresionaritmetica 
                            | expresionaritmetica EXPONENTE expresionaritmetica
                            | MENOS expresionaritmetica %prec UMENOS
                            | cualquiernumero
                            | cualquieridentificador
                            | PARIZQ expresionaritmetica PARDER

    cualquiernumero   : ENTERO
                        | DECIMAL

    cualquiercadena   : CADENASIMPLE
                        | CADENADOBLE

    cualquieridentificador : ID
                             | ID PUNTO ID
    
    vallogico         : FALSE
                        | TRUE

##### FUNCIONES MATEMATICAS, TRIGONOMETRICAS, BINARIAS
    funcion_matematica_ws : ABS PARIZQ expresionaritmetica PARDER
                            | CBRT PARIZQ expresionaritmetica PARDER
                            | CEIL PARIZQ expresionaritmetica PARDER
                            | CEILING PARIZQ expresionaritmetica PARDER

    funcion_matematica_s  : DEGREES PARIZQ expresionaritmetica PARDER
                            | DIV PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                            | EXP PARIZQ expresionaritmetica PARDER
                            | FACTORIAL PARIZQ expresionaritmetica PARDER
                            | FLOOR PARIZQ expresionaritmetica PARDER
                            | GCD PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                            | LN PARIZQ expresionaritmetica PARDER
                            | LOG PARIZQ expresionaritmetica PARDER
                            | MOD PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                            | PI PARIZQ PARDER
                            | POWER PARIZQ expresionaritmetica COMA expresionaritmetica PARDER
                            | RADIANS PARIZQ expresionaritmetica PARDER
                            | ROUND PARIZQ expresionaritmetica PARDER
                            | SIGN PARIZQ expresionaritmetica PARDER
                            | SQRT PARIZQ expresionaritmetica PARDER
                            | WBUCKET PARIZQ explist PARDER
                            | TRUNC PARIZQ expresionaritmetica PARDER
                            | RANDOM PARIZQ expresionaritmetica PARDER

    explist           : expresionaritmetica COMA expresionaritmetica COMA expresionaritmetica COMA expresionaritmetica

    funcion_trigonometrica    : ACOS PARIZQ expresionaritmetica PARDER
                                | ACOSD PARIZQ expresionaritmetica PARDER
                                | ASIN PARIZQ expresionaritmetica PARDER
                                | ASIND PARIZQ expresionaritmetica PARDER
                                | ATAN PARIZQ expresionaritmetica PARDER
                                | ATAND PARIZQ expresionaritmetica PARDER
                                | ATAN2 PARIZQ expresionaritmetica PARDER
                                | ATAN2D PARIZQ expresionaritmetica PARDER
                                | COS PARIZQ expresionaritmetica PARDER
                                | COSD PARIZQ expresionaritmetica PARDER
                                | COT PARIZQ expresionaritmetica PARDER
                                | COTD PARIZQ expresionaritmetica PARDER
                                | SIN PARIZQ expresionaritmetica PARDER
                                | SIND PARIZQ expresionaritmetica PARDER
                                | TAN PARIZQ expresionaritmetica PARDER
                                | TAND PARIZQ expresionaritmetica PARDER
                                | SINH PARIZQ expresionaritmetica PARDER
                                | COSH PARIZQ expresionaritmetica PARDER
                                | TANH PARIZQ expresionaritmetica PARDER
                                | ASINH PARIZQ expresionaritmetica PARDER
                                | ACOSH PARIZQ expresionaritmetica PARDER
                                | ATANH PARIZQ expresionaritmetica PARDER

    func_bin_strings_1    :  LENGTH PARIZQ cadena PARDER

    func_bin_strings_2    : SUBSTRING PARIZQ cadena COMA cualquiernumero COMA cualquiernumero PARDER 
                            | SUBSTR PARIZQ cadena COMA cualquiernumero COMA cualquiernumero PARDER
                            | TRIM PARIZQ cadena PARDER

    func_bin_strings_3    : MD5 PARIZQ cadena PARDER

    func_bin_strings_4    :  GET_BYTE PARIZQ cadena COMA ENTERO PARDER
                            | SET_BYTE PARIZQ cadena COMA ENTERO COMA ENTERO PARDER
                            | SHA256 PARIZQ cadena PARDER
                            | CONVERT PARIZQ alias PARDER
                            | ENCODE PARIZQ cadena COMA cadena PARDER
                            | DECODE PARIZQ cadena COMA cadena PARDER

    op_bin_strings        : op_bin_strings CONCAT op_bin_strings
                            | op_bin_strings BITWAND op_bin_strings
                            | op_bin_strings BITWOR op_bin_strings
                            | op_bin_strings BITWXOR op_bin_strings
                            | op_bin_strings BITWNOT op_bin_strings
                            | op_bin_strings BITWSHIFTL op_bin_strings
                            | op_bin_strings BITWSHIFTR op_bin_strings 
                            | cadena

    cadena                : cualquiercadena
                            | cualquieridentificador

##### BETWEEN, PREDICATES, DISTINCT . . .
    between_state         : cualquiernumero BETWEEN valores AND valores
                            | cadenastodas BETWEEN valores AND valores

    not_between_state     : cualquiernumero NOT BETWEEN valores AND valores
                            | cadenastodas NOT BETWEEN valores AND valores

    predicates_state      : valores IS NULL
                            | valores IS NOT NULL
                            | valores ISNULL
                            | valores NOTNULL

    is_distinct_state     :  valores IS DISTINCT FROM valores
                            | valores IS NOT DISTINCT FROM valores

    valores               : cualquiernumero
                            | cualquiercadena
                            | cualquieridentificador

    empty                 : 

#### FASE 2
##### INDEX
    indexinstr   : CREATE INDEX ID ON ID PARIZQ ID PARDER PTCOMA
                    | CREATE INDEX ID ON ID USING HASH PARIZQ ID PARDER PTCOMA
                    | CREATE INDEX ID ON ID PARIZQ ID COMA ID PARDER PTCOMA
                    | CREATE INDEX ID ON ID PARIZQ valororderby PARDER PTCOMA
                    | CREATE UNIQUE INDEX ID ON ID PARIZQ columnas PARDER PTCOMA
                    | CREATE INDEX ID ON ID PARIZQ LOWER PARIZQ ID PARDER PARDER PTCOMA
                    | CREATE INDEX ID ON ID PARIZQ ID PARDER whereselect PTCOMA
                    | CREATE INDEX ID ON ID PARIZQ ID ID PARDER PTCOMA

##### LLAMADAS A PROCEDIMIENTOS

    llamadaprocedimiento  : EXECUTE ID PARIZQ PARDER PTCOMA

    llamadaprocedimiento  : EXECUTE ID PARIZQ listaexpresiones PARDER PTCOMA

##### LLAMADAS A FUNCIONES
    llamadafunciones   : SELECT ID PARIZQ PARDER PTCOMA

    llamadafunciones   : SELECT ID PARIZQ listaexpresiones PARDER PTCOMA
##### PLSQL PROCEDIMIENTOS Y FUNCIONES
    plsql_instr   : CREATE procedfunct ID PARIZQ parametrosfunc PARDER tiporetorno cuerpofuncion

    procedfunct  : PROCEDURE 
                    | FUNCTION
                
    tiporetorno  : RETURNS type_column1 AS
                    | LANGUAGE PLPGSQL AS
                    | AS
                    | empty

    parametrosfunc  : listaparametrosfunc
                       | empty

    listaparametrosfunc : listaparametrosfunc COMA parfunc
                            | parfunc
    
    parfunc    : OUT ID type_column1
                  | INOUT ID type_column1
                  | ID type_column1
                  | type_column1

    cuerpofuncion  : CADDOLAR declaraciones cuerpo CADDOLAR LANGUAGE PLPGSQL PTCOMA
                    | CADDOLAR declaraciones cuerpo CADDOLAR PTCOMA

    declaraciones   : DECLARE listadeclaraciones
                    | empty
    
    listadeclaraciones : listadeclaraciones declaracion
                          | declaracion

    declaracion : ID constantintr type_column1 notnullinst asignavalor PTCOMA

    declaracion : ID ALIAS1 FOR DOLAR ENTERO PTCOMA
                   | ID ALIAS1 FOR ID PTCOMA

    declaracion : ID cualquieridentificador MODULO TYPE PTCOMA

    declaracion : ID cualquieridentificador MODULO ROWTYPE PTCOMA

    constantintr : CONSTANT
                    | empty

    notnullinst  : NOT NULL
                    | empty

    asignavalor      : DEFAULT expresion
                        | PTIGUAL expresion
                        | IGUAL expresion
                        | empty

    cuerpo     : BEGIN instrlistabloque END PTCOMA

    instrlistabloque : listabloque
                        | empty

    listabloque : listabloque bloque
                   | bloque

    bloque       : raisenotice
                    | asignacionbloque
                    | subbloque
                    | returnbloque
                    | instrexecute
                    | getdiagnostic
                    | instrnull
                    | instrif
                    | instrcase
                    | commitinstr
                    | rollbackinstr
                    | insert_instr
                    | update_instr
                    | alter_instr PTCOMA
                    | create_enum  
                    | drop_table   
                    | delete_instr
                    | truncate_instr
                    | select_instr

    commitinstr : COMMIT PTCOMA

    rollbackinstr : ROLLBACK PTCOMA

    raisenotice   : RAISE NOTICE CADENASIMPLE COMA ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE PTCOMA

    asignacionbloque : ID IGUAL expresion PTCOMA

    asignacionbloque : ID PTIGUAL expresion PTCOMA

    returnbloque : RETURN condicion PTCOMA

    returnbloque : RETURN QUERY select_instr1 PTCOMA
    
    returnbloque : RETURN QUERY instrexecute PTCOMA

    returnbloque : RETURN PTCOMA

    subbloque : declaraciones cuerposub

    cuerposub : BEGIN listasubbloque END PTCOMA

    cuerposub : BEGIN empty END PTCOMA

    listasubbloque : listasubbloque subbloque1
                      | subbloque1

    subbloque1   : raisenotice1
                    | asignacionbloque    

    raisenotice1  : RAISE NOTICE CADENASIMPLE COMA ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE COMA OUTERBLOCK PUNTO ID PTCOMA
                     | RAISE NOTICE CADENASIMPLE PTCOMA             

    type_column1   : SMALLINT
                      | INTEGER
                      | BIGINT
                      | RDECIMAL
                      | RDECIMAL PARIZQ ENTERO COMA ENTERO PARDER
                      | NUMERIC
                      | NUMERIC PARIZQ ENTERO PARDER
                      | REAL
                      | FLOAT
                      | INT
                      | DOUBLE
                      | MONEY
                      | VARCHAR
                      | VARCHAR PARIZQ ENTERO PARDER
                      | CHARACTER VARYING PARIZQ ENTERO PARDER
                      | CHARACTER PARIZQ ENTERO PARDER
                      | CHAR 
                      | CHAR PARIZQ ENTERO PARDER
                      | TEXT
                      | TIMESTAMP 
                      | TIMESTAMP PARIZQ ENTERO PARDER
                      | DATE
                      | TIME
                      | BOOLEAN
                      | ID
                      | TIME PARIZQ ENTERO PARDER
                      | RECORD
                      | TABLE PARIZQ parametrosfunc PARDER

    instrexecute    : EXECUTE FORMAT PARIZQ CSIMPLE select_instr1 CSIMPLE PARDER intotarget usingexpresion

    instrexecute    : EXECUTE CSIMPLE select_instr1 CSIMPLE intotarget usingexpresion

    intotarget    : INTO ID
                    | empty

    usingexpresion  : USING listaexpresiones
                       | empty
    
    listaexpresiones : listaexpresiones COMA expresion
                        | expresion


