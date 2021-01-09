# Servidor Web Tytus

## Integrantes Grupo 9

**Encargados Cliente Web**

- 201700965 José Carlos I Alonzo Colocho
- 201700995 Luis Pedro Pineda Gonzalez

**Encargado del Servidor Python**

- 201700918 Cristian Alberto Suy Mejia

## Manual Tecnico

**Requisitos Minimos Servidor**

- Windows 10 o posterior
- Python 3.6.9 64-bit
- Flask
- Flask Cors
- PLY
- Graphviz

**Instalacion Dependencias**
Una vez se cuente con los requerimientos minimos, para la ejecucion del servidor se hace mediante la siguiente linea de comando desde la carpeta donde esta el servidor en consola 

```PowerShell
    C:Ubicacion/.../python ServerF.py
```

y la instalacion de algunas de las dependecias con los siguientes comandos

```PowerShell
    pip install flask
    pip install flask-corse
    pip install ply
    pip install graphviz
```

**Explicacion**

> Una vez cumpliendo con los requirimientos minimos procedemos a la exportacion de las librerias que utilizaremos

```python
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
```

> Flask nos ayudara para la comunicacion entre el cliente y el servidor, de esta libreria tambien necesitaremos jsonify el cual se encarga de retornar un archivo en formato json al cliente y request nos ayudara para poder utilizar para los metodos POST y PUT que vengan por parte del servidor, recibiendo el contenido de igual manera en formato json

```python
app = Flask(__name__)
CORS(app)
```

> Luego de importado cada libreria, se procede a iniciar la aplicacion que usaremos como servidor, el encargado de las rutas el cual es el app, y CORS es el encargado de poder recibir los fetch por parte del cliente.

**Creacion de las rutas**

> Una vez tengamos el app que nos ayudara para las rutas, procedemos a crear una ruta

```python
@app.route('/')
def raiz():
    print('estoy en el inicio')
    return jsonify({"mensaje":"Menu Principal"})
```

> Para poder iniciar una ruta colocamos @app.route, este metodo recibe 2 parametros siendo el 2do opcional, en este caso el primer parametro es la ruta y el segundo parametro es el metodo a realizar (GET, POST, PUT, DELETE, etc), si no se coloca ese parametro por defecto utiliza GET

```python
@app.route('/login', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = {
        "name": request.json['name'],
        "password": request.json['password']
    }
    usuarios.append(nuevo_usuario)
    print(request.json)
    return jsonify({"mensaje": "Exito"})
```
> Para la insercion de usuarios, utilizamos el metodo POST, asi que al momento de crear la ruta, nosotros colocamos el segundo parametro de la siguiente forma, haciendo entender que recibira un metodo POST methods=['POST'].

**Ejecucion de Querys**

> Este apartado al no tener aun el Parser de SQL, lo que hace esta funcion es nada mas retornar un json con el mensaje ejecutando Query

```python 
@app.route('/query')
def Ejecutar():
     global datos
    texto = request.json['query']
    #Esta es la parte de implementacion de Compiladores 2 y EDD
    instrucciones = g.parse(texto)
    erroresSemanticos = []
    salida = ""

    for instr in instrucciones['ast'] :

            if instr != None:
                result = instr.execute(datos)
                if isinstance(result, error):
                    salida = salida + str(result.desc) + "\n" #imprimir en consola
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    salida = salida + str(instr.ImprimirTabla(result)) + "\n" #imprimir en consola
                else:
                    salida = salida + str(result)  + "\n" #imprimir en consola

    errores = g.getMistakes()
    salidaE = ""
    for error1 in errores:
        salidaE += error1.toString() + "\n"
    salida = salida + salidaE  + "\n"
    errores.clear()
    erroresSemanticos.clear()

    del instrucciones
    print(salida)
    return jsonify({"mensaje":salida})
```

**Debug del server**

> Para correr el servidor y no tengas problemas de parar los servicios e iniciarlos de nuevo al momento de hacer un cambio, procedmos a crear una condicional de la siguiente manera 

```python
if __name__ == '__main__':
    app.run(debug=True, port=8888)
```
> Donde colocamos que haga un Debug automatico, y ademas el servidor se escuchara por el puerto 8888

## Manual de Usuario

**Interaccion con el usuario**

Al ingresar al sitio nos encontraremos con una ventana que nos pedira iniciar sesion, en esta las credenciales de administrador corresponden a los valores *Admin* *Admin*.

<p algin = "center">
    <img src = "img/login.png">
</p>

Luego de haber ingresado las credenciales para poder iniciar se nos presentara la pantalla en la cual cada ya se pueden realizar las acciones basicas y comunes con una base de datos.

<p align = "center">
    <img src = "img/inicio.png">
</p>

**Funciones** 

- Ejecutar, este ejecutara el script escrito en la consola de querys.

- Create backup, este realiza un backup de la base de datos.

- Help, desplega una pagina de ayuda que indica el funcionamiento en tytusDB.

- Create database, crea una nueva base de datos.

- Delete database, elimina una de las bases de datos existentes.

- Drop, esta elimina una tabla perteneciente a una base de datos.

- New script, esta limpiara la consola de querys para poder escribir un script desde cero.

- Open script, esta abrira un archivo localizado en nuestro computador que contenga una script.

