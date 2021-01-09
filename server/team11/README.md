# MANUAL TÉCNICO

UNIVERSIDAD DE SAN CARLOS DE GUATEMALA  
FACULTAD DE INGENIERÍA  
ESCUELA DE CIENCIAS Y SISTEMAS  
CURSO: SISTEMAS DE BASES DE DATOS 1  
ESCUELA DE VACACIONES DICIEMBRE 2020 
___

## TytusDB
![](https://upload.wikimedia.org/wikipedia/commons/4/4a/Usac_logo.png)
___
## Team 11
- JORGE JUAREZ - 201807022
- JOSE MORAN - 201807455
- ROMAEL PEREZ - 201213545
___
## Índice
- [Descripción General](Descripción-general)
- [Requerimientos Funcionales](Requerimientos-funcionales)
- [Administracion de la Base de Datos](Administracion-de-la-Base-de-Datos)
- [Tecnologias Utilizadas](Tecnologias-Utilizadas)
- [Otros Recursos Importantes](Otros-Recursos-Importantes)
- [Licencias y Convenios](Licencias-y-convenio)
- [Glosario](Glosario)

___
### Descripción general 
Es un proyecto Open Source en desarrollo para crear un administrador de bases de datos utilizando distintos modos de almacenamiento mediante el uso distintas estructuras de datos.
Este paquete es el encargado de gestionar el almacenamiento de las bases de datos del proyecto, el cual proporciona al servidor un conjunto de funciones para manipular la información que ingresa a las bases de datos.

TytusBD tiene cinco modos de almacenamiento, este paquete brinda la modalidad de almacenacenaje para la estructura de datos mediante un árbol AVL, siendo esta estructura la base para poder manipular los datos a traves de las funciones que ofrece el DBMS. El almacenamiento funciona con tres tipos de arboles AVL desarrollados en el lenguaje Python para poder separar los tipos de informacion como: las bases de datos, las tablas y los registros. Para la persistencia de los datos  utiliza un sistema jerárquico de ficheros y serialización de objetos que guardan la información de cada estructura.

#### Bases de datos

- Una base de datos es un conjunto de tablas, para este diseño, es un conjunto de estructuras arbóreas. 

- El servidor de la base de datos podrá contener n bases de datos. 

___
## Requerimientos funcionales
- El software es el encargado de gestionar el almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para extraer la información.
- El modo de almacenamiento sera por medio de la estructura de un arbol AVL.
- Cada registro que corresponde a una tabla será almacenado en cada nodo en el arbol correspondiente para las tablas.
- El servidor de la base de datos podrá contener n bases de datos.
- Se manejan los archivos de manera binaria para no exponer la información.
- Los métodos y funciones deben cumplir con el tipo de dato que rigen sus parámetros y los valores a retornar segun su significado.
- Se brindara una interfaz iteractiva para la visualizacion de los datos y el comportamiento de las estructuras

___
## Administrador de la base de datos

El administrador de la base de datos se compone de dos componentes:

- Servidor: es un servidor http. Se debe seleccionar un puerto adecuado que no tenga conflictos con otros servidores. En la carpeta de instalación de la base de datos se debe crear una carpeta llamada /data donde se almacenarán las bases de datos. Se debe crear un usuario admin y su contraseña. Además de crear n usuarios configurando el acceso a las bases de datos.

- Cliente: es un cliente que para algunos equipos será web y para otros será una aplicación de escritorio. Este cliente se conectará al servidor y podrá hacer la mayoría de las operaciones que hace pgadmin de PostgreSQL. Dentro del cliente, cuando se navegue dentro de las diferentes bases de datos que existen se puede invocar un editor de queries, el cual invocará la función parser() del SQL Parser para desplegar el resultado. Este editor debe tener la característica de resaltado de sintaxis.

![Arquitectura cliente servidor](https://edgarbc.files.wordpress.com/2014/02/501f9-cliente-servidor.png?w=950)
___
## Tecnologias Utilizadas
- Servidor
    - Flask-cors
    - Jsonify
- Cliente
    - Angular
    - Angular Material
    - Ace Editor
    - Bootswatch
    - Sweet alert
___
## Otros Recursos Importantes
El servidor se desarrollo sobre el Sistema operativo Linux, siendo este el SO mas popular para la implementacion de servidores.

Para la instalacion de dependencias se utilizo el siguiente comando: 
`npm install`

Y para ejecutar el cliente se utilizao el siguiente comando:
`ng serve `
___
## Licencias y convenio
El proyecto está diseñado bajo una licencia Open Source, específicamente **MIT**. Por convenio, los estudiantes aparecerán como contribuidores junto con el copyright. Además, cualquier biblioteca autorizada también se debe colocar la licencia y el copyright en el archivo LICENSE.md en su carpeta respectiva.

 # Glosario
 - **Aplicacion web:** Herramienta que los usuarios pueden acceder por medio de un servidor web.
 - **Base de Datos:** Coleccion de registros o informacion que tienen alguna relacion entre si.
 - **DBMS:** Data Base Management System o sistema administrador de Bases de Datos.
- **Interfaz grafica:** Se utiliza en informática para nombrar a la conexión funcional entre dos sistemas, programas, dispositivos o componentes de cualquier tipo, que proporciona una comunicación de distintos niveles, permitiendo el intercambio de información.
- **Servidor:** Es un programa informatico que procesa la informacion y realiza conexiones sincronas o asincronas para responder a un cliente.
- **SQL:** Structure Querry Language o lenguaje estructurado de Consultas, este lenguaje es por el cual se lleva a cabo la creacion y administracion de bases de datos.


___
___
___




# MANUAL  DE USUARIO

UNIVERSIDAD DE SAN CARLOS DE GUATEMALA  
FACULTAD DE INGENIERÍA  
ESCUELA DE CIENCIAS Y SISTEMAS  
CURSO: SISTEMAS DE BASES DE DATOS 1  
ESCUELA DE VACACIONES DICIEMBRE 2020 
___

## TytusDB
![](https://upload.wikimedia.org/wikipedia/commons/4/4a/Usac_logo.png)
___
## Team 11
- JORGE JUAREZ - 201807022
- JOSE MORAN - 201807455
- ROMAEL PEREZ - 201213545
___
## Índice
- [Descripción General](Descripción-general)
- [Interfaz gráfica](Interfaz-gráfica)
    - [Ventana principal](Ventana-principal)
    - [Estadisticas](Estadisticas)
    - [Menu](Menu)
- [Glosario](Glosario)
___
# Descripción general 
TytusDB en su version web es una nueva alternativa de DBMS, el diseño del cliente web esta basado en el pgadmin de PostgreSQL.
Dentro de esta aplicacion web se puede navegar dentro de las distintas bases de datos.
___
# Alcance de proyecto
Debido a que el proyecto se encuentra en su primera fase, dentro de esta entrega se cuenta unicamente con la interfaz de usuario, conexión al servidor de prueba.
En la siguiente fase seran implementadas todas las funcionalidades.
___
# Interfaz gráfica
 TytusDB en su version web cuenta con una interfaz grafica que facilita la creación y manejo de bases de datos. Por medio de la misma, el usuario podrá crear, administrar y visualizar las bases de datos creadas a traves de botones y un area de edición.

 # Ventana Principal
 ![Ventana Principal](https://imgur.com/mMsAxVX.png)
 
Los componentes principales de TytysDB web son:

- **Area de conexión con el servidor**
- **Area de edicion:** Es donde se escribirán las sentncias SQL para la creacion y administracion de las bases de datos.
- **Area de errores:** Mostrará los distintos errores en caso existan.

# Menu
![manejo](https://imgur.com/79HixpY.png)

Cuenta con distintas opciones que ayudan a tener una mejor administracion de las base de datos por ejemplo:
- **File:** Administracion de distintos archivos (abrir, guardar, etc.)
- **Tools:** Herramientas necesarias para la administracion
- **Help:** Brinda soporte para la administracion

# Update
![update](https://imgur.com/lgVXh2E.png)

En este apartado se pueden observar el servidor al cual se esta conectado, las bases de datos creadas y tablas.

# SQL
![SQL](https://imgur.com/7v1mmYY.png)
En la pestaña SQL se observa el area de edicion con codigo en SQL para crear y administrar bases de datos dentro del sistema TytusDB.

# Resultados
![Resultados](https://imgur.com/bQh8SwB.png)

En la pestña de Resultados se observan los resultados a las consultas realizadas por medio del lenguaje SQL a las bases de datos creadas.

# Estadisticas
![Estadisitcas](https://imgur.com/0g0cnBi.png)

En esta pestaña se visualizaran las estadisticas concernientes a las bases de datos.
 ___
 # Glosario
 - **Aplicacion web:** Herramienta que los usuarios pueden acceder por medio de un servidor web.
 - **Base de Datos:** Coleccion de registros o informacion que tienen alguna relacion entre si.
 - **DBMS:** Data Base Management System o sistema administrador de Bases de Datos.
- **Interfaz grafica:** Se utiliza en informática para nombrar a la conexión funcional entre dos sistemas, programas, dispositivos o componentes de cualquier tipo, que proporciona una comunicación de distintos niveles, permitiendo el intercambio de información.
- **Servidor:** Es un programa informatico que procesa la informacion y realiza conexiones sincronas o asincronas para responder a un cliente.
- **SQL:** Structure Querry Language o lenguaje estructurado de Consultas, este lenguaje es por el cual se lleva a cabo la creacion y administracion de bases de datos.

