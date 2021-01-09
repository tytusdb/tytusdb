from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
import datetime
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato

class Extract(Instruccion):
    def __init__(self, tiempo, caracter, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram, strSent)
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
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return seg
        elif(self.tiempo == "MINUTE"):
            minute = time.minute
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return minute
        elif(self.tiempo == "HOUR"):
            hour = time.hour
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return hour
        elif(self.tiempo == "DAY"):
            day = date.day
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return day
        elif(self.tiempo == "MONTH"):
            month = date.month
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return month
        elif(self.tiempo == "YEAR"):
            year = date.year
            self.tipo = Tipo("",Tipo_Dato.INTEGER)
            return year

    def traducir(self, tabla, arbol, cadenaTraducida):
        resultado = self.ejecutar(tabla, arbol)
        if isinstance(resultado,Excepcion):
            return resultado        
        codigo = ""
        temporal = arbol.generaTemporal()
        codigo += "\t" + temporal + " = " + str(resultado) + "\n"
        nuevo = Simbolo3d(self.tipo, temporal, codigo, None, None)
        return nuevo

'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''