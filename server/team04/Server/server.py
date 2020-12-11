#TyTusDB server. 
#Dev by Group 4
#BD1 2020


import http.server
import socketserver


# Setting server port
PORT = 8000

# Def. myHandler (Request handler)
myHandler = http.server.SimpleHTTPRequestHandler

# Setting and starting server
with socketserver.TCPServer(("", PORT), myHandler) as myServer:
    print("Server runing at localhost:" + str(PORT))
    myServer.serve_forever()


