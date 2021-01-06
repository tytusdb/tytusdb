# Tytus - Manual Tecnico
---

## Definicion Del Prototipo
Se plantea una solución inicial para un sistema de almacenamiento de información 
de un DBMS, que cuenta con las funciones principales para la manipulación de bases de datos.
El prototipo se desarrollo en lenguaje de Python en su version 3.8.1. Se utilizaron las librerias
"os" para funcionalidades dependientes de Sistema Operativo, "re" para la gestion de expresiones regulares, "pickle" para la representacion de objetos como cadenas de bytes y su almacenamiento en archivos, "shutil" para el manejo de alto nivel de archivos, "tkinter" para la implementación de la interfaz gráfica, "graphviz" para el dibujado de las estructuras de datos utilizadas, todas pertenecientes al módulo de Python. Se desarrollo una interfaz gráfica que brinde al usuario una 
forma sencilla para interactuar con la solución y se pueda observar el comportamiento de las 
estructuras de datos y como funcionan estas mismas dentro de la solución. Las estructuras de datos utilizadas fueron árboles en su mayoria, en específico árboles AVL y árboles B+, esto para mejorar el rendimiento de ejecución de la solución.

## Requerimientos Funcionales
* Tener instalado el entorno de [Python](https://www.python.org/downloads/) en el ordenador en su versión 3.8.1 o superior.
* Tener instalado el programa de visualización gráfica [Graphviz](https://graphviz.org/download/).

## Proposito Del Prototipo
El desarrollo de un sistema de almacenamiento prototipo de un gestor de base de datos, 
cuyo sistema tendrá la tarea de interactuar con los datos almacenados, 
para luego proporcionar la interfaz entre los datos de bajo nivel almacenados 
en la base de datos, los programas de aplicación y las consultas enviadas al sistema. 
Podrá gestionar la reserva de espacio de almacenamiento y las estructuras de datos
usadas para representar la información almacenada.

## Alcance Del Proyecto
El sistema será capaz de cumplir con un conjunto de funciones, las cuales facilitarán 
al usuario el manejo de los datos almacenados. El usuario podrá crear o eliminar una 
base de datos, tendrá la libertad poder crear, renombrar o eliminar 
tablas dentro de la base de datos. Támbien podrá visualizar una lista de los nombres de las tablas 
que se encuentren en la base datos, extraer y devolver una lista con elementos que 
corresponden a cada registro de la tabla, una lista con los elementos que corresponden 
a un rango de registros de la tabla.

## Funcionalidad Del Prototipo
El prototipo se encarga de la administración del almacenamiento de la 
información correspondiente al DBMS. El prototipo provee las funciones 
principales de un DBMS. La información se encuentra almacenada en árboles,
especificamente en arboles AVL para las bases de datos y para las tablas 
y en árboles B+ para los registros. La utilización de árboles para la 
gestión de los datos se centra en que se trato de buscar el menor tiempo 
de procesamiento para la información. Para el almacenamiento de la información 
en el disco se utilizo un archivo de extensión *".bin"* para no exponer la información
que se encuentra en la carpeta Data en el directorio del prototipo

## Requisitos Funcionales
* Crear Bases De Datos
* Mostrar Bases De Datos
* Modificar Bases De Datos
* Eliminar Bases De Datos
* Crear Tablas
* Mostrar Tablas
* Modificar Tablas
* Eliminar Tablas
* Mostrar Registros De Tabla
* Mostrar Porciones De Registros De Tabla
* Modificar Atributos De Llave Primaria
* Eliminar Atributos De Llave Primaria
* Agregar Columnas A Tablas
* Eliminar Columnas De Tablas
* Insertar Registros
* Carga Masiva De Registros
* Extraer Un Registros Específico
* Actualizar Registros
* Eliminar Registro En Específico
* Eliminar Todos Los Registros

## Requisitos No Funcionales
* Rendimiento De La Aplicación
* Durabilidad De La Información
* Flexibilidad Del Manejo De Datos
* Válidación De Llaves Primarias

## Diagrama General Del Prototipo
<p align="center"><img src = "https://github.com/tytusdb/tytus/blob/main/storage/team13/images/Arquitectura.png"></p>



## Diagrama De Clases Del Prototipo
<p align="center"><img src = "https://github.com/tytusdb/tytus/blob/main/storage/team13/images/Diagrama%20De%20Clases.png"></p>







