import grammar2 as g
from reportTable import *
from InstruccionesDGA import tabla as ts

#print(g.funciones)

f = open("entrada.txt", "r")
a = open("c3d.py", "w")

a.write('''from InstruccionesDGA import tabla as ts
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont as ncont
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt
from reportTable import *

cont = ncont
pila = []
for i in range(100):
    pila.append(i)

def ejecutar():
    global cont
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
a.write('\tgraphTable(ts)\n')
for fa in g.funciones:
   
   a.write(fa)

a.write('''ejecutar()''')
a.close()
#graphTable(ts)