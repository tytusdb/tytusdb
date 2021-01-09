#TyTusDB server. 
#Dev by Group 4
#BD1 2020

import sys
sys.path.append('../../../../parser/team26/G26/')
sys.path.append('../../../../parser/team26/G26/Utils')
sys.path.append('../../../../parser/team26/G26/Expresiones')
sys.path.append('../../../../parser/team26/G26/Instrucciones')
sys.path.append('../../../../storage/storageManager')

# Server imports
from http.server import HTTPServer, BaseHTTPRequestHandler
import io
import os
import json

# Parser imports
import Instrucciones.DML.select as select
from Error import *
import jsonMode as storage
import gramatica as g
import Utils.Lista as l

# Data list
storage.dropAll()
datos = l.Lista({}, '')


# Setting server port
PORT = 8000

#Def. requests handler.
class MyRequestHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        #Definiendo rutas para peticiones get
        if self.path == '/getUsers':           
            self.do_getUsers()
        elif self.path == '/getDatabases':
            self.do_getDatabases()
        else:
            self.send_response(400)
            self.wfile.write(bytes("",'utf-8'))
 
    def do_POST(self):
        #Definiendo rutas para peticiones post
        if self.path == "/":
            self.do_root()
        elif self.path == "/checkLogin":
            self.do_Check()
        elif self.path == "/createUser":
            self.do_createUser()
        elif self.path == "/runQuery":
            self.do_runQuery()
        else:
            self.send_response(400) 
            self.wfile.write(bytes("",'utf-8'))

    def do_runQuery(self):
        global datos
        
        dataSize = int(self.headers['Content-Length'])
        reqBody = self.rfile.read(dataSize)
        reqData = json.loads(reqBody.decode("utf-8"))
        texto = reqData["text"]

        ####################################################ENVIANDO AL PARSER

        instrucciones = g.parse(texto)
        erroresSemanticos = []
        contenido = ""
        text = ""


        for instr in instrucciones['ast']:
        
            if instr != None:
                result = instr.execute(datos)
                if isinstance(result, Error):
                    contenido = contenido + str(result.desc) + "\n"
                    erroresSemanticos.append(result)
                elif isinstance(instr, select.Select) or isinstance(instr, select.QuerysSelect):
                    contenido = contenido + str(instr.ImprimirTabla(result))  + "\n"
                else:
                    contenido = contenido + str(result) + "\n"

        databases = ""
        url = "../../../../parser/team26/G26/data/json/databases"
        try:
            databases = open(url).read()
        except:
            databases = ""
            print("F")
        
        ####################################################FIN PARSER    
        
        respuesta = { "consola": contenido, "jsonText": text, "databases": databases }
        myJsonResponse = json.dumps(respuesta)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(myJsonResponse,'utf-8'))

    def do_createUser(self):
        try:
            dataSize = int(self.headers['Content-Length'])
            reqBody = self.rfile.read(dataSize)
            reqData = json.loads(reqBody.decode("utf-8"))
            username = reqData["username"]
            password = reqData["password"]
            print("Data received: " + str(reqData))
            url = "./data/tytus.json"
            myFile = open(url).read()
            jsonResponse = json.loads(myFile)
            existe = False
            for user in jsonResponse:
                if user["username"] == username:
                    existe = True
            if existe is False:
                jsonResponse.append({ "username": username, "password": password })
                jsonFormatted = json.dumps(jsonResponse, indent=2)
                self.saveFile("tytus.json", bytes(jsonFormatted, 'utf-8'))       
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(existe),'utf-8'))
        except:
            myFile = "error"
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(myFile, 'utf-8'))
    
    def do_Check(self):
        try:
            dataSize = int(self.headers['Content-Length'])
            reqBody = self.rfile.read(dataSize)
            reqData = json.loads(reqBody.decode("utf-8"))
            username = reqData["username"]
            password = reqData["password"]
            print("Data received: " + str(reqData))
            url = "./data/tytus.json"
            myFile = open(url).read()
            jsonResponse = json.loads(myFile)
            join = False
            for user in jsonResponse:
                if user["username"] == username and user["password"] == password:
                    join = True               
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(join),'utf-8'))
        except:
            myFile = "error"
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(myFile, 'utf-8'))

    def do_getUsers(self):
        myFile = ""
        url = "./data/tytus.json"
        try:
            myFile = open(url).read()
            self.send_response(200)
        except:
            myFile = "File not found"
            self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(myFile, 'utf-8'))

    def do_getDatabases(self):

        text = ""
        try:
            f = open("../../../../parser/team26/G26/Utils/tabla.txt", "r")
            text = f.read()
            text = text.replace('\'','"')
            text = text.replace('False','"False"')
            text = text.replace('None','""')
            text = text.replace('True','"True"')
        except:
            text = ""

        databases = ""
        try:
            databases = open("../../../../parser/team26/G26/data/json/databases").read()           
        except:
            databases = ""
        self.send_response(200)
        respuesta = { "jsonText": text, "databases": databases }
        myJsonResponse = json.dumps(respuesta)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(myJsonResponse, 'utf-8'))
         
    def do_root(self):
        dataSize = int(self.headers['Content-Length']) #Getting size of data
        myData = self.rfile.read(dataSize) #Reading data (form)
        decodedData = myData.decode("utf-8")#Decoding data
        self.send_response(200)
        self.send_header("Content-type", "text/plain") #Setting headers 
        self.end_headers()
        self.saveFile("database.tytus", bytes(decodedData, 'utf-8'))
        self.wfile.write(bytes(decodedData, 'utf-8'))

    #Method to create file on server
    def saveFile(self, filename, content):
        #Checking if data directory exists and created if not
        if not os.path.exists('./data'):
            os.makedirs('./data')
        #Setting full path
        myPath = "./data/" + filename
        newFile = open(myPath, "wb") #Temporary example
        newFile.write(content)
        newFile.close()

# Setting and starting server
myServer = HTTPServer(('localhost', PORT), MyRequestHandler)
print("Server running at localhost: " + str(PORT))
myServer.serve_forever()



