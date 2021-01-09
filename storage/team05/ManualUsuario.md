# MANUAL USUARIO

# TYTUS TB
# ADMINISTRADOR DE ALMACENAMIENTO
# <center> INTEGRANTES </center>

## <center> CARLOS EMILIO CAMPO MORAN </center>

## <center> JOSE RAFAEL SOLIS FRANCO </center>

## <center> MADELYN ZUSETH PEREZ ROSALES </center>

## <center> JOSE FRANCISCO DE JESUS SANTOS SALAZAR </center>

# UNIVERSIDAD DE SAN CARLOS DE GUATEMALA
# FACULTAD DE INGENIERIA
# ESCUELA DE CIENCIAS Y SISTEMAS
# ESTRUCTURA DE DATOS
# 2020

### <center>**INTRODUCCION**</center>

<p align= "justify" > TYTUS TB es un administrador de base de datos que facilita al usuario ingresar información de manera ordenada y precisa, teniendo así un mejor manejo de datos. El manual que se presenta a continuación es una guía al usuario para que pueda tener un mejor manejo en la utilizacion del formulario.</p>

---
### <center>**ADVERTENCIAS Y CONSEJOS DE SEGURIDAD**</center>
Cuando se utilize este programa hay que tener presente estos consejos:

1. Cuando se desea crear una tabla, hay que crear una base de datos antes, almenos debe de existir como minimo una base de datos.
2. Para agregar datos hay que tener creada por lo menos una tabla.
3. Para carga masiva hay que tener presente los dos consejos anteriores.
4. Para generar reporte de la tabla Hash hay que tener descargado Graphviz en el computador.
5. Leer la descripcion general del sistema antes de utilizar el programa
6. Cuando desee hacer una carga masiva, procure que el archivo sea extension .csv, de lo contrario no le permitira subir.

---
### <center> **DESCRIPCION GENERAL DEL SISTEMA** </center>

TYTUS TB es un formulario accesible para al usuario para que pueda tener acceso  y poder tener un mejor manejo para la organizacion de manejo de Bases de Datos. El formulario de TYTUS TB contiene una pagina inicial (Main) donde muestra los datos que han sido creados y guardados. Pero primero hay que conocer las opciones anteriores para poder tener un mejor orden. TYTUS TB se descompone de menus que se presentan a continuacion.

## 1. Menu Archivo:
El menu Archivo se descompone de submenus que tienen las siguientes funciones:

## 1.1. Guardar:
Se ejecuta automaticamente, pero guarda la informacion de la base de datos

## 1.2. Salir:
Cerrara el programa

[OpcionesArchivo](ImagenesManual/OpcionesArchivo.JPG)

## 2. Menu Base de datos:
El menu Base de Datos maneja todo lo que se relaciona a creacion, eliminacion y modificacion de base de datos
[OpcionesBaseDatos](ImagenesManual/OpcionesBaseDatos.JPG)

>A continuacion se presenta el submenu del menu Base de Datos y sus funciones

## 2.1 Submenu Alter DataBase:
1. Selecciona la base de datos a Cambiar e ingresa el nuevo nombre de la base de datos, presionar el boton para confirmar cambios
[AlterDataBase](ImagenesManual/AlterDataBase.JPG)

## 2.2 Menu Create DataBase:
1. Ingresa el nombre de la base de datos a crear y presionar el boton
[CreateDataBase](ImagenesManual/CreateDataBase.JPG)

## 2.3 Menu Drop DataBase:
    1. Selecciona la base de datos a eliminar en el combo box y presionar boton para aplicar cambios
[DropDataBase](ImagenesManual/DropDataBase.JPG)

## 3. Menu Tablas:

El menu Tablas maneja todo lo que se relacione a creacion, eliminacion y modificacion de tablas
[OpcionesTablas](ImagenesManual/OpcionesTablas.JPG)

>A continuacion se presenta el listado de Menu Tablas
## 3.1. Add Column
    1. Selecciona la base de datos a modificar y presionar Mostrar Tablas
[OpcionesAddColumn1](ImagenesManual/OpcionesAddColumn1.JPG)

    2. Selecciona la tabla a modificar
[OpcionesAddColumn2](ImagenesManual/OpcionesAddColumn2.JPG)

    3. Ingresa el valor por defecto de la columna nueva y presionar boton Agregar Columna
[OpcionesAddColumn3](ImagenesManual/OpcionesAddColumn3.JPG)

## 3.2. Alter Add Primary Key

    1. Selecciona la base de datos a modificar y presionar Mostrar Tablas
[AlterAddPrimaryKey1](ImagenesManual/AlterAddPrimaryKey1.JPG)

    2. Selecciona la tabla a modificar
[AlterAddPrimaryKey2](ImagenesManual/AlterAddPrimaryKey2.JPG)

    3. Ingrese una lista de columnas delimiatadas por coma para generar la llave primaria y presionar boton Agregar PK para aplicar
[AlterAddPrimaryKey3](ImgenesManual/AlterAddPrimaryKey3.JPG)

## 3.3. Alter Drop Primary Key:

    1. Seleccionar la base de datos a modificar y presionar Mostrar tablas
[AlterDropPrimaryKey1](ImagenesManual/AlterDropPrimaryKey1.JPG)

    2. Selecciona la tabla a eliminar la llave primaria y aplicar presionando el boton Drop Primary Key
[AlterDropPrimaryKey2](ImagenesManual/AlterDropPrimaryKey2.JPG)

## 4.4. Alter Table:

    1. Selecciona la base de datos a modificar y presionar Mostrar Tablas
[AlterTable1](ImagenesManual/AlterTable1.JPG)

    2. Selecciona la base de datos a modificar
[AlterTable2](ImagenesManual/AlterTable2.JPG)

    3. Ingresar  el nuevo nombre de la tabla y presionar el boton modificar tabla
[AlterTable3](ImagenesManual/AlterTable3.JPG)

## 4.5. Create Table:

    1. Selecciona la base de datos a crear la tabla
[CreateTable1](ImagenesManual/CreateTable1.JPG)

    2. Ingrese el nombre de la tabla
[CreateTable1](ImagenesManual/CreateTable2.JPG)

    3. Ingresa el numero de columnas que tendra la tabla y presionar el boton para aplicar cambios
[CreateTable1](ImagenesManual/CreateTable3.JPG)

## 4.6. Drop Column:

    1. Selecciona la base de datos a modificar y presionar boton Mostrar Tablas
[DropColumn1](ImagenesManual/DropColumn1.JPG)

    2. Seleccionar la tabla a modificar
[DropColumn2](ImagenesManual/DropColumn2.JPG)

    3. Ingresa el numero de columna a eliminar y presionar boton Eliminar Columna para aplicar
[DropColumn3](ImagenesManual/DropColumn3.JPG)

## 4.7. Drop Table:

    1. Selecciona la Base de datos a Modificar y presiona Boton Mostrar Tablas
[DropTable1](ImagenesManual/DropTable1.JPG)

    2. Selecciona la tabla a eliminar y presionar el boton Eliminar Tabla para aplicar cambios
[DropTable2](ImagenesManual/DropTable2.JPG)

## 4.8. Extract Range Table:

    1. Selecciona la base de datos y presionar Mostrar Tablas
[ExtractRangeTable1](ImagenesManual/ExtractRangeTable1.JPG)

    2. Seleccionar la tabla a mostrar y presionar mostrar cantidad de columnas para actualizar combobox
[ExtractRangeTable2](ImagenesManual/ExtractRangeTable2.JPG)

    3. Seleccionar el numero de columna y los valores minimos y maximos, presionar extract range table
[ExtractRangeTable3](ImagenesManual/ExtractRangeTable3.JPG)

## 4.9. Extract Table:
    
    1. Selecciona la base de datos a mostrar y presionar mostrar tabla
[ExtractTable1](ImagenesManual/ExtractTable1.JPG)

    2. Seleccionar la tabla a mostrar contenido
[ExtractTable2](ImagenesManual/ExtractTable2.JPG)

    3. Presionar Extract Table para mostrar el contenido de la tabla
[ExtractTable3](ImagenesManual/ExtractTable3.JPG)

## 5. Menu Tuplas:

## 5.1. Delete:

    1. Seleccionar base de datos y tabla a modificar
[Delete1](ImagenesManual/Delete1.JPG)

    2. ingresar la llaver primaria a eliminar  y presionar Delete
[Delete2](ImagenesManual/Delete2.JPG)

## 5.2. Extract Row:

    1. Seleccionar Base ddatos y mostrar tablas
[ExtractRow1](ImagenesManual/ExtractRow1.JPG)

    2. seleccionar tabla a extraer
[ExtractRow2](ImagenesManual/ExtractRow2.JPG)

    2. seleccionar tabla a extraer
[ExtractRow3](ImagenesManual/ExtractRow3.JPG)

## 5.3. Insert:

    1.Selecciona la base de datos a sobrecargar y presionar Mostrar tablas
[Insert1](ImagenesManual/Insert1.JPG)

    2. Seleccionar la tabla a insertar
[Insert2](ImagenesManual/Insert2.JPG)

    3. Ingrese el registro a cargar delimitado por comas y presionar Insert para aplicar
[Insert3](ImagenesManual/Insert3.JPG)

## 5.4. LoadCsv

    1. Seleccionar el archivo a cargar tipo csv
[LoadCsv1](ImagenesManual/LoadCsv1.JPG)

    2. Seleccionar la base de datos a cargar y presionar Mostrar Tabla
[LoadCsv2](ImagenesManual/LoadCsv2.JPG)

    3. Seleccionar la tabla a sobrecargar y presionar  Cargar Informacion
[LoadCsv3](ImagenesManual/LoadCsv3.JPG)

## 5.5. Truncate

    1. Seleccionar la base de datos y tabla a truncar y presionar boton
[Truncate](ImagenesManual/Truncate.JPG)

## 5.6. Update

    1. Seleccionar la base de datos y tabla a truncar y presionar boton
[Update1](ImagenesManual/Update1.JPG)

    2. Seleccionar tabla a actualziar
[Update2](ImagenesManual/Update2.JPG)

    3. Ingresar el registro a actualizar y la columna presionar Update para aplicar
[Update3](ImagenesManual/Update3.JPG)

## 6. Reportes:
En este menu se generan los reportes 
    1. Seleccionar que tipo de reporte generar en pdf y abrir automaticamente
[OpcionesReportes](ImagenesManual/OpcionesReportes.JPG)

## 7. Meny Ayuda:

    1. Ayuda redireccionara al repositorio, acerca de mostrara informacion de los programadores
[OpcionesAyuda1](ImagenesManual/OpcionesAyuda1.JPG)

    1. Ayuda redireccionara al repositorio, acerca de mostrara informacion de los programadores
[OpcionesAyuda2](ImagenesManual/OpcionesAyuda2.JPG)

## MAIN:
El main aparece al principio de abrir el programa

    1. Seleccion Base de datos
[Main1](ImagenesManual/Main1.JPG)

    2. Al presionar Mostrar Tablas carga las tablas de la base de datos seleccionada
[Main2](ImagenesManual/Main2.JPG)

    3. Al presionar Mostrar Contenido, abrira un PDF con el contenido de la tabla
[Main3](ImagenesManual/Main3.JPG)

---

### <center> **INSTRUCCION PARA SOLUCION DE PROBLEMAS** </center>
1. Antes de generar reportes, hay que revisar si se ha agregado mas del algun dato, de lo contrario le aparecera Nulo.
2. Cuando agregaue una tabla siempre revise si la tabla no ha sido creada anteriormente, no permite tablas de nombre duplicado.
3. Para que no se le pierdan sus datos al cerrar el programa, es recomendable que genere los reportes de los datos que ha guardado antes de cerrar el programa, ya que se pueden perder. Si ustede genera un reporte despues puede leer el archivo.
4. Si ustede desea subir datos, convierta su archivo a extension .csv antes de subirlo.















