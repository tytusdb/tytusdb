import grammar2 as g

#print(g.funciones)

f = open("entrada.txt", "r")
a = open("c3d.py", "w")

a.write('''from InstruccionesDGA import tabla 
from InstruccionesDGA import cont 
from InstruccionesDGA import NombreDB
from tablaDGA import *
from sql import * 
import mathtrig as mt
#Funcion sql.execute

pila = []
for i in range(100):
    x.append(i)

def ejecutar(): \n''')

input = f.read()

raiz = g.parse(input)

results = []
res =''
    #executeGraphTree(raiz)
for val in raiz:
    res += val.traducir()
    
    #pass
a.write(res)

for fa in g.funciones:
   
   a.write(fa)


a.close()