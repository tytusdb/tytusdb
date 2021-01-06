from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion

class clase_return(Instruccion):
    def __init__(self, expresion, strGram, linea, columna):
        self.expresion = expresion
        self.linea = linea
        self.columna = columna

    def ejecutar(self, tabla, arbol):   
        pass
        
    def getCodigo(self, tabla, arbol):
        temp_return = arbol.getTemporal()
        dic_expresion = self.expresion.getCodigo(tabla, arbol)
        
        codigo = f"\t{temp_return} = pointer + 0\n"
        codigo += dic_expresion['codigo']
        codigo += f"\tstack[{temp_return}] = {dic_expresion['dir']}\n"
        return codigo