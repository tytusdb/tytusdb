from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Decode(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("DECODE")
        print(self.valor.decode('base64','strict'))
        #return self.valor.decode('base64','strict')
'''
instruccion = Decode("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''