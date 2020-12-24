# Manual de Tecnico EDD_Grupo 9

Diseño, desarrollo e implementacion de software para el manejo de bases de datos e informacion de la Universidad de San Carlos de Guatemala, grupo 9 del curso estructuras de datos.

## Introducción
    * Nota: El contenido del manual técnico da por hecho que el usuario tiene los conocimientos basicos de informatica.
La universidad de San Carlos de Guatemala se dispone junto con los colaboradores correspondientes a los cursos de Bases de Datos, Compiladores 2 y Estructuras de Datos, a realizar un software de codigo abierto para el manejo de informacion por medio de estructuras relacionales llamado Tytus. Dicho software tiene como proposito poner a disposicion una aplicacion simple pero poderosa para el manejo de bases de datos, por lo cual se detalla el desarrollo del software.

## Objetivos
* #### General
Informar y especificar al usuario sobre la estructura y funcionamiento del software presentado con el fin de poder realizar soporte, modificaciones y asi actualizar el sistema.

* #### Especificos
    * Conocer las estructuras utilizadas en el desarrollo del proyecto.
    * Conocer el funcionamiento y el flujo que las bases de datos, tablas y tuplas continen.

## Alcance
El documento será elaborado para las personas con conocimiento en desarrollo de software, orientado a guiar el proceso de dar soporte a la estructura de datos.

## Modulos 

#### Gui
En este modulo los usuarios podran realizar las funciones que Tytus db ofrece, de una manera grafica para ser mas accesible y entendible para cualquier usuario que desee utilizar nuestro gestor de bases de datos. Cuenta con diferentes ventanas para la navegabilidad. Cuenta con lector de archivos CSV para agilizar la carga de datos a las bases de datos creadas.

#### ISAMMode
En este archivo contenemos todas las funciones que Tytus db ofrece, esto con la finalidad de importar este archivo y acceder a la poderosa capacidad que ofrece nuestro gestor de bases de datos. Este archivo contiene la instancia de las bases de datos para poder ser utilizada sin problemas. Este archivo contiene todas las funciones como lo son la gestion de bases de datos (creacion,eliminacion,actualizacion y vista de bases de datos), también contiene todo el CRUD de las tablas al igual que con las bases de datos, contiene la gestion de tuplas (insercion, delete, update, mostrar una tupla).

#### Bases de Datos
Este modulo contiene toda la estructura del gestor Tytus, porque contiene la instancia de las tablas y basandonos en un estructura jerarquica conseguimos que las tablas contencan la instancia de ISAM, en este modulo contamos con las funciones que gestionan las bases de datos, como lo son la creación, la eliminacion, la edicion de nombre, y la opcion que muestra todas las bases de datos existentes.

#### Tablas
Para este modulo se penso en un diccionario, los cuales proporciona Python, porque es una estructura facil y muy potente que podemos utilizar y aprobechar de una manera muy optima, ya que al momento de acceder a los datos es de manera O(1) por el hecho de manejar sus datos con indices. Para conseguir esto utilizamos una clase la cual contendra los valores necesarios y que accedemos con frecuencia como lo son las llaves primarias, el nombre de la tabla, el numero de columnas de dicha tabla y lo mas importante la instancia hacia las tuplas (ISAM), para poder acceder a sus metodos de nivel tupla.

#### ISAM
Este modulo es uno de los mas importantes para nuestra estructura de bases de datos porque es el que contiene todos los datos de nuestra estructura, en este modulo almacenaremos todos los datos que los usuarios quieran. Para ello pretendemos utilizar una estructura de arbol ISAM, que es una estructura que combina un arbol y un tipo de tablas indexadas, esto para facil acceso a nuestros datos.

## Contenido Tecnico Del Sistema

### Diagrama Conceptual
![D](./img/DiagramaConceptual.png)

### Diagrama de Clases
![D](./img/DiagramaDeClases.png)

## Requerimientos Del Sistema
El software Tytus es una aplicacion de bases de datos que usa tecnologias diferentes para sus diferentes modulos asi:
    * Estructuras de Datos: Tecnología basada en el lenguaje de programacion Python 
    * Graficar: Tecnología basada en Graphviz

## Configuracion De La Aplicación

Para poder utilizar la aplicacion es necesario importar el archivo llamado MainG para ello es necesario implementar la siguiente linea de codigo:

```python
	from team09 import ISAMMode
```
Despues de haber incluido la linea de codigo podremos darle un seudonimo a la importacion para hacerlo mas facil de manejar por ejemplo podriamos llamarlo con la letra i 

```python
	from team09 import ISAMMode as i
```
Con esto nos facilitamos el uso de la importacion, despues de haberlo hecho ya podremos utilizar todas las funciones que Tytus Db ofrece. 
Para ello tendremos que ingresar la funcion que queramos utilizar como por ejemplo crear una base de datos nueva para ello debemos utilizar el import y seguido a ello la funcion a utilizar

```python
	i.createDatabase(params)
```
