# Manual técnico
UNIVERSIDAD DE SAN CARLOS DE GUATEMALA<br>
FACULTAD DE INGENIERIA<br>
ESCUELA DE SISTEMAS<br>
SISTEMAS DE BASES DE DATOS 1 - A<br>
ESCUELA DE VACACIONES - DICIEMBRE 2020<br>

| <h2>Tabla de Contenido</h2> |
| ----- |
| [Integrantes](##Integrantes) |
| [Objetivos](##Objetivos) |
| [Alcance](##Alcance) |
| [Requisitos técnicos](##Requisitos-técnicos) |
| [Arquitectura](##Arquitectura) |
| [Descripción](##Descripción) |
| [Funcionamiento](##Funcionamiento) |
| [Modelos UML](##Modelos-UML) |
| [Funciones](##Funciones) |

## Integrantes
| Carné | Nombre |
| ---- | ---- |
| 201602907 | [BRYAN GONZÁLEZ](https://github.com/bmoisesg) |
| 201602890 | [JOSUE ABELARDE](https://github.com/Abelarde) |
| 201602942 | [MARIO TUN](https://github.com/mariotun) |
| 201602782 | [SERGIO OTZOY](https://github.com/Otzoy97) |


## Objetivos
* Utilizar diagramas para explicar la comunicación entre cliente-servidor de la aplicación
* Explicar el viaje de una petición HTTP desde el cliente al servidor
* Explicar el flujo de ejecución del servidor, luego de recibir una petición.

## Alcance
Este manual está dirigido a cualquier persona que tengan conocimientos en aplicaciones web y desea probar la comunicación entre un servidor y cliente de forma local.

La aplicación consta de un servidor web Python (Flask) y un cliente web Angular. El servidor web, además, depende de un interprete de SQL.

## Requisitos técnicos
- Windows 10
- 1 GB de espacio libre en el disco
- 8 GB de RAM
- Python 3.8.5
- pip para Python 3.8.5 (la versión más reciente)
- Angular CLI

## Arquitectura
![Arquitectura Cliente Servidor](capturas/arq_app.png?raw=true "")

### Correr cliente
Para correr el cliente es necesario ubicarse en la carpeta [cliente](../../../client/fase2/team05) y ejecutar los siguientes comandos:


```cmd
$ npm install
$ ng serve
```

El primer comando instala las dependencias del cliente web para poder funcionar, el siguiente comando <i>levanta</i> el cliente [http://localhost:4000](http://localhost:4000)

### Correr servidor
Para correr el servidor es necesario ubicarse en la carpeta del [servidor](../../../server/fase2/team05) y ejecutar los siguientes comandos:

```bash
$ pip install --user pipenv
$ pipenv install
$ pipenv shell
$ python app.py
```
El primer comando instala un entorno virtual para ejecutar de forma asilada y controlada el servidor; luego crea el entorno virutal (anteriormente mencionado) e instala las dependencias (dentro de el entorno recién creado) necesarias para levantar el servidor; después abre una consola que accede al entorno virtual en cuestión y por último intenta levantar el servidor. 

Si no muestra ningún error, el servidor debería de correr en [http://localhost:5000](http://localhost:5000)

## Descripción
La aplicación consta de un cliente en Angular y un servidor Python (Flask) para correr sobre Windows 10x64 (o superior)

- Cliente
    - Angular CLI: 11.0.5
    - Node: 14.15.3
    - OS: win32 x64
- Servidor
    - Python 3.8.5

El [cliente Angular](../../../client/fase2/team05) posee 4 componentes y 3 servicios:
- Componentes
  - navbar
  - tree
  - editor
  - tabla
- Servicios
  - database
  - share
  - tableData

El [servidor Python](../../../server/fase2/team05) (Flask) posee 4 archivo que componen la API y una librería (SQL Parser)
- API
  - <span>app.py</span>
  - router/index.py
  - router/database.py - endpoints:
    - db/create
    - db/showall
  - router/query.py - endpoints:
    - query/exec
- Libreria
  - Fase1 (contiene el SQL Parser)

## Funcionamiento
- El cliente realiza una petición (request) POST o GET a través de los servicios de Angular
- El servidor recibe la petición
- El servidor envía el query al SQL Parser
- El servidor recibe la respuesta del SQL Parser y envía la respuesta al cliente
- El cliente recibe la respuesta (response) y actualiza la vista (si fuese necesario) con los datos recibidos

## Modelos UML
### Diagrama de paquetes para el servidor Python (Flask)
![Diagrama servidor](capturas/uml_server.png?raw=true "")
### Diagrama de clases para el cliente Angular
![Diagrama servidor](capturas/uml_client.png?raw=true "")

## Funciones
* Ejecución de querys (utilizando SQL Parser)
* Creación de bases de datos
* Mostrar bases de datos y sus tablas