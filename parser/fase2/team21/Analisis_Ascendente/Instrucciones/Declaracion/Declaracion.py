from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion



class Declaracion(Instruccion):
    '''en colate sube id o None
    en constant y notnull sube True o False
    en asignacionv sube AsignacionVariable o None'''
    def __init__(self, caso, id, constant, tipo, colate, notnull, asignacionv, linea, columna):
        self.caso = caso
        self.id = id
        self.constant = constant
        self.tipo = tipo
        self.colate = colate
        self.notnull = notnull
        self.asignacionv = asignacionv
        self.linea = linea
        self.columna = columna

    def traducir(dec, ts, consola, exception, tv, regla, antes, optimizado):
        #consola.append('\tasignacion\n')
        if dec.asignacionv != None:
            if isinstance(dec.asignacionv, AsignacionVariable):
                e = Expresion.traducir(dec.asignacionv.E, ts, consola, exception, tv, regla, antes, optimizado, dec.id)
                consola.append(f'\t{dec.id} = {e}\n')
        else:
            consola.append(f'\t{dec.id} = \'\'\n')


class AsignacionVariable(Instruccion):
    '''#1 default
       #2 igual
       #3 dospuntos igual'''
    def __init__(self, caso, E, linea, columna):
        self.caso = caso
        self.E = E
        self.linea = linea
        self.columna = columna