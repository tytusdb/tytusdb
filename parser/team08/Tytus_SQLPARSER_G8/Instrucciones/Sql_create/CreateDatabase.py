from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class CreateDatabase(Instruccion):
    def __init__(self, id, tipo, opcion, id23, owner, id2, entero , linea, columna):
        Instruccion.__init__(self,tipo,linea,columna)
        self.valor = valor
        self.opcion = opcion

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))

    #t[0] = CreateDatabase(id,tipo, id2, owner, entero, t.lineno, t.lexpos)
'''
instruccion = CreateDatabase("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''