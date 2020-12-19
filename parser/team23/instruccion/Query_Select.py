from abstract.instruccion import *
from tools.tabla_tipos import *
from tools.console_text import *

class Query_Select(instruccion):
    def __init__(self,comando,expresiones, line, column, num_nodo):
        super().__init__(line,column)
        self.comando=comando
        self.expresiones=expresiones
 
        
        self.nodo = nodo_AST('SELECT',num_nodo)
        self.nodo.hijos.append(nodo_AST('SELECT',num_nodo+1))

        if( comando.lower() == 'greatest'):
            print('ENTRA GREATEST')
            self.nodo.hijos.append(nodo_AST('GREATEST', num_nodo+2))
        elif ( comando.lower() == 'least' ):
            print('ENTRA least')
            self.nodo.hijos.append(nodo_AST('LEAST', num_nodo+2))
        
        if expresiones != None:
            for element in expresiones:
                if element != None:
                    self.nodo.hijos.append(element.nodo)

    def ejecutar(self):
        pass 