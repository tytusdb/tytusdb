from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion

class CreateFunction(Instruccion):
    def __init__(self, id, tipo, lcol, id2, Instrucciones, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.id = id
        self.listaDeColumnas = lcol
        self.expresion = id2
        self.Instrucciones = Instrucciones

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        #Aqui vamos a guardar la funcion
        tabla.setFuncion(self)

'''
instruccion = CreateFunction("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''