# Tytus DBMS Grupo # 08
### Cliente Desktop Linux
#### Universidad de San Carlos de Guatemala, Diciembre 2020
> Integrantes
> - Cinthya Andrea Palomo Galvez 201700670
> - Karla Julissa Ajtún Velásquez 201700565
> - Javier Alejandro Monterroso Lopez 201700831
> - Byron Antonio Orellana Alburez 201700733

# Manual de Usuario
## Interfaz Grafica 
![WhatsApp Image 2021-01-08 at 8 19 29 PM](https://user-images.githubusercontent.com/14981793/104080686-18cc2e00-51ef-11eb-9488-e63eea236b8f.jpeg)

## Editor de texto
La interfaz gráfica se compone de un editor de texto con resaltado de sintaxis sql en el cual podemos escribir consultas y nos genera la salida correspondiente en la parte inferior de la aplicación
## Arbol de Directorios
También se cuenta con un navegador en la barra lateral izquierda para poder visualizar las diferentes bases de datos a las que tenemos acceso
## Enviar Consulta
Se envia el texto en el area de texto al servidor para ser analizado y que se nos muestre en la consola de salida
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
**versión utilizada para Python 3.8.5**
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
