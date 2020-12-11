from Interprete.NodoAST import NodoArbol

class Arbol ():

    def __init__(self, instructions):
        self.instrucciones:list(NodoArbol) = instructions
        self.console:list() = []
