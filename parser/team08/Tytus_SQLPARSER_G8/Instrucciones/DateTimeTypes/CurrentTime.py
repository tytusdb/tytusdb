from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 

class CurrentTime(Instruccion):
    def __init__(self, id, operacion, id2, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #hora
        todays_date = datetime.now()
        date_time_obj = datetime.datetime.strptime(todays_date, '%Y-%m-%d %H:%M:%S')
        time = date_time_obj.time()
        return time

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''