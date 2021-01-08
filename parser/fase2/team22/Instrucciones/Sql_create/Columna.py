from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d

class Columna(Instruccion):
    def __init__(self, nombre, tipo, constraint, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.nombre = nombre
        self.tipo = tipo
        self.constraint=constraint
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        if self.tipo.toString() != "enum":
            code.append(c3d.asignacionString(t0, self.nombre + ' ' + self.tipo.toString()))
        else:
            code.append(c3d.asignacionString(t0, self.nombre + ' ' + self.tipo.nombre))

        if self.tipo.dimension != None:
            t1 = c3d.getTemporal()
            if not isinstance(self.tipo.dimension, list):
               code.append(c3d.operacion(t1, Identificador(t0), Valor('"(' + str(self.tipo.dimension) + ')"', "STRING"), OP_ARITMETICO.SUMA))
            else:
                code.append(c3d.operacion(t1, Identificador(t0), Valor('"(' + str(self.tipo.dimension[0]) + ',' + str(self.tipo.dimension[1]) + ')"', "STRING"), OP_ARITMETICO.SUMA))
            t0 = t1

        if self.constraint != None:
            for const in self.constraint:
                t1 = c3d.getTemporal()
                code.append(c3d.operacion(t1, Identificador(t0), Valor('" ' + const.toString().replace("_", " ") + '"', "STRING"), OP_ARITMETICO.SUMA))
                t0 = t1

        return code
