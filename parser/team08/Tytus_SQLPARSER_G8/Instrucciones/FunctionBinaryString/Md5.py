from Instrucciones.TablaSimbolos.Instruccion import Instruccion
import hashlib 
class Md5(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("MD5")  
        # encoding GeeksforGeeks using encode() 
        # then sending to md5() 
        print(hashlib.md5(self.valor.encode()))
        return hashlib.md5(self.valor.encode()) 
'''
instruccion = Md5("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)
'''