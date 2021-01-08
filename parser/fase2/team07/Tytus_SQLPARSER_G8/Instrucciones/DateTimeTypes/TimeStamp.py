from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 
from Instrucciones.TablaSimbolos.Simbolo3D import Simbolo3d
from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato

class TimeStamp(Instruccion):
    def __init__(self, id, strGram,linea, columna, strSent):
        Instruccion.__init__(self,None,linea,columna,strGram, strSent)
        self.identificador = id

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #el id es para guardarlo en la tabla
        #exp = Simbolo(self.identificador,self.operacion,self.valor,self.linea,self.columna)
        #ts.setVariable(exp)
        todays = datetime.today()
        today = todays.strftime("%Y-%m-%d %H:%M:%S")
        self.tipo = Tipo("",Tipo_Dato.TIMESTAMP)
        return today

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