#TyTusDB server. 
#Dev by Group 4
#BD1 2020

import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import io


# Setting server port
PORT = 8000

#Def. requests handler.
class MyRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain") #Setting headers 
        self.end_headers()


    def do_GET(self):
        if self.path == '/':           
            pass
        try:
            myFile = open(self.path[1:]).read()
            self.send_response(200)
        except:
            myFile = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(myFile, 'utf-8'))
    
    

    def do_POST(self):
        dataSize = int(self.headers['Content-Length']) #Getting size of data
        myData = self.rfile.read(dataSize) #Reading data (form)
        decodedData = myData.decode("utf-8")#Decoding data
        self._set_headers()
        self.saveFile(bytes(decodedData, 'utf-8'))
        self.wfile.write(bytes(decodedData, 'utf-8'))
        


    #Method to create file on server
    def saveFile(self, file):
        newFile = open("database.tytus", "wb") #Temporary example
        newFile.write(file)
        newFile.close()

# Setting and starting server
myServer = HTTPServer(('localhost', PORT), MyRequestHandler)
print("Server running at localhost: " + str(PORT))
myServer.serve_forever()



