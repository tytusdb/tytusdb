# Documentación técnica
> TytusDB es un proyecto Open Source para desarrollar un administrador de bases de datos. Está compuesto por tres componentes interrelacionados: el administrador de almacenamiento de la base de datos; El administrador de la base de datos, este administrador se compone a su vez de un servidor y de un cliente; y el SQL Parser.  — [Documentación Oficial](https://github.com/tytusdb/tytus)

## Contenido
- [Administrador de almacenamiento](#adminStorage)
    - [Modos de almacenamiento](#storageMode)
- [Administrador de la base de datos](#adminDB)
    - [Servidor](#server)
    - [Cliente](#client)
- [SQL Parser](#parser)
- [Angular y Electrón](#angularElectron)
- [Instalador](#instalador)
- [Instalador del Servidor](#instaladorServer) 
- [Librerías y Frameworks](#librerias)


## Administrador de almacenamiento<a name="adminStorage"></a>
Este componente es el encargado de gestionar, archivar, organizar y compartir los bytes de informacion del almacenamiento de las bases de datos, proporcionando al servidor un conjunto de funciones para extraer la información.

### Modos de almacenamiento<a name="storageMode"></a>
- **Árbol AVL** *(Grupo 14)*
    - [Manual Técnico](../storage/AVL/docs/TechnicalManual.md)
    - [Manual de Usuario](../storage/AVL/docs/UserManual.md)
- **Árbol B** *(Grupo 15)*
    - [Manual Técnico](../storage/BTree/docs/Manual_de_Usuario.md)
    - [Manual de Usuario](../storage/BTree/docs/Manual_Tecnico.md)
- **Árbol B+** *(Grupo 16)*
    - [Manual Técnico](../storage/BPTree/doc/techManual_doc.md)
    - [Manual de Usuario](../storage/BPTree/doc/userManual_doc.md)
- **ISAM** *(Grupo 17)*
    - [Manual Técnico](../storage/ISAM/doc/Technical_guide.md)
    - [Manual de Usuario](../storage/ISAM/doc/user_guide.md)
- **Tablas Hash** *(Grupo 18)*
    - [Manual Técnico](../storage/Hash/docs/Manual_tecnico.md)
    - [Manual de Usuario](../storage/Hash/docs/Manual_de_usuario.md)
- Archivos JSON

## Administrador de la base de datos<a name="adminDB"></a>
### Servidor<a name="server"></a>
Es un servidor http. Se debe seleccionar un puerto adecuado que no tenga conflictos con otros servidores. Se tiene un usuario admin y su contraseña. Además, se puede crear n usuarios configurando el acceso a las bases de datos.

Componente utilizado *Grupo 5:*
- [Manual](../server/README.md)

### Cliente<a name="client"></a>
Es un cliente que para algunos equipos será web y para otros será una aplicación de escritorio. Este cliente se conectará al servidor y podrá hacer la mayoría de las operaciones que hace pgadmin de PostgreSQL. Dentro del cliente, cuando se navegue dentro de las diferentes bases de datos que existen se puede invocar un editor de queries.

Componente utilizado *Grupo 5:*
- [Manual Técnico](../client/team05/TECNICO.md)
- [Manual de Usuario](../client/team05/README.md)

## SQL Parser<a name="parser"></a>
Este componente proporciona al servidor una función encargada de interpretar sentencias del subconjunto del lenguaje SQL especificado en la [sintáxis](../docs/sql_syntax/README.md).

Componente utilizado *Grupo 28:*
- [Manual Técnico](../parserT28/docs/Manual_Tecnico.md)
- [Manual de Usuario](../parserT28/docs/Manual_de_Usuario.md)

## Angular y Electrón<a name="angularElectron"></a>
### Configurando Electrón
Se crea un archivo Typescript llamado “main.ts” y otro de tipo JSON llamado “tsconfig.json”, donde se añade la configuración de Typescript dentro de la carpeta “electron”.
Esta carpeta es la que se crea en la carpeta raíz de la app el cual será el back-end de Electron y es donde se va a configurar todos los eventos relacionados con Electron.

Se modifica el archivo "tsconfig.json" tomando en cuenta que outDir se ubicará en "./dist" y el tipo de module que se usa es "commonjs", donde se esta montando el apartado de Electrón. Se ubica en el fichero “main.ts”, que será el encargado de lanzar nuestra app Angular, como una aplicación de Escritorio con Electrón.

### Definiendo el fichero principal de Electrón
Primero se añade los imports necesarios y se hace la referencia a la ventana del navegador.
También se registran algunos listener para tener las notificaciones del estado de la app, y se crea una nueva ventana de Electron para colocar nuestra aplicación Angular.

### Integrando Angular en Electrón
Lo que se realiza es habilitar la opción para que se integrar la aplicación de Angular dentro de Electrón. Para poder realizarlo, en la ventana del navegador esta el método llamado "loadUrl". Con ese método se carga el "index.html" de la aplicacion de Angular ya compilada.

### Compilando main.ts e inicializar Electrón
Para compilar el "main.ts" a JavaScript, se crea un nuevo script dentro de la seccion de script package.json y se le da el nombre de "electron". Tambien se le da un punto de entrada de la aplicación de Electrón, especificando la propiedad "main".

Se ejecula el script "electron" para inicializar la aplicación de Electron, con el siguiente comando.
``` bash
npm run electron
```
Al ejecutar y compilar todo correctamente, ya esta lista la app.

## Instalador<a name="instalador"></a>
### Instalar el paquete de Electron
Comando para usar en scripts npm.
``` bash
npm install electron-packager --save-dev
```
Comando para utilizar en cli.
``` bash
npm install electron-packager -g
```

### Construir el paquete de Windows desde la terminal
Comando para crear el ejecutable de Windows.
``` bash
electron-packager ./ --overwrite --platform=win32 --arch=x64 tytusDB
```

## Instalador del Servidor  <a name="instaladorServer"> </a>

Para crear un ejecutable con Python necesitamos contar con Python y pip. 

### Instalar PyInstaller 

Comando para instalar PyInstaller con pip 

``` bash
pip install pyinstaller 
```

### Empaquetar Aplicación 

Nos ubicamos en la carpeta en donde se encuentra nuestro archivo que se encarga del funcionamiento de la aplicación.

Comando para generar una carpeta con el ejecutable, solo necesitamos el nombre de nuestro archivo. 

``` bash
pyinstaller main.py 
```

Luego se puede comprimir la carpeta para poder mandarla al cliente y ejecutar el archivo .exe que se genero. 

## Librerías y Frameworks <a name="librerias"></a>


### Librerías de Python 

- pip install PIL
- pip install pillow
- pip install flask
- pip install flask-cors
- pip install pandas
- pip install prettytable

### Librerías de Node

- Electron: Electron Packager "^15.2.0"
- Angular: "^11.0.3"
- Jquery: "^3.5.1"
- CodeMirror: "^5.58.3"
