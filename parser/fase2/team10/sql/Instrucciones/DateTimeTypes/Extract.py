from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
from sql.Instrucciones.TablaSimbolos.Simbolo import Simbolo 
import datetime

class Extract(Instruccion):
    def __init__(self, tiempo, caracter, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tiempo = tiempo
        self.caracter = caracter

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        date_time_obj = datetime.datetime.strptime(self.caracter, '%Y-%m-%d %H:%M:%S')
        date = date_time_obj.date()
        time = date_time_obj.time()
        if(self.tiempo == "SECOND"):
            seg = time.second
            return seg
        elif(self.tiempo == "MINUTE"):
            minute = time.minute
            return minute
        elif(self.tiempo == "HOUR"):
            hour = time.hour
            return hour
        elif(self.tiempo == "DAY"):
            day = date.day
            return day
        elif(self.tiempo == "MONTH"):
            month = date.month
            return month
        elif(self.tiempo == "YEAR"):
            year = date.year
            return year

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''