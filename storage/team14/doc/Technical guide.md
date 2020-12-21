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

---------Marcos----------

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

-------Isam---------
