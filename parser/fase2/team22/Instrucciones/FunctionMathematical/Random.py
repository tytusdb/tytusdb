import math
import random
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
from Optimizador.C3D import Valor as ClassValor
from Optimizador.C3D import OP_ARITMETICO as ClassOP_ARITMETICO
from Optimizador.C3D import Identificador as ClassIdentificador

class Random(Instruccion):
    def __init__(self, strGram, linea, columna):
        Instruccion.__init__(self,Tipo(Tipo_Dato.DOUBLE_PRECISION),linea,columna,strGram)

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return random.random()

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getLastTemporal()
        t1 = c3d.getTemporal()
        code.append(c3d.operacion(t1, ClassIdentificador(t0), ClassValor("\"RANDOM()\"", "STRING"), ClassOP_ARITMETICO.SUMA))

        return code

'''
instruccion = Random("hola mundo",None, 1,2)
instruccion.ejecutar(None,None)
'''