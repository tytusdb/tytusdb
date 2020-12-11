class ObjetoSemantico:
    ''' Representacion del nodo en el que se encuentran los lexemas con sus caracteristicas '''


class NodoSemantico_Objeto(ObjetoSemantico):
    def __init__(self, lexema,linea ,columna):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna

    def imprimir_prueba(self,Cadena):
        print(str(Cadena))
        return 'holas'