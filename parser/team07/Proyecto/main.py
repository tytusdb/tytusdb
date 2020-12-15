import gramatica as g

f =  open("./archivoEntrada.txt")
input = f.read()

instrucciones = g.parse(input)