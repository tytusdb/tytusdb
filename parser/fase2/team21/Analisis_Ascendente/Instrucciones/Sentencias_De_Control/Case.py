from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
import tytus.parser.fase2.team21.Analisis_Ascendente.ascendente as tr

class When(Instruccion):
    def __init__(self, E, instrucciones, fila, columna):
        self.E = E
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna


class CaseF2(Instruccion):
    '''elseCase puede ser None o lista de instrucciones'''
    def __init__(self, E, listaWhen, elseCase, fila, columna):
        self.E = E
        self.listaWhen = listaWhen
        self.elseCase = elseCase
        self.fila = fila
        self.columna = columna


    def traducir(cs, ts, consola, metodos_funciones, exception, tv, concatena, regla, antes, optimizado):
        if cs.elseCase == None:
            #no tiene else
            condicion = Expresion.traducir(cs.E, ts, consola, exception, tv, regla, antes, optimizado, None)
            salida = tv.Et()
            # recorrer case
            i = 0
            if cs.listaWhen != None and len(cs.listaWhen) != 0:
                for c in cs.listaWhen:
                    cond2 = Expresion.traducir(c.E, ts, consola, exception, tv, regla, antes, optimizado, None)
                    tempCond = tv.Temp()
                    consola.append(f'\t{tempCond} = {condicion} == {cond2}\n')
                    siguiente = salida
                    if len(cs.listaWhen) != i + 1:
                        siguiente = tv.Et()
                    consola.append(f'\tif not {tempCond}:\n\t\tgoto .{siguiente}\n')
                    if c.instrucciones != None:
                        tr.traduccion(c.instrucciones, ts, consola, metodos_funciones, exception, concatena, tv)
                    #consola.append(f'\tgoto .{salida}\n') equivalente a break no es necesario
                    consola.append(f'\tlabel .{siguiente}\n')

                    i = i + 1

                    #reporte optimizacion
                    regla.append('3')
                    et = siguiente[1:]
                    print(et)
                    et = int(et)
                    antes.append(f'if {tempCond}:<br> &nbsp goto .{siguiente}<br>else:<br> &nbsp goto .L{et + 1}<br>label .{siguiente}<br>#instrucciones<br>label .L{et + 1}')
                    optimizado.append(f'if not {tempCond}:<br> &nbsp goto .{siguiente}<br>#instrucciones<br>label .{siguiente}')

        else:
            #tiene else
            condicion = Expresion.traducir(cs.E, ts, consola, exception, tv, regla, antes, optimizado, None)
            salida = tv.Et()
            #recorrer case
            if cs.listaWhen != None and len(cs.listaWhen) != 0:
                for c in cs.listaWhen:
                    cond2 = Expresion.traducir(c.E, ts, consola, exception, tv, regla, antes, optimizado, None)
                    tempCond = tv.Temp()
                    consola.append(f'\t{tempCond} = {condicion} == {cond2}\n')
                    siguiente = tv.Et()
                    consola.append(f'\tif not {tempCond}:\n\t\tgoto .{siguiente}\n')
                    if c.instrucciones != None:
                        tr.traduccion(c.instrucciones, ts, consola, metodos_funciones, exception, concatena, tv)
                    consola.append(f'\tgoto .{salida}\n') #equivalente a break, por el else lo dejare
                    consola.append(f'\tlabel .{siguiente}\n')

                    # reporte optimizacion
                    regla.append('3')
                    et = siguiente[1:]
                    print(et)
                    et = int(et)
                    antes.append(f'if {tempCond}:<br> &nbsp goto .{siguiente}<br>else:<br> &nbsp goto .L{et + 1}<br>label .{siguiente}<br>#instrucciones<br>label .L{et + 1}')
                    optimizado.append(f'if not {tempCond}:<br> &nbsp goto .{siguiente}<br>#instrucciones<br>label .{siguiente}')



                    #defElse = tv.Et()
            #consola.append(f'\tlabel .{defElse}\n')
            tr.traduccion(cs.elseCase, ts, consola, metodos_funciones, exception, concatena, tv)
            consola.append(f'\tlabel .{salida}\n')