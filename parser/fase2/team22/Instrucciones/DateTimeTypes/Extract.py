from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
import datetime
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

class Extract(Instruccion):
    def __init__(self, tiempo, caracter, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.tiempo = tiempo
        self.caracter = caracter

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        print("estamos en extract " + self.tiempo)
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

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"EXTRACT(" + self.tiempo + " FROM TIMESTAMP '" + self.caracter + "')\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''