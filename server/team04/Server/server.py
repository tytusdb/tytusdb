#TyTusDB server. 
#Dev by Group 4
#BD1 2020

import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import io
import os
import json


# Setting server port
PORT = 8000

#Def. requests handler.
class MyRequestHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        #Definiendo rutas para peticiones get
        if self.path == '/getUsers':           
            self.do_getUsers()
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
        else:
            self.send_response(400) 
            self.wfile.write(bytes("",'utf-8'))

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



