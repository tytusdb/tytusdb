import parser_asc as parser_asc
import ts as TS
from expresiones import *
from instrucciones import *

# def procesar_instrucciones(instrucciones, ts) :
#     ## lista de instrucciones recolectadas
#     for instr in instrucciones :
#         if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
#         elif isinstance(instr, Definicion) : procesar_definicion(instr, ts)
#         elif isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
#         elif isinstance(instr, Mientras) : procesar_mientras(instr, ts)
#         elif isinstance(instr, If) : procesar_if(instr, ts)
#         elif isinstance(instr, IfElse) : procesar_if_else(instr, ts)
#         else : print('Error: instrucción no válida')

f = open("./entrada.txt", "r")
input = f.read()
    
instrucciones = parser_asc.parse(input)
ts_global = TS.TablaDeSimbolos()

# procesar_instrucciones(instrucciones, ts_global)