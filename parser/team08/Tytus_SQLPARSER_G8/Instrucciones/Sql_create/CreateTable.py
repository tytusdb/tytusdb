from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class CreateTable(Instruccion):
    def __init__(self, id, tipo, campos, ids, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = id
        self.campos = campos
        self.ids = ids

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = CreateTable("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''