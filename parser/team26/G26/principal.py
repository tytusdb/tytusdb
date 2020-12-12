import gramatica as g

ruta = '../G26/entrada.txt'
f = open(ruta, "r")
input = f.read()
# print(input)

instrucciones = g.parse(input)
print(instrucciones)

# print(instrucciones)
for instr in instrucciones :
    print(instr.execute())

print(instrucciones)
