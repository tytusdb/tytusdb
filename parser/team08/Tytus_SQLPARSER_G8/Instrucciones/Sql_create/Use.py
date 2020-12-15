from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Use(Instruccion):
    def __init__(self, id, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        self.valor = id

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print('Ejecutando USE ID ;')
        #print(self.valor + " linea: " + str(self.linea) + " columna: " + str(self.columna))
'''
instruccion = Use("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''