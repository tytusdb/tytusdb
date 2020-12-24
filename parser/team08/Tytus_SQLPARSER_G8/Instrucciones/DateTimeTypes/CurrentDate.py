from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 

class CurrentDate(Instruccion):
    def __init__(self, linea, columna):
        Instruccion.__init__(self,None,linea,columna)
        

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #año-mes-dia
        todays_date = datetime.now()
        date_time_obj = datetime.datetime.strptime(todays_date, '%Y-%m-%d %H:%M:%S')
        date = date_time_obj.date()
        return date

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''