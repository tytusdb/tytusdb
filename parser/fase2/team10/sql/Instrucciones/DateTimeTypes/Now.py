from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from sql.Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from datetime import datetime 

class Now(Instruccion):
    def __init__(self, strGram,linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.TIMESTAMP),linea,columna,strGram)

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        todays_date = datetime.now()
        current_time = todays_date.strftime("%Y-%m-%d %H:%M:%S")
        return current_time
