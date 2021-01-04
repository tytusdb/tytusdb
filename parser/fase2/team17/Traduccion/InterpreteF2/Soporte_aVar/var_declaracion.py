from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.simbolo import Simbolo
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

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
            tmp = self.exp.traducir(entorno, arbol)
            val_exp:Valor = self.exp.getValueAbstract(entorno, arbol)
            simbol:Simbolo = Simbolo(str(self.identificador), val_exp.tipo, val_exp)
            simbol.setTemp(str(tmp))
            entorno.insertar_variable(simbol)
        else:
            tmp = arbol.getTemp()
            arbol.addC3D(tmp + " = ''")
            val_exp:Valor = Valor(TIPO.CADENA, 'NULL')
            simbol:Simbolo = Simbolo(str(self.identificador), val_exp.tipo, val_exp)
            simbol.setTemp(str(tmp))
            entorno.insertar_variable(simbol)
        #self.analizar_semanticamente(entorno, arbol)
        return

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass
