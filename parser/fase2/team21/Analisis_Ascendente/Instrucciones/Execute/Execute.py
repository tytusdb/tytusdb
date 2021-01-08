from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import *

class Execute(Instruccion):
    def __init__(self, caso, id, listaE, linea, columna):
        self.caso = caso
        self.id = id
        self.listaE = listaE
        self.linea = linea
        self.columna = columna


    def traducir(exec, ts, consola, exception, tv, regla, antes, optimizado):
        if exec.listaE == None:
            consola.append(f'\t{exec.id}()\n')
        else:
            temporales = []
            for e in exec.listaE:
                t = Expresion.traducir(e, ts, consola, exception, tv, regla, antes, optimizado, None)
                try:
                    data = int(t)
                    temporales.append(t)
                except:
                    temporales.append("\'\\\'"+str(t).replace("\'","")+"\\\'\'")
            i = 0
            params = ""
            for te in temporales:
                params += str(te)
                if i + 1 != len(temporales):
                    params += ', '
                i = i + 1
            consola.append(f'\t{exec.id}({params})\n')