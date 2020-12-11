import gramatica as g

ruta = 'C:/Users/Leni_n/Desktop/Nueva carpeta/entrada.txt'
f = open(ruta, "r")
input = f.read()
# print(input)

instrucciones = g.parse(input)
# print(instrucciones)
