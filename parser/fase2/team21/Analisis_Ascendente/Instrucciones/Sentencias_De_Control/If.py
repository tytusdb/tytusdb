from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
import tytus.parser.fase2.team21.Analisis_Ascendente.ascendente as tr

class SElseIf(Instruccion):
    def __init__(self, E, instrucciones, fila, columna):
        self.E = E
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna



class SIF(Instruccion):
    '''condicion, sentencias del if, lista de else if, boolean de else, sentencias de else
    elseif puede venir como [none] o none'''

    def __init__(self, E, instrucciones, elsesif, Belse, instruccionesElse, fila, columna):
        self.E = E
        self.instrucciones = instrucciones
        self.elsesif = elsesif
        self.Belse = Belse
        self.instruccionesElse = instruccionesElse
        self.fila = fila
        self.columna = columna



    def traducir(sif, ts, consola,metodos_funciones, exception, tv, concatena, regla, antes, optimizado):
        ei = False
        if sif.elsesif != None:
            if len(sif.elsesif) == 1:
                if sif.elsesif[0] != None:
                    ei = True
                else:
                    ei = False
            else:
                ei = True
        if ei:
            #tiene elsif
            #tiene else
            condicion = Expresion.traducir(sif.E, ts, consola, exception, tv, regla, antes, optimizado, 'IF')
            verdadero = tv.Et()
            falso = tv.Et()
            consola.append('\tif ' + condicion + ':\n\t\t goto .' + verdadero + '\n')
            consola.append(f'\telse:\n\t\tgoto .{falso}\n')
            consola.append(f'\tlabel .{verdadero}\n')
            #reporte optimizacion
            regla.append('3')
            antes.append(f'if {condicion}:<br> &nbsp goto .{verdadero}<br>else:<br> &nbsp goto .{falso}<br>label .{verdadero}<br>#instrucciones<br>label .{falso}')
            optimizado.append(f'if not {condicion}:<br> &nbsp goto .{verdadero}<br>#instrucciones<br>label .{verdadero}')

            if sif.instrucciones != None:
                tr.traduccion(sif.instrucciones, ts, consola,metodos_funciones, exception, concatena, tv)
            #cuenta de la etiqueta final
            final = int(falso[1:]) #numero de la etiqueta falso
            final = final + len(sif.elsesif) * 2
            if sif.instruccionesElse != None:
                final = final + 1
            etfinal = 'L' + str(final)
            consola.append(f'\tgoto .{etfinal}\n')
            consola.append(f'\tlabel .{falso}\n')
            #recorrer elsif
            for eli in sif.elsesif:
                condicion = Expresion.traducir(eli.E, ts, consola, exception, tv, regla, antes, optimizado, 'IF')
                verdadero = tv.Et()
                falso = tv.Et()
                consola.append('\tif ' + condicion + ':\n\t\t goto .' + verdadero + '\n')
                consola.append(f'\telse:\n\t\tgoto .{falso}\n')
                consola.append(f'\tlabel .{verdadero}\n')
                #reporte optimizacion
                regla.append('3')
                antes.append(f'if {condicion}:<br> &nbsp goto .{verdadero}<br>else:<br> &nbsp goto .{falso}<br>label .{verdadero}<br>#instrucciones<br>label .{falso}')
                optimizado.append(f'if not {condicion}:<br> &nbsp goto .{verdadero}<br>#instrucciones<br>label .{verdadero}')

                if eli.instrucciones != None:
                    tr.traduccion(eli.instrucciones, ts, consola,metodos_funciones, exception, concatena, tv)
                consola.append(f'\tgoto .{etfinal}\n')
                consola.append(f'\tlabel .{falso}\n')
            if sif.instruccionesElse != None:
                consola.append('\t#en else\n')
                tr.traduccion(sif.instruccionesElse, ts, consola,metodos_funciones, exception, concatena, tv)
                fn = tv.Et()
                consola.append(f'\tlabel .{fn}\n')
        else:
            if sif.Belse:
                #tiene else
                condicionIf = Expresion.traducir(sif.E, ts, consola, exception, tv, regla, antes, optimizado, 'IF')
                verdadero = tv.Et()
                falso = tv.Et()
                consola.append('\tif ' + condicionIf + ':\n\t\t goto .' + verdadero + '\n')
                consola.append(f'\telse:\n\t\tgoto .{falso}\n')
                consola.append(f'\tlabel .{verdadero}\n')
                #reporte optimizacion
                regla.append('3')
                antes.append(f'if {condicionIf}:<br> &nbsp goto .{verdadero}<br>else:<br> &nbsp goto .{falso}<br>label .{verdadero}<br>#instrucciones<br>label .{falso}')
                optimizado.append(f'if not {condicionIf}:<br> &nbsp goto .{verdadero}<br>#instrucciones<br>label .{verdadero}')

                continuacion = tv.Et()   #donde quedara lo que esta despues de else
                if sif.instrucciones != None:
                    #agregar
                    consola.append('\t#parte verdadera\n')
                    consola.append('\tprint("verdadera")\n')
                    tr.traduccion(sif.instrucciones, ts, consola,metodos_funciones, exception, concatena, tv)
                    consola.append(f'\tgoto .{continuacion}\n')
                consola.append(f'\tlabel .{falso}\n')
                if sif.instruccionesElse != None:
                    #agregar
                    consola.append('\t#parte falsa\n')
                    consola.append('\tprint("falsa")\n')
                    tr.traduccion(sif.instruccionesElse, ts, consola,metodos_funciones,exception, concatena, tv)
                consola.append(f'\tlabel .{continuacion}\n')
                consola.append('\t#continuacion\n')
                consola.append('\tprint("continuacion")\n')
            else: #solo if
                condicion = Expresion.traducir(sif.E, ts, consola, exception, tv, regla, antes, optimizado, 'IF')
                verdadero = tv.Et()
                falso = tv.Et()
                consola.append(f'\tif {condicion}:\n\t\t goto .{verdadero}\n')
                consola.append(f'\telse:\n\t\tgoto .{falso}\n')
                consola.append(f'\tlabel .{verdadero}\n')
                # reporte optimizacion
                regla.append('3')
                antes.append(f'if {condicion}:<br> &nbsp goto .{verdadero}<br>else:<br> &nbsp goto .{falso}<br>label .{verdadero}<br>#instrucciones<br>label .{falso}')
                optimizado.append(f'if not {condicion}:<br> &nbsp goto .{verdadero}<br>#instrucciones<br>label .{verdadero}')

                if sif.instrucciones != None:
                    consola.append('\tprint("verdadera")\n')
                    tr.traduccion(sif.instrucciones, ts, consola,metodos_funciones, exception, concatena, tv)
                consola.append(f'\tlabel .{falso}\n')