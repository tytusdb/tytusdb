- [Alcances del Proyecto](#Alcances-del-proyecto)
  - [Crear bases de datos](#Crear-bases-de-datos)
  - [Visualizar las bases de datos](#Visualizar-las-bases-de-datos)
  - [Renombrar las bases de datos](#Renombrar-las-bases-de-datos)
  - [Eliminar bases de datos](#Eliminar-base-de-datos)
  - [Cambiar el modo de la base de Datos](#Cambiar-el-modo-de-la-base-de-Datos)
  - [Cambiar la codificación](#Cambiar-la-codificación)
  - [Crear tabla](#Crear-tabla)
  - [Visualizar tablas](#Visualizar-tablas)
  - [Extraer registros](#Extraer-registros)
  - [Extraer registros dentro de un rango](#Extraer-registros-dentro-de-un-rango)
  - [Definir primary key](#Definir-primary-key)
  - [Eliminar primary key](#Eliminar-primary-key)
  - [Creacion de una Foreign Key](#Creacion-de-una-Foreign-Key)
  - [Eliminacion de una Foreign Key](#Eliminacion-de-una-Foreign-Key)
  - [Creacion de indices](#Creacion-de-indices)
  - [Eliminación de índices](#Eliminación-de-índices)
  - [Creación de índice único](#Creación-de-índice-único)
  - [Eliminación de índice único](#Eliminación-de-índice-único)
  - [Renombrar tabla](#Renombrar-tabla)
  - [Cambiar el modo de una tabla](#Cambiar-el-modo-de-una-tabla)
  - [Agregar una columna](#Agregar-una-columna)
  - [Eliminar una columna](#Eliminar-una-columna)
  - [Eliminar tabla](#Eliminar-tabla)
  - [Añadir registros](#Añadir-registros)
  - [Carga masiva de registros](#Carga-masiva-de-registros)
  - [Extraer un registro](#Extraer-un-registro)
  - [Actualizar registro](#Actualizar-registro)
  - [Eliminar registro](#Eliminar-registro)
  - [Eliminar todos los registros](#Eliminar-todos-los-registros)
  - [Calcular Checksum de base de datos](#Calcular-Checksum-de-base-de-datos)
  - [Calcular checksum de tabla](#Calcular-checksum-de-tabla)
  - [Compresión de base de datos](#Compresión-de-base-de-datos)
  - [Descompresion de base de datos](#Descompresion-de-base-de-datos)
  - [Compresion de tabla](#Compresion-de-tabla)
  - [Descompresion de tabla](#Descompresion-de-tabla)
  - [Cifrado de base de datos](#Cifrado-de-base-de-datos)
  - [Descifrado de base de datos](#Descifrado-de-base-de-datos)
  - [Activar modo seguro](#Activar-modo-seguro)
  - [Desactivar modo seguro](#Desactivar-modo-seguro)
  - [Diagrama de estructuras](#Diagrama-de-estructuras)
  - [Diagrama de dependencias](#Diagrama-de-dependencias)

- [Requerimientos del Sistema](#Requerimientos-del-Sistema)

## Alcances del proyecto

### Crear bases de datos
Cuando el servidor solicite la creación de una nueva bases de datos, se llamará al método [createDatabase](#createDatabase) ingresando el nombre que se desea para la base de datos, se verificará que la base de datos no exista aún, porque de existir se negará la solicitud y no se permitirá la creación hasta que se ingresé un nombre que todavía no exista en los registros, tambien se verifica el modo en que se desea crear esta base de datos y la codificacion, si alguna de estas es una entrada invalida se negara la creacion.

### Visualizar las bases de datos
Cuando el servidor solicite la visualización de todas las bases de datos, se llamará al método [showDatabases](#showDatabases) el cual regresará el listado de todas las bases de datos que se encuentran almacenadas.

### Renombrar la base de datos
Cuando el servidor solicite renombrar una base de datos, se llamará al método [alterDatabase](#alterDatabase) mediante el cual se solicitará el nombre que se desea cambiar para verificar si existe la base de datos y poder colocar el nuevo nombre.

### Eliminar base de datos
Cuando el servidor solicite eliminar una base de datos, se llamará al método [dropDatabase](#dropDatabase) mediante el cual se solicitará el nombre de la base de datos que se desea eliminar, si la base existe se eliminará sin ningún problema.

### Cambiar el modo de la base de Datos
Cuando el servidor solicite cambiar el modo de la base de datos, se llamará al método [alterDatabaseMode](#alterDatabaseMode) mediante el cual se procede a reestructurar la base de datos desde la forma que almacena las tablas hasta la estructura que tiene cada tabla para los registros actuales y las futuras inserciones.

### Cambiar la codificación
Cambia la codificacion que es aceptada por una base de datos, se llama al metodo [alterDatabaseEncoding](#alterDatabaseEncoding)

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

### Creacion de una Foreign Key
Agrega un índice de llave foránea, creando una estructura adicional con el modo indicado para la base de datos, se llamara al método [alterTableAddFK](#alterTableAddFK).

### Eliminacion de una Foreign Key
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada, se llamara al método [alterTableDropFK](#alterTableDropFK).

### Creacion de indices
Agrega un índice, creando una estructura adicional con el modo indicado para la base de datos, se llama al método [alterTableAddIndex](#alterTableAddIndex).

### Eliminación de índices
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada, se llama al método [alterTableDropIndex](#alterTableDropIndex).

### Creación de índice único
Agrega un índice único, creando una estructura adicional con el modo indicado para la base de datos, se llama al método [alterTableAddUnique](#alterTableAddUnique).

### Eliminación de índice único
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada, se llama al método [alterTableDropUnique](#alterTableDropUnique).

### Renombrar tabla
Cuando el servidor solicite renombrar una tabla se llamará al método [alterTable](#alterTable) mediante el cual se verificará si la tabla a la que se le desea cambiar el nombre existe, de ser así se modificará el nombre.

### Cambiar el modo de una tabla
Cuando el servidor solicite cambiar el modo de una tabla en especifico, se llamará al método [alterTableMode](#alterTableMode) mediante el cual se procede a hacer una copia de la base de datos y unicamente se inserta en esta la tabla especificada y todos sus registros se insertan de acuerdo al modo que se cambio.

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

### Calcular Checksum de base de datos
Genera un diggest a partir del contenido de la base de datos incluyendo sus tablas, se llama al método [checksumDatabase](#checksumDatabase).

### Calcular checksum de tabla
Genera un diggest a partir del contenido de la tabla de una base de datos, se llama al método [checksumTable](#checksumTable).

### Compresión de base de datos
Comprime una base de datos, se llama al metodo [alterDatabaseCompress](#alterDatabaseCompress).

### Descompresion de base de datos
Descomprime una base de datos, se llama al metodo [alterDatabaseDecompress](#alterDatabaseDecompress).

### Compresion de tabla
Comprime una tabla, se llama al metodo [alterTableCompress](#alterTableCompress).

### Descompresion de tabla
Descomprime una tabla, se llama al metodo [alterTableDecompress](#alterTableDecompress).

### Cifrado de base de datos
Cifra el texto backup con la llave password y devuelve el criptograma, se llama al metodo [encrypt](#encrypt).

### Descifrado de base de datos
Descifra el texto cipherBackup con la llave password y devuelve el texto plano, se llama al metodo [decrypt](#decrypt).

### Activar modo seguro
Activa el modo seguro para una tabla de una base de datos, se llama al metodo [safeModeOn](#safeModeOn).

### Desactivar modo seguro
Desactiva el modo seguro en la tabla especificada de la base de datos, se llama al metodo [safeModeOff](#safeModeOff).

### Diagrama de estructuras
Genera un gráfico mediante Graphviz acerca de la base de datos especificada, se llama al metodo [graphDSD](#graphDSD).

### Diagrama de dependencias
Genera un gráfico mediante Graphviz acerca de las dependencias funcionales de una tabla especificada de una base de datos. [graphDF](#graphDF).

## Requerimientos del Sistema
- Tener instalado la versión más reciente de python
- Tener instalado Graphviz


## Servidor

Las bases de datos del servidor son manejadas por el DBMS, en un archivo binario que almacena la información de cada base de datos como el nombre que se le asigna como identificador único, se recuperan las bases de datos y toda su informacion se almacena en 3 diccionarios.

Funciones CRUD de las bases de datos:

- [Creación de Bases de Datos "*createDatabase*"](#createDatabase)
- [Presentación de Bases de Datos "*showDatabases*"](#showDatabases)
- [Modificación de Bases de Datos "*alterDatabase*"](#alterDatabase)
- [Eliminación de Bases de Datos "*dropDatabase*"](#dropDatabase)

### createDatabase
```python
def createDatabase(database: str, mode: str, encoding: str) -> int:
```

Creación de base de datos. Método que recibe como parámetro `database` el nombre de la base de datos a crear, `mode` el modo en el que se creara la base de datos y sus respectivas tablas, `encoding` la codificación en la que se recibiran los datos de las tuplas. El flujo de este metodo comienza verificando la codificacion ingresada, de encontrarse en las posibles codificaciones se procede a verificar que el nombre de la base de datos no se encuentre en uso, de no estar en uso se procede a comparar el modo en el que se desea crear la base de datos, si este es uno de los 7 posibles se crea la base de datos con el paquete correspondiente.

#### Valores de Retorno:
- 0: Se ha creado la base de datos.
- 1: Error al crear la base de datos.
- 2: Nombre de base de datos se encuentra en uso.
- 3: Modo incorrecto.
- 4: Codificacion incorrecta.


### showDatabases
```python
def showDatabases() -> list:
```

Método utilizado en casi todos los métodos que presenta este DBMS, ya que con este comprobamos que las bases de datos que se quieran crear, editar o eliminar existan en el servidor. El flujo de este método recolecta los nombres de las bases de datos del diccionario y los almacena en una lista.

### alterDatabase
```python
def alterDatabase(databaseOld, databaseNew) -> int:
```

Modificación de base de datos. Método que renombra bases de datos tomando como parametros el nombre de la base de datos a modificar y el nuevo nombre de esta. El flujo de este método comienza verificando que el nombre de la base de datos antigua se encuentre en el diccionario de nombres de bases de datos y el nombre nuevo no se encuentre en el diccionario. Si esto se cumple se procede a verificar en que modo se encuentra la base de datos y con este modo modificar el nombre, se procede a copiar los datos de la base de datos a una nueva llave, se elimina la anterior del diccionario.

#### Valores de Retorno:
- 0: Se ha modificado la base de datos.
- 1: Error al modificar la base de datos.
- 2: Nombre de base de datos databaseOld no existente.
- 3: Nombre de base de datos databaseNew se encuentra en uso.

### dropDatabase
```python
def dropDatabase(database: str) -> int: 
```

Método que elimina la base de datos indicada en el parámetro `database`. El flujo de este parámetro comienza verificando que la base de datos se encuentre en el diccionario, procede a verificar el modo con el que se creo y con este metodo se procede a eliminar la base de datos, por ultimo se elimina de los diccionarios, y como ultimo paso se procede a guardar el diccionario con el método [commit](#commit).

#### Valores de Retorno:
- 0: Se ha eliminado la base de datos.
- 1: Error al eliminar la base de datos.
- 2: Base de datos no existente.


### alterDatabaseMode
```python
def alterDatabaseMode(database: str, mode: str) -> int:
```

Método que cambia el modo de almacenamiento de una base de datos completa por cualquier otro de los disponibles. El flujo de este método inicia verificando que la base de datos exista, se obtiene el nombre de esta con el parámetro database. Posteriormente verifica que el modo al que se quiere cambiar la base exista, este se obtiene del parámetro mode. Luego verifica que el la base de datos no se encuentre ya en el modo al que se quiere cambiar. Si cumple con las validaciones anteriores, se crea una base de datos con un nombre temporal en el modo que se solicita, se extraen todos los registros de todas las tablas y se crean nuevas tablas en la base de datos con el nombre temporal, insertando los registros extraídos, al finalizar se elimina la base de datos original y se renombre la de nombre temporal al de la original.

#### Valores de Retorno:
- 0: Se ha eliminado la base de datos.
- 1: Error al eliminar la base de datos.
- 2: Base de datos no existente.


### alterDatabaseEncoding
```python
def alterDatabaseEncoding(database: str, encoding: str) -> int:
```

Metodo que cambia la modificacion aceptada para el registro de datos en una base de datos. El flujo de este metodo comienza verificando que la codificacion ingresada sea correcta, continua verificando que la base de datos no tenga ya definida esta codificacion, si todo esto es correcto continua haciendo una copia de las tablas, y los registros de la tablas en diccionario, conforme se hacen las copias se codifica de la codificacion original a bytes la informacion y se decodifican de bytes a la nueva codificacion, si existe algun problema o caracter no soportado se terminara el proceso, si todo se logra convertir se procede a limpiar los registros de la tabla y por ultimo se registran todos los datos nuevamente. Se cambia la codificacion asociada a la base de datos en el diccionario respectivo y se guarda la informacion con el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha modificado la codificacion.
- 1: Error al modificar.
- 2: Base de datos no existente.
- 3: Nombre de codificacion no existente.


## Bases de Datos
Las tablas de las bases de datos son manejadas por el DBMS, en archivos binarios uno por cada tabla, que almacenan la información de estas, llevando por nombre la concatenación del nombre de la base de datos a la que pertenecen y el identificador único de estas.

Funciones CRUD de las tablas:

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

Método que crea una tabla tomando como nombre el parámetro `table`, definiendo el número de columnas de esta con el parámetro `numberColumns`, en la base de datos especificada en el parámetro `database`. El flujo de este método comienza verificando que la base de datos se encuentre en el diccionario, que la tabla no se encuentre en el diccionario de la base de datos, se guardara la informacion en el diccionario, en un archivo binario que llevara por nombre la concatenación del nombre de la base de datos a la que pertenece y su nombre también haciendo uso de [commit](#commit).

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


### alterTableMode
```python
def alterTableMode(database: str, table: str, mode: str) -> int:
```

Método que cambia el modo de almacenamiento de una tabla especifica por cualquier otro de los disponibles. El flujo de este método inicia verificando que la base de datos exista, se obtiene el nombre de esta con el parámetro database. Seguido de esto, verifica que la tabla que se envía en el parámetro table exista. Posteriormente verifica que el modo al que se quiere cambiar la base exista, este se obtiene del parámetro mode. Si cumple con las validaciones anteriores, se extraen todos los registros de la tabla, se obtiene el numero de columnas que tiene la tabla y la llave primaria si la tiene, luego se elimina la tabla original, se crea la tabla en el modo requerido con las características que se recuperaron anteriormente y se le ingresan los registros extraídos.

#### Valores de Retorno:
- 0: Se ha eliminado la base de datos.
- 1: Error al eliminar la base de datos.
- 2: Base de datos no existente.


### dropTable
```python
def dropTable(database: str, table: str) -> int: 
```

Método que elimina la tabla `table` de la base de datos `database`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a eliminar esta con todos sus registros, para confirmar la eliminacion elimina el archivo que contenia los registros de la tabla, y se guarda la base de datos actualizada con [commit](#commit).


## Tablas
- [Definición de llave primaria "*alterAddPK*"](#alterAddPK)
- [Eliminación de llave primaria "*alterDropPK*"](#alterDropPK)
- [Definición de llave foranea "*alterTableAddFK*"](#alterTableAddFK)
- [Eliminación de llave foranea "*alterTableDropFK*"](#alterTableDropFK)
- [Definición de índice único "*alterTableAddUnique*"](#alterTableAddUnique)
- [Eliminación de índice único "*alterTableDropUnique*"](#alterTableDropUnique)
- [Definición de índice "*alterTableAddIndex*"](#alterTableAddIndex)
- [Eliminación de índice "*alterTableDropIndex*"](#alterTableDropIndex)
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

### alterTableAddFK
```python 
def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list) -> int:
```

Método que vincula una llave foránea en la tabla `table` en la base de datos `database` y utilizando la tabla de referencia `tableRef` para las llaves primarias, almacenando las referencias de `tableRef` en un nuevo archivo y manejando como metadato `indexName` para poder encontrarlo más rápido. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` y `tableRef` se encuentran en esta lista se procederá a verificar la integridad referencial dentro de `tableRef`, si se cumple la integridad se procede a crear el nuevo metadato y la nueva estructura donde se almacenará la tabla de referencia, posteriormente para actualizar los atributos de la tabla se utiliza el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha vinculado la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Cantidad no exacta entre columns y columnsRef.
- 5: No se cumple la integridad referencial

### alterTableDropFK
```python 
def alterTableDropFK(database: str, table: str, indexName: str) -> int:
```

Método que desvincula una llave foránea en la tabla `table` en la base de datos `database`, mediante el atributo `indexName` se procede a buscar si el metadato existe al igual que la estructura que almacena las referencias. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` y `tableRef` se encuentra en esta lista se procederá buscar el `indexName` dentro de los metadatos de la tabla, de ser así se procede a eliminar tanto el metadato como la estructura que almacena las referencias, posteriormente para actualizar los atributos de la tabla se utiliza el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha eliminado la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Nombre de índice no existente.

### alterTableAddUnique
```python 
def alterTableAddUnique(database: str, table: str, indexName: str, columns: list) -> int:
```

Método que vincula un índice único en la tabla `table` en la base de datos `database`, manejando como metadato `indexName` para poder encontrarlo más rápido y creando una estructura donde se almacena las columnas que pertenecen al índice. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a verificar la integridad referencial dentro de `table`, si se cumple la integridad se procede a crear el nuevo metadato y la nueva estructura donde se almacenarán las columnas que forman parte del índice, posteriormente para actualizar los atributos de la tabla se utiliza el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha vinculado el índice.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Cantidad no exacta entre columns y columnsRef.
- 5: No se cumple la integridad referencial

### alterTableDropUnique
```python 
def alterTableDropUnique(database: str, table: str, indexName: str) -> int:
```

Método que elimina el índice único en la tabla `table` en la base de datos `database`, buscando como metadato de la tabla el atributo `indexName`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a verificar si existe el metadato dentro de la tabla, de ser así se eliminará tanto metadato como la estructura donde se almacenan las columnas que forman parte del índice, posteriormente para actualizar los atributos de la tabla se utiliza el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha eliminado el índice.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Nombre de índice no existente.

### alterTableAddIndex
```python 
def alterTableAddIndex(database: str, table: str, indexName: str, columns: list) -> int:
```

Método que vincula un índice en la tabla `table` en la base de datos `database`, manejando como metadato `indexName` para poder encontrarlo más rápido y creando una estructura donde se almacena las columnas que pertenecen al índice. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista, se procede a crear el nuevo metadato y una nueva estructura donde se almacenarán las columnas que forman parte del índice, posteriormente para actualizar los atributos de la tabla se utiliza el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha vinculado el índice.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Cantidad no exacta entre columns y columnsRef.

### alterTableDropIndex
```python 
def alterTableDropIndex(database: str, table: str, indexName: str) -> int:
```

Método que elimina el índice vinculado a la tabla `table` en la base de datos `database`, buscando como metadato de la tabla el atributo `indexName`. El flujo de este método comienza con el método [initCheck](#initCheck), se extrae la lista de bases de datos del servidor con el método [rollback](#rollback) guardando esto en una lista temporal y el método retorna una lista con los nombres de las bases de datos existentes, se comprueba que exista `database`, de existir se procede a buscar las tablas asociadas a esta base de datos con el método [rollback](#rollback), se retorna una lista con los nombres de las tablas, si `table` se encuentra en esta lista se procederá a verificar si existe el metadato dentro de la tabla, de ser así se eliminará tanto metadato como la estructura donde se almacenan las columnas que forman parte del índice, posteriormente para actualizar los atributos de la tabla se utiliza el metodo [commit](#commit).

#### Valores de Retorno:
- 0: Se ha eliminado el índice.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Nombre de índice no existente.

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


### encrypt
```python
def encrypt(backup: str, password: str) -> str:
```

Método que encripta un texto con una contraseña específica. El flujo de este método inicia generando una llave con el algoritmo SH256, utilizando el parámetro password, para posteriormente crear una llave con el método Fernet de la librería cryptography, esta se le envía al método encrypt de la misma librería, el cual encripta el texto del parámetro backup.

#### Valores de Retorno:
- Archivo cifrado: exitosa.
- None: hay error

### decrypt
```python
def encrypt(backup: str, password: str) -> str:
```

Método que desencripta un texto con una contraseña específica. El flujo de este método inicia generando una llave con el algoritmo SH256, utilizando el parámetro password, para posteriormente crear una llave con el método Fernet de la librería cryptography, esta se le envía al método decrypt de la misma librería, el cual desencripta el texto del parámetro cipherBackup.

#### Valores de Retorno:
- Archivo cifrado: exitosa.
- None: hay error

### safeModeOn
```python
def safeModeOn(database: str, table: str): -> int
```

Activa la bandera de modo seguro de la tabla especificada. El flujo de este método es volver verdadero un booleano llamado safeMode y posteriormente crea un archivo json con el nombre de la base de datos y tabla especificada.

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Modo seguro existente.

### safeModeOff
```python
def safeModeOff(database: str, table: str): -> int
```

Desactiva la bandera de modo seguro de la tabla especificada. El flujo de este método es volver falso un booleano llamado safeMode y posteriormente elimina el archivo json con el nombre de la base de datos y tabla especificada.

#### Valores de Retorno:
- 0: Se ha definido la llave.
- 1: Error en la operación.
- 2: Base de datos no existente.
- 3: Tabla no existente.
- 4: Modo seguro no existente.


### loadCSV
```python
def loadCSV(file: str, database: str, table: str) -> list:
```

Método que lee todos los registros en el archivo `file` y los inserta en la tabla `table` en la base de datos `database`. El flujo de este método con declarar una lista para almacenar los registros que se inserten a la tabla, con la función open de la librería de archivos csv leemos todas las líneas del archivo `file` y se agregan a una lista auxiliar. Se recorren todos los registros que tiene la lista auxiliar, en cada iteración del recorrido de la lista auxiliar se insertan los registros a la tabla `table` utilizando el metodo [insert](#insert) con los datos de cada fila como parametros, si se insertan sin conflicto los registros se añaden a la lista principal del método, al terminar de leer el archivo se retorna la lista con los registros que se insertaron exitosamente. Si existe algún error o el archivo se encuentra vacío se retornara una lista vacía.

### graphDSD
```python
def graphDSD(database: str) -> str:
```
Genera el diagrama de estructura de datos de `database`. El flujo de este método es verificar que `database` exista dentro del registro de las bases de datos, de ser así, se procede a verificar todos los vinculos que poseen entre sí todas las tablas registradas dentro de la base de datos, posteriormente se genera un archivo .DOT y un archivo .PNG para poder visualizar el diagrama generado.

#### Valores de Retorno:
- Archivo en formato Graphviz para dibujar.
- None: Si hay un error.

### graphDF
```python
def graphDF(database: str, table: str) -> str:
```
Genera el diagrama de dependencias de una tabla ubicada dentro de una base de datos. El flujo de este método es verificar que `database` exista dentro del registro de las bases de datos, de ser así, se verifica que `table` exista dentro del registro de tablas, de ser así, se procede a verificar las dependencias que poseen las columnas entre sí, luego se procede a generar el archivo .DOT y un archivo .PNG donde se podrá visualizar el diagrama generado.

#### Valores de Retorno:
- Archivo en formato Graphviz para dibujar.
- None: Si hay un error.
