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

<div id='Funcionalidades'/>

## Funcionalidades
   | **Opción**                         | **Funcionalidad** |
   | ----------------------             | ----------------- |
   | Cambiar el modo de almacenamiento de una Base de Datos                     | Se debe de seleccionar un base de datos y seguidamente el modo de almacenamiento al que se quiere cambiar. |
   | Cambiar el modo de almacenamiento de una Tabla                     | Se debe de seleccionar una Tabla y seguidamente el modo de almacenamiento al que se quiere cambiar. |
   | Agregar índice de Llave Foránea                     | Se debe de seleccionar una Base de datos, una tabla, un nombre para el índice, el nombre de una tabla de referencia y los índices de la llave primaria. |
   | Destruir índice de Llave Foránea                     | Se debe de seleccionar una Base de datos, una tabla, un nombre para el índice y los índices de la llave primaria. |
   | Destruir Índice Único                     | Se debe de seleccionar una Base de datos, una tabla y un nombre para el índice. |
   | Cambiar Índice Único de una Tabla                     | Se debe de seleccionar una Base de datos, una tabla, un nombre para el índice y los índices de la llave primaria. |
   | Destruir Índice Único de una Tabla                     | Se debe de seleccionar una Base de datos, una tabla y un nombre para el índice. |
   | Cambiar codificación a una Base de Datos                     | Se debe seleccionar una base de datos y seguidamente el tipo de codificación. |
   | Generar diggest de una Base de Datos                     | Se debe indicar una Base de Datos y el modo en que está almacenada. |
   | Generar diggest de una Tabla                     | Se debe indicar una Base de Datos, una tabla y el modo en que está almacenada. |
   | Compresión de una Base de Datos                     | Se debe indicar una Base de Datos y el nivel de compresión deseado. |
   | Quitar compresión de una Base de Datos                     | Se debe indicar una Base de Datos. |
   | Compresión de una tabla                     | Se debe indicar una Base de Datos, una Tabla y el nivel de compresión deseado. |
   | Cifrar una Base de Datos o un Backup                     | Se debe seleccionar una base de datos o backup y seguidamente la llave. |
   | Decifrar una Base de Datos o un Backup                     | Se debe seleccionar una base de datos cifrada o backup cifrado  y seguidamente la llave. |
   | Activar modo seguro                     | Se debe seleccionar una base de datos y seguidamente una tabla de esa base de datos. |
   | Desactivar modo seguro                     | Se debe seleccionar una base de datos y seguidamente una tabla de esa base de datos. |
   | BlockChain                     | Cuando el modo seguro está activado, se registran todos los movimientos de inserción o elimación en una tabla. |
   | Gráfico de una Base de Datos                     | Se debe seleccionar una base de datos. |
   | Gráfico de dependecias de una Tabla                     | Se debe seleccionar una base de datos y una tabla. |

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
| BlockChain | Cadena de bloques encriptados, enlazados entre si haciendo uso de un Hash propio para cada bloque. |
| Hash | Es una función que convierte una entrada de letras y números en una salida cifrada de una longitud fija. |
| Checksum | Es el resultado de la ejecución de un algoritmo dentro de un archivo único. |

<div id='questions'/> 

## Preguntas Frecuentes (FAQ)
**1. ¿Se puede tener más de una tabla con el modo seguro activo?** 

> _R//_ *No*

**2. ¿Puedo referenciar una llave foránea a una misma tabla?** 

> _R//_ *No*

**3. ¿Se puede agregar dos veces el mismo nombre único a una tabla?** 

> _R//_ *No*

**4. Cuando desactivo el modo seguro, ¿por qué no encuentro registro de lo sucedido durante el timepo en que el modo seguro estuvo activado?** 

> _R//_ *Cuando se desactiva el modo seguro el registro creado es eliminado por completo.*

**5. ¿Por qué no se genera el Cheksum?** 

> _R//_ *Puede que este indicando el uso de un algoritmo distinto a los permitidos (MD5, SHA256).*

**6. ¿Puedo usar una codificación distinta a lo proporcionados por Tytus?** 

> _R//_ *No.*
