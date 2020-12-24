from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 

class Now(Instruccion):
    def __init__(self, linea, columna):
        Instruccion.__init__(self,None,linea,columna)

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        
        todays_date = datetime.now()
        current_time = todays_date.strftime("%Y-%m-%d %H:%M:%S")
        return current_time

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''