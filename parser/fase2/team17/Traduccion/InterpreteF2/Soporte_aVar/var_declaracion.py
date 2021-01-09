from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.simbolo import Simbolo
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ReporteOptimizacion import ReporteOptimizacion
from InterpreteF2.Reporteria.ReporteTS import ReporteTS

class var_declaracion(NodoArbol):

    def __init__(self, identificador, tipo, exp, line, coliumn):
        super().__init__(line, coliumn)
        self.exp = exp
        self.tipo = tipo
        self.identificador = identificador

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        if self.exp != None:
            val_exp:Valor = self.exp.getValueAbstract(entorno, arbol)
            if str(self.tipo) != str(val_exp.tipo):
                # ERROR de tipos incompatibles
                pass
        return

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        if self.exp != None:

            expres = self.exp.traducir(entorno, arbol)

            # modulo de insercion a TS
            try:
                val_exp = self.exp.getValueAbstract(entorno, arbol)
                simbol: Simbolo = Simbolo(str(self.identificador), val_exp.tipo, val_exp)
                if str(expres[1]) == '8-12' or str(expres[1]) == '9-13' or str(expres[1]) == '10-14' or \
                        str(expres[1]) == '11-15' or str(expres[1]) == '16' or str(expres[1]) == '17' \
                        or str(expres[1]) == '18':
                    simbol.setTemp(str(expres[0]))
                else:
                    simbol.setTemp(str(expres))
                entorno.insertar_variable(simbol)
            except:
                val_exp = Valor(2, 'DML')
                simbol: Simbolo = Simbolo(str(self.identificador), val_exp.tipo, val_exp)
                if str(expres[1]) == '8-12' or str(expres[1]) == '9-13' or str(expres[1]) == '10-14' or \
                        str(expres[1]) == '11-15' or str(expres[1]) == '16' or str(expres[1]) == '17' \
                        or str(expres[1]) == '18':
                    simbol.setTemp(str(expres[0]))
                else:
                    simbol.setTemp(str(expres))
                entorno.insertar_variable(simbol)



            # -->
            # Modulo de rporteria:
            reportero = ReporteTS(str(self.identificador), str(self.identificador), 'Variable', 'N/A', str(self.linea), str(self.columna))
            arbol.ReporteTS.append(reportero)
            # -->


            # ----------------------------------------------------------------------------------

            # modulo de insercion a TS optimizado
            try:
                tmp = str(self.identificador)
                if str(expres[1]) == '8-12':
                    # Regla no. 9 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' + 0'
                    optimizado = str(tmp) + ' = ' + str(expres[0])
                    reportero = ReporteOptimizacion('Regla 12', original, optimizado, str(self.linea),
                                                    str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '9-13':
                    # Regla no. 9 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' - 0'
                    optimizado = str(tmp) + ' = ' + str(expres[0])
                    reportero = ReporteOptimizacion('Regla 13', original, optimizado, str(self.linea),
                                                    str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '10-14':
                    # Regla no. 9 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' * 1'
                    optimizado = str(tmp) + ' = ' + str(expres[0])
                    reportero = ReporteOptimizacion('Regla 14', original, optimizado, str(self.linea),
                                                    str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '11-15':
                    # Regla no. 9 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' / 1'
                    optimizado = str(tmp) + ' = ' + str(expres[0])
                    reportero = ReporteOptimizacion('Regla 15', original, optimizado, str(self.linea),
                                                    str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '16':
                    # Regla no. 16 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' * 2'
                    optimizado = str(tmp) + ' = ' + str(expres[0]) + ' + ' + str(expres[0])
                    reportero = ReporteOptimizacion('Regla 16', original, optimizado, str(self.linea),
                                                    str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '17':
                    # Regla no. 17 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' * 0'
                    optimizado = str(tmp) + ' = 0'
                    reportero = ReporteOptimizacion('Regla 17', original, optimizado, str(self.linea),
                                                    str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '18':
                    # Regla no. 18 -----------------------------
                    original = str(tmp) + ' = 0 / ' + str(expres[0])
                    optimizado = str(tmp) + ' = 0'
                    reportero = ReporteOptimizacion('Regla 18', original, optimizado, str(self.linea),
                                                    str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
            except:
                pass
            # ----------------------------------------------------------------------------------




        else:
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = '' #" + str(self.identificador))
            val_exp:Valor = Valor(2, 'NULL')
            simbol:Simbolo = Simbolo(str(self.identificador), val_exp.tipo, val_exp)
            simbol.setTemp(str(tmp))
            entorno.insertar_variable(simbol)

            # -->
            # Modulo de rporteria:
            reportero = ReporteTS(str(self.identificador), str(self.identificador), 'Variable', 'N/A', str(self.linea),
                                  str(self.columna))
            arbol.ReporteTS.append(reportero)
            # -->

        #self.analizar_semanticamente(entorno, arbol)
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
