from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class Assignment(Instruccion):
    def __init__(self, id, expresion, strGram,linea, columna):
        self.id = id
        self.expresion = expresion
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, tabla, arbol):   
        pass

    def getCodigo(self, tabla, arbol):
        temp_return = arbol.getTemporal()
        dic_expresion = self.expresion.getCodigo(tabla, arbol)
        symbol = arbol.getSymbol(self.id, arbol.getScope())
        
        codigo = f"\t{temp_return} = pointer + {symbol['pointer']}\n"
        codigo += dic_expresion['codigo']
        codigo += f"\tstack[{temp_return}] = {dic_expresion['dir']}\n"        
        return codigo