from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class UpdateTable(Instruccion):
    def __init__(self, id, tipo, lCol, insWhere, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.lCol = lCol
        self.insWhere = insWhere

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

'''
instruccion = UpdateTable("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)
'''