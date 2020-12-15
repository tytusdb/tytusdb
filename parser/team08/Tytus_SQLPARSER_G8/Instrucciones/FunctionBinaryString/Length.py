from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Length(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("LENGTH")
        print(len(self.valor))
        return len(self.valor)
'''
instruccion = Length("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''