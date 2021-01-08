from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from datetime import datetime 
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

class Now(Instruccion):
    def __init__(self, strGram,linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.TIMESTAMP),linea,columna,strGram)

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        print('EJECUTA NOW?')
        todays_date = datetime.now()
        current_time = todays_date.strftime("%Y-%m-%d %H:%M:%S")
        return current_time

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"NOW()\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code