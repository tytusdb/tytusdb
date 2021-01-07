import grammar2 as g
from reportTable import *
from InstruccionesDGA import tabla as ts

#print(g.funciones)

f = open("entrada.txt", "r")
a = open("c3d.py", "w")

a.write('''from InstruccionesDGA import tabla as ts
from datetime import date
from InstruccionesDGA import cont as contador
from InstruccionesDGA import NombreDB
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt


pila = []
for i in range(100):
    pila.append(i)

def ejecutar():
    cont = contador
	\n''')



input = f.read()

raiz = g.parse(input)

results = []
res =''
    #executeGraphTree(raiz)
for val in raiz:
    
    res += val.traducir()

    
    #pass
a.write(res)
a.write('\tsql.execute(\'3D\')\n\n')
for fa in g.funciones:
   
   a.write(fa)

a.write('''ejecutar()''')
a.close()
#graphTable(ts)