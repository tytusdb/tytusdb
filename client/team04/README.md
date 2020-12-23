# Cliente Tytus DB (FASE I)

## Información General
- SO: Linux-Ubuntu 20.04
- Lenguaje: Python
- Grupo 4
- Diciembre 2020

**Librerias necesarias**

```python
import tkinter as tk
from tkinter import *
import http.client
import json
```

**Variables Globales**
Con ellas se controlan las pestañas

```python
control = 0
notebook = None
```

**Clase Arbol**

```python
class Arbol(Frame):
    ...
```

> La clase Arbol ultiliza el treeview de Tkinter para crear el panel izquierdo del cliente, hace referencia a las imagenes de la carpeta "resources" para mostrar los iconos en el arbol.

**Clase Campo**

```python
class Campo(Frame):
    ...
```

> Aqui se maneja el campo de texto, utiliza dos clases mas para poder mostrar el numero de lineas. TextLineNumbers crea un widget que genera las lineas dependiendo del area de Texto, CustomText crea el area de texto con la que se conectara el TextLineNumbers.

**ventana.py**

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
> En este método se crean las pestañas, para ello se creó un arreglo donde se guardará cada pestaña que se cree, se utilzó el método appened para añadir más páginas al notebook, y también sus cajas de texto.

# Conexion cliente-servidor

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


## Iniciar la interfaz

Se utiliza:
```
python ventana.py
```

## Menu
Se crearon los menus Archivo, Editar, Herramientas y Ayuda. En la primera fase solo el menu ayuda y archivo tienen opciones utilizables.


## Campo de Texto
Un editor que tiene numero de linea, opcion para multiples pestañas y un scroll para su mejor manejo.

## Vista de Bases
El panel izquiero del cliente se utiliza para tener una mejor visualizacion de las bases de datos conectadas. Es un vista de arbol que se expande hasta llegar a las tablas.
