# Cliente Tytus DB (FASE II)

## Información General
- SO: Linux-Ubuntu 20.04
- Lenguaje: Python
- Grupo 4
- Diciembre 2020

## Manual Tecnico

- al momento de realizar click en GET se puede ver el registro del usuario efectuado exitosamente.

** Metodo Spellcheck(self) **
Este metodo se encarga de resaltar con colores las palabras reservadas que se escriben
dentro del campo de texto.

** getDatabases() **
Este metodo se encarga se encarga de generar el arbor de forma automatica

*** Para realizar: Conexion cliente-servidor***

```python
myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)
```

> Se crea la conexion con el servidor.

```python
headers = {
    "Content-type": "application/json"
    }
```

> Se establecen los headers para cada tipo de peticion

```python
myConnection.request("GET", "/getUsers", "", headers)
response = myConnection.getresponse()
```

> Se envia una peticion y "responde" obtiene la respuesta del servidor.

## Manual de usuario
> Al ingresar a TytuSQL se podrá apreciar una interfaz como la imagen que se presenta, la ventana principal está compuesta por una barra de menú que tiene las opciones principales y de más ayuda para el usuario.

![Interfaz inicial](resources/Ventan.PNG?raw=true "Inicio") 

> Como se puede ver, se dispone de un campo de texto enumerada para realizar  consultas, esta aplicación podrá abrir modelos y archivos .sql, en la opción archivo se encuentran las siguientes opciones:
- Nueva ventana: Abre una nueva ventana de TytuSQL.
- Abrir Query: Abre un archivo .sql en su respectiva pestaña.
- Abrir Modelo: Abre un modelo ER.
- Nueva Query: Abre una nueva pestaña con un campo de texto en blanco.
- Guardar como: Guarda un archivo que ha sido editado previamente en TytuSQL.
- Guardar: Sobreescribe un archivo previamente abierto.
- Cerrar pestaña actual: Cierra la pestaña en la que el usuario está.
- Salir: Se sale de la aplicación.

![Interfaz inicial](resources/abrir.png?raw=true "Inicio") 

Al darle clic en abrir, se podrá ver el archivo .sql desplegado en una pestaña diferente.

![Interfaz inicial](resources/archivo.png?raw=true "Inicio") 

**Herramientas**
> Como se puede observar en la imagen de abajo, se tiene una menú llamado opción, que a su vez contiene las siguientes opciones:
- Configuración
- Utilidades
- GET
- POS
- CREATE USER
![Herramientas](resources/herramientas.png?raw=true "Herramientas") 

**GET**
> Esta opción conecta con el servidor para poder obtener a los usuarios registrados en él

![GET](resources/get.png?raw=true "GET") 

**POS**
> Conecta con el servidor para loggearse con el usuario.

![POS](resources/pos.png?raw=true "POS") 

**CREATE USER**
> Al escoger esta opción se puede registrar un usuario a la base de datos.

![Creación de usuariol](resources/crearUser.png?raw=true "Crear usuario") 

> Se debe llenar los campos con usuario y contraseña.

![Interfaz inicial](resources/llenarCampos.png?raw=true "Llenar campos") 



## Manual de Usuario (Server)

> Debido a que el servidor trabaja de forma interna no se necesita más que una línea de comando, la función de este comando es conectar al servidor en su respectivo puerto para que pueda recibir las peticiones desde la aplicación. El puerto que se decidió utilizar fue el 8000. A continuación se muestra una imagen de como se debe ingresar dicho comando.

![Interfaz inicial](resources/server.png?raw=true "Conexión del servidor") 

## Iniciar la interfaz

Se utiliza:
```
python ventana.py
```

