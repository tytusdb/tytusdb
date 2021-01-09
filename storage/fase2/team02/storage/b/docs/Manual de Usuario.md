MANUAL DE USUARIO
===================
## Índice
- [Introduccion](#introduccion)
- [Descripción General del Sistema](#descrip)
- [Aplicacion](#apli)
- [Glosario](#glosario)
- [FAQ](#questions)

<div id='introduccion'/>

## Introducción
La finalidad de la interfaz gráfica es permitir al usuario la administración de sus bases de datos con una mayor facilidad que al hacerlo en una consola, Este manual permite al usuario comprender la composición de la interfaz gráfica y el cómo interactuar con la base de datos creada; la cual ha sido implementada con un Árbol B de grado 5. 

<div id='descrip'/>

## Descripción

  - **Estructura de Almacenamiento**: 
Para la realización de este proyecto, la estructura o modo de almacenamiendo utilizada fue por medio de un Arbol B de tamaño cinco.
  - **Bases de Datos**:
Las _Bases de Datos_ son un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su uso posterior. Cada _Base de Datos_ se compone de una o más _tablas_.
  
  - **Tablas**:
Las _tablas_ se componen de una o más columas y filas, tambien llamadas _tuplas_.

 - **Tuplas**:
Contienen la informacion correspondiente a un determinado registro dentro de una _tabla_.  

<div id='apli'/>

## Aplicación

### Requerimientos de la Aplicación
* Tener instalado [pip](https://pypi.org/project/pip/).

* Ejecutar el siguiente comando en la consola: `pip install PIL`

* Ejecutar el siguiente comando en la consola: `pip install pillow`

* Para iniciar copiar, en un archivo .py fuera de la carpeta del paquete, el siguiente código:
```
from team17 import Interfaz as i
i.runInterface()
```

### Interfaz Gráfica (GUI)
El programa **_`Tytus 2020`_** cuenta con una vista gráfica la cual facilita la interacción entre el sistema y el usuario final para un mejor manejo de datos. Por medio de dicha interfaz, al usuario se le permite visualizar de forma _gráfica_ la estructura con la cual los datos estan siendo almacenados en la memoria del computador. El usuario puede navegar por la aplicación seleccionando a través de botones la acción que desea realizar, si ocurre un error en el ingreso de datos el programa le notificará al usuario el tipo de error que se está cometiendo. 

- Ventana Inicial: La _Ventana Inicial_ cuenta con tres opciones: *Reportes*, *Funciones* y *_Acerca De_*.

![](https://github.com/tytusdb/tytus/blob/main/storage/team17/docs/img/Init.png)

   | **Opción** | **Funcionalidad** |
   | ---------- | ----------------- |
   | Reportes   | Por medio de esta opción, el usuario podrá generar y visualizar la estructura de los datos en forma de _Árbol B_ |
   | Funciones  | Con esta funcion, el usuario puede acceder a todas las funcionalidades de Bases de Datos, Tablas y Tuplas  |
   | Acerca De  | Muesta la información del Centro de estudios así como de los programadores del sistema |
     
- Ventana Reportes: En esta ventana el usuario deberá de seleccionar una base de datos y seguidamente seleccionar una tabla, también podrá seleccionar una llave primaria de la tabla para visualizar un elemento en específico según lo desee.
  
![](https://github.com/tytusdb/tytus/blob/main/storage/team17/docs/img/Rep.png)

- Ventana Funciones: En esta pestaña se mostrarán todas las funcionalidades del sistema.

![](https://github.com/tytusdb/tytus/blob/main/storage/team17/docs/img/Func.png)

   | **Opción**                         | **Funcionalidad** |
   | ----------------------             | ----------------- |
   | Nueva Base de Datos                | Para crear una nueva base de datos, el usuario solo deberá de ingresar el nombre que desee |
   | Mostrar Bases de Datos             | Mostrará en pantalla todas las bases de datos existentes en la memoria del computador |
   | Cambiar Nombre a una Base de Datos | El usuario debe de seleccionar una base de datos y posteriormente ingresar el nuevo nombre |
   | Eliminar una Base de Datos         | El usuario deberá de seleccionar la base de datos a eliminar |
   | Nueva Tabla                        | Se debe de seleccionar una base de datos y posteriormente ingresar el nombre de la nueva tabla |
   | Mostrar Tablas                     | Se debe de seleccionar una base de datos para mostrar las tablas que contiene dicha base de datos |
   | Mostrar Datos                      | Se debe de seleccionar una base de datos y posteriormente seleccionar una tabla para poder visualizar los datos |
   | Rango Tabla                        | Se debe de seleccionar una base de datos, una tabla, un número de columna y posteriormente ingresar el límite inferior y superior |
   | Agregar Llave Primaria             | Se debe de seleccionar una base de datos, una tabla y posteriormente ingresar las columnas que se desean que sean llaves primarias |
   | Eliminar Llave Primaria            | Se debe de seleccionar una base de datos y posteriormente una tabla para que su llave primaria sea eliminada |
   | Cambiar nombre de una Tabla        | Se debe de seleccionar una base de datos, una tabla y escribir el nuevo nombre que se le desea dar a dicha tabla |
   | Agregar columna a una Tabla        | Se debe de seleccionar una base de datos, una tabla y el nuevo valor a ingresar en todos los registros existentes |
   | Elimina columna de una Tabla       | Se debe de seleccionar una base de datos, una tabla y el numero de columna que se desea eliminar |
   | Eliminar una Tabla                 | Se debe de seleccionar una base de datos y seguidamente la tabla a eliminar |
   | Insertar Tupla                     | Se debe de seleccionar una base de datos, una tabla y seguidamente ingresar los datos a ingresar en la fila o tupla |
   | Cargar CSV                         | Se debe de seleccionar una base de datos y una tabla, seguidamente ingresar el nombre del archivo con su extensión |
   | Extraer una Tupla                  | Se debe de seleccionar una base de datos, una tabla y seguidamente la llave primaria |
   | Eliminar una Tupla                 | Se debe de seleccionar una base de datos, una tabla y seguidamente la llave primaria |
   | Truncate Tabla                     | Se debe de seleccionar un base de datos y seguidamente una tabla |
   
- Ventana Acerca De: Se mostrarán datos del centro de estudios así como de los programadores del sistema **_`Tytus 2020`_**


![](https://github.com/tytusdb/tytus/blob/main/storage/team17/docs/img/A_D.png) 

<div id='glosario'/>

## Glosario

| Palabra | Descripción | 
| ------------------------------- | ----------------------------------------- |
| Arbol B | Tipo de estructura de almacenamiento de datos |
| Interfaz Gráfica | Interacción entre el usuario y el sistema |
| Registro | Valor o valores a ingresar en una tupla |
| Tupla | Fila |
| Llave primaria | Identificador único para una tabla de una base de datos |
| CSV | Valores separados por coma o Comma-Separated Values por sus siglas en inglés |
| Truncate | Elimina todos los registros de determinado lugar |

<div id='questions'/> 

## Preguntas Frecuentes (FAQ)
**1. ¿Puedo crear dos veces la misma base de datos?**    

> _R//_ *No, el nombre de la base de datos debe de ser único.*

**2. ¿Cuantas tablas puedo crear dentro de una base de datos?**   

> _R//_ *No existe un límite para crear tablas dentro de una base de datos.*

**3. ¿Cuáles son los nombres válidos para Bases de Datos y Tablas?**   

> _R//_ *El primer caracter debe de ser una letra del abecedario y no puede llevar nombres de palabras reservadas.*

**4. ¿Pueden existir llaves primarias duplicadas?** 

> _R//_ *No, la llave primaria es un identificador único para cada registro.*

**5. ¿Por qué no puedo insertar un nuevo registro?** 

> _R//_ *Puede que este mal escrito, la llave este duplicada o no cumpla con la longitud de columnas de la tabla.*

**6. ¿Por qué no puedo agregar una llave primaria?** 

> _R//_ *Puede que la columna seleccionada contenga valores repetidos.*

**7. ¿Cómo cargo un CSV?** 

> _R//_ *Debes de seleccionar una base de datos y una tabla la cual debe de tener la misma cantidad de columnas que el archivo que deseas cargar*

**8. ¿Puedo modificar el grado del árbol?** 

> _R//_ *No, por el momento esa función no ha sido habilita*

**9. ¿Cuántas columnas puedo poner como llave primaria?** 

> _R//_ *No hay límite, solo se debe verificar que las columnas no contengan valores repetidos*

**10. ¿Una base de datos puede tener las mismas tablas que otra base de datos?** 

> _R//_ *Sí*
