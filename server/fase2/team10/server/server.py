import socket
import json
import sys
import pickle
import analizer.interpreter as interpreter

def importFile(name):
    try:
        with open("./" + name + ".json", "r") as file:
            databases = json.load(file)
            return databases
    except:
        if name == "Databases":
            return []
        return {}

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serv_add = ('localhost', 10000)
print("hi")
serv.bind(serv_add)

serv.listen(1)


while True:    
    print("waiting for connection")
    #obj = interpreter.execution("create database prueba3; use prueba1; drop table cliente ; create table cliente(id integer primary key);");
    #print(obj)
    #print("send data")
    #json_data = json.dumps(obj, sort_keys=False, indent=2)
    #print("data %s" % json_data)
    connection, client_address = serv.accept()
    try:
        print(client_address)
        while True:
            data = connection.recv(4096)
            print(data.decode('utf-8'))

            #recibimos el script del query tool y la decodificamos a utf 8 
            scritp_sql = data.decode('utf-8')
            temp = {}

            #Verificamos si es un query de base de datos o un servicion de tytus
            if scritp_sql == 'tytus.connect_server':
                messages = []
                messages.append('Servidor y cliente se han sincronizado.\n')
                temp = {
                    "obj": {
                        "messages": messages,
                        "querys": [],
                        "lexical": [],
                        "syntax": [],
                        "semantic": [],
                        "postgres": [],
                        "symbols": [],
                        "indexes": [],
                    },
                    "databases": importFile("Databases")
                }        
            else:
                obj = interpreter.execution(scritp_sql)
                temp = {"obj": obj, "databases":importFile("Databases")} 

            #Preparamos los datos de retorno
            json_data = json.dumps(temp, sort_keys=False, indent=2)
            #Realiza la interpretacion
            ##obj = interpreter.execution(scritp_sql)
            #temp = {"obj": obj, "databases":importFile("Databases")} 
            #json_data = json.dumps(temp, sort_keys=False, indent=2)
            #Imprimimos el json desde el server
            print("data %s" % json_data)
            if data:
                #connection.sendall(pickle.dumps(obj))
                #mandamos la data obtenida del analisis como obj json
                connection.sendall(json_data.encode())
            else:
                print("end data")
                break
    finally:
        connection.close()

