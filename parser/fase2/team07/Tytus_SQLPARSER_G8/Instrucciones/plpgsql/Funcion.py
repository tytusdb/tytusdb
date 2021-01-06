from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Funcion(Instruccion):
    def __init__(self, id, parametros, tipo, declaraciones, instrucciones, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna, strGram, strSent)
        self.id = id
        self.parametros = parametros
        self.tipo = tipo
        self.declaraciones = declaraciones
        self.instrucciones = instrucciones

    def ejecutar(self, tabla, arbol):
        tabla.setFuncion(self)

    def traducir(self,tabla,arbol,cadenaTraducida):
        codigo = ""
        
        return codigo
        pass