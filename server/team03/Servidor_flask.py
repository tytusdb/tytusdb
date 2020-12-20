from flask import Flask, request

app = Flask(__name__)

@app.route('/prueba',methods = ['GET'])
def prueba():
    return 'prueba'

@app.route('/prueba2', methods = ['POST'])
def prueba2():
    if request.method == 'POST':
        content = request.get_json()
        name = content['name']

        try:
            response = "hola " + name
            return response
        except ClientError as e:
            logging.error(e)
            return e.response