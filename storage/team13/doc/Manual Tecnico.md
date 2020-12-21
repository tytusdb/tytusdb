# Manual Tecnico
---

## Definicion Del Prototipo
Se plantea una solucion inicial para un sistema de almacenamiento de informacion 
de un DBMS, que cuenta con las funciones principales para la manipulacion de bases de datos.
El prototipo se desarrollo en lenguaje de Python en su version 3.8.1. Se utilizaron las librerias
"os" para funcionalidades dependientes de Sistema Operativo, "re" para la gestion de expresiones regulares, "pickle" para la representacion de objetos como cadenas de bytes y su almacenamiento en archivos, "shutil" para el manejo de alto nivel de archivos, "tkinter" para la implementacion de la interfaz grafica, "graphviz" para el dibujado de las estructuras de datos utilizadas, todas pertenecientes al modulo de Python. Se desarrollo una interfaz grafica que brinde al usuario una 
forma sencilla para interactuar con la solucion y se pueda observar el comportamiento de las 
estructuras de datos y como funcionan estas mismas dentro de la solucion. Las estructuras de datos utilizadas fueron arboles en su mayoria, en especifico arboles AVL y arboles B+, esto para mejorar el rendimiento de ejecution de la solucion.

## Requerimientos Funcionales
* Tener instalado el entorno de Python en el ordenador en su version 3.8.1 o superior

## Proposito Del Prototipo
El desarrollo de un sistema de almacenamiento prototipo de un gestor de base de datos, 
cuyo sistema tendrá la tarea de interactuar con los datos almacenados, 
para luego proporcionar la interfaz entre los datos de bajo nivel almacenados 
en la base de datos, los programas de aplicación y las consultas enviadas al sistema. 
Podrá gestionar la reserva de espacio de almacenamiento y las estructuras de datos
usadas para representar la información almacenada.

## Alcance Del Proyecto
El sistema será capaz de cumplir con un conjunto de funciones, las cuales facilitaran 
al usuario el manejo de los datos almacenados. El usuario podrá crear o eliminar una 
base de datos, tendrá la libertad de renombrarla; podrá crear, renombrar o eliminar 
tablas dentro de la base de datos, visualizar una lista de los nombres de las tablas 
que se encuentren en la base datos, extraer y devolver una lista con elementos que 
corresponden a cada registro de la tabla, una lista con los elementos que corresponden 
a un rango de registros de la tabla.

## Funcionalidad Del Prototipo
El prototipo se encarga de la administracion del almacenamiento de la 
informacion correspondiente al DBMS. El prototipo provee las funciones 
principales de un DBMS. La informacion se encuentra almacenada en arboles,
especificamente en arboles AVL para las bases de datos y para las tablas 
y en arboles B+ para los registros. La utilizacion de arboles para la 
gestion de los datos se centra en que se trato de buscar el menor tiempo 
de procesamiento para la informacion. Para el almacenamiento de la informacion 
en el disco se utilizo un archivo de extension .bin para no exponer la informacion
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
* Extraer Un Registros Especifico
* Actualizar Registros
* Eliminar Registro En Especifico
* Eliminar Todos Los Registros

## Requisitos No Funcionales
* Rendimiento De La Aplicacion
* Durabilidad De La Informacion
* Flexibilidad Del Manejo De Datos
* Validacion De Llaves Primarias

## Diagrama General Del Prototipo
![..](https://github.com/tytusdb/tytus/blob/main/storage/team13/images/Arquitectura.png)
---
---

## Diagrama De Clases Del Prototipo
![..](https://github.com/tytusdb/tytus/blob/main/storage/team13/images/Diagrama%20De%20Clases.png)
---
---




