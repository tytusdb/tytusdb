from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Reporteria.ErroresSemanticos import ErroresSemanticos

class RAISE_complex(NodoArbol):

    def __init__(self, exp, ID, line, column):
        super().__init__(line, column)
        self.exp = exp
        self.ID = ID

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return TIPO.CADENA

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        try:
            tmp = self.getValueAbstract(entorno, arbol)
            arbol.addC3D("print(str(" + str(tmp) + "))")
        except:
            arbol.addC3D("print(str(Invalid))")
            descripcion = 'Expresion invalida para el print'
            reportero = ErroresSemanticos(descripcion, str(self.linea), str(self.columna), 'Raise complex')
            arbol.ErroresSemanticos.append(reportero)
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return str(self.data)

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        expresion_: Valor = self.exp.getValueAbstract(entorno, arbol)
        expresion: str = str(expresion_.data)
        expresion_spliteada = expresion.split("%")
        if len(expresion_spliteada) == 2:
            #var = str(self.ID) # <-- aqui va codigo de acceso a la TS para getVar
            #val:Valor = entorno.obtener_varibale(str(self.ID))
            var = str(entorno.obtener_temporal_deVar(str(self.ID)))
            #var = str(val.data)
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = " + '\'' + str(expresion_spliteada[0]) + '\' + ' + var + ' + \'' + str(expresion_spliteada[1]) + "\'")
            return tmp
        else:
            # ERROR -> no hay simbolo de acceso para incrustar var
            pass
        return ""

