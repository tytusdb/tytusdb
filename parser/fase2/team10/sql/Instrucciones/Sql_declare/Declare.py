from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Simbolo import Simbolo 

class Declare(Instruccion):
    def __init__(self, id, operacion, id2, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.identificador = id
        self.valor = id2
        self.operacion = operacion
        

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #el id es para guardarlo en la tabla
        exp = Simbolo(self.identificador,self.operacion,self.valor,self.linea,self.columna)
        ts.setVariable(exp)
        print("imprimir_declaracion")

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''