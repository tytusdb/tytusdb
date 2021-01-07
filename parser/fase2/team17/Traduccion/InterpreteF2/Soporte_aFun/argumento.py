from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos
from InterpreteF2.simbolo import Simbolo

class argumento(NodoArbol):

    def __init__(self, identificador, tipo, line, coliumn):
        super().__init__(line, coliumn)
        self.tipo = tipo
        self.identificador = identificador

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        tmp = arbol.getTemp()
        arbol.addC3D(tmp + " = " + str(self.identificador))
        val_exp:Valor = Valor(TIPO.CADENA, 'NULL')
        simbol:Simbolo = Simbolo(str(self.identificador), val_exp.tipo, val_exp)
        simbol.setTemp(str(tmp))
        entorno.insertar_variable(simbol)

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getID(self):
        return self.identificador
