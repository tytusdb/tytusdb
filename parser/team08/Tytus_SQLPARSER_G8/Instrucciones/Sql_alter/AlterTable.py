from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class AlterTable(Instruccion):
    def __init__(self, id, tipo, opcion, id2, listaId, listaId2, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.id2 = id2
        self.opcion = opcion
        self.listaId = listaId
        self.listaId = listaId2

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = AlterTable("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''