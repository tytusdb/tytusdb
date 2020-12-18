import socket 

host = '127.0.0.1'
port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
server.bind((host , port))
server.listen(1)
print('servidor en el puerto',port)

while True:
    conn , addr = server.accept()
    request = conn.recv(1024).decode('utf-8')
    string_list = request.split(' ')
    method = string_list[0]
    requesting_file = string_list[1]

    print('Client request',requesting_file)

    myfile = requesting_file.split('?')[0]
    myfile = myfile.lstrip('/')

    if(myfile == ''):
        myfile = 'index.html'

    try:
        file = open(myfile , 'rb')
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'
        mimetype = 'text/html'            

        header += 'Content-Type: '+str(mimetype)+'\n\n'

    except Exception as e:
        print("-")
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')

    final_response = header.encode('utf-8')
    final_response += response
    conn.send(final_response)
    conn.close()
