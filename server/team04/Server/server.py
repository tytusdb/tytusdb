#TyTusDB server. 
#Dev by Group 4
#BD1 2020


from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver


# Setting server port
PORT = 8000

class MyRequestHandler(BaseHTTPRequestHandler):

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
    

# Setting and starting server
myServer = HTTPServer(('localhost', PORT), MyRequestHandler)
print("Server running at localhost: " + str(PORT))
myServer.serve_forever()



