# [BD1] TyTusDB
#### Universidad de San Carlos de Guatemala, Diciembre 2020
> Integrantes
> - Cinthya Andrea Palomo Galvez 201700670
> - Karla Julissa Ajtún Velásquez 201700565
> - Javier Alejandro Monterroso Lopez 201700831
> - Byron Antonio Orellana Alburez 201700733

**Configuración de Rutas**

```python
import sys
sys.path.append('../../../../parser/team26/G26')
sys.path.append('../../../../parser/team26/G26/Utils')
sys.path.append('../../../../parser/team26/G26/Expresiones')
sys.path.append('../../../../parser/team26/G26/Instrucciones')
sys.path.append('../../../../parser/team26/G26/Librerias')
sys.path.append('../../../../storage/storageManager')
```
> Estos paquetes se importan de el parser del grupo de Compiladores 2, así como el almacenamiento del storageManager de Estructura de Datos

**Librerías necesarias para la comunicación del servidor**

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
```

**Librerías necesarias para el funcionamiento del parser**
```python
import json
import gramatica as g
import Utils.Lista as l
import jsonMode as storage
import Instrucciones.DML.select as select
from Error import *
```
> Se utiliza por defecto el puerto: `PORT=8000`

> Se realizan las siguientes peticiones tipo *GET* hacia el ***Store Manager*** a través del ***Query tool***

```python
if self.path == '/getUsers': #Obtiene a los usuarios dentro del Store Manager 
self.do_getUsers()
elif self.path =='/getDB': #Obtiene las bases de datos existentes en el Store Manager
self.do_getDB()
```

> Se realizan las siguientes peticiones tipo *POST* hacia el ***Store Manager*** a través del ***Query tool***

```python
if self.path == "/":
self.do_root()
elif self.path == "/checkLogin": #Compara las credeciales del inicio de sesion
self.do_Check()
elif self.path == "/createUser": #Crea un usuario nuevo en el Store Manager
self.do_createUser()
elif self.path == "/dataquery": #Envia una consulta desde la consola para el Query Tool
self.do_dataquery()
```

> Al momento de realizar una consulta desde el editor de texto, se envía la petición **/dataquery** por lo que tiene una respuesta desde el parser, la cual se recibe y se lee en un formato Json, la cual es procesada y mostrada y enviada hacia el cliente

*Ejemplo de método de respuesta de una consulta*
```python
def do_getUsers(self):
url = "../../../../server/fase2/team08/Server/data/json/TEST-TBUSUARIO"
try:
myFile = open(url).read()
self.send_response(200)
except:
myFile = "File not found"
self.send_response(404)
self.send_header('Content-type', 'application/json')
self.end_headers()
self.wfile.write(bytes(myFile, 'utf-8'))
```

**Iniciar el servidor manualmente**

> Para iniciar el servidor se necesita tener al menos 
* Python Versión 3.8
* Graphviz (cualquier versión)
* ply (version 4>)
> El servidor se inicia dentro de la carpeta Server con el comando
```
python3 server.py
```
> Para detener el servidor
```
CTRL+C
```
