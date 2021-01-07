from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion

class Declaracion(Instruccion):
    def __init__(self, id, constante, tipo, notnull, default, expresion, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna,strGram)
        self.id = id
        self.constante = constante
        self.notnull = notnull
        self.default = default
        self.expresion = expresion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        resultado = self.expresion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        return resultado
        
    def traducir(self, tabla, arbol):
        super().traducir(tabla,arbol)