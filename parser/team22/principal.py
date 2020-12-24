import parser_asc_new as parser_asc
from instrucciones import *
from ts import *
from type_checker import *

f = open("./entrada.txt", "r")
input = f.read()
    
instrucciones = parser_asc.parse(input)

tabla_simbolos = TablaDeSimbolos()
tabla_errores = parser_asc.tabla_errores
consola = []
salida = []

type_checker = TypeChecker(tabla_simbolos, tabla_errores, consola, salida)

def leer_instrucciones(intrucciones):
    for instruccion in instrucciones:
        if isinstance(instruccion, Crear_BD):
            if instruccion.replace is False:
                type_checker.createDatabase(instruccion.id, instruccion.line)
            else:
                type_checker.dropDatabase(instruccion.id, instruccion.line)
                type_checker.createDatabase(instruccion.id, instruccion.line)
        elif isinstance(instruccion, Show_BD):
            type_checker.showDatabase(instruccion.like)
        elif isinstance(instruccion, Alter_BD):
            type_checker.alterDatabase(instruccion.databaseOld, instruccion.databaseNew, instruccion.line)
        elif isinstance(instruccion, Drop_BD):
            type_checker.dropDatabase(instruccion.database, instruccion.line)

leer_instrucciones(instrucciones)

print('**************** Consola: ****************')
for element in consola:
    print(element)

print('**************** Salida: ****************')
for element in salida:
    print(element)

print('**************** Tabla de Simbolos: ****************')
for element in tabla_simbolos.simbolos:
    print(tabla_simbolos.simbolos[element].imprimir())

print('**************** Errores: ****************')
for element in parser_asc.tabla_errores.errores:
    print(element.imprimir())