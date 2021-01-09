from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

class CurrentDate(Instruccion):
    def __init__(self, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        
    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #año-mes-dia
        todays_date = datetime.today()
        date = todays_date.strftime("%Y-%m-%d")
        return date

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"CURRENT_DATE\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code
'''
instruccion = Declare("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''