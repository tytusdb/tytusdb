import grammar2 as g
from reportTable import *
from InstruccionesDGA import tabla as ts

#print(g.funciones)

f = open("entrada.txt", "r")
a = open("c3d.py", "w")

a.write('''
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont 
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt
from reportTable import *


pila = []
for i in range(100):
\tpila.append(i)

def ejecutar():
\tglobal cont
\tglobal ts
\tNombreDB = ts.nameDB
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

a.write('\tgraphTable(ts)\n')
for fa in g.funciones:
       
   a.write(fa)

a.write('''ejecutar()''')
a.close()



