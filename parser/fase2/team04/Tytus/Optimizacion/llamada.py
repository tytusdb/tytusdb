from Optimizacion.expresion import Expresion

class Llamada(Expresion): 
    def __init__(self, expresion, lista_expresiones, linea):
        self.expresion = expresion
        self.lista_expresiones = lista_expresiones
        self.linea = linea
        
    def toString(self):
        lista_valores = []
        for exp in self.lista_expresiones:
            lista_valores.append(exp.toString())
            
        codigo = f"{self.expresion.toString()}({','.join(lista_valores)})\n"
        return codigo