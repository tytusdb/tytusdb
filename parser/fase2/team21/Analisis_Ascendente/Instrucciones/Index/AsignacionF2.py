from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.select import Select
import  tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.Select3 as Select3


class AsignacionF2(Instruccion):
    '''#1 :=
       #2 ='''
    def __init__(self, caso, id, E, linea, columna):
        self.caso = caso
        self.id = id
        self.E = E
        self.linea = linea
        self.columna = columna

    def traducir(asig, ts, consola, exception, tv, regla, antes, optimizado,lista):
        #consola.append('\tasignacion\n')
        print("asignacion!!")
        print(asig)
        print(asig.E)
        data = asig.E
        print(data, "datos->>><")
        try:
            if data.caso == 3:
                print("simon")
                print(data)
                '''
                t54 = " SELECT   COUNT(*)    FROM   tbProducto  ;"
                t1 = T(t0)
                T1 = T3(t1)
                stack.append(T1)'''
                obtener =tv.Temp()
                consola.append(f"\n\t{obtener} =\"{data.concatena[0]}\"")
                obtener2 = tv.Temp()
                consola.append(f"\n\t{obtener2} =T({obtener})")
                consola.append(f"\n\tT1 = T3({obtener2})")
                consola.append(f"\n\t{asig.id} = T1[1] \n")
            elif data.caso == 5:
                if isinstance(data,Select):
                    #f\"{info}\""
                    info = Select3.obtenerTraduccion2(data,ts,consola,lista,tv)
                    obtener = tv.Temp()
                    consola.append(f"\n\t{obtener} =f\"{info}\"")
                    obtener2 = tv.Temp()
                    consola.append(f"\n\t{obtener2} =T({obtener})")
                    consola.append(f"\n\tT1 = T3({obtener2})")
                    consola.append(f"\n\t{asig.id} = T1[1] \n")





            else:

                print("si sale")
                print(asig.E.listaE)
                e = Expresion.traducir(asig.E, ts, consola, exception, tv, regla, antes, optimizado, asig.id)
                print(e)
                consola.append(f'\t{asig.id} = {e}\n')
        except:

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