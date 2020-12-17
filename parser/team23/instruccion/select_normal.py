from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class select_normal(instruccion):
    def __init__(self,distinto,listaO,fin, line, column, num_nodo):
        super().__init__(line,column)
        self.distinto=distinto
        self.nodo = nodo_AST('SELECT',num_nodo)
        self.nodo.hijos.append(nodo_AST('SELECT',num_nodo+1))
        if (distinto!=None):
            self.nodo.hijos.append(nodo_AST(distinto,num_nodo+2))
        self.nodo.hijos.append(nodo_AST(listaO,num_nodo+3))
        self.nodo.hijos.append(nodo_AST('FROM',num_nodo+4))
        print('Si jala select')
        if fin != None:
            for element in fin:
                if element != None:
                    self.nodo.hijos.append(element.nodo)
        
    def ejecutar(self):
        pass 