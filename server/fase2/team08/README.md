# [BD1] TyTusDB
#### Universidad de San Carlos de Guatemala, Diciembre 2020
> Integrantes
> - Cinthya Andrea Palomo Galvez 201700670
> - Karla Julissa Ajtún Velásquez 201700565
> - Javier Alejandro Monterroso Lopez 201700831
> - Byron Antonio Orellana Alburez 201700733

**Librerias necesarias**

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
```

**Confuración inicial y ejecución del servidor**

```python
myServer = HTTPServer(('localhost', PORT), MyRequestHandler)
print("Server running at localhost: " + str(PORT))
myServer.serve_forever()
```

> myServer es una instancia de un servidor HTTPServer el cual recibe como parámetros la tupla con el host y el puerto y también recibe el handler definido y configurado previamente.

**Iniciar el servidor manualmente**

    > python server.py

- Ctrl-C to stop the server

**Endpoints
    > Para el POST tenemos 3 Rutas principales cada 1 con diferente funcion
```python
if self.path == "/":
            self.do_root()
        elif self.path == "/checkLogin":
            self.do_Check()
        elif self.path == "/createUser":
            self.do_createUser()
        elif self.path == "/dataquery":
            self.do_dataquery()
```

>CheckLogin: Chequea las creedenciales para logearse
>createUser: Crea un nuevo usuario
>dataquery: envia el texto del editos para su posterior analizis por el Parser 