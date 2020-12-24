Manual Técnico
=============
## Indice
- [Introducción](#introduccion)
- [Objetivos](#objetivos)
- [Alcances del proyecto](#alcances)
- [Requerimentos funcionales](#requerimientos)
- [Explicación de código](#code)
- [Diagrama de clases](#clases)
- [E - grafía](#egrafia)


<div id='introduccion'/>

## Introducción
El presente documento describe contenido relacionado a la parte técnica del proyecto TytusDB, desarrollado por estudiantes del curso de Estructuras de Datos. Describe las estructuras de datos utilizadas, así como la implementación inmediata en el proyecto y su interacción como sistema de datos, específicamente en el apartado de almacenamiento.

<div id='objetivos'/>

## Objetivos
### **General:**
- Proveer un conjunto de herramientas capaces de gestionar la información de un sistema de bases de datos de manera eficiente.
### **Específicos:**
- Utilizar el lenguaje de programación Python para el desarrollo de una solución eficiente en el manejo de la información. 
- Implementar un arbol B+ para el manejo de las tuplas en el sistema. 
- Desarrollar un sistema capaz de representar de forma gráfica las distintas estructuras implementadas en la gestión de datos.
<div id="alcances"/>

## Alcances del proyecto
- El proyecto se basa en un sistema que gestiona el almacenamiento de datos a nivel interno en un sistema mas grande encargado de la gestión de bases de datos DBMS (DataBase Management System). Este subsistema construye una de las funciones fundamentales del DBMS denominado particularmente como TytusDB, el cual posee una licencia de tipo MIT bajo su definición, reglas y limitaciones.
- Todas las funciones y métodos son desarrollados por estudiantes, para el curso de Estructuras de Datos, Universidad de San Carlos de Guatemala. Por lo que tiene como enfoque, la implementación de estructuras arboleas, particularmente un árbol B+ y un AVL para el almacenamiento de datos. Específicamente, bases de datos, tablas y tuplas.
- La persistencia de los datos se maneja con un sistema que utiliza un sistema jerárquico de ficheros y serialización de objetos que guardan la información de cada estructura.


<div id="requerimientos"/>

## Requerimientos Funcionales
- El software -Administrador de almacenamiento- es el encargado de gestionar el almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para extraer la información.
- Tendrá que operar bajo un solo modo de almacenamiento, el cual es establecido por el tipo de estructura utilizada. Por lo que el nivel de eficiencia debe coincidir. En este caso con un árbol b+ y un arbol AVL.
- Cada registro que corresponde a una tupla de una tabla será almacenado en cada nodo o cada elemento de una página de las estructuras anteriores. 
- Cada atributo será débilmente tipado, a efectos de no verificar tipo en este punto, ya que lo hará el parser de SQL (Segmento de software no incluido en el proyecto).
- El servidor de la base de datos podrá contener n bases de datos.
- Se manejan los archivos de manera binaria para no exponer la información.
- Los métodos y funciones deben cumplir con el tipo de dato que rigen sus parámetros.
- El nombre de las bases de datos y de las tablas deben cumplir el formato de un identificador.


<div id="code"/>

## Explicación de Código
### [AVLTree.py](https://github.com/tytusdb/tytus/blob/main/storage/team18/storage/AVLTree.py)
### **Descripción:**
En este archivo se encuentran las clases que representan la estructura de un árbol AVL y sus funciones. Esta estructura es la encargada de manejar el conjunto de bases de datos y el conjunto de tablas.
### **Clases:**
> `TreeNode` Representa un nodo del árbol AVL

> `AVLTree` Representa la estructura de un árbol AVL, contiene las funciones para manejar los nodos.

### **Funciones:**
|Nombre de la función |Descripción| Clase |
| ------------ | ------------ |------------|
| `add(self, root, key)` | Añade un nuevo nodo al árbol. |`AVLTree`|
| `delete(self, root, key)` | Elimina un nodo existente del árbol. |`AVLTree`|
| `preOrder(self, root, f, key)` | Recorre el árbol de forma pre orden. |`AVLTree`|
| `postOrder(self, root)` | Recorre el árbol de forma post orden y retorna una cadena con todos los valores almacenados. |`AVLTree`|
| `search(self, root, key)` | Verifica si existe algun nodo con el valor "key" en el árbol. |`AVLTree`|
| `getRoot(self)` | Retorna la raiz del árbol. |`AVLTree`|
| `graph(self, database)` | Genera una imagen del árbol con Graphviz |`AVLTree`|


### [BplusTree.py](https://github.com/tytusdb/tytus/blob/main/storage/team18/storage/BplusTree.py)
### **Descripción:**
En este archivo se encuentran las clases que representan la estructura de un árbol B+ y las funciones que lo componen. Esta estructura es la encargada de manejar el conjunto de tuplas de las diferentes tablas.

### **Clases:**
> `Node` Representa un nodo del árbol B+

> `BPlusTree` Representa la estructura de un árbol B+, contiene las funciones para manejar los nodos.

### **Funciones:**
|Nombre de la función |Descripción| Clase |
| ------------ | ------------ |------------|
| `insert(self, key, value)` |añade un nuevo valor al Nodo.  |`Node`|
 `insert(self, key, value)` |añade un nuevo valor al árbol.  |`BPlusTree`|
| `delete(self, keys)` |Elimina un valor almacenado dentro del arbol con el codigo dado.|`BPlusTree`|
| `graficar(self, database, table)` |Genera una imagen del árbol con Graphviz|`BPlusTree`|
| `reorganizar(self)` |Reorganiza la estructura de los nodos dentro del árbol|`BPlusTree`|
| `GenKey(self, register)` |Genera el codigo de almacenaje de los valores registrados en el árbol|`BPlusTree`|
| `search(self, keys)` |Realiza una busqueda de un valor por medio de sus llaves primarias|`BPlusTree`|
| `CreatePK(self, Pk)` |Crea la llave primaria perteneciente al árbol|`BPlusTree`|
| `DeletePk(self)` |Elimina llave primaria del árbol|`BPlusTree`|
| `addColumn(self, default)` |Añade una nueva columna con un valor por defecto a todos los valores almacenados dentro del árbol|`BPlusTree`|
| `dropColumn(self, column)` |Elimina una columna en todos los valores almacenados dentro del árbol|`BPlusTree`|
| `update(self, data, columns)` |Actualiza un valor almacenado dentro del árbol correpondiente a al codigo indicado.|`BPlusTree`|
| `truncate(self)` |Elimina todos los valores y nodos de la estructura|`BPlusTree`|


### [Interfazz.py](https://github.com/tytusdb/tytus/blob/main/storage/team18/storage/Interfazz.py)
### **Descripción:**
Este archivo contiene el código crea la interfaz gráfica, utilizada para mostrar las estructuras y sus contenidos a travez de la herramienta [Graphviz](https://graphviz.org/ "Graphviz").

### **Funciones:**
|Nombre de la función |Descripción|
| ------------ | ------------ |
| `show_data_bases()` | muestra la interfaz grafica de la lista de base de datos junto a sus bases de datos. |
| `show_tables(parent_window, database)` | Muestra la interfaz grafica con la grafica de una tabla junto a sus tablas. |
| `extract_table(database, table, parent_window)` |Muestra la interfaz grafica de las Tablas junto a todas sus tuplas|
| `table_graph(tupla, key, table, database)` |Genera la grafica de una tupla en una nueva ventana.|
| `upload_csv(entry)` |Genera una ventana de dialogo para abrir un archivo csv.|
| `create_database_window(parent)` |Ventana en la cual se crean bases de datos.|
| `alter_database_window(parent, names)` |Ventana en la cual se puede cambiar el nombre a una base de datos|
| `show_tables_window(parent, names)` |Ventana en la cual se muestran todas las tablas de una base de datos.|
| `drop_database_window(parent, names)` |Ventana en la cual se pueden eliminar bases de datos.|
| `create_table_window(grandParent,parent, database)` |Ventana en la cual se crean tablas en una base de datos seleccionada con anterioridad|
| `refresh_tables(parent, actual, database)` |Reinicia las Ventanas luego de realizar cambios en las bases de datos, tablas o tuplas.|
| `extract_table_window(database, names)` |Ventana en la cual se muestran todos lás tuplas de una tabla indicada|
| `extract_range_table_window(database, names)` |Ventana en la cual se meustra un conjunto de tuplas mayores que un dato indicado y menores a un segundo dato|
| `alter_table_window(grandParent, parent, database, names)` |Ventana en la cual se edita el nonmbre de una tabla indicada.|
| `drop_table_window(grandParent, parent, database, names)` |Ventana en la cual se puede eliminar una tabla indicada.|
| `alter_addPK_window(grandParent, parent, database, table)` |En esta ventana se agrega las relaciones de llave primaria a una tabla indicada en las columnas indicadas|
| `alter_addColumn_window(grandParent, parent, database, table)` |En esta ventana se permite agregar una columna con un valor por defecto a todas las tuplas de una tabla|
| `alter_dropColumn_window(grandParent, parent, database, table)` |En esta ventana se permite eliminar una columna indicada en todas las tuplas de una tabla|
| `extract_row_window(database, table)` |En esta ventana se solicita una llave con la cual se mostrara el valor que representa esta dentro de la tabla|
|`update_window(grandParent, parent, database, table)`|Esta ventana permite actualizar una tupla de la tabla, solicitando los datos a editar y la columna en la cual editar|
|`delete_window(grandParent, parent, database, table)`|Esta ventana permite eliminar una tupla de la tabla indicanda por medio de su llave primaria|


### [Serializable.py](https://github.com/tytusdb/tytus/blob/main/storage/team18/storage/Serializable.py)
### **Descripción:**
Este archivo contiene el código crea la interfaz gráfica, utilizada para mostrar las estructuras y sus contenidos a travez de la herramienta [Graphviz](https://graphviz.org/ "Graphviz").

### **Funciones:**
|Nombre de la función |Descripción|
| ------------ | ------------ |
| `Read(direction, name)` | Lee el archivo binario con nombre "name", en la ruta indicada por el parámetro "direccion" y retorna el objeto leído.  |
| `delete(direction)` | Elimina la carpeta indicada por el parámetro |
| `write(direction, name, data)` |Crea una carpeta y escribe los datos del parámetro "data" en el archivo con nombre "name" en la ruta de archivos "direccion" |
| `update(direction, name, data)` | Sobrescribe los datos del archivo "name" con los nuevos datos del parámetro "data"  |
| `Rename(direction,oldDirection, NewDirection)` | Renombra un archivo archivo |

### [Storage.py](https://github.com/tytusdb/tytus/blob/main/storage/team18/storage/Storage.py)
### **Descripción:**
Este archivo contiene el conjunto de funciones utilizadas por el administrador de almacenamiento para insertar, extraer y modificar datos en el sistema.

### **Funciones:**
| Nombre de la función| Descripción|
|--- |---|
|`checkData()`| Verifica la existencia de la carpeta /Data y el archivo Databases.bin, y si no existen los crea|
| `validateIdentifier(identifier)`| Función utilizada para validar que los nombres sean identificadores validos de SQL.|
| `createDatabase(database)`| Crea una base de datos. Parámetro database: es el nombre de la base de datos.|
| `showDatabases()`| Devuelve una lista de los nombres de las bases de datos.|
|`alterDatabase(dataBaseOld, dataBaseNew)`| Renombra la base de datos databaseOld por databaseNew. Los parámetros deben ser identificadores validos.|
| `dropDatabase(database)`| Elimina por completo la base de datos indicada en database.|
| `createTable(database, table, numberColumns)`| Crea una tabla en una base de datos especificada recibiendo una lista de índices referentes a la llave primaria y llave foránea.|
| `showTables(database)`| Devuelve una lista de los nombres de las tablas de una base de datos.|
| `extractTable(database, table)`| Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla.|
| `extractRangeTable(database, table, columnNumber, lower, upper)`| Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabla.|
| `alterAddPK(database, table, columns)`| Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas, esto para anticipar el índice de la estructura de la tabla cuando se inserten registros.|
| `alterDropPK(database, table)`| Elimina la llave primaria actual en la información de la tabla, manteniendo el índice actual de la estructura del árbol hasta que se invoque de nuevo el alterAddPK().|
| `alterTable(database, tableOld, tableNew)`| Renombra el nombre de la tabla de una base de datos especificada.|
| `alterAddColumn(database, table, default)`                       | Agrega una columna al final de cada registro de la tabla y base de datos especificada.|
| `alterDropColumn(database, table, columnNumber)`|Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias.|
| `dropTable(database, table`| Elimina por completo una tabla de una base de datos especificada.|
| `dropAll()`| Elimina por completo todos los datos almacenados.|
| `insert(database, table, register)`| Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.|
| `loadCSV(filepath, database, table)`| Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado. La base de datos y la tabla deben existir, y coincidir con el número de columnas. Si hay llaves primarias duplicadas se ignoran. No se utilizan títulos de columnas y la separación es por comas.|
| `extractRow(database, table, columns)`| Extrae y devuelve un registro especificado por su llave primaria.|
|`update(database, table, register, columns)`|Permite actualizar los datos de un registro en específico, especificando su llave primaria, es posible modificar las propias llaves primarias, sin embargo, se verificará que la nueva primaria no esté repetida, esto para mantener la consistencia de los datos, si la nueva primaria se repite se forma un error. |
|`delete(database, table, columns)`| Elimina un registro de una tabla y base de datos especificados por la llave primaria.|
|`truncate(database, table)`| Elimina todos los registros de una tabla y base de datos.|




<div id="clases"/>

## Diagrama de clases
![](https://github.com/tytusdb/tytus/blob/main/storage/team18/doc/img/DiagramaDeClases.png)

<div id="egrafia"/>

## E - grafías

- Joyanes A. Luis , Zahonero M. Ignacio . (2004). Algoritmos y estructuras de datos una perspectiva en C.
- pickle — Python object serialization. Library.  https://docs.python.org/3/library/pickle.html
- os — Miscellaneous operating system interfaces. Library. https://docs.python.org/3/library/os.html
- re — Regular expression operations. Library. https://docs.python.org/3/library/re.html
- shutil — High-level file operations. Library. https://docs.python.org/3/library/shutil.html
- tkinter — Python interface to Tcl/Tk. Library.https://docs.python.org/3/library/tkinter.html
