from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.Reporteria.ReporteOptimizacion import ReporteOptimizacion
from InterpreteF2.Soporte_aVar.var_declaracion import var_declaracion

class var_asignacion(NodoArbol):

    def __init__(self, identificador, exp, line, coliumn):
        super().__init__(line, coliumn)
        self.exp = exp
        self.identificador = identificador

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):

        if entorno.varibaleExiste(str(self.identificador)):
            pass
        else:
            tmp = ''
            try:
                nodo = var_declaracion(str(self.identificador), 0, self.exp, self.linea, self.columna)
                tmp = nodo.traducir(entorno, arbol)
            except:
                tmp = arbol.getTemp()
                arbol.addC3D(tmp + ' = \'Invalid\'')
            return tmp

        tmp = entorno.obtener_temporal_deVar(str(self.identificador))
        #val:Valor = self.exp.getValueAbstract(entorno, arbol)
        expres = self.exp.traducir(entorno, arbol)

        try:
            if str(tmp) == str(expres[0]):

                if str(expres[1]) == '8-12':
                    # Regla no. 8 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' + 0'
                    optimizado = 'Se elimina la instruccion'
                    reportero = ReporteOptimizacion('Regla 8', original, optimizado, str(self.linea), str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '9-13':
                    # Regla no. 8 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' - 0'
                    optimizado = 'Se elimina la instruccion'
                    reportero = ReporteOptimizacion('Regla 9', original, optimizado, str(self.linea), str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '10-14':
                    # Regla no. 8 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' * 1'
                    optimizado = 'Se elimina la instruccion'
                    reportero = ReporteOptimizacion('Regla 10', original, optimizado, str(self.linea), str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '11-15':
                    # Regla no. 11 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' / 1'
                    optimizado = 'Se elimina la instruccion'
                    reportero = ReporteOptimizacion('Regla 11', original, optimizado, str(self.linea), str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '16':
                    arbol.addC3D(tmp + ' = ' + str(expres[0]) + ' + ' + str(expres[0]))
                    # Regla no. 16 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' * 2'
                    optimizado = str(tmp) + ' = ' + str(expres[0]) + ' + ' + str(expres[0])
                    reportero = ReporteOptimizacion('Regla 16', original, optimizado, str(self.linea), str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '17':
                    arbol.addC3D(tmp + ' = 0')
                    # Regla no. 17 -----------------------------
                    original = str(tmp) + ' = ' + str(expres[0]) + ' * 0'
                    optimizado = str(tmp) + ' = 0'
                    reportero = ReporteOptimizacion('Regla 17', original, optimizado, str(self.linea), str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
                elif str(expres[1]) == '18':
                    arbol.addC3D(tmp + ' = 0')
                    # Regla no. 18 -----------------------------
                    original = str(tmp) + ' = 0 / ' + str(expres[0])
                    optimizado = str(tmp) + ' = 0'
                    reportero = ReporteOptimizacion('Regla 18', original, optimizado, str(self.linea), str(self.columna))
                    arbol.ReporteOptimizacion.append(reportero)
                    # -----------------------------------------------------------------------------
                    return
            elif str(expres[1]) == '8-12':
                arbol.addC3D(tmp + ' = ' + str(expres[0]))
                # Regla no. 9 -----------------------------
                original = str(tmp) + ' = ' + str(expres[0]) + ' + 0'
                optimizado = str(tmp) + ' = ' + str(expres[0])
                reportero = ReporteOptimizacion('Regla 12', original, optimizado, str(self.linea), str(self.columna))
                arbol.ReporteOptimizacion.append(reportero)
                # -----------------------------------------------------------------------------
                return
            elif str(expres[1]) == '9-13':
                arbol.addC3D(tmp + ' = ' + str(expres[0]))
                # Regla no. 9 -----------------------------
                original = str(tmp) + ' = ' + str(expres[0]) + ' - 0'
                optimizado = str(tmp) + ' = ' + str(expres[0])
                reportero = ReporteOptimizacion('Regla 13', original, optimizado, str(self.linea), str(self.columna))
                arbol.ReporteOptimizacion.append(reportero)
                # -----------------------------------------------------------------------------
                return
            elif str(expres[1]) == '10-14':
                arbol.addC3D(tmp + ' = ' + str(expres[0]))
                # Regla no. 9 -----------------------------
                original = str(tmp) + ' = ' + str(expres[0]) + ' * 1'
                optimizado = str(tmp) + ' = ' + str(expres[0])
                reportero = ReporteOptimizacion('Regla 14', original, optimizado, str(self.linea), str(self.columna))
                arbol.ReporteOptimizacion.append(reportero)
                # -----------------------------------------------------------------------------
                return
            elif str(expres[1]) == '11-15':
                arbol.addC3D(tmp + ' = ' + str(expres[0]))
                # Regla no. 9 -----------------------------
                original = str(tmp) + ' = ' + str(expres[0]) + ' / 1'
                optimizado = str(tmp) + ' = ' + str(expres[0])
                reportero = ReporteOptimizacion('Regla 15', original, optimizado, str(self.linea), str(self.columna))
                arbol.ReporteOptimizacion.append(reportero)
                # -----------------------------------------------------------------------------
                return
            elif str(expres[1]) == '16':
                arbol.addC3D(tmp + ' = ' + str(expres[0]) + ' + ' + str(expres[0]))
                # Regla no. 16 -----------------------------
                original = str(tmp) + ' = ' + str(expres[0]) + ' * 2'
                optimizado = str(tmp) + ' = ' + str(expres[0]) + ' + ' + str(expres[0])
                reportero = ReporteOptimizacion('Regla 16', original, optimizado, str(self.linea), str(self.columna))
                arbol.ReporteOptimizacion.append(reportero)
                # -----------------------------------------------------------------------------
                return
            elif str(expres[1]) == '17':
                arbol.addC3D(tmp + ' = 0')
                # Regla no. 17 -----------------------------
                original = str(tmp) + ' = ' + str(expres[0]) + ' * 0'
                optimizado = str(tmp) + ' = 0'
                reportero = ReporteOptimizacion('Regla 17', original, optimizado, str(self.linea), str(self.columna))
                arbol.ReporteOptimizacion.append(reportero)
                # -----------------------------------------------------------------------------
                return
            elif str(expres[1]) == '18':
                arbol.addC3D(tmp + ' = 0')
                # Regla no. 18 -----------------------------
                original = str(tmp) + ' = 0 / ' + str(expres[0])
                optimizado = str(tmp) + ' = 0'
                reportero = ReporteOptimizacion('Regla 18', original, optimizado, str(self.linea), str(self.columna))
                arbol.ReporteOptimizacion.append(reportero)
                # -----------------------------------------------------------------------------
                return
        except:
            pass

        arbol.addC3D(tmp + ' = ' + expres)

        '''if str(val.tipo) == '2':
            arbol.addC3D(tmp + ' = ' + '\'' + str(val.data) + '\'')
        else:
            arbol.addC3D(tmp + ' = ' + str(val.data))'''
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
