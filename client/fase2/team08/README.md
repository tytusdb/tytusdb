# Tytus DBMS Grupo # 08
### Cliente Desktop Linux
> - SO:Linux Ubuntu
> - Lenguaje: Python 3.9.0
#### Universidad de San Carlos de Guatemala, Diciembre 2020
> Integrantes
> - Cinthya Andrea Palomo Galvez 201700670
> - Karla Julissa Ajtún Velásquez 201700565
> - Javier Alejandro Monterroso Lopez 201700831
> - Byron Antonio Orellana Alburez 201700733

# Manual de Usuario
## Interfaz Grafica 
![Captura de pantalla de 2021-01-09 02-16-02](https://user-images.githubusercontent.com/36779113/104086838-a8d69b80-5220-11eb-80b0-56810a46dc7b.png)

## Editor de texto
La interfaz gráfica se compone de un editor de texto con resaltado de sintaxis sql en el cual podemos escribir consultas y nos genera la salida correspondiente en la parte inferior de la aplicación
## Arbol de Directorios
También se cuenta con un navegador en la barra lateral izquierda para poder visualizar las diferentes bases de datos a las que tenemos acceso
```python
class Arbol(Frame):
```
## Enviar Consulta
Se envia el texto en el area de texto al servidor para ser analizado y que se nos muestre en la consola de salida
```python
def DataQuery():
```
# Menú
## Archivo
![Captura de pantalla de 2021-01-09 01-49-50](https://user-images.githubusercontent.com/36779113/104086385-1c76a980-521d-11eb-873c-6fff65a57d53.jpg)

### Abrir Query
> - Abrir y buscar en el ordenador un nuevo query
```python
def abrir():
```
### Nueva Query 
> - Agregar una nueva pestaña
```python
def añadir(titulo):
```
### Guardar como...
> - Guardar el documento actual de la pestaña en un lugar específico
```python
def guardarComo():
```
### Guardar
> - Guardar el archivo
```python
def guardarArchivo():
```
### Cerrar pestaña actual
> - Cerrar la pestaña actual en uso
```python
def cerrarPestaña():
```
### Salir
> - Salir del frame
```python
def cerrarVentana():
```

## Herramientas
![Captura de pantalla de 2021-01-09 01-45-16](https://user-images.githubusercontent.com/36779113/104086390-2dbfb600-521d-11eb-93e2-194e7d7e511d.jpg)

### Limpiar consola
> - Limpia la consola
```python
def LimpiarConsola()::
```
### GET USERS
> - obtiene los usuarios de una tabla en específico
```python
def myGET():
```
### GET USERS INTERN
> - Obtiene los usuarios que ingresan al frame
```python
def Get_User():
```
### CREATE USER
> - Crea usuarios dentro del frame
```python
def crearUsuario():
```
### Refresh
> - Refresca la pantalla y reinicia el frame
```python
def refresh():
```
### Login
> - Ingreso a la base de datos
```python
def LogIn():
```

# Manual Técnico 
## Conexión con el servidor
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
## Librerias
### Http Client
Libreria que nos permite la comunicacion con el servidor y realizar peticiones web
```python
import http.client
```
### Tkinter
Es un binding de la biblioteca gráfica Tcl/Tk para el lenguaje de programación Python. Se considera un estándar para la interfaz gráfica de usuario (GUI) para Python, para lo que se instaló:
**versión utilizada para Python 3.9.0**
```python
sudo apt-get install python3-tk
```
y se importó las librerías:
```python
import tkinter
```
### PIL
Para la instalación de las imágenes se utilizó la librería PIL

```python
from PIL import ImageTk, Image
```
para instalarlo para Python 3:

```python
python3 -m pip install Pillow
pip install Pillow
```
se importó para el parser la librería prettytable, graphviz y supervisor:
```python
python -m pip install -U prettytable
pip3 install graphviz
pip3 install supervisor==4.1.0
```
