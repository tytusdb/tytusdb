# Cliente Tytus DB (FASE I)

## Información General
- SO: Linux-Ubuntu 20.04
- Lenguaje: Python
- Grupo 4
- Diciembre 2020

## Manual Tecnico

**Librerias necesarias**

```python
import tkinter as tk
from tkinter import *
import http.client
import json
```

**Arbol.py**

- Nota
En la zona izquierda de la pantalla, se puede ver el arbol de navegacion del DBMS, donde estan las bases de datos creadas


```python
class Arbol(Frame):
    ...
```

> La clase Arbol ultiliza el treeview de Tkinter para crear el panel izquierdo del cliente, hace referencia a las imagenes de la carpeta "resources" para mostrar los iconos en el arbol. La clase es un tipo Frame que almacena toda la treeview.

**Campo.py**

Se crea el campo de texto enumerado que se utiliza en tytusDB.

```python
class TextLineNumbers(Canvas):
    ...
```

> La clase crea un canvas que muestra la cantidad de lineas de un Text, se autogenera a la hora de crear una nueva linea en el Text y decrese cuando se borra una linea.

```python
class CustomText(Text):
    ...
```

> Un Text manejado por completamente en esta clase, se utilizara en la segunda fase para mejorar la forma de manejar Querys en la interfaz, un ejemplo seria resaltando palabras identificadoras.

```python
class Campo(Frame):
    ...
```

> Aqui se maneja el campo de texto, utiliza dos clases mas para poder mostrar el numero de lineas. TextLineNumbers crea un widget que genera las lineas dependiendo del area de Texto, CustomText crea el area de texto con la que se conectara el TextLineNumbers. Todo entre en el frame de creado por la clase Campo.

```python
class MyDialog(tkinter.simpledialog.Dialog):
    ...
```

> Crea un widget Dialog para manejar dos campos, usuario y contraseña, los que se utilizan para enviar parametros al servidor.

**Ventana.py**

El centro de todo el cliente, aqui se manejan todas las clases para crear la interfaz y la conexion con el servidor.

***Variables Globales***

```python
control = 0
notebook = None
consola = None
```
> Se utiliza control para saber en que pestaña se ubica el usuario.
> Se utiliza notebook para el control de las pestañas en todo momento y de su contenido.
> Consola se usa para darle los valores necesarios determinados por las acciones del usuario.

***Metodos***

```python
def CrearMenu(masterRoot):
    ...
```
> En este método se crea la barra del menú de la aplicación, esta compuesta de 4 opciones principales: Archivo, Editar, Herramientas y ayuda. cada una tiene un submenú, en el de archivo, que es uno de los más relevantes, se encuentra la opción de guardar, guardar Como, cerrar archivo y abrir un documento. Para hacer esta parte de la interfaz se utilizó la clase "Menu" de tkinter,  y se utilizó uno de sus métodos que es "add_command".

```python
def abrir():
    ...
```
> Este método se creó para abrir documentos .sql, se importó la librería "os" para acceder a los métodos para el manejo de archivos, se utilizó global para poder usar variables declaradas afuera del ámbito, en la variable archivo se guarda el archivo que se desea abrir, y luego se pregunta si el archivo no está vació, si no lo está, se podrá acceder al nombre de este y se manda a llamar al método "añadir" para agregar la nueva pestaña y poder visualizar el archivo.

```python
def Spellcheck(self):
    ...
```
Este metodo se encarga de resaltar con colores las palabras reservadas que se escriben
dentro del campo de texto.

```python
def getDatabases():
    ...
```
Este metodo se encarga se encarga de generar el arbor de forma automatica

```python
def guardarComo():
    ...
```
> Este método se creó para poder guardar un archivo nuevo, es decir; se ha creado dentro de la aplicación, aquí se accede al índice actual, es decir; al indice que el usuario está usando, para poder guardar el archivo, luego de ello se abre el gestor de archivos para agregar el nombre.

```python
def guardarArchivo():
    ...
```
> Este método esi similar al de guardarComo, con excepción de que este se sobre escribe al archivo anteriormente abierto.

```python
def cerrarPestaña():
    ...
```
> Este método es pequeño, ya que solamente cierra la pestaña actual en la que está el usuario, para ellos se utiliza nuestra etiqueta donde hacemos referencia al objeto Notebook y usamos el select para obtener el indice, luego utilizamos el "index" para convertirlo a entero y finalmente aplicamos el método "forget" para cerrar esa pestaña.

```python
def CrearVentana():
    ...
```
> Conecta todo en un frame para crear el cliente.

```python
def añadir(titulo):
    ...
```
> En este método se crean las pestañas, para ello se creó un arreglo donde se guardará cada pestaña que se cree, se utilizó el método appened para añadir más páginas al notebook, y también sus cajas de texto.

```python
def LogIn():
    ...
```
> Crea el Dialog donde se colocaran las credenciales de usuario y contraseña, luego se vera en el servidor si son correctas.

```python
def myGET():
    ...
```
> Metodo de conexion al servidor por medio de un una peticion GET, se conecta al servidor y pide los usuarios que este contenga por medio de la peticion "/getUsers". La respuesta que regrese el servidor sera colocada en la consola de salida.

```python
def myPOST():
    ...
```
> Metodo de conexion al servidor por medio de un una peticion POST, se toman los valores obtenidos del metodo LogIn, estos se convierten a JSON para enviar la informacion con la peticion "/checkLogin". Luego de la peticion se espera la respuesta y se colocae en la consola de salida.

```python
def crearUsuario():
    ...
```
> Por medio de un Dialog, generado por la clase MyDialog, se obtiene dos valores (usuario y contraseña), estos son casteados a formato JSON y enviados al servidor con un metodo POST con la peticion "/createUser", del lado del servidor los valores se agregaran al registro de usuarios.

***Conexion cliente-servidor***

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

> Al dar clic en la opción GET se puede ver que se registró el usuario exitosamente.

## Manual de Usuario (Server)

las librerias necesarias para el servidor son:
- HTTPServer
- BaseHTTPRequestHandler

El puerto que se utilizo es el puerto:
 - 8000

> Debido a que el servidor trabaja de forma interna no se necesita más que una línea de comando, la función de este comando es conectar al servidor en su respectivo puerto para que pueda recibir las peticiones desde la aplicación. El puerto que se decidió utilizar fue el 8000. A continuación se muestra una imagen de como se debe ingresar dicho comando.

![Interfaz inicial](resources/server.png?raw=true "Conexión del servidor") 

## Iniciar la interfaz

Se utiliza:
```
python ventana.py
```
