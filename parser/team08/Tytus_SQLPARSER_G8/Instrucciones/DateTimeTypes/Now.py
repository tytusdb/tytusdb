from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 

class Now(Instruccion):
    def __init__(self, linea, columna):
        Instruccion.__init__(self,None,linea,columna)

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        todays_date = datetime.now()
        return todays_date

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''