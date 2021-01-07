from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion

class AsignacionF2(Instruccion):
    '''#1 :=
       #2 ='''
    def __init__(self, caso, id, E, linea, columna):
        self.caso = caso
        self.id = id
        self.E = E
        self.linea = linea
        self.columna = columna

    def traducir(asig, ts, consola, exception, tv, regla, antes, optimizado):
        #consola.append('\tasignacion\n')
        #print("asignacion!!")
        #print(asig)
        e = Expresion.traducir(asig.E, ts, consola, exception, tv, regla, antes, optimizado, asig.id)
        consola.append(f'\t{asig.id} = {e}\n')




class Return(Instruccion):
    def __init__(self, E, linea, columna):
        self.E = E
        self.linea = linea
        self.columna = columna

    def traducir(ret, ts, consola, exception, tv, regla, antes, optimizado):
        e = Expresion.traducir(ret.E, ts, consola, exception, tv, regla, antes, optimizado, None)
        consola.append(f'\treturn {e}\n')