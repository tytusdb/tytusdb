from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 

class TimeStamp(Instruccion):
    def __init__(self, id, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.identificador = id

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #el id es para guardarlo en la tabla
        #exp = Simbolo(self.identificador,self.operacion,self.valor,self.linea,self.columna)
        #ts.setVariable(exp)
        todays = datetime.today()
        today = todays.strftime("%Y-%m-%d %H:%M:%S")
        return today

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''