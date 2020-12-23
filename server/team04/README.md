
# [BD1] TyTusDB


## Información General
- SO: Linux-Ubuntu 20.04
- Lenguaje: Python
- Grupo 4
- Diciembre 2020

**Librerias necesarias**

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
```

**Declarando variable para puerto (8000)**

```python
PORT = 8000
```

**Para manegar las peticiones debemos definir y declarar el handler**

```python
class MyRequestHandler(BaseHTTPRequestHandler):
    ...
```

> La clase MyRequestHandler será la encargada de manejar todas las peticiones, esta clase implementa la interfaz BaseHTTPRequestHandler la cual nos permitirá sobreescribir los métodos do_GET y do_POST para configurar y setear las peticiones GET y POST respectivamente.



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