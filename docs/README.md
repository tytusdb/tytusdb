# Enunciado del Proyecto (FASE II)
*Versión de descripción general*

Universidad de San Carlos de Guatemala  
Facultad de Ingeniería  
Cursos: 772 Estructuras de Datos | 774 Sistemas de Bases de Datos 1 | 781 Organización de Lenguajes y Compiladores 2  
Diciembre 2020

## Índice
- [Competencias del proyecto](#competencias-del-proyecto) 
- [Condiciones del proyecto](#condiciones-del-proyecto)
- [TytusDB](#tytusdb)
- [Administrador de almacenamiento](#administrador-de-almacenamiento)
- [Administrador de la base de datos](#administrador-de-la-base-de-datos)
- [SQL Parser](#sql-parser)
- [Reportes y entrega](#reportes-y-entrega)

## Competencias del proyecto

### Competencia general
- Poner en práctica los conocimientos teóricos adquiridos durante cada curso y aplicarlo a un proyecto real de código abierto fortaleciendo las competencias de administración de equipos de desarrollo.

### Competencias específicas
- El estudiante construye un intérprete para el subconjunto del lenguaje SQL mediante la traducción dirigida por la sintaxis.
- El estudiante utiliza la herramienta PLY o SLY de Python para la traducción.
- El estudiante proporciona una solución de estructuras de datos para gestionar la información de un sistema de bases de datos.
- El estudiante construye un servidor http y un cliente para que se conecten y accedan a las funciones definidas para el administrador de la base de datos.

## Términos del proyecto

### Equipos de desarrollo

- Seguirán los mismos grupos de la fase 1 por curso, excepto aquellos que se desintegraron. 
- Además deben confirmar quién será el coordinador de cada equipo para agregar o modificar al coordinador como colaborador del repositorio para aceptar los commits. 

### Lenguaje de programación

El lenguaje seleccionado es Python, y no deben utilizarse bibliotecas adicionales si no hacen falta, por ejemplo, para compiladores 2 si deben utilizar PLY. Cualquier otra biblioteca debe ser autorizada por el catedrático.

### Licencias y convenio

El proyecto está diseñado por el catedrático bajo una licencia Open Source, específicamente MIT. Por convenio, los estudiantes aparecerán como contribuidores junto con el copyright. Además, cualquier biblioteca autorizada también se debe colocar la licencia y el copyright en el archivo LICENSE.md en su carpeta respectiva.

### Manejo de versiones

Cada integrante de los equipos debe hacer sus propuestas de cambio mediante pull request directamente al master de este repositorio (no hacer pull request de la rama de cada uno para evitar conflictos), queda a discreción de cada equipo utilizar de manera independiente una rama u otro repositorio para pruebas.

### Guía de estilo de Python

Para esta fase se debe escribir código con base en la guía de estilo de Python según el [PEP 8](https://www.python.org/dev/peps/pep-0008/).

## TytusDB

Es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos, que estará a cargo del curso de Estructuras de Datos; el administrador de la base de datos, que estará a cargo del curso de Sistemas de Bases de Datos 1, este administrador se compone a su vez de un servidor y de un cliente; y el SQL Parser, que estará a cargo del curso de Organización de Lenguajes y Compiladores 2.

<p align="center">
  <img src="img/tytusdb_architecture_v3.jpg" width="800" alt="TytusDB Architecture">
</p>

## Administrador de almacenamiento

La fase 2 de Estructuras de Datos consiste en desarrollar los siguientes requerimientos:

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
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 level incorrecto.  

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
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 level incorrecto.  

```
def alterTableDecompress(database: str, table: str) -> int:
```
Quita la compresión de una base de datos especificada.  (UPDATE)  
Parámetro database: es el nombre de la base de datos a utilizar.  
Parámetro table: es el nombre de la tabla a utilizar.  
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 table no existente, 4 no había compresión.  


### 7. Seguridad

Los conceptos de seguridad se aplicarán en dos sub componentes:
- Criptografía: el storageManager debe proveer la manera de cifrar y descifrar ya sea una base de datos completa o también cifrar o descifrar una backup de una base de datos.

```
def encrypt(backup: str, password: str) -> str:
```
Crifra el texto backup con la llave password y devuelve el criptograma. Se puede utilizar cualquier método y biblioteca.  (UPDATE)  
Parámetro backup: es el nombre de la base de datos a utilizar.  
Parámetro password: es la llave para cifrar.  
Valor de retorno: contenido del archivo cifrado, None si hay un error.  

```
def decrypt(cipherBackup: str, password: str) -> str:
```
Descrifra el texto cipherBackup con la llave password y devuelve el texto plano. Se puede utilizar cualquier método y biblioteca.  (UPDATE)  
Parámetro cipherBackup: es el nombre de la base de datos a utilizar.  
Valor de retorno: contenido del archivo cifrado, None si hay un error.  

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


## Administrador de la base de datos

Conforme a la arquitectura, el administrador de la base de datos debe ser capaz de interactuar con los conponentes indicados en la figura antes vista.

Se sugiere iniciar con el Query Tool, que para el inicio de esta fase se estará completando en el curso correspondiente.


## SQL Parser

La segunda fase del proyecto, en cuanto al parser de SQL, consiste en agregar los siguientes componentes:

- Índices: agregar al parser la administración de índices, la especificación está en el capítulo 11 de la documentación de PostgreSQL [Indexes](https://www.postgresql.org/docs/13/indexes.html)

- PL/pgSQL: agregar al parser el lenguaje procedural, la especificación está en el capítulo 42 de la documentación de PostgreSQL [PL/pgSQL — SQL Procedural Language](https://www.postgresql.org/docs/13/plpgsql.html)

- Traducción, optimización y ejecución de código: la ejecución del lenguaje PL/pgSQL se realizará mediante la traducción hacia un lenguaje intermedio basado en Python y que cumpla con las características del código de tres direcciones. El código generado debe ejecutarse desde Python para mostrar los resultados al administrador de bases de datos.

## Reportes y entrega

### Reportes para estructuras de datos
Los reportes de las estructuras utilizadas se deben mostrar mediante una aplicación de interfaz gráfica utilizando cualquier herramienta gráfica (que cumpla compatibilidades de licencia). 

Para la fase 2, se debe mostrar los dos grafos de dependencias y el blockchain.

### Reportes para compiladores 2
Los reportes por entregar son los siguientes (mostrar el resultado en una ventana cuando sea ejecutada la funciones que invoquen a los reportes):
- Reportes de errores léxico, sintácticos y semánticos. Debe mostrar como mínimo el tipo, la descripción y el número de línea.
- Reporte de tabla de símbolos. Debe mostrar las variables, funciones y procedimientos con mínimo los siguientes datos: identificador, tipo, dimensión, declarada en, y referencias.
- Reporte de AST. Cuando se requiera, debe mostrar el árbol de sintaxis abstracta utilizando Graphviz en una nueva ventana que muestre solo la imagen o documento.
- Reporte gramatical. Se debe crear en la carpeta del equipo un archivo con Markdown que muestre las dos gramáticas con sintaxis BNF. En otro documento se debe mostrar la definición dirigida por la sintaxis con la gramática seleccionada, indicando que expresiones se utilizaron, precedencia, símbolos terminales y no terminales, y las reglas semánticas. Tomar en cuenta que no es el código escrito, sino es un reporte de explicación generado automáticamente, diferente del producto entregable del proyecto que es más enfocado a la construcción del intérprete. Este reporte está enfocado más a la ejecución específica.
- Reporte de optimizaciones. Se debe mostrar en qué parte del código aplicó alguna optimización y qué tipo. Basarse en las optimizaciones indicadas en el libro de texto, tanto de bloques como de mirilla.

### Reportes para bases de datos
Respecto del componente de este curso no se tendrán reportes, ya que mediante el cliente se podrán ejecutar las funciones solicitadas e incluso el resultado de consultas de SQL.

### Manual técnico y de usuario
En la carpeta del equipo se debe crear con Markdown un archivo de manual técnico y otro de manual de usuario. Se puede utilizar cualquier referencia bibliográfica para elaborar los manuales, se sugiere ver este [enlace](https://web.mit.edu/course/21/21.guide/docution.htm) del MIT.

### Consideraciones
- La entrega se realizará mediante commits a este repositorio, para cada equipo se le indicará su carpeta específica.
- La calificación se realizará de manera virtual (ya sea en meet o zoom) con las cámaras activadas, cada calificación será almacenada.
- No se recibe ningún proyecto después de finalizada la entrega.
- Copias de proyectos obtendrán una nota 0, por lo que pierde automáticamente el laboratorio, se utilizará la herramienta JPlag https://jplag.ipd.kit.edu/
- Durante la calificación se verificará la autoría mediante preguntas, si no la responde se procederá a anular su nota del proyecto.
- Cualquier aclaración o modificación del proyecto se realizará mediante este documento, nadie excepto el catedrático puede modificar este archivo, si alguien lo modificará se tomarán acciones de anulación de proyecto.
- Los estudiantes al hacer un commit aceptan las condiciones, licencias y convenios relacionados con el fin del proyecto.
- Media vez los componentes sean funcionales, estos deben poder interactuar con cualquier otro componente de la arquitectura antes planteada. 
- En cuanto al almacenamiento y extracción de datos, se debe considerar únicamente la codificación UTF8.

### Calificación
- Un porcentaje será evaluado mediante una hoja de calificación (nota grupal).
- Un porcentaje será evaluado mediante Stack Ranking de equipos con características similares (el mejor obtiene la mejor nota). El proyecto del equipo ganador será utilizado como base de TytusDB y también para la segunda fase (nota grupal). 
- Un porcentaje será evaluado mediante el total de commits aceptados y la calidad de estos mediante Stack Ranking por equipo (nota individual).
- Un porcentaje será por calificación interna del equipo también por Stack Ranking por equipo (nota individual).
- Un porcentaje será evaluado mediante una pregunta o en su defecto modificación de código (nota individual).

### Fecha de entrega
La fecha de entrega es el miércoles 6 de enero hasta las 11:59pm, se tomará hasta el último commit aceptado.

