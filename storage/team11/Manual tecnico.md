
# MANUAL TÉCNICO

UNIVERSIDAD DE SAN CARLOS DE GUATEMALA  
FACULTAD DE INGENIERÍA  
ESCUELA DE CIENCIAS Y SISTEMAS  
CURSO: 772 ESTRUCTURA DE DATOS  
DICIEMBRE 2020  
___

# TytusDB

![](https://upload.wikimedia.org/wikipedia/commons/4/4a/Usac_logo.png =250x250)

## Team 11
* Carlos Esteban Vivar Torres      201801597
* Mynor Rene Ruiz Guerra           201801329
* Eliezer Abraham Zapeta Alvarado  201801719
* Elmer Gustavo Sanchez Garcia     201801351
___

## Índice
- [Descripción General](#Descripción-general)
- [Requerimientos Funcionales](#Requerimientos-funcionales)
- [Licencias y Convenios](#Licencias-y-convenio)
- [Funcionalidades](#Funcionalidades)
    - [Funciones CRUD de las bases de datos](#Funciones-CRUD-de-las-bases-de-datos)
    - [Funciones CRUD de las tablas](#Funciones-CRUD-de-las-tablas)
    - [Funciones CRUD de las tuplas](#Funciones-CRUD-de-las-tuplas)
- [Glosario](#Glosario)
- [E-grafías](#E-grafías)


### Descripción general 
Es un proyecto Open Source en desarrollo para crear un administrador de bases de datos utilizando distintos modos de almacenamiento mediante el uso distintas estructuras de datos.
Este paquete es el encargado de gestionar el almacenamiento de las bases de datos del proyecto, el cual proporciona al servidor un conjunto de funciones para manipular la información que ingresa a las bases de datos.

TytusBD tiene cinco modos de almacenamiento, este paquete brinda la modalidad de almacenacenaje para la estructura de datos mediante un árbol AVL, siendo esta estructura la base para poder manipular los datos a traves de las funciones que ofrece el DBMS. El almacenamiento funciona con tres tipos de arboles AVL desarrollados en el lenguaje Python para poder separar los tipos de informacion como: las bases de datos, las tablas y los registros. Para la persistencia de los datos  utiliza un sistema jerárquico de ficheros y serialización de objetos que guardan la información de cada estructura.

## Requerimientos funcionales
- El software es el encargado de gestionar el almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para extraer la información.
- El modo de almacenamiento sera por medio de la estructura de un arbol AVL.
- Cada registro que corresponde a una tabla será almacenado en cada nodo en el arbol correspondiente para las tablas.
- El servidor de la base de datos podrá contener n bases de datos.
- Se manejan los archivos de manera binaria para no exponer la información.
- Los métodos y funciones deben cumplir con el tipo de dato que rigen sus parámetros y los valores a retornar segun su significado.
- Se brindara una interfaz iteractiva para la visualizacion de los datos y el comportamiento de las estructuras

## Licencias y convenio
El proyecto está diseñado bajo una licencia Open Source, específicamente **MIT**. Por convenio, los estudiantes aparecerán como contribuidores junto con el copyright. Además, cualquier biblioteca autorizada también se debe colocar la licencia y el copyright en el archivo LICENSE.md en su carpeta respectiva. 

## Funcionalidades
#### Funciones CRUD de las bases de datos
___
### [Manager.py](https://github.com/tytusdb/tytus/blob/main/storage/team11/Manager.py)
Nombre de la funcion | Parametros | Descripcion | Clase
---------------------|------------|-------------|-------
```createDatabase``` | ```( db_nombre )``` | Verifica si el nombre de la base de datos existe, de no ser asi crea un nodo en el arbol AVL para base de datos.| ```Manager```
```showDatabases``` | ```( )``` | Devuelve una lista de los nombres de las bases de datos, si ocurrió un error o no hay bases de datos devuelve una lista vacía [].| ```Manager```
```alterDatabase``` | ```( databaseOld, databaseNew )```  | Renombra una base de datos, realiza la busqueda en el arbol para encontrar el nodo correspondiente.| ```Manager```
```alterDatabase``` | ```( databaseOld, databaseNew )```  | Renombra una base de datos, realiza la busqueda en el arbol para encontrar el nodo correspondiente.| ```Manager```
```dropDatabase``` | ```( database )``` | Elimina por completo el nodo correspondiente a la base de datos indicada. | ```Manager```




___


## Funciones Basicas de los arboles AVL:
 Estas funciones son utilizadas en los distintos tipos de arboles que contiene el paquete, las siguientes funcionalidades describen el comportamiento que la estructura de un arbol AVL debe cumplir, balanceado, ordenado y estructurado para que nos garantice una eficiencia alta.

Nombre de la funcion | Parametros | Descripcion | Clase
---------------------|------------|-------------|-------
```add``` | ```( element )``` | Agrega un nodo al arbol con los atributos correspondientes, posteriormente verifica si el arbol esta balanceado, si no, lo balanceara.| ```ArbolAVLDB```
```get_height``` | ```( root )``` | Returna la altura de un nodo en especifico| ```ArbolAVLDB```, ```ArbolAVLManager```, ```ArbolAVLR```
```rotacion_left``` | ```( Nodo )``` | Ejecuta una rotacion de sus nodos hacia la izquierda |```ArbolAVLDB```, ```ArbolAVLManager```, ```ArbolAVLR```
```rotacion_right``` | ```( Nodo )``` | Ejecuta una rotacion de sus nodos hacia la derecha |```ArbolAVLDB```, ```ArbolAVLManager```, ```ArbolAVLR```
```get_balance``` | ```( root )``` | Retorna la resta entre 2 alturas de nodos especificos | ```ArbolAVLDB```, ```ArbolAVLManager```, ```ArbolAVLR```
```delete_nodo``` | ```(root, value)``` | Busca un nodo especifico que desea eliminar, posteriormente verifica si todo el arbol esta balanceado.| ```ArbolAVLDB```, ```ArbolAVLManager```, ```ArbolAVLR```
```find_nodo``` | ```( root )``` | Retorna el nodo que se encuentra mas a la izquierda| ```ArbolAVLDB```, ```ArbolAVLManager```, ```ArbolAVLR```
```search_value``` | ```( root )``` | Busca una nodo en el arbol que corresponda al valor que se busca y si la encuentra retorna el nodo. | ```ArbolAVLDB```, ```ArbolAVLManager```, ```ArbolAVLR```

___
### [ArbolAVLManager.py](https://github.com/tytusdb/tytus/blob/main/storage/team11/ArbolAVLManager.py)
Nombre de la funcion | Parametros | Descripcion | Clase
---------------------|------------|-------------|-------
```update_db``` | ```( db )``` | Este metodo hace llamada ha un metodo recursivo para actualizar una base de datos especifica| ```ArbolAVLManager```
```__update_db``` | ```( db )``` | Este metodo recursivo recorre el arbol de bases de datos y actualiza su elemento| ```ArbolAVLManager```
```get_databases``` || Este retorna una lista de las bases de datos existentes| ```ArbolAVLManager```
```__inorder``` |```( nodo )``` | Ordena los nodos(bases de datos) del arbol AVL y los guarda en una lista.| ```ArbolAVLManager```
__graficar|```( padre, actual, left )``` | Grafica el arbol AVL de bases de datos.| ```ArbolAVLManager```


___
### [ArbolAVLDB.py](https://github.com/tytusdb/tytus/blob/main/storage/team11/ArbolAVLDB.py)
Nombre de la funcion | Parametros | Descripcion | Clase
---------------------|------------|-------------|-------
```insert_tupla``` | ```( table,register )``` | Este metodo hace llamada ha un metodo recursivo para insertar un tupla de una clase Tabla| ```ArbolAVLDB```
```__insert_tupla``` | ```( root,table,register )``` | Este metodo se encarga de la llamada de un funcion de la clase Tabla que pertenece a un nodo| ```ArbolAVLDB```
```extract_row``` | ```( table,columns )``` | Ejecuta un llamada a un metodo recursivo  para extrar una fila|```ArbolAVLDB```
```__extract_row``` | ```( Nodo )``` | Ejecuta una llamado a un metodo de la clase Tabla para extraer una fila,retorna el valor encontrada si lo encuentra |```ArbolAVLDB```
```load_csv``` | ```( table,file )``` | Ejecuta una funcion recursiva para cargar un archivo csv | ```ArbolAVLDB```
```__load_csv``` | ```(root,table,file)``` |Ejecuta una llamada al metodo loadCSV de la clase Tabla para insertar registros multiples,retorna el valor encontrada si lo encuentra | ```ArbolAVLDB```
```truncate``` | ```( table )``` | Ejecuta un metodo recursivo para elimanar registros de una tabla| ```ArbolAVLDB```
```__truncate``` | ```( root, table )``` | Ejecuta una llamada al metodo truncate de la clase Tabla para eliminar registros multiples,retorna el valor encontrada si lo encuentra  | ```ArbolAVLDB```
```alter_drop_pk``` | ```( table_name )``` | Ejecuta un metodo recursivo para elimanar una llave primaria de una tabla.| ```ArbolAVLDB```
```__alter_drop_pk``` | ```( table_name )``` | Ejecuta una llamada al metodo alterDropPK de la clase Tabla para eliminar la llave primaria de una tabla,retorna el valor encontrada si lo encuentra.| ```ArbolAVLDB```
```update_alter_add_column``` | ```( root, table_name )``` | Agrega una columna al final de cada registro de la tabla y base de datos especificada | ```ArbolAVLDB```
```__update_alter_add_column``` | ```( root, table_name )``` | Ejecuta una llamada al metodo alterAddColumn de la clase Tabla para agregar una columna extra de una tabla,retorna el valor encontrada si lo encuentra. | ```ArbolAVLDB```
```update_table_pk``` | ```( table_name, columns )``` | Busca el nodo de la tabla solicitada, asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas.| ```ArbolAVLDB```
```update_alter_add_column``` | ```( root, table_name )``` | Agrega una columna al final de cada registro de la tabla y base de datos especificada | ```ArbolAVLDB```

___
### [ArbolAVLR.py](https://github.com/tytusdb/tytus/blob/main/storage/team11/ArbolAVLR.py)

Nombre de la funcion | Parametros | Descripcion | Clase
---------------------|------------|-------------|-------
```get_tables``` | ```(  )``` | Llama a una funcion recursiva y retorna una lista con los registros de cada una de las tablas| ```ArbolAVLR```
```__inorder``` | ```( nodo )``` | Funcion que retorna un lista de llaves primarias en orden del arbol AVL.| ```ArbolAVLR```
```extra_table``` | ```(  )``` | Retorna una lista con los nodos de una base de datos especifica.| ```ArbolAVLR```
```__extract_table``` | ```( nodo )``` | Retorna un a lista con los nombres de las tablas en orden del arbol AVL| ```ArbolAVLR```
```__truncate``` | ```( nodo )``` | Elimina los registros de una tabla especifica, la eliminacion se hace por medio de la funcion del arbol AVL.| ```ArbolAVLR```
```update_node``` | ```( value, register )``` | Actualiza la informacion de un registro especifico.| ```ArbolAVLR```
```extractRangeTable``` | ```( column_number, lower, upper )``` | Retorna una lista con todos los registros de una tabla especifica.| ```ArbolAVLR```
```__extract_range_table``` | ```( nodo, column_number, lower, upper)``` | Obtiene una lista con los registros de una tabla especifica que cumplan con la condicion que esten entre el rango del dato lower y upper.| ```ArbolAVLR```
___
### [Binary.py](https://github.com/tytusdb/tytus/blob/main/storage/team11/Binary.py)
Nombre de la funcion | Parametros | Descripcion | Clase
---------------------|------------|-------------|-------
```commit``` | ```( file_name )``` | Crea y escribe los datos en archivos binarios .bin| ```Binary```
```rollback``` | ```( file_name )``` | Lee los datos que estan guardados en un archivo binario .bin| ```Binary```
```verify_string``` | ```( string )``` | Se encarga de verficar que los nombres cumplan con la nomenclatura de las base de datos| ```Binary```
```verify_columns``` | ```( nums_columns, columns )``` | Se encarga de verficar que los numeros de columna correspondan a una tabla especifica| ```Binary```
___
#### Funciones CRUD de las tablas
### [DataBase.py](https://github.com/tytusdb/tytus/blob/main/storage/team11/DataBase.py)
Nombre de la funcion | Parametros | Descripcion | Clase
---------------------|------------|-------------|-------
```create_table``` | ```( table, number_columns)``` | Crea una instancia de tabla y lo agrega en un nodo al arbol de tablas| ```Database```
```show_tables``` | ( ) | Devuelve una lista de los nombres de las tablas de una base de datos, si ocurrió un error o no hay bases de datos devuelve una lista vacía | ```Database```
```extract_table``` | ```( table_name )``` | Extrae y retorna una lista con elementos que corresponden a cada registro de la tabla| ```Database```
```extract_range_table``` | ```( table_name, column_number, lower, upper )``` | Extrae y retorna una lista con los elementos que corresponden a un rango de registros de la tabla| ```Database```
```alter_add_pk``` | ```( table_name, columns )``` | Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas| ```Database```
```alter_drop_pk``` | ```( table_name )``` | Elimina la llave primaria actual en la información de la tabla, manteniendo el índice actual de la estructura del árbol|```Database```
```alter_table``` | ```( table_old, table_new )``` | Renombra el nombre de la tabla de una base de datos especificada|```Database```
```alter_add_column``` |  ```( table_name, default )``` | Agrega una columna al final de cada registro de la tabla y base de datos especificada |```Database```
```alter_drop_column``` |  ```( table_name, column_number )``` | Elimina una n-ésima columna de cada registro de la tabla excepto si son llaves primarias |```Database```
```drop_table``` |  ```( table_name )``` | Elimina por completo una tabla de una base de datos especificada |```Database``` 


___
#### Funciones CRUD de las tuplas
### [Table.py](https://github.com/tytusdb/tytus/blob/main/storage/team11/Table.py)


Nombre de la funcion | Parametros | Descripcion | Clase
---------------------|------------|-------------|-------
```get_tables``` | ```( )``` | Obtiene los nombres de las tablas de una base de datos con recorrido en orden y los retorna como una lista.| ```ArbolAVLR```
```__inorder``` | ```( nodo )``` | Ordena los nodos del arbol AVL y los guarda en una lista.| ```ArbolAVLDB```
```extra_table``` | ```( )``` | Obtiene la lista de tablas ordenadas y la retorna. ```ArbolAVLR```
```__extract_table``` | ```( nodo )``` | Obtiene los datos de las tablas y los retorna, exceptuando la llave primaria utilizada al insertar en el arbol | ```ArbolAVLR```
```__extract_table``` | ```( nodo )``` | Obtiene los datos de las tablas y los retorna, exceptuando la llave primaria utilizada al insertar en el arbol. |```ArbolAVLR```
```truncate``` |  |Hace una llamada a una funcion recursiva y retorna el valor de dicha funcion |```ArbolAVLR```
```__truncate```| ```( nodo )``` |Elimina los registros de una tabla especifica, sin eliminar a la tabla misma |```ArbolAVLR```
```update_node```| ```( value, register )``` |Actualiza los datos de un nodo especifico con los valores enviados. este metodo funciona cuando la llave primaria es oculta. | ```ArbolAVLR```
```extract_range_table```|```( nodo, column_numbre,lower, upper )``` |Retorna los datos de los registros que esten en el rango y en la columna especificado.  | ```ArbolAVLR```
```extractRow``` | ```( pkList )``` | Extrae y devuelve un registro especificado por su llave primaria | ```ArbolAVLR```
```insert``` | ```( data )``` | Inserta un registro en la estructura de datos asociada a la tabla y la base de datos. | ```Table```
```delete``` | ```( register )``` | Elimina un registro de una tabla y base de datos especificados por la llave primaria | ```Table```
```define_pk``` | ```( colmns )``` | Define como llaves primarias las columnas especificadas de la tabla| ```Table```




___
# Glosario
- **Paquete:** Un paquete es un contenedor de clases que permite agrupar las distintas partes de un programa y que por lo general tiene una funcionalidad y elementos comunes, definiendo la ubicación de dichas clases en un directorio de estructura jerárquica. 
- **DBMS:** (database management system, en español, administrador de bases de datos): Es aquel sistema que administra las tecnologías de la información y la comunicación, siendo responsable de los aspectos técnicos, tecnológicos, científicos, inteligencia de negocios y legales de bases de datos, y de la calidad de datos.
- **Servidor:** Es una aplicación en ejecución capaz de atender las peticiones de un cliente y devolverle una respuesta en concordancia. Los servidores se pueden ejecutar en cualquier tipo de computadora, incluso en computadoras dedicadas a las cuales se les conoce individualmente como el servidor.
- **Arbol:** Un árbol es un tipo abstracto de datos ampliamente usado que imita la estructura jerárquica de un árbol, con un valor en la raíz y subárboles con un nodo padre, representado como un conjunto de nodos enlazados.
- **Arbol AVL:** Los árboles AVL están siempre equilibrados de tal modo que para todos los nodos, la altura de la rama izquierda no difiere en más de una unidad de la altura de la rama derecha o viceversa.
- **Tupla:** Una tupla es una secuencia de valores agrupados. Una tupla sirve para agrupar, como si fueran un único valor, varios valores que, por su naturaleza, deben ir juntos.
- **Fichero:** Un archivo es un fichero (dato) almacenado en algún recurso de memoria, generalmente en Disco Duro, pero dependiendo del uso (en ciertos casos) son almacenados en RAM. 
- **CRUD:** En informática, CRUD es el acrónimo de "Crear, Leer, Actualizar y Borrar" (del original en inglés: Create, Read, Update and Delete), que se usa para referirse a las funciones básicas en bases de datos o la capa de persistencia en un software.
- **Open Source (codigo abierto):** Es el software cuyo código fuente y otros derechos que normalmente son exclusivos para quienes poseen los derechos de autor, son publicados bajo una licencia de código abierto o forman parte del dominio público.
# E-grafías
___
- tkinter — Python interface to Tcl/Tk. Library.https://docs.python.org/3/library/tkinter.html
- Arbol AVL https://www.geeksforgeeks.org/avl-tree-set-2-deletion/
- Estructura de datos https://www.ecured.cu/Estructura_de_datos
