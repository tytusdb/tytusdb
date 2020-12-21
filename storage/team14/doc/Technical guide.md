# Manual Técnico **ISAM Mode**

- [Objetivos](#Objetivos)
  - [Objetivo General](#General)
  - [Objetivos Específicos](#Específicos)

- [Alcances del Proyecto](#Alcances-del-proyecto)
  - [Crear bases de datos](#Crear-bases-de-datos)
  - [Visualizar las bases de datos](#Visualizar-las-bases-de-datos)
  - [Renombrar las bases de datos](#Renombrar-las-bases-de-datos)
  - [Eliminar bases de datos](#Eliminar-base-de-datos)
  - [Crear tabla](#Crear-tabla)
  - [Visualizar tablas](#Visualizar-tablas)
  - [Extraer registros](#Extraer-registros)
  - [Extraer registros dentro de un rango](#Extraer-registros-dentro-de-un-rango)
  - [Definir primary key](#Definir-primary-key)
  - [Eliminar primary key](#Eliminar-primary-key)
  - [Renombrar tabla](#Renombrar-tabla)
  - [Agregar una columna](#Agregar-una-columna)
  - [Eliminar una columna](#Eliminar-una-columna)
  - [Eliminar tabla](#Eliminar-tabla)
  - [Añadir registros](#Añadir-registros)
  - [Carga masiva de registros](#Carga-masiva-de-registros)
  - [Extraer un registro](#Extraer-un-registro)
  - [Actualizar registro](#Actualizar-registro)
  - [Eliminar registro](#Eliminar-registro)
  - [Eliminar todos los registros](#Eliminar-todos-los-registros)

- [Requerimientos del Sistema](#Requerimientos-del-Sistema)

## Objetivos

### General
Proporcionar métodos para un almacenamiento seguro y eficaz de bases de datos para el servidor, utilizando una estructura específica([ISAM](#ISAM)).

### Específicos
- Almacenar de forma segura las bases de datos enviadas por el servidor mediante archivo .bin
- Almacenar las tablas ubicadas dentro de las bases de datos en diferentes archivos .bin
- Almacenar las tuplas de cada tabla en la estructura [ISAM](#ISAM)

## Alcances del proyecto

### Crear bases de datos
Cuando el servidor solicite la creación de una nueva bases de datos, se llamará al método [createDatabase](#createDatabase) ingresando el nombre que se desea para la base de datos, se verificará que la base de datos no exista aún, porque de existir se negará la solicitud y no se permitirá la creación hasta que se ingresé un nombre que todavía no exista en los registros.

### Visualizar las bases de datos
Cuando el servidor solicite la visualización de todas las bases de datos, se llamará al método [showDatabases](#showDatabases) el cual regresará el listado de todas las bases de datos que se encuentran almacenadas.

### Renombrar la base de datos
Cuando el servidor solicite renombrar una base de datos, se llamará al método [alterDatabase](#alterDatabase) mediante el cual se solicitará el nombre que se desea cambiar para verificar si existe la base de datos y poder colocar el nuevo nombre.

### Eliminar base de datos
Cuando el servidor solicite eliminar una base de datos, se llamará al método [dropDatabase](#dropDatabase) mediante el cual se solicitará el nombre de la base de datos que se desea eliminar, si la base existe se eliminará sin ningún problema.

### Crear tabla
Cuando el servidor solicite crear una tabla, se llamará al método [createTable](#createTable) mediante el cual se solicitará el nombre de la base de datos donde se desea crear la nueva tabla, al igual que el nombre que llevará la nueva tabla, verificando que la tabla todavía no exista dentro de los registros.

### Visualizar tablas
Cuando el servidor solicite visualizar las tablas almacenadas dentro de una base de datos, se llamará al método [showTables](#showTables) mediante el cual se buscará la base de datos deseada, al encontrarla se mostrará el listado de las tablas.

### Extraer registros
Cuando el servidor solicite mostrar los registros almacenados dentro de una tabla, se llamará al método [extractTable](#extractTable) mediante el cual se verificará la existencia tanto de la tabla como de la base de datos, al verificar que ambas existen se retornará la lista de registros almacenados en la tabla.

### Extraer registros dentro de un rango
Cuando el servidor solicite visualizar ciertos registros, se llamará al método [extractRangeTable](#extractRangeTable) mediante el cual se extraerá solamente los registros que se encuentren dentro del rango establecido.

### Definir primary key
Cuando el servidor solicite vincular una primary key a tabla, se llamará al método [alterAddPK](#alterAddPK) mediante el cual se verificará que la bases de datos y tabla existan, de ser así, se verificará que la tabla todavía no posea una primary key vinculada, al no poseer primary key vinculada pero si registros, se verificará que con la nueva primary key en ningún registro exista dos veces el mismo identificador, de ser así no se vinculará la primary key, pero en caso contrario si se vinculará.

### Eliminar primary key
Cuando el servidor solicite eliminar la primary key vinculada a una tabla, se llamará al método [alterDropPK](#alterDropPK) mediante el cual se verificará que la tabla posea una primary key vinculada, de ser así, se eliminará el vínculo manteniendo los identificadores hasta que se vinculé una nueva.

### Renombrar tabla
Cuando el servidor solicite renombrar una tabla se llamará al método [alterTable](#alterTable) mediante el cual se verificará si la tabla a la que se le desea cambiar el nombre existe, de ser así se modificará el nombre.

### Agregar una columna
Cuando el servidor solicite agregar una nueva columna a todos los registros existentes en una tabla, se llamará al método [alterAddColumn](#alterAddColumn) mediante el cual se agregará una nueva columna con el valor "default" a cada uno de los registros que existen dentro de la tabla deseada.

### Eliminar una columna
Cuando el servidor solicite eliminar una columna de los registros almacenados en una tabla, se llamará al método [alterDropColumn](#alterDropColumn) mediante el cual se verificará que la columna no pertenezca a una primary key vinculada, de no formar parte de la primary key se procedé a eliminar la columna de cada uno de los registros.

### Eliminar tabla
Cuando el servidor solicite eliminar una tabla de una base de datos, se llamará al método [dropTable](#dropTable) mediante el cual se verificará que la tabla exista para poder eliminarla con todos sus registros.

### Añadir registros
Cuando el servidor solicite ingresar un nuevo registro en una tabla, se llamará al método [insert](#insert) mediante el cual se verificará que la tabla exista, y si aún no existe un registro con una primary key igual, de cumplir entonces se almacenará utilizando la estructura ISAM.

### Carga masiva de registros
Cuando el servidor solicite cargar mediante un archivo CSV varios registros, se llamará al método [loadCSV](#loadCSV) mediante el cual se utilizará el método [insert](#insert) recorriendo todo el archivo.

### Extraer un registro
Cuando el servidor solicite buscar un registro almacenado en una tabla, se llamará al método [extractRow](#extractRow) mediante el cual se buscará dentro de la estructura si el registro ya fue creado mediante su primary key, de existir entonces se retornará el listado de registros que se encuentran almacenados.

### Actualizar registro
Cuando el servidor solicite actualizar los registros de una tabla, se llamará al método [update](#update) mediante el cual se buscará en la estructura el registro que se desea actualizar, al encontrarlo se procederá a actualizar los registros por los nuevos ingresados.

### Eliminar registro
Cuando el servidor solicite eliminar un registro almacenado en una tabla, se llamará al método [delete](#delete) mediante el cual se buscará en la estructura el registro que se desea eliminar, al encontrarlo se procederá a eliminarlo de la estructura.

### Eliminar todos los registros
Cuando el servidor solicite eliminar todos los registros de una tabla, se llamará al método [truncate](#truncate) mediante el cual se buscará la raiz de la estructura para poder eliminar todos los registros ingresados.

## Requerimientos del Sistema
- Tener instalado la versión más reciente de python
- Tener instalado Graphviz

1. [ISAMMode](#ISAMMode)
   - [Servidor](#Servidor)
   - [Bases de Datos](#Bases-de-Datos)
   - [Tablas](#Tablas)
   - [Otros](#Otros)
   
______
## ISAMMode
Controlador de todas las funciones del DBMS para el servidor, bases de datos y tablas. Este controlador se encuentra en el archivo [ISAMMode.py](storage/team14/ISAMMode.py)


## Servidor

Las bases de datos del servidor son manejadas por el DBMS, en un archivo binario que almacena la información de cada base de datos como el nombre que se le asigna como identificador único, y los nombres de las tablas que pertenecen a la misma.

Para este módulo se utiliza el archivo Database.py el cual almacena la clase DataBase y el método creador de este objeto el cual pide como único parametro el nombre para identificar este.

En el archivo principal del DBMS [ISAMMode.py](storage/team14/ISAMMode.py) se encuentran las funciones CRUD de las bases de datos:

- [Creación de Bases de Datos "*createDatabase*"](#createDatabase)
- [Presentación de Bases de Datos "*showDatabases*"](#showDatabases)
- [Modificación de Bases de Datos "*alterDatabase*"](#alterDatabase)
- [Eliminación de Bases de Datos "*dropDatabase*"](#dropDatabase)

### createDatabase
```python
def createDatabase(database: str) -> int:
```

Creación de base de datos. Método que recibe como parámetro `database` el nombre de la base de datos a crear. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en un lista temporal, comprueba que `database` no esté registrado utilizando el método de [showDatabases](#showDatabase) que devuelve una lista de los nombres de las bases de datos registrados, de ser así se procede a añadir la base de datos a la lista temporal y se guarda esta lista nuevamente en el archivo del cual se extrajo la información con el método [commit](#commit).

#### Valores de Retorno:
- 0: Se ha creado la base de datos.
- 1: Error al crear la base de datos.
- 2: Nombre de base de datos se encuentra en uso.


### showDatabases
```python
def showDatabases() -> list:
```

Método utilizado en casi todos los métodos que presenta este DBMS, ya que con este comprobamos que las bases de datos que se quieran crear, editar o eliminar existan en el servidor. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, de no tener bases de datos registradas se retornará una lista vacía.


### alterDatabase
```python
def alterDatabase(databaseOld, databaseNew) -> int:
```
Modificación de base de datos. Método que renombra bases de datos tomando como parametros el nombre de la base de datos a modificar y el nuevo nombre de esta. El flujo de este método comienza con el método [initCheck](#initCheck), se obtiene la lista de nombres en uso para bases de datos del servidor con el método [rollback](#rollback), se comprueba que la base de datos que se quiere modificar exista usando de referencia el parámetro `databaseOld`, y que el nuevo nombre no este en uso siendo este `databasenew`, de ser estas comprobaciones cumplidas se procede a cambiar el nombre de la base de datos en la lista de bases de datos y se procede a guardar la lista con el método [commit](#commit).

#### Valores de Retorno:
- 0: Se ha modificado la base de datos.
- 1: Error al modificar la base de datos.
- 2: Nombre de base de datos databaseOld no existente.
- 3: Nombre de base de datos databaseNew se encuentra en uso.


### dropDatabase
```python
def dropDatabase(database: str) -> int: 
```

Método que elimina la base de datos indicada en el parámetro `database`. El flujo de este parámetro comienza con el método [initCheck](#initCheck), se obtiene la lista de nombres en uso para bases de datos con el método [rollback](#rollback), se comprueba que la base de datos que se quiere eliminar exista, de existir la base de datos se procede a eliminar los archivos que almacenan la información de las tablas que contenía esta base de datos de la carpeta de información, se elimina de la lista de bases de datos el nombre de esta base de datos, y como ultimo paso se procede a guardar la lista con el método [commit](#commit).

#### Valores de Retorno:
- 0: Se ha eliminado la base de datos.
- 1: Error al eliminar la base de datos.
- 2: Base de datos no existente.


## Bases de Datos
Las tablas de las bases de datos son manejadas por el DBMS, en archivos binarios uno por cada tabla, que almacenan la información de estas, llevando por nombre la concatenación del nombre de la base de datos a la que pertenecen y el identificador único de estas.

Para este módulo se utiliza el archivo [Database.py](storage/team14/Table.py) el cual almacena la clase Table y el método creador de este objeto el cual pide el nombre de la tabla para identificadorla, y el número de columnas con la que contará.

En el archivo principal del DBMS [ISAMMode.py](storage/team14/ISAMMode.py) se encuentran las funciones CRUD de las tablas:

- [Creación de tablas "*createTable*"](#createTable)
- [Presentación de tablas "*showTables*"](#showTables)
- [Presentación de datos de tablas "*extractTable*"](#extractTable)
- [Presentación de datos de tablas según rango definido "*extractRangeTable*"](#extractRangeTable)
- [Modificación de tablas "*alterTable*"](#alterTable)
- [Eliminación de tablas "*dropTable*"](#dropTable)

### createTable
```python
def createTable(database: str, table: str, numberColumns: int) -> int:
```

Método que crea una tabla tomando como nombre el parámetro `table`, definiendo el número de columnas de esta con el parámetro `numberColumns`, en la base de datos especificada en el parámetro `database`. El flujo de este método comienza con el método [initcheck](#initcheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en un lista temporal, comprueba que el nombre de la base de datos a la que se desea agregar la tabla esté registrada utilizando el método de [showDatabases](#showDatabase) que devuelve una lista de los nombres de las bases de datos registrados, de ser así se procede a verificar que el nombre de la tabla no este en uso utilizando el método de [showTables](#showTables), si esto es correcto se procede a agregar el nombre de la a la lista de tablas de la base de datos, se procede a guardar la base de datos con el método [commit](#commit) y por ultimo se guarda el objeto tabla con sus atributos de nombre y numero de columnas en un archivo binario que llevara por nombre la concatenación del nombre de la base de datos a la que pertenece y su nombre también haciendo uso de [commit](#commit).

#### Valores de Retorno:
- 0: Se ha creado la tabla.
- 1: Error al crear la tabla.
- 2: Base de datos no existente.
- 3: Nombre de tabla en uso.


### showTables
```python
def showTables(database: str) -> list:
```

Método utilizado en casi todos los métodos de tablas que presenta este DBMS, ya que con este comprobamos que las tablas que se quieran crear, editar o eliminar existan en la base de datos especificada. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el metodo [rollback](#rollback), se retorna una lista con los nombres de las tablas, de estar vacia la base de datos se retorna una lista vacia.


### extractTable
```python
def extractTable(database: str, table: str) -> list:
```

Metodo que muestra todos los datos pertenecientes a una tabla. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el metodo [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procede a añadir todos los registros que almacena en una lista la cual se retorna, si la tabla no almacena registros todavia se retornara una lista vacia. Si la operacion muestra un error, no existe la base de datos o, no existe la tabla se retornara None. 


### extractRangeTable
```
def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
```

Método que muestra los registros entre el rango definido por `lower` y `upper` en la columna `columna` de la tabla `table` en la base de datos `database`.  El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el metodo [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procede a añadir todos los registros que almacena en el rango definido en una lista la cual se retorna, si la tabla no almacena registros todavia se retornara una lista vacia. Si la operacion muestra un error, no existe la base de datos o, no existe la tabla se retornara None.


### alterTable
```python
def alterTable(database: str, tableOld: str, tableNew: str) -> int:
```

Método que cambia el nombre de la tabla `tableOld` por `tableNew` en la base de datos `database`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `tableOld` se encuentra en esta lista y `tableNew` no, se procede a cambiar el nombre de la tabla, se registra el cambio en el archivo de las bases de datos con el método [commit](#commit), y se elimina el archivo que contenia el nombre anterior de la tabla y se crea uno nuevo tambien con el metodo de [commit](#commmit).

#### Valores de Retorno:
- 0: Se ha realizado el cambio.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Nuevo nombre de tabla en uso.


### dropTable
```python
def dropTable(database: str, table: str) -> int: 
```

Método que elimina la tabla `table` de la base de datos `database`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a eliminar esta con todos sus registros, para confirmar la eliminacion elimina el archivo que contenia los registros de la tabla, y se guarda la base de datos actualizada con [commit](#commit).


## Tablas
- [Definición de llave primaria "*alterAddPK*"](#alterAddPK)
- [Eliminación de llave primaria "*alterDropPK*"](#alterDropPK)
- [Inserción de columna "*alterAddColumn*"](#alterAddColumn)
- [Eliminación de Columna "*alterDropColumn*"](#alterDropColumn)
- [Inserción de Tuplas "*insert*"](#insert)
- [Muestra de Tupla "*extractRow*"](#extractRow)
- [Modificación de Tupla "*update*"](#update)
- [Eliminación de Tupla "*delete*"](#delete)
- [Eliminacion de registros de tabla "*truncate*"](#truncate)
- [Carga de Archivo CSV "*loadCSV*"](#loadCSV)

### alterAddPK
```python
def alterAddPK(database: str, table: str, columns: list) -> int:
```

Método que define la llave primaria o identificador único en la tabla `table` de la base de datos `database` según el dato que contenga la lista `columns` o concatenando los datos de varias columnas si la lista contiene mas de un dato. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a verificar que no tenga una llave primaria definida previamente, de ser asi se procede reordenar los registros concatenando las columnas especificadas y definiendo estas como identificador único, se actualiza la tabla con el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Llave primaria existente.


### alterDropPK
```python 
def alterDropPK(database: str, table: str) -> int:
```

Método que desvincula la llave primaria de los registros de la tabla `table` en la base de datos `database` antes definida por [alterAddPK](#alterAddPK), mientras no se defina una nueva llave despues de desvincular la llave primaria se mantendra el orden antes establecido. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a verificar que tenga una llave primaria definida, de ser asi se procedera a desvincular esta llave primaria de la tabla, para actualizar los atributos de la tabla se utiliza el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Llave primaria no definida.


### alterAddColumn
```python
def alterAddColumn(database: str, table: str, default: any) -> int:
```

Método que añade una un valor `default` a todos los registros de la tabla `table` y aumenta el numero de columnas que registra esta tabla en la base de datos `database` . El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a añadir a todos los registros el valor predefinido en la nueva columna. Se actualizará el archivo de la tabla que guarda la información con [commit](#commit)

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.


### alterDropColumn
```
def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
```

Método que elimina un valor de todos los registros de la tabla `table` en la columna `columnNumber` en la base de datos `database`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a comprobar que la columna `columnNumber` no sea la columna o sea parte de las columnas definidas como llave primaria, sí no viola esta restricción se procede a eliminar los valores en esta columna a todos los registros. Se actualizará el archivo de la tabla que guarda la información con [commit](#commit).

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Columna no apta para eliminacion por ser llave primaria o dejar sin columnas a la tabla.
- 5: Numero de columna mayor al registro de columnas en la tabla.


### insert
```python
def insert(database: str, table: str, register: list) -> int:
```

Método que inserta registros con valores `register` en la tabla `table` en la base de datos `database`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a comprobar que si la tabla cuenta con una llave primaria ya definida el valor en la posición de la llave primaria en `register` no se encuentre registrada, si no hay conflicto con la llave primaria se procede a registrar los valores en la tabla como un objeto *Tuple*. Se actualizará el archivo de la tabla que guarda la información con [commit](#commit). 

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Llave primaria duplicada.
- 5: Cantidad de valores mayor al numero de columnas en la tabla.


### extractRow
```python
def extractRow(database: str, table: str, columns: list) -> list:
```

Método que muestra los valores del registro `columns` en la tabla `table` en la base de datos `database`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a comprobar que si la tabla cuenta con una llave primaria ya definida los valores de `columns` se encuentren en los registros de la tabla, si se encuentra la coincidencia se retornara una lista con los valores del registro. Si ocurre un error o no los valores no coinciden con ningún registro se retornara una lista vacia.


### update
```python
def update(database: str, table: str, register: dict, columns: list) -> int:
```

Método que modifica los valores del registro `columns` en la tabla `table` en la base de datos `database` cambiándolos por los valores de `register`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a comprobar que si la tabla cuenta con una llave primaria ya definida los valores de `columns` se encuentren en los registros de la tabla, si se encuentra la coincidencia se procede a cambiar los valores del registro según las columnas ingresadas en `register`, si una columna a modificar es parte de la llave primaria se cancela la modificación de lo contrario el registro original se elimina y se vuelve a ingresar con los datos modificados. Se actualizará el archivo de la tabla que guarda la información con [commit](#commit).

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Llave primaria no existente.


### delete
```python
def delete(database: str, table: str, columns: list) -> int:
```

Método que elimina registros según la llave primaria `columns` en la tabla `table` en la base de datos `database`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a comprobar que si la tabla cuenta con una llave primaria ya definida los valores de `columns` se encuentren en los registros de la tabla, si se encuentra la coincidencia se procede a eliminar el registro al cual pertenece la llave primaria de la tabla. Se actualizará el archivo de la tabla que guarda la información con [commit](#commit).

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Llave primaria no existente.


### truncate
```python
def truncate(database: str, table: str) -> int:
```

Método que elimina todos los registros en la tabla `table` en la base de datos `database`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a borrar por completo todos los registros que estuvieran relacionados a esta tabla. Se actualizará el archivo de la tabla que guarda la información con [commit](#commit).

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.


### loadCSV
```python
def loadCSV(file: str, database: str, table: str) -> list:
```

Método que lee todos los registros en el archivo `file` y los inserta en la tabla `table` en la base de datos `database`. El flujo de este método con declarar una lista para almacenar los registros que se inserten a la tabla, con la función open de la librería de archivos csv leemos todas las líneas del archivo `file` y se agregan a una lista auxiliar. Se recorren todos los registros que tiene la lista auxiliar, en cada iteración del recorrido de la lista auxiliar se insertan los registros a la tabla `table` utilizando el metodo [insert](#insert) con los datos de cada fila como parametros, si se insertan sin conflicto los registros se añaden a la lista principal del método, al terminar de leer el archivo se retorna la lista con los registros que se insertaron exitosamente. Si existe algún error o el archivo se encuentra vacío se retornara una lista vacía. 


## Otros
- [Verificacion de Directorios "*initCheck*"](#initCheck) 
- [Lectura de Archivos "*rollback*"](#rollback)
- [Guardado de Archivos "*commit*"](#commit)

### initCheck
```python
def initCheck()
```

Método que comprueba que el directorio que almacena la información del servidor exista, de no existir crea el directorio. Comprueba que el archivo que contiene la información de las bases de datos exista, de no existir crea el archivo. Comprueba que el directorio que almacena la información de las tablas exista, de no existir crea el directorio.


### rollback
```python
def rollback(fileName: str)
```

Método que extrae del archivo binario con nombre `fileName` bases de datos y tablas. El flujo de este método comienza añadiendo el directorio de la información del servidor, y la extensión **.bin** a la dirección del archivo que buscara la función *open* de archivos de Python, si encuentra el archivo obtiene el objeto que almacena el archivo y lo retorna para su uso posterior.


### commit
```python
def commit(objeto: any, fileName: str)
```

Método que crea o actualiza el archivo con nombre `fileName` con el objeto `objeto`. El flujo de este método es, abrir un archivo binario en la dirección del directorio de la información del servidor añadiéndole el nombre del directorio a `fileName` y agregándole la extensión .bin, almacena el objeto `objeto` en el archivo de forma binaria y cierra el archivo para su uso posterior.

### ISAM
Cada una de las tuplas que se encuentran almacenadas dentro de las tablas de cada base de datos, se almacenan mediante la estructura de datos conocida como [ISAM](#ISAM), de esta manera se busca obtener una mayor eficiencia al momento de hacer uso de las funciones CRUD de las tuplas; cada una de las tuplas posee un identificador único, mejor conocido como, Primary Key(PK), mediante el identificador se logra acceder a los registros.

ISAM proviene de Indexed Sequential Access Method, es una estructura estática de índices, es eficiente cuando no existen muchas inserciones o actualizaciones, de lo contrario se va perdiendo dicha eficiencia volviendo la estructura obsoleta; su estructura se basa en un árbol B+, debido que todas las entradas de datos se encuentran almacenados dentro de los nodos hojas, posee una variante respecto al árbol B+ y es que al momento que los nodos hojas se encuentran totalmente llenos, se agregan otros nodos conocidos como, páginas overflow, dentro de estos nodos se va almacenando más información sin tener que alterar la estructura base del árbol B+.

Para este módulo se utiliza el archivo [ISAM.py](storage/team14/ISAM.py) dentro del cual se encuentra el manejo de toda la estructura, posee las clases LeafNode, IndexNode, Tuple e ISAM, con dichas clases se establece un manejo óptimo y eficaz de la estructura, se estableció un árbol de grado 3 con 3 niveles de altura.

Dentro del archivo [ISAM.py](storage/team14/ISAM.py) se encuentran los siguientes métodos:

- [Inserción de nodos "insert"](#insert)
- [Crear página hoja "makeIndexLeaf"](#makeIndexLeaf)
- [Eliminar un nodo "delete"](#delete)
- [Eliminar todos los nodos "truncate"](#truncate)
- [Ordenar arreglo "sort"](#sort)
- [Mostrar en pantalla "print"](#print)
- [Graficar la estructura "chart"](#chart)
- [Buscar un nodo "search"](#search)
- [Extraer todos los registros "extractAll"](#extractAll)
- [Extraer todos los nodos "extractAllObject](#extractAllObject)
- [Nueva Primary Key "newPK"](#newPK)
- [Extraer un rango de nodos "extractRange"](#extractRange)
- [Añadir al final "addAtEnd"](#addAtEnd)
- [Eliminar una columna "deleteColumn"](#deleteColumn)
- [Actualizar un nodo "update"](#update)

### insert
```python
def insert(self, data):
```

Método utilizado para ingresar un nuevo nodo a la estructura, se solicita el identificador y registros que se desean almacenar, se valida si el nodo auxiliar ya se encuentra lleno, si no se encuentra lleno, se inserta el nuevo registro y se ordena mediante el metodo [sort()](#sort), si el nodo ya se encuentra lleno, entonces se procede a verificar si el nuevo registro es menor, mayor o un valor intermedio dentro de los valores ya almacenados, si es menor, se inserta hacia la izquierda; si es intermedio, se inserta en el centro y si es mayor, se inserta en la derecha, se repite el proceso mediante recursividad hasta encontrar un nodo disponile para almacenar el nuevo registro. Si el registro se almacena en un nodo de tipo IndexNode, entonces se procede a realizar una copia de tipo LeafNode, y se elimina el registro del tipo IndexNode, de esta manera se cumple el tipo de estructura, almacenando solamente en nodos hojas o páginas overflow. Si se alcanza el nivel 2, se procede a llenar las páginas overflow, utilizando el mismo criterio que sean de grado 3, y solamente almacenará hacia nodos siguientes.

### makeIndexLeaf
```python
def makeIndexLeaf(self, register):
```

Método utilizado para realizar la copia de un nodo Index hacia un nodo Hoja, retornando la Tupla que será almacenada en el nuevo nodo Hoja.

### delete
```python
def delete(self, valor):
```

Método que se encarga de eliminar un registro solicitado, se recorre toda la estructura, verificando si en los nodos Index se encuentra el nodo a eliminar también se verifica si existen registros en él, de no ser así se procede a buscar el nodo Hoja con todos los registros, al encontrarlo se elimina su registro, y si el nodo queda totalmente vacio se elimin, de no quedar vacio el nodo, solamente se eliminará el registro solicitado.

### truncate
```python
def truncate(self):
```

Método utilizado para eliminar todos los nodos ya existentes, se llama al nodo raiz y se le asigna un valor None, de esta manera se elimina cualquier tipo de registro hacia los demas nodos.

### sort
```python
def sort(self, array):
```
Método utilizado para ordenar los registros ubicados dentro de los nodos, se solicita la lista que se desea ordenar y mediante el ordenamiento burbuja se retorna la nueva lista ya ordenada.

### print
```python
def print(self):
```
Método utilizado para mostrar en consola todos los registros que posee la estructura, se recorre desde el nodo raiz y hasta que se encuentra un nodo None pasaría a verificar el siguiente nodo.

### chart
```python
def chart(self):
```
Método utilizado para graficar le estrucutra, se utiliza Graphviz como auxiliar y poder graficar todas las estructuras posibles, se crea un archivo .dot posteriormente se convierte en .png, se recorre cada uno de lo nodos, desde la raiz hasta los None, al terminar con un nodo, pasaría al siguiente utilizando recursividad, hasta terminar todos los nodos, creando el nuevo archivo con la estructura graficada.

### search
```python
def search(self, value):
```

Método que retorna un nodo deseado, se solicita el valor que se esta buscando, recorriendo toda la estructura y verificando en cada uno de los nodos existentes, si el nodo se encuentra entonces se retornan todos los registros almacenados, en caso contrario solamente se retornará una lista vacia.

### extractAll
```python
def extractAll(self):
```

Método que retorna una lista con todos los registros que se encuentran disponibles, se realiza un recorrrido desde la raiz hasta las páginas overflow, si estas existen, en caso contrario solamente hasta los nodos hoja y nodos index que posean registros, si existen registros en el nodo valuado, entonces se comenzará a llenar una lista para posteriormente retornarla.

### extractAllObject
```python
def extractAllObject(self):
```

Método que retorna una lista con todos los objetos que se encuentran disponibles, incluyendo su identificador, se realiza un recorrrido desde la raiz hasta las páginas overflow, si estas existen, en caso contrario solamente los nodos hoja y nodos index, si existen registros en el nodo valuado, entonces se comenzará a llenar una lista para posteriormente retornarla.

### newPK
```python
def newPK(self, PKs):
```

Método que registra una nueva Primary Key para todos los nodos, al momento de definir una nueva primary key, se llamará al método para recorrer toda la estructura e ir creando el nuevo identificador y reemplazando el antiguo por el nuevo.

### extractRange
```python
def extractRange(self, lower, upper, column):
```

Método que retorna una lista de registros que se encuentran dentro de un rango específico, se realiza un recorrido de todos los nodos junto con una validación si los registros almacenados cumplen con las restricciones, de ser así se almacenarán en una lista que posteriormente se retornará para visualizar dichos registros.

### addAtEnd
```python
def addAtEnd(self, default):
```

Método que agrega una columna al final de cada registro, estableciendo un valor por default que llevará dicha columna, se realiza un recorrido de la estructura y en cada registros se añade dicha columna, sin importar si es nodo index, hoja o página overflow.

### deleteColumn
```python
def deleteColumn(self, n):
```

Método que elimina una columna de todos los registros, siempre y cuando la columna no se encuentre como primary key, porque de ser así se rechaza la petición. Se recorre toda la estructura eliminando la columna especificada en cada registro.

### update
```python
def update(self, register, cols, PKCols):
```

Método que reemplaza los valores solicitados, se busca mediante la primary key el nodo que se desea actualizar, se recorre toda la estructura, si encuentra el nodo, procede a reemplazar los valores deseados y eliminar el registro anterior para poder actualizarlo con los nuevos registros
