import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)
from Nodo import Nodo

import json

class Start(Nodo):
    def __init__(self, nombreNodo, fila, columna, valor):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)

    def execute(self, enviroment):
        for hijo in self.hijos: 
            hijo.execute(enviroment)
            
    def addChild(self, node):
        self.hijos.append(node)

    def createChild(self, nombreNodo, fila, columna, valor):
        nuevo = Start(nombreNodo,fila,columna,valor)
        self.hijos.append(nuevo)
    
