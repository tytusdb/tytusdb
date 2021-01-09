from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Having(Instruccion):
    def __init__(self, valor, tipo, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

'''
instruccion = Having("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''