# Imports

# Librerias para el servidor
from http.server import  BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/":
            self.printMessage()   
        else:
            self.send_response(400) 
            self.wfile.write(bytes("",'utf-8'))

    def do_GET(self):
        if self.path=="/":
            self.printMessage()
            print("copiado")
        else:
            self.send_response(400)
            self.wfile.write(bytes("","utf-8"))


    def printMessage(self):
        print(self)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes("Osdk", 'utf-8'))

TytusServer = HTTPServer(('localhost', 4040), Handler)
print("Corriendo server en puerto 4040")
TytusServer.serve_forever()