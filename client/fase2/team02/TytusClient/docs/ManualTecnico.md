# TytusDB - Manual Técnico

Universidad de San Carlos de Guatemala  
Facultad de Ingeniería  
Cursos: 772 Estructuras de Datos | 774 Sistemas de Bases de Datos 1 | 781 Organización de Lenguajes y Compiladores 2  
Diciembre 2020

## Índice
- [TytusDB](#tytusdb)
- [Administrador de almacenamiento](#administrador-de-almacenamiento)
- [Administrador de la base de datos](#administrador-de-la-base-de-datos)
- [Librerias](#librerias)
- [Metodos o Funciones](#metodos-o-funciones)
- [Clases](#clases)
- [Query Tool](#query-tool)


## TytusDB

Es un proyecto Open Source para desarrollar un administrador de bases de datos el cual funciona por defecto en el puerto 10000. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos,  el administrador de la base de datos, este administrador se compone a su vez de un servidor y de un cliente ambos realizados con el lenguajes de programación python; y el SQL Parser.

## Administrador de almacenamiento

Este componente es el encargado de gestionar el almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para extraer la información.

## Administrador de la base de datos

El administrador de la base de datos se compone de dos componentes:

- Servidor: es un servidor http. Este servidor trabaja en el puerto 10000. En la carpeta de instalación de la base de datos se crea una carpeta llamada /data donde se almacenan las bases de datos. Por defecto existe un usuario admin y su contraseña la cual es 123. Además de crear n usuarios configurando el acceso a las bases de datos.

- Cliente: es un cliente tipo aplicación de escritorio en sistemas operativos windows. Este cliente se conectará al servidor y podrá hacer la mayoría de las operaciones que hace un adminisitrador de base de datos comunmente. Dentro del cliente, cuando se ejecute el cliente la aplicacion seguira el siguiente flujo de trabajo.

## Librerias

- TKinter: Es utilizada para la interfaz grafica de la aplicación.

- Requests: Nos permite comunicarnos al servidor por medio de la petición POST.

- Os: Nos facilita el acceso a archivos a la hora de abrir o guardar un script.

## Metodos o Funciones

- main(): Arranca la interfaz grafica y es donde inicia el flujo de ejecución de la aplicación.

- iniciarSesion(root): Permite enviar credenciales al servidor para poder validar al usuario y responde de acuerdo a la respuesta del servidor.

## Clases

### Example

Esta clase genera la interfaz grafica y la barra de herramientas.

#### Metodos o Funciones (Example)

- addQueryTool(self): Agrega una nueva pestaña sin texto para un nuevo script.

- run(self): Ejecuta el script dentro de la pestaña del query tool seleccionada.

- saveFile(self): Guarda el script dentro de nuestro computador.

- openFile(self): Permite abrir un script y mostralo en la aplicación.

### CustomNotebook

Esta clase genera el árbol de servidores en la aplicación

#### Metodos o Funciones (CustomNotebook)

- on_close_press(self, event): Permite abrir una rama y mostrar sus nodos hijo.

- on_close_release(self, event): Permite cerrar la rama y ocultar sus nodos hijo.

- initialize_custom_style(self): Inicializa el arbol de servidores.