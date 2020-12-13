from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Trim(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print("STRIP")
        print(self.strip())
        return self.strip()
'''
instruccion = Trim("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''