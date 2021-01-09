# __Manual de usuario__

## Introducción
El siguiente manual tiene como fin introducir al usuario al manejo y conocimiento de TytusDB para su uso funcional.  

### __TytusDB__
TytusDB es un administrador de bases de datos, el cual está compuesto en este caso por un administrador de almacenamiento y una interfaz gráfica para el manejo de operaciones y reportes.

El software desarrollado cuenta con dos distintas ventanas de opciones para que el usuario pueda interactuar y hacer uso de la misma, las cuales se detallan más adelante.
<br>

### Requerimientos del sistema
Cualquier computadora funcional en el que se pueda ejecutar archivos '.exe' y tener una versión del intérprete de Python instalada. Se recomienda Python 3.
<br><br>

## Menú principal
<hr>
<div align="center" alt="Menu">
  <img src="img/Menu.png" />
</div>
En ella el usuario puede acceder a las funcionalidades básicas de la aplicación, tales como las operaciones entre bases de datos, los repores gráficos y salir del sistema.

<br><br>

## Funciones
<hr>
<div align="center" alt="Funciones">
  <img src="img/Funciones.png" />
</div>
Es la primera ventana que ofrece todas operaciones que se pueden realizar entre las bases de datos, sus tablas pertenecientes y los registros que conforman cada tabla.
<br><br>

+ ### __Bases de datos:__
   - Create database:  
   Crea una base de datos nueva. Recibe el nombre con el que se identificará la base de datos.
    <div align="center">
    <img src="img/CreateDB.png"/>
    </div>
    <br>

    - Show databases:  
    Devuelve una lista de los nombres de las bases de datos existentes.
    <br><br>

    - Alter database:  
    Renombra la base de datos databaseOld por databaseNew.
    <div align="center">
    <img src="img/AlterDB.png"/>
    </div>
    <br>
    
    - Drop database:  
    Elimina por completo la base de datos indicada en database.
    <div align="center">
    <img src="img/DropDB.png"/>
    </div>
    <br>

    - Format DMS:  
    Elimina por completo todo la información almacenada en el administrador de base de datos.

    <br>

+ ### __Tablas:__
    - Create table:  
    Crea una tabla en una base de datos especificada recibiendo el nombre de la base de datos a la que pertenece, el nombre de la tabla, y una lista de índices referentes a la llave primaria.
    <div align="center">
    <img src="img/CreateTBL.png"/>
    </div>
    <br>

    - Show tables:  
    Devuelve una lista de los nombres de las tablas de la base de datos que se solicita.
    <div align="center">
    <img src="img/ShowTBL.png"/>
    </div>
    <br>

    - Extract table:  
    Extrae y devuelve una lista con elementos que corresponden a cada registro de la tabla y base de datos en cuestión.
    <div align="center">
    <img src="img/ExtractTBL.png"/>
    </div>
    <br>

    - Extract range table:  
    Extrae y devuelve una lista con los elementos que corresponden a un rango de registros de la tabla.
    Upper y lower corresponden a los límites superior e inferior del rango a extraer de la columna indicada de la tabla.
    <div align="center">
    <img src="img/ExtractRange.png"/>
    </div>
    <br>

    - Alter add PK:  
    Asocia a la tabla una llave primaria simple o compuesta mediante la lista de número de columnas, esto para anticipar el índice de la estructura de la tabla cuando se inserten registros a la tabla de una base de datos.
    <div align="center">
    <img src="img/AddPK.png"/>
    </div>
    <br>

    - Alter drop PK:  
    Elimina la llave(s) primaria actual en la información de la tabla de una base de datos.
    <div align="center">
    <img src="img/DropPK.png"/>
    </div>
    <br>

    - Alter table:  
    Renombra el nombre de la tabla de una base de datos especificada.
    <div align="center">
    <img src="img/AlterTBL.png"/>
    </div>
    <br>

    - Alter add column:  
    Agrega una columna al final de cada registro de la tabla y base de datos especificada.
    <div align="center">
    <img src="img/AddColumn.png"/>
    </div>
    <br>

    - Alter drop column:  
    Eliminar una n-ésima columna de cada registro de la tabla de una base de datos, excepto si son llaves primarias.
    <div align="center">
    <img src="img/DropColumn.png"/>
    </div>
    <br>

    - Drop table:  
    Elimina por completo una tabla de una base de datos especificada.
    <div align="center">
    <img src="img/DropTBL.png"/>
    </div>
    <br>

+ ### __Tuplas:__
    - Insert:  
    Inserta un registro en la estructura de datos asociada a la tabla y la base de datos.
    <div align="center">
    <img src="img/Insert.png"/>
    </div>
    <br>

    - Load CSV:  
    Carga un archivo CSV de una ruta especificada indicando la base de datos y tabla donde será almacenado. La base de datos y la tabla deben existir, y coincidir con el número de columnas. Si hay llaves primarias duplicadas se ignorarán. No se utilizan títulos de columnas y la separación es mediante comas (',').
    <div align="center">
    <img src="img/LoadCSV.png"/>
    </div>
    <br>

    - Extract row:  
    Extrae y devuelve una lista de un registro especificado por su llave primaria de una tabla perteneciente a una base de datos especificada.
    <div align="center">
    <img src="img/ExtractRow.png"/>
    </div>
    <br>

    - Update:  
    Actualiza un registro de acuerdo a la llave primaria en la estructura de datos asociada a la tabla y la base de datos.
    <div align="center">
    <img src="img/Update.png"/>
    </div>
    <br>

    - Delete:  
    Elimina un registro de una tabla y base de datos especificados por la llave primaria.
    <div align="center">
    <img src="img/Delete.png"/>
    </div>
    <br>

    - Truncate:  
    Elimina todos los registros de una tabla y base de datos existente.
    <div align="center">
    <img src="img/Truncate.png"/>
    </div>

<br>

### Manejo de errores:

Es frecuente que puedan ocurrir ciertos errores al momento de ingresar datos y manejar las funciones del administrador, para ello se le retornará un mensaje de error con un número que le indica que error ha cometido.

<br>

+ __Error 1:__  
Cualquier error en la operación no contemplado

+ __Error 2:__  
Base de datos no existente

+ __Error 3:__  
Tabla no existente

+ __Error 4:__  
Conflicto con una llave primaria o al momento de renombrar algo que ya existe

+ __Error 5:__  
Columna fuera de límites

<br>
<div align="center">
<img src="img/Errores.png"/>
</div><br><br>

## Reportes y navegación
<hr>
La aplicación muestra de manera gráfica y navegable las siguientes estructuras:

+ Bases de datos
+ Conjunto de tablas
+ Tabla (AVL)
+ Tupla

<br>

### Reporte de bases de datos:

Al iniciar la ventana de 'Reportes' lo primero que se despliega en el apartado izquierdo es una lista de todas las bases de datos que se hayan creado. Asimismo en el panel se encuentra gráficamente cada una de ellas.
<div align="center">
<img src="img/ReportesDB.png"/>
</div>
<br><br>

### Reporte de tablas:

Al hacer click sobre una base de datos de la lista izquierda, se visualiza el conjunto de tablas pertenecientes a esa base de datos y se llena la lista desplegable de cada una de las tablas.
<div align="center">
<img src="img/ReporteTablas.png"/>
</div>
<br><br>

### Reporte de tabla (AVL):

Se selecciona una de las tablas de la lista desplegable 'Tablas' y aparece un AVL gráfico que muestra la estructura de datos que representa todo el contenido de la tabla a esa base de datos.
<div align="center">
<img src="img/ReporteAVL.png"/>
</div>
<br><br>

### Reporte de tupla:

Se selecciona un registro perteneciente a la llave primaria que se encuentra en la lista desplegable 'Tuplas'. En seguida se muestra el conjunto de registros que pertenecen a la tupla.
<div align="center">
<img src="img/ReporteTupla.png"/>
</div>
<br><br>

## Soporte técnico
<hr>

* romeo11marroquin@gmail.com
* fernandovasquez.castillo@gmail.com
* luis.danniel@hotmail.com
* esavilaortiz@gmail.com
