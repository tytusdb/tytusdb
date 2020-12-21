from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Codigo de consulta sql
@app.route('/execute', methods=['POST'])
def execute():
    req_data = request.get_json()
    print(req_data['code'])
    return ('procesando..')

#Creando base de datos
@app.route('/Create_DB', methods=['POST'])
def Create_DB ():
    return 'Creando Base de datos..'

#Borrando base de datos
@app.route('/Drop_DB', methods=['POST'])
def Drop_DB ():
    return 'Borrando Base de datos..'

#Creando Tabla
@app.route('/Create_Table', methods=['POST'])
def Create_Table ():
    return 'Creando tabla..'

if __name__ == '__main__':
    app.run()