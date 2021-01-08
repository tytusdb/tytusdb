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
  - [Cambiar el modo de la base de Datos](#Cambiar-el-modo-de-la-base-de-Datos)
  - [Cambiar el modo de una tabla](#Cambiar-el-modo-de-una-tabla)
  - [Creacion de una Foreign Key](#Creacion-de-una-Foreign-Key)
  - [Eliminacion de una Foreign Key](#Eliminacion-de-una-Foreign-Key)
  - [Creación de índice único](#Creación-de-índice-único)
  - [Eliminación de índice único](#Eliminación-de-índice-único)
  - [Creacion de indices](#Creacion-de-indices)
  - [Eliminación de índices](#Eliminación-de-índices)
  - [Cambiar la codificación](#Cambiar-la-codificación)
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

### Cambiar el modo de la base de Datos
Cuando el servidor solicite cambiar el modo de la base de datos, se llamará al método [alterDatabaseMode](#alterDatabaseMode) mediante el cual se procede a reestructurar la base de datos desde la forma que almacena las tablas hasta la estructura que tiene cada tabla para los registros actuales y las futuras inserciones.

### Cambiar el modo de una tabla
Cuando el servidor solicite cambiar el modo de una tabla en especifico, se llamará al método [alterTableMode](#alterTableMode) mediante el cual se procede a hacer una copia de la base de datos y unicamente se inserta en esta la tabla especificada y todos sus registros se insertan de acuerdo al modo que se cambio.

### Creacion de una Foreign Key
Agrega un índice de llave foránea, creando una estructura adicional con el modo indicado para la base de datos, se llamara al método [alterTableAddFK](#alterTableAddFK).

### Eliminacion de una Foreign Key
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada, se llamara al método [alterTableDropFK](#alterTableDropFK).

### Creación de índice único
Agrega un índice único, creando una estructura adicional con el modo indicado para la base de datos, se llama al método [alterTableAddUnique](#alterTableAddUnique).

### Eliminación de índice único
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada, se llama al método [alterTableDropUnique](#alterTableDropUnique).

### Creacion de indices
Agrega un índice, creando una estructura adicional con el modo indicado para la base de datos, se llama al método [alterTableAddIndex](#alterTableAddIndex).

### Eliminación de índices
Destruye el índice tanto como metadato de la tabla como la estructura adicional creada, se llama al método [alterTableDropIndex](#alterTableDropIndex).

### Cambiar la codificación
Cambia la codificacion que es aceptada por una base de datos, se llama al metodo [alterDatabaseEncoding](#alterDatabaseEncoding)

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

## Bases de Datos
Las tablas de las bases de datos son manejadas por el DBMS, en archivos binarios uno por cada tabla, que almacenan la información de estas, llevando por nombre la concatenación del nombre de la base de datos a la que pertenecen y el identificador único de estas.

Funciones CRUD de las tablas:

- [Creación de tablas "*createTable*"](#createTable)
- [Presentación de tablas "*showTables*"](#showTables)
- [Presentación de datos de tablas "*extractTable*"](#extractTable)
- [Presentación de datos de tablas según rango definido "*extractRangeTable*"](#extractRangeTable)
- [Modificación de tablas "*alterTable*"](#alterTable)
- [Eliminación de tablas "*dropTable*"](#dropTable)
