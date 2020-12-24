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

print('**************** Tabla de Simbolos: ****************')
for element in parser_asc.tabla_simbolos.simbolos:
    print(parser_asc.tabla_simbolos.simbolos[element].imprimir())

print('**************** Errores: ****************')
for element in parser_asc.tabla_errores.errores:
    print(element)