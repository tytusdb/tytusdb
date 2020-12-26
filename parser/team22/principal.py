import parser_asc_new as parser_asc
from instrucciones import *
from ts import *
from type_checker import *

#f = open("./entrada.txt", "r")
#input = f.read()
    
instrucciones = []
tabla_simbolos = TablaDeSimbolos()
tabla_errores = parser_asc.tabla_errores
consola = []
salida = []

type_checker = TypeChecker(tabla_simbolos, tabla_errores, consola, salida)

def parse(input):
    global instrucciones
    global consola
    global tabla_simbolos
    global tabla_errores
    global salida    
    instrucciones = parser_asc.parse(input)
    leer_instrucciones(instrucciones)
    return [consola,tabla_simbolos,tabla_errores,salida]

def leer_instrucciones(intrucciones):
    global salida
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
        elif isinstance(instruccion, Cambio_BD):
            type_checker.useDatabase(instruccion.id, instruccion.line)
        elif isinstance(instruccion, Select):
            objeto = instruccion.objeto['objeto']
            if isinstance(objeto, FuncionTrigonometrica1):
                salida.append([[instruccion.objeto['alias']],[type_checker.Funciones_Trigonometricas_1(objeto.funcion, objeto.valor, objeto.line)]])
            elif isinstance(objeto, FuncionTrigonometrica2):
                salida.append([[instruccion.objeto['alias']],[type_checker.Funciones_Trigonometricas_2(objeto.funcion, objeto.valor1, objeto.valor2, objeto.line)]])
            elif isinstance(objeto, FuncionAritmetica):
                type_checker.Validando_Operaciones_Aritmeticas(objeto.valor1, objeto.valor1, objeto.operacion)
        elif isinstance(instruccion, Crear_TB):
            type_checker.createTable(instruccion.id, instruccion.columnas, instruccion.line)
        elif isinstance(instruccion, Drop_TB):
            type_checker.dropTable(instruccion.table, instruccion.line)
        elif isinstance(objeto, FuncionAritmetica):
            type_checker.Validando_Operaciones_Aritmeticas(instruccion.valor1, instruccion.valor1, instruccion.operacion)
       

print('**************** Consola: ****************')
for element in consola:
    print(element)

print('**************** Salida: ****************')
if len(salida) > 0:
    print(salida[len(salida) - 1])

print('**************** Tabla de Simbolos: ****************')
for element in tabla_simbolos.simbolos:
    print(tabla_simbolos.simbolos[element].imprimir())

print('**************** Errores: ****************')
for element in parser_asc.tabla_errores.errores:
    print(element.imprimir())