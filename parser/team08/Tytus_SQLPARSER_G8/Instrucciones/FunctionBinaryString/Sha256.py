from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from hashlib import sha256
class Sha256(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("Sha256")
        print(sha256(self.valor))
        return sha256(self.valor)
'''
instruccion = Sha256("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''