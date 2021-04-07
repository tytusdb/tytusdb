from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 

class CurrentTime(Instruccion):
    def __init__(self, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        
    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #hora
        todays_date = datetime.today()
        time = todays_date.strftime("%H:%M:%S")
        return time

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''