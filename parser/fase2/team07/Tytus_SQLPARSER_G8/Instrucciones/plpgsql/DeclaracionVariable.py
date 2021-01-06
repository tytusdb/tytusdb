from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class DeclaracionVariable(Instruccion):
    def __init__(self, id, constante, tipo, isnull, asignacion_valor, strGram, linea, columna, strSent):
        Instruccion.__init__(self,tipo,linea,columna, strGram, strSent)
        self.id = id
        self.constante = constante
        self.tipo = tipo
        self.isnull = isnull
        self.asignacion_valor = asignacion_valor

    def ejecutar(self, tabla, arbol):
        pass

    def traducir(self,tabla,arbol,cadenaTraducida):
        codigo = ""

        return codigo