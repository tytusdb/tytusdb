# Manual de Usuario EDD_Grupo 9

## Funciones Generales Fase 2
 ### Funcionalidades en Bases de datos
*  ### Administrador de  almacenamiento 
* Solo se ingresa el nombre de la base de datos, el modo que se desea y el tipo de codificacion **debe de cumplir con las reglas de indentificadores en SQL**
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Existente
    *	3 --> Modo Incorrecto
    *	4 --> Codificación Incorrecta
```python
	def createDatabase(database: str, mode: string, encoding: string) -> int:
```
### Administrador del modo de almacenamiento 
*  ### Cambiar el modo de la base de datos 
* El storageManager debe permitir cambiar el modo de almacenamiento de una base de datos o de una tabla en cualquier momento. Al suceder, si no hay ningun error, se debe construir la estructura de datos asociada al modo y eliminar la anterior.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	4 --> Modo Incorrecto
```python
	def alterDatabaseMode(database: str, mode: str) -> int:
```
*  ### Cambiar el modo de una tabla 
* Cambia el modo de almacenamiento de una tabla de una base de datos especificada.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existente
    *	4 --> Modo Incorrecto
```python
	def alterTableMode(database: str, table: str, mode: str) -> int:
```
### Administrador de indices
*  ### Agregar una llave foranea 
* Agrega un índice de llave foránea, creando una estructura adicional con el modo indicado para la base de datos. 
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table o TableRef no Existen
    *	4 --> Cantidad no Exacta Entre Columns y ColumnsRef
```python
	def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
```

*  ### Eliminar una llave foranea 
* Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existen
    *	4 --> Nombre de Indice no Existente
```python
	def alterTableDropFK(database: str, table: str, indexName: str) -> int:
```
*  ### Agregar un Indice Unico 
* Agrega un índice único, creando una estructura adicional con el modo indicado para la base de datos.  
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existen
    *	5 --> No Cumple con la Integridad de Unicidad
```python
	def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
```

*  ### Elimina un Indice Unico 
* Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existen
    *	4 --> Nombre de Indice no Existente
```python
	def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
```
*  ### Agregar un Indice 
* Agrega un índice, creando una estructura adicional con el modo indicado para la base de datos.   
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existen
```python
	def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
```

*  ### Elimina un Indice Unico 
* Destruye el índice tanto como metadato de la tabla como la estructura adicional creada.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existen
    *	4 --> Nombre de Indice no Existente
```python
	def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
```
### Administrador de la codificación
*  ### Metodo de codificacion 
* Asociada una codificación a una base de datos por completo. 
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Nombre de Codificación no Existente
```python
	def alterDatabaseEncoding(database: str, encoding: str) -> int:
```
### Generacion del Checksum
*  ### Checksum de la base de datos
* Genera un diggest a partir del contenido de la base de datos incluyendo sus tablas. 
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	Cadena --> Devuelve un string
	* 	None --> Error en la operacion
```python
	def checksumDatabase(database: str, mode: str) -> str:
```

*  ### Checksum de la tabla
* Genera un diggest a partir del contenido de la tabla de una base de datos.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	Cadena --> Devuelve un string
	* 	None --> Error en la operacion
```python
	def checksumTable(database: str, table:str, mode: str) -> str:
```
### Compresion de datos
*  ### Comprimir una base de datos
* Agregue compresión utilizando la biblioteca zlib de python y las funciones compress y decompress. Se debe agregar a columna tipo varchar o text de cada tabla de la base de datos. De igual manera, al extraer la información se debe descomprimir.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Level Incorrecto
```python
	def alterDatabaseCompress(database: str, level: int) -> int:
```
*  ### Descomprimir una base de datos
* Quita la compresión de una base de datos especificada.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> No Había Compresión
```python
	def alterDatabaseDecompress(database: str) -> int:
```

*  ### Comprimir una tabla
* Agregue compresión utilizando la biblioteca zlib de python y las funciones compress y decompress. Se debe agregar a columna tipo varchar o text de cada tabla de la base de datos. De igual manera, al extraer la información se debe descomprimir. De igual manera, al extraer la información se debe descomprimir.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existe
    *   4 --> Level Incorrecto
```python
	def alterTableCompress(database: str, table: str, level: int) -> int:
```

*  ### Descomprimir una tabla
* Quita la compresión de una base de datos especificada.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existe
    *   4 --> No Habia Compresion
```python
	def alterTableDecompress(database: str, table: str) -> int:
```
### Seguridad
*  ### Criptografia
* Crifra el texto backup con la llave password y devuelve el criptograma. Se puede utilizar cualquier método y biblioteca.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	Archivo --> Contiene el archivo cifrado
	* 	None --> Error en la operacion
```python
	def encrypt(backup: str, password: str) -> str:
```
*  ### Desencriptar
* Descrifra el texto cipherBackup con la llave password y devuelve el texto plano. Se puede utilizar cualquier método y biblioteca.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	Archivo --> Contiene el archivo cifrado
	* 	None --> Error en la operacion
```python
	def decrypt(cipherBackup: str, password: str) -> str:
```
*  ### BlockChain Safe mode on
* el storageManager debe proveer un mecanismo para trabajar en modo seguro una tabla. Es decir, al activar el modo seguro de una tabla, cuando se realicen operaciones de inserción se debe ir creando bloques con sus respectivos valores Hash (esto almacenado en un archivo JSON), cuando algún bloque sea modificado o eliminado la cadena quedará incosistente 
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existe
    *   4 --> Modo Seguro Existente
```python
	def safeModeOn(database: str, table: str): -> int
```

*  ### BlockChain Safe mode of
* Desactiva el modo seguro en la tabla especificada de la base de datos.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Inexistente
    *	3 --> Table no Existe
    *   4 --> Modo Seguro no Existente
```python
	def safeModeOff(database: str, table: str): -> int
```
### Grafos
*  ### DSD
* Genera un gráfico mediante Graphviz acerca de la base de datos especificada. 
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	Archivo --> Contiene el archivo graphviz
	* 	None --> Error en la operacion
```python
	def graphDSD(database: str) -> str:
```
*  ### DF
* Genera un gráfico mediante Graphviz acerca de las dependencias funcionales de una tabla especificada de una base de datos. 
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	Archivo --> Contiene el archivo graphviz
	* 	None --> Error en la operacion
```python
	def graphDSD(database: str) -> str:
```

## Funciones Generales Fase 1
  ### Funcionalidades en Bases de datos
*  ### Creacion de bases de datos
* Solo se ingresa el nombre de la base de datos **debe de cumplir con las reglas de indentificadores en SQL**
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Existente
```python
	def createDatabase(database: str) -> int:
```

*  ### Visualizacion de bases de datos
El valor de retorno es un arreglo que cambia segun los datos

* [None]-->  Arreglo Vacio
* [Data1,Data2,Data3] --> Arreglo Con los datos
```python
	def showDatabases() -> list:
```

*  ### Modifica Nombre de bases de datos
* Parametros: 

	* databaseOld: Nombre de la base de datos que se quiere modificar 
	* databaseNew: Nombre Nuevo de la base de datos

	El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*  0 --> Operacion Exitosa
	*  1 --> Error en la operacion
	*  2 --> Base de Datos No Existente
	*  3 --> Base de Datos Existente
```python
	def alterDatabase(databaseOld, databaseNew) -> int:
```
	

*  ### Eliminacion de bases de datos
* Solo se ingresa el nombre de la base de datos **debe de cumplir con las reglas de indentificadores en SQL**
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Existente
```python
	def dropDatabase(database: str) -> int: 
```
##	   Funcionalidades en Tablas

*  ### Creacion de tablas en bases de datos
* **database:** es el nombre de la base de datos a utilizar.	

* **table:** es el nombre de la tabla que se desea crear.

* **numberColumns:** es el número de columnas que tendrá cada registro de la tabla.

El valor de retorno es un entero que debe de cumplir con lo siguiente:

* 0 --> Operacion Exitosa
* 1 --> Error en la operacion
* 2 --> Base de Datos Existente
	
	
```python
	def createTable(database: str, table: str, numberColumns: int) -> int:
```

*  ### Visualizacion tablas en la bases de datos
El valor de retorno es un arreglo que cambia segun los datos
*	[	]-->  Arreglo Vacio si no hay tablas en la base de datos
* 	[Data1,Data2,Data3] --> Arreglo Con las tablas en dicha base
*	None --> Si no existe la base de datos
```python
	def showTables(database: str) -> list:
```

*  ### Visualizar una tabla especifica de la  bases de datos
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea crear.
El valor de retorno es un arreglo que cambia segun los datos
	*	[	]-->  Arreglo Vacio si no hay tablas en la base de datos
	* 	[Data1,Data2,Data3] --> Arreglo Con las tablas en dicha base
	*	None --> Si no existe la base de datos
```python
	def extractTable(database: str, table: str) -> list:
```

*  ### Visualiza una tabla con un rango especifico de la  bases de datos
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea crear.
* **columnNumber:** es el número de índice de columna a restringir o verificar con los valores upper y lower.
* **upper:** es el límite superior (inclusive) del rango a extraer de la columna indicada de la tabla.
* **lower:** es el límite inferior (inclusive) del rango a extraer de la columna indicada de la tabla.
El valor de retorno es un arreglo que cambia segun los datos
	*	[	]-->  Arreglo Vacio si no hay tablas en la base de datos
	* 	[Data1,Data2,Data3] --> Arreglo Con las tablas en dicha base
	*	None --> Si no existe la base de datos
```python
	def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
```

*  ### Asocia llave primaria o compuesta en tablas de la bases de datos
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea crear.
* **columns:** es el listado de números de columnas que formarán parte de la llave primaria. 
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla no existe
	*	4 --> Llave Primaria Existe
	*	5 --> columnas fuera de límites.
```python
	def alterAddPK(database: str, table: str, columns: list) -> int:
```


*  ### Elimina la llave primaria actual en la información de la tabla en la base de datos
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea utilizar.
El valor de retorno es un arreglo que cambia segun los datos
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla no existe
	*	4 --> Llave Primaria no Existe
```python
	def extractTable(database: str, table: str) -> list:
```

*  ### Renombra el nombre de la tabla de una base de datos especificada
* Parametros: 
* **database:** es el nombre de la base de datos a utilizar.
* **tableOld:** es el nombre de la tabla a renombrar.
* **tableNew:** es el nuevo nombre con que renombrará la tableOld.
Valor de retorno: 0 operación exitosa, 1 error en la operación, 2 database no existente, 3 tableOld no existente, 4 tableNew existente.
	El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla Antigua no existe
	*	4 --> Llave Primaria no Existe
	```python
		def alterTable(database: str, tableOld: str, tableNew: str) -> int:
	```

*  ### Agrega una columna al final de cada registro de la tabla y base de datos especificada
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea modificar.
* **default:** es el valor que se establecerá en a la nueva columna para los registros existentes.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla no existe
```python
	def alterAddColumn(database: str, table: str, default: any) -> int:
```


*  ### Eliminar una n-ésima columna de cada registro de la tabla excepto si son llaves primarias.
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea eliminar.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla no existe
	*	4 --> Lllave no puede eliminarse o tabla quedarse sin columnas
	*	5 --> columnas fuera de límites.
```python
	def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
```


*  ### Elimina por completo una tabla de una base de datos especificada. 
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea eliminar.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla no existe 
```python
	def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
```
##	   Funcionalidades en Tuplas


*  ### Inserta un registro en la estructura de datos asociada a la tabla y la base de datos
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea utilizar
* **register:** es una lista de elementos que representan un registro.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos Existente
	*	3 --> Tabla no existe
	*	4 --> Lllave primaria duplicada
	*	5 --> columnas fuera de límites.
```python
	 def insert(database: str, table: str, register: list) -> int:
```

*  ### Extrae y devuelve un registro especificado por su llave primaria.
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea utilizar.
* **columns:** es la llave primaria 
Valor de retorno: lista con los valores del registro, si ocurrió un error o no hay registro que mostrar devuelve una lista vacía [].
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	[	]-->  Arreglo Vacio si no hay registro o hay algun error
	* 	[Data1,Data2,Data3] --> Lista con los valores del registro,
```python
	  def extractRow(database: str, table: str, columns: list) -> list:
```

*  ### Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea utilizar.
* **register:** es una lista de elementos llave:valor que representa los elementos a actualizar del registro. La llave el número de coluna y el valor el contenido del campo.
Valor de retorno: lista con los valores del registro, si ocurrió un error o no hay registro que mostrar devuelve una lista vacía [].
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla no existe
	*	4 --> Lllave Primaria no Existe
```python
	  def update(database: str, table: str, register: dict, columns: list) -> int: 
```

*  ### Elimina un registro de una tabla y base de datos especificados por la llave primaria.
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea utilizar.	
* **columns:** es la llave primaria.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla no existe
	*	4 --> Lllave Primaria no Existe
```python
	 def delete(database: str, table: str, columns: list) -> int:
```

*  ### Elimina todos los registros de una tabla y base de datos.
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea utilizar.	
* **columns:** es la llave primaria.

El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	0 --> Operacion Exitosa
	* 	1 --> Error en la operacion
	*	2 --> Base de Datos no Existente
	*	3 --> Tabla no existe.
```python
	 def truncate(database: str, table: str) -> int:
```

*  ### Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado.
* **Informacion Importante :** La base de datos y la tabla deben existir, y coincidir con el número de columnas. Si hay llaves primarias duplicadas se ignoran. No se utilizan títulos de columnas y la separación es por comas. 
* **database:** es el nombre de la base de datos a utilizar.
* **table:** es el nombre de la tabla que se desea utilizar.
El valor de retorno es un entero que debe de cumplir con lo siguiente:
	*	[dato1,dato2,dato3] --> lista con los valores enteros que devuelve el insert por cada fila
	* 	[__] --> Lista Vacia, sucedio un error o el archivo no tiene filas
```python
	 def loadCSV(file: str, database: str, table: str) -> list: 
```