from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class DropDatabase(Instruccion):
    def __init__(self, id, tipo, opcion, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.opcion = opcion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = Use("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''