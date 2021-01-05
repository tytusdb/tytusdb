from InterpreteF2.NodoAST import NodoArbol
from InterpreteF2.Tabla_de_simbolos import Tabla_de_simbolos
from InterpreteF2.Arbol import Arbol
from InterpreteF2.Valor.Valor import Valor
from InterpreteF2.Primitivos.TIPO import TIPO
from InterpreteF2.Primitivos.COMPROBADOR_deTipos import COMPROBADOR_deTipos

class var_acceso(NodoArbol):

    def __init__(self, identificador, line, coliumn):
        super().__init__(line, coliumn)
        self.identificador = identificador

    def analizar_semanticamente(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        val:Valor = entorno.obtener_varibale(str(self.identificador))
        return int(val.tipo)

    def traducir(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        temp = 'NULL'
        if entorno.varibaleExiste(str(self.identificador)):
            temp = entorno.obtener_temporal_deVar(str(self.identificador))
        return temp

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        pass

    def getString(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        return str(self.identificador)

    def getValueAbstract(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        val: Valor = entorno.obtener_varibale(str(self.identificador))
        return val
