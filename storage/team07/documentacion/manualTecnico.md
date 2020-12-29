


### Universidad de San Carlos de Guatemala
### Facultad de Ingeniería
### Laboratorio de Estructuras de Datos

# MANUAL DE TECNICO

# METODOS Y FUNCIONES
#### createDatabase(database: str): Metodo que nos permite crear una base de datos
#### showDatabases(): Metodo que nos permite ver todas las base de datos creadas
#### alterDatabase(databaseOld, databaseNew): Metodo que nos permite modificar una base de datos teniendo como parametro el nombre antiguo con el valor nuevo
#### dropDatabase(database): Metodo que permite eliminar la base de datos buscada 
#### createTable(database, table, numberColumns): Metodo que te permite crear una tabla con parametro de a que base de datos se agregara, el nombre de la tabla y numero de columnas
#### showTables(database): Metodo que nos permite ver todas las tablas ingresadas.
#### dropTable(database, table): Metodo que nos permite eliminar una tabla con parametro la base de datos en la cual esta la tabla y el nombre de la tabla.
#### alterTable(database, tableOld, tableNew): Metodo que nos permite modificar el nombre de la tabla.
#### insert(database, table, register): Metodo que nos permite ingresar valores a una tabla.
#### alterAddPK(database, table, columns): Metodo que nos permite modificar los valores insertados en la tablas.
#### extractTable(database, table): Metodo que nos retorna los valores de la tabla.
#### truncate(database, table): Metodo que nos eliminara todos los registros de la tabla
