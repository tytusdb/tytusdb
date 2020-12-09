# -EDD-ProyectoF1
## Estructura de las tablas (Tablas hash). (Welmann Paniagua)
  - createDatabase(mode, database): crea una base de datos con cierto número de modo de almacenamiento (mode=1, 2, 3, 4, 5).
  - showDatabases(): devuelve una lista de los nombres de las bases de datos, el nombre es único.
  - alterDatabase(databaseOld, databaseNew): cambia el nombre de una base de datos.
  - dropDatabase(database): elimina por completo la base de datos indicada.

## Estructura de las bases de datos. (Alejandra Navarro) (Pablo Rivas)
- createTable(database, tableName, numberColumns): crea una tabla según el modo de almacenamiento, la base de datos debe de existir, y solo se define el número de columnas.
- showTables(database): devuelve una lista de los nombre de las tablas de una base de datos, los nombre de tablas son únicos.
- alterTable(database, tableOld, tableNew): cambia el nombre de una tabla de una base de datos.
- dropTable(database, tableName): elimina por completo la tabla indicada.
- alterAdd(database, tableName, columnName): agrega una columna a cada registro de la tabla.
- alterDrop(database, tableName, columnNumber): elimina una n-esima columna de cada registro de la tabla.
- extractTable(database, table): extrae y devuelve en una lista de listas el contenido de la tabla.
	 
## Estructura de la lista de bases de datos. (Fercho) 
- insert(database, table, columns): inserta un registro en la estructura de datos persistente, database es el nombre de la base de datos, table es el nombre de la tabla y columns es una lista de campos a insertar. Devuelve un True si no hubo problema, y un False si no se logró insertar.
- update(database, table, id, columnNumber, value): actualiza el valor de una columna x en un registro id de una tabla de una base de datos. Devuelve True si se actualizó correctamente y False si no se logró actualizar.
- deleteTable(database, tableName, id): elimina un nodo o elemento de página indicado de una tabla y base de datos especificada.
- truncate(database, tableName): vacía la tabla de todos los registros.
- extractRow(database, table, id): extrae y devuelve una tupla especificada
      -Adicional se deberá implementar desde aquí todas las funciones, solo llamándolas y pasándole los parámetros
## Esta función solo es de llamar las funciones add y hacer las comprobaciones para crear la base o tabla. (Fercho)
- loadCSV(filecsv, database, table, [modo]): carga un archivo csv de un ruta especificada indicando la ruta de la base de datos y en qué tabla será guardada. Si la tabla existe verifica la cantidad de columnas, si no corresponde da error. Si la tabla no existe, la crea. Si la base de datos no existe, la crea con el modo especificado.
 
## Reportes
Cada estructura tendrá su propio método para auto-graficarse, Pablo será el encargado de llamar estos métodos para ir mostrando la estructuración. (Pablo Rivas)
## Manuales. 
Todos aportaremos para el manual, sin embargo, me gustaría que alguno se encargara de darle un bonito diseño (Fercho).
