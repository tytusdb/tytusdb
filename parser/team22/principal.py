import parser_asc as parser_asc

f = open("./entrada.txt", "r")
input = f.read()
    
instrucciones = parser_asc.parse(input)
print('**************** Consola: ****************')
for element in parser_asc.consola:
    print(element)

print('**************** Salida: ****************')
for element in parser_asc.salida:
    print(element)