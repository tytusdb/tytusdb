import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *


f = open("C:/Users/Steven Sis/Desktop/All/Compi2/fase2/OLC2-Fase2/Optimizador/entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)

for e in g.respuesta:
    print(e,end="")

print('\n Reporte--\n')
for rep in g.reporte_optimizar:
    print(rep)
#ts_global = TS.TablaDeSimbolos()

#procesar_instrucciones(instrucciones, ts_global)