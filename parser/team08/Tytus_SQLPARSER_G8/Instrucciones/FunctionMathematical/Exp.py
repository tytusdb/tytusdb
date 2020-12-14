from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Exp(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("EXP")

'''
instruccion = Exp(80,None, 1,2)

instruccion.ejecutar(None,None)
'''