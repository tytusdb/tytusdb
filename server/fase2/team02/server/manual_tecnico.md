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

#### run
~~~
app.run(port=, host=)
~~~
Con esta instruccion se pone a escuchar al servidor, definiendole el puerto, y el host

## Version sistema
- Lenguaje: Python version 3.9.1
- SO: Windows 10
- RAM 8 GB


