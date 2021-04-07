from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato

class CurrentDate(Instruccion):
    def __init__(self, strGram, linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram, strSent)
        
    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #año-mes-dia
        todays_date = datetime.today()
        date = todays_date.strftime("%Y-%m-%d")
        self.tipo = Tipo("",Tipo_Dato.DATE)
        return date

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