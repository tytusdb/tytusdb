# MANUAL TECNICO G2

## Servidor

Para crearlo se utilizo:
  - libreria FLASK
  - libreria cors_flask
  - Puerto 10000
  - Host 0.0.0.0

### Inicializando servidor
~~~
app = Flask(__name__)
CORS(app)
~~~
Con esta instruccion se inicializa el servidor y se habilita que el cliente pueda enviarle peticiones sin ningun problema

#### Conectar
~~~
@app.route('/conexionBD', methods=['POST'])
def conectar():
~~~
El servidor responde a una peticion POST para conectarse a la base de datos, con esta funcion verifica que los datos del usuario recibidos, sean validos, de ser asi, retorna un mensaje en JSON aceptando la conexion o rechazandola

### Query
@app.route('/query',methods=['POST'])
def transaccionar():
~~~
Recibe las peticiones del cliente y se encarga de realizar las peticiones a la base de datos. Finalmente retorna el resultado al cliente en formato JSON.

### Users
@app.route('/newUser', methods=['POST'])
def addUser():
~~~
Añade un nuevo usuario a la conexión. Recibe como entrada el nombre del usuario y la contraseña en formato JSON. Si el usuario ya existe, se retorna un mensaje indicando que el nombre ya ha sido tomado, de lo contrario los datos son almacenados y se devuelve un mensaje indicando que el usuario ha sido creado.

#### run
~~~
app.run(port=, host=)
~~~
Con esta instruccion se pone a escuchar al servidor, definiendole el puerto, y el host

## Version sistema
- Lenguaje: Python version 3.9.1
- SO: Windows 10
- RAM 8 GB


