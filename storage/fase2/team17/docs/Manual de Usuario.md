MANUAL DE USUARIO
===================
## Índice
- [Introduccion](#introduccion)
- [Descripción General del Sistema](#descrip)
- [Aplicacion](#apli)
- [Funcionalidades](#funcionalidades)
- [Glosario](#glosario)
- [FAQ](#questions)

<div id='introduccion'/>

## Introducción
La finalidad de la interfaz gráfica es permitir al usuario la administración de sus bases de datos con una mayor facilidad que al hacerlo en una consola. Este manual permite al usuario la visualización de las distintas estructuras como lo son las relaciones de las tablas de una base de datos, la relación de una tabla con respecto a sus llaves primarias e índices únicos así como la visualización del blockchain de los registros al momento de activar el modo seguro en la aplicación.

<div id='descrip'/>

## Descripción

  - **Estructura de Almacenamiento**: 
Para la realización de este proyecto, la estructura o modo de almacenamiendo son: árboles; AVL, B, B+, tablas: Hash e Isam así como el modo JSON y Dict.
  - **Bases de Datos**:
Las _Bases de Datos_ son un conjunto de datos pertenecientes a un mismo contexto y almacenados sistemáticamente para su uso posterior. Cada _Base de Datos_ se compone de una o más _tablas_.
  
  - **Tablas**:
Las _tablas_ se componen de una o más columas y filas, tambien llamadas _tuplas_.

 - **Tuplas**:
Contienen la informacion correspondiente a un determinado registro dentro de una _tabla_.  

<div id='apli'/>

## Aplicación
### Interfaz Gráfica (GUI)
El programa **_`Tytus 2020`_** cuenta con una vista gráfica la cual facilita la interacción entre el sistema y el usuario final para un mejor manejo de datos. Por medio de dicha interfaz, al usuario se le permite visualizar de forma _gráfica_ una estructura relacional de las Bases de Datos así como de sus Tablas. El usuario puede navegar por la aplicación seleccionando a través de botones la acción que desea realizar, si ocurre un error en el ingreso de datos el programa le notificará al usuario el tipo de error que se está cometiendo. 

- Ventana Inicial: La _Ventana Inicial_ cuenta con tres opciones: *Seguridad*, *Grafos* y *_Acerca De_*.

![](https://github.com/DiiAns23/Prueba-2/blob/Master/img/inicio.png)

   | **Opción** | **Funcionalidad** |
   | ---------- | ----------------- |
   | Seguridad   |Para esta función, el usuario podrá realizar funciones como: ModeSafeOff así como mostrar el grafo de un BlockChain|
   | Grafos  | Con esta funcion, el usuario podrá realizar funciones como: Mostrar las relaciones de dependencia de las tablas de una base de datos así como la relación de las PK con los índices únicos con respecto a sus demás datos |
   | Acerca De  | Muesta la información del Centro de estudios así como de los programadores del sistema |
     
- Ventana Seguridad: En esta ventana el usuario podrá seleccionar las opciones: ModeSafeOff o BlockChain.
  
![](https://github.com/DiiAns23/Prueba-2/blob/Master/img/seguridad.png)

   | **Opción** | **Funcionalidad** |
   | ---------- | ----------------- |
   | ModeSafeOff   |Para desactivar el modo seguro, el usuario deberá de ingresar el nombre de una base de datos y su respectiva tabla|
   | BlockChain  | Para mostrar el grafo del blockchain, el usuario deberá de ingresar el nombre de una base de datos y su respectiva tabla |

- Ventana Grafos: El usuario podrá seleccionar las opciones para graficar las tablas de una base de datos y sus relaciones o mostrar la dependencia de los datos de una tabla con respecto a su Llave Primaria e Índice Único.

![](https://github.com/DiiAns23/Prueba-2/blob/Master/img/grafos.png)

   | **Opción** | **Funcionalidad** |
   | ---------- | ----------------- |
   | Bases de Datos | Para mostrar el grafo de las relaciones de dependencia de una base de datos y sus tablas el usuario deberá de ingresar el nombre respectivo para cada una de ellas|
   | Tabla  | El usuario deberá de ingresar el nombre de la base de datos y una tabla para mostrar la dependencia de sus datos con respecto a una LLave Primaria o Índice Único |
   
- Ventana Acerca De: Se mostrarán datos del centro de estudios así como de los programadores del sistema **_`Tytus 2020`_**

![](https://github.com/DiiAns23/Prueba-2/blob/Master/img/acercade.png) 