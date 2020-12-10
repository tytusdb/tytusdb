import gramatica2 as g
i


f = open("./entradaproyecto.txt", "r")
input = f.read()

instrucciones = g.parse(input)



