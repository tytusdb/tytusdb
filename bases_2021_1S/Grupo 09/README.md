# Proyecto De Clase  
---
## Integración De Tytus DB
----
#### **Requerimientos Previos A La Instalación**

Se necesitan las siguientes dependencias y librerias para el correcto funcionamiento del programa
+ certifi Versión 2020.12.5
+ chardet Versión 4.0.0
+ click Versión 7.1.2
+ Flask Versión 1.1.2
+ Flask-Cors Versión 3.0.10
+ graphviz Versión 0.16
+ idna Versión 2.10
+ itsdangerous Versión 1.1.0
+ Jinja2 Versión 2.11.3
+ MarkupSafe Versión 1.1.1
+ numpy Versión 1.20.2
+ pandas Versión 1.2.4
+ ply Versión 3.11
+ prettytable Versión 2.1.0
+ python-dateutil Versión 2.8.1
+ pytz Versión 2021.1
+ requests Versión 2.25.1
+ six Versión 1.15.0
+ urllib3 Versión 1.26.4
+ wcwidth Versión 0.2.5
+ Werkzeug Versión 1.0.1

#### **Proceso De Instalación**
----
Para optimizar la instalación de todas las dependencias y librerias que se mencionaron con anterioridad, ejecutar los servidores y aplicaciones se generó un archivo install.exe el cual unicamente hay que ejecutar y seguir los pasos que se indican dentro del instalador con el fin de instalar y ejecutar Tytus DB,
al clickear el archivo install.exe se desplegara una terminal la cual al finalizar el proceso se cierra automaticamente, este proceso crea 
una carpeta en el disco local C llamada Tytus, dentro de esta existe otra carpeta llamada Ejecutable y dentro el archivo Tytus.exe
el cual hay que clickear para ejecutar la aplicación.  

## Arquitectura Utilizada En Tytus DB
----
#### Cliente Y Servidor
----
Para el cliente y servidor se utilizo el proyecto del grupo no.5 fase II del cual su documentacion se encuentra en los siguientes enlaces

- [Manual Técnico y De Usuario (Cliente)](<Tytus/Clienteteam05/README.md>)
- [Manual Técnico y De Usuario (Servidor)](<Tytus/Serverteam05/README.md>)

### Observaciones

#### SERVER 

http://localhost:8887/Tytus/prueba	Tipo GET
Retorna un Json con un Mensage de conectado
http://localhost:8887/Tytus/parser	Tipo POST
Obtiene el Json Enviado desde el Cliente y lo Envia al Parser para realizar el analisis	
http://localhost:8887/Tytus/consultar	Tipo POST
Obtiene el Json Enviado desde el Cliente y lo Envia al Parser para realizar la consulta
http://localhost:8887/Tytus/EDD/reportTBL	Tipo POST
Obtiene el Json Enviado desde el Cliente y lo Envia al Storage para Obtener el Grafico
http://localhost:8887/Tytus/EDD/reportDB	Tipo POST
Obtiene el Json Enviado desde el Cliente y lo Envia al Storage para Obtener el Grafico
http://localhost:8887/Tytus/EDD/reportAVL	Tipo POST
Obtiene el Json Enviado desde el Cliente y lo Envia al Storage para Obtener el Grafico
http://localhost:8887/Tytus/EDD/reportTPL	Tipo POST
Obtiene el Json Enviado desde el Cliente y lo Envia al Storage para Obtener el Grafico
http://localhost:8887/Tytus/SHTABLE	Tipo POST
Obtiene el Json Enviado desde el Cliente y lo Envia al Storage para Obtener el listado de tablas en una base de datos

#### CLIENTE

Consideraciones:

- Se debe Seleccionar El query que se desea analizar previo a Presionar el boton de Run Script

- Para los reportes se debe de asegurar que los parametros ingresados sean los correctos

#### Query Tool
----
Para la parte de analisis se utilizo el proyecto del grupo no.29 fase I del cual su documentación se encuentra en los siguientes enlaces:

- [Manual Técnico](<Tytus/Query Tool/team29/docs/Manual Tecnico/ManualTecnico.md>)
- [Manual Del Usuario](<Tytus/Query Tool/team29/docs/Manual de Usuario/ManualUsuario.md>)
- [Gramática Ascendente](<Tytus/Query Tool/team29/docs/Gramáticas/GramaticaAscendente.md>)
- [Gramática Descendente](<Tytus/Query Tool/team29/docs/Gramáticas/GramaticaDescendente.md>)

### Observaciones

Sintaxis Permitida

[ Valor ] = Puede O No Venir

Bases De Datos 

Create Data Base 

Los parametros owner, if not exists y mode se puede definir en la sintaxis pero aun no esta implementado en el storage

		create [or replace] database [if not exists] name
		[owner = user]
		[mode = number_mode]
		
Show Data Bases
		
Ejemplo De Regex = '%Id%'
		
		show databases [like regex] 
		
Alter Data Base 	

La funcion alter se puede definir en la sintaxis pero aun no esta implementada en el storage

		alter database name rename to new_name
		
		alter database name owner to { new_owner || current_user || session_user } 
		
Drop Data Base 

		drop database [if exist] name 	
		
Use Data Base 

		use name
	
Tablas 

Create Table 

El parametro check se pueden definir en la sintaxis pero aun no esta implementado en el storage 

		create my_first_table (
		
			column1 type [default value] [[not] null] [[constraint name] unique] [[constraint name] check (condition_column1)]
			[, column2...]
			[, [constraint name] check (condition_many_columns)...]
			[, unique (column1 [, column2]...)]
		
		);	
		
		create table my_first_table (
		
			column1 type [primary key]
			[, column2 type [references table]]
			[, column3...]
		
		);
		
		create table my_first_table (
		
			column1 type
			[, column2...]
			[, [primary key (column1,..., column_n)]]
			[, [foreign key (column1,..., column_n) references table (column1_other,..., column_n_other)]]
		
		);
		
Drop Table
	
		drop table my_first_table;
		
Alter Table 

La funcion drop, add check, add constraint, add foreign key,
alter column set, drop constraint, rename column
se puede definir en la sintaxis pero aun no estan implmentadas en el storage

		alter table name_table add column column_name type;
		alter table name_table drop column column_name;		
		alter table table add check (name <> '');
		alter table table add constraint some_name unique (column);
		alter table table add foreign key (column_group_id) references column_groups;
		alter table table alter column column set not null;
		alter table table drop constraint some_name;
		alter table table rename column column1 to column1_1;	
		
Delete 

La funcion delete se puede definir en la sintaxis pero aun no esta implementada en el storage
		
		delete from [ only ] table_name [ * ] [ [ as ] alias ]
		[ using from_item [, ...] ]
		[ where condition | where current of cursor_name ]
		[ returning * | output_expression [ [ as ] output_name ] [, ...] ]	
		
Inheritance
	
La funcion inherits se puede definir en la sintaxis pero aun no esta implementada en el storage
	
		create table cities (
			name            text,
			population      float,
			elevation       int     -- in feet
		);

		create table capitals (
			state           char(2)
		) inherits (cities);
	
Insert 

		insert into products values (1, 'Cheese', 9.99);
		
Update 
	
La funcion update se puede definir en la sintaxis pero aun no esta implementada en el storage (Bug Storage)
	
		update products set price = 10 where price = 5;
		
Delete 

La funcion delete se puede definir en la sintaxis pero aun no esta implementada en el storage
		
		delete from products where price = 10;
		
Select 

La funcion select se puede definir en la sintaxis y esta implementada en el storage sin embargo, la forma en la que esta implementada en la sintaxis no permite integrarlo con el storage

		select [distinct] select_list from table_expression 
		[where search_condition] 
		[group by grouping_column_reference [, grouping_column_reference]...]

#### Storage
----
Para la parte de almacenamiento se utilizo el proyecto del grupo no.16 fase I del cual su documentación se encuentra en el siguiente enlace

- [Manual Técnico y De Usuario](<Tytus/Storage/team16/README.md>)

### Observaciones

Rutas Permitidas Para Storage Server

http://localhost:9998/Tytus/prueba Tipo GET

http://localhost:9998/DB/CreateDB	Tipo POST
	Recibe un json con nameDB como atributo el cual contendra el nombre de la base de datos a crear

http://localhost:9998/DB/showDatabase	Tipo GET
	Retorna el listado de bases de datos creadas

http://localhost:9998/DB/alterDatabase	Tipo POST
	Recibe un json con nameDBold,nameDBnew que contendra el nombre de la base de datos a alterar

http://localhost:9998/DB/dropDatabase	Tipo POST
	Recibe un json con nameDB como atributo el cual contendra el nombre de la base de datos a eliminar

http://localhost:9998/TABLE/createTable	Tipo POST
	Recibe un Json con nameDB,nameTab y numCol los cuales son nombre de la base de datos, nombre de la tabla y el numero de columnas

http://localhost:9998/TABLE/showTables	Tipo POST
	Recibe un Json con nameDB el cual es el nombre de la base de datos

http://localhost:9998/TABLE/extractTable	Tipo POST
	Recibe un Json con nameDB,nameTab los cuales son nombre de la base de datos y nombre de la tabla que se extraeran

http://localhost:9998/TABLE/extractRangeTable	Tipo POST
	Recibe un Json con nameDB,nameTab,numCol,lower,upper los cuales son nombre de la base de datos, nombre de la tabla que se extraeran, numero de columna,
	valor mas bajo y valor mas alto

http://localhost:9998/TABLE/alterAddPK	Tipo POST
	Recibe un Json con nameDB, nameTab, columns los cuales son el nombre de la base de datos, nombre de la tabla y las columnas

http://localhost:9998/TABLE/alterDropPK	Tipo POST
	Recibe un Json con nameDB, nameTab los cuales son el nombre de la base de datos y nombre de la tabla

http://localhost:9998/TABLE/alterAddFK	Tipo POST
	Recibe un Json con nameDB, nameTab,references los cuales son el nombre de la base de datos, nombre de la tabla y una referencia

http://localhost:9998/TABLE/alterAddIndex	Tipo POST
	Recibe un Json con nameDB, nameTab,references los cuales son el nombre de la base de datos, nombre de la tabla y una referencia

http://localhost:9998/TABLE/alterTable	Tipo POST
	Recibe un Json con nameDB, nameTabOld, nameTabnew references los cuales son el nombre de la base de datos, nombre de la tabla antigua y nombre de la tabla nueva

http://localhost:9998/TABLE/alterAddColumn	Tipo POST
	Recibe un Json con nameDB, nameTab, default los cuales son el nombre de la base de datos, nombre de la tabla y una valor por defecto

http://localhost:9998/TABLE/alterDropColumn	Tipo POST
	Recibe un Json con nameDB,nameTab y numCol los cuales son nombre de la base de datos, nombre de la tabla y el numero de columnas

http://localhost:9998/TABLE/dropTable	Tipo POST
	Recibe un Json con nameDB, nameTab los cuales son el nombre de la base de datos y nombre de la tabla

http://localhost:9998/TUPLA/insert	Tipo POST
	Recibe un Json con nameDB, nameTab,registrer los cuales son el nombre de la base de datos, nombre de la tabla y los valores que se insertaran

http://localhost:9998/TUPLA/loadCSV	Tipo POST
	Recibe un Json con file,nameDB, nameTab, registrer los cuales son el archivo, nombre de la base de datos y nombre de la tabla

http://localhost:9998/TUPLA/extractRow	Tipo POST
	Recibe un Json con nameDB, nameTab, columns los cuales son el nombre de la base de datos, nombre de la tabla y las columnas

http://localhost:9998/TUPLA/update	Tipo POST
	Recibe un Json con nameDB, nameTab,registrer,columns los cuales son el nombre de la base de datos, nombre de la tabla , los valores que se insertaran y la columna que se alterara

http://localhost:9998/TUPLA/delete	Tipo POST
	Recibe un Json con nameDB, nameTab, columns los cuales son el nombre de la base de datos, nombre de la tabla y las columnas

http://localhost:9998/TUPLA/truncate	Tipo POST
	Recibe un Json con nameDB,nameTab los cuales son nombre de la base de datos y nombre de la tabla

http://localhost:9998/REP/reportTBL	Tipo POST
	Recibe un Json con nameDB con el nombre de la base de datos a graficar

http://localhost:9998/REP/reportDB	Tipo POST
	No recibe ningun Json unicamente retorna la grafica de las bases de datos

http://localhost:9998/REP/reportAVL	Tipo POST
	Recibe un Json con nameDB,nameTab los cuales son nombre de la base de datos y nombre de la tabla a graficar

http://localhost:9998/REP/reportTPL	Tipo POST
	Recibe un Json con nameDB,nameTab,llave los cuales son nombre de la base de datos, nombre de la tabla y llave de la tupla a graficar

