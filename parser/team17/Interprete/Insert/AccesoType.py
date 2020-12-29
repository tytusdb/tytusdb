from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.Primitivos.TIPO import TIPO
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.simbolo import Simbolo

class AccesoType(NodoArbol):

    def __init__(self, indentificador, acceso, line, coliumn):
        super().__init__(line, coliumn)
        self.indentificador = indentificador
        self.acceso = acceso

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        identificador = self.indentificador.referencia
        val:Valor = entorno.obtener_varibale(identificador)
        indiceV:Valor = self.acceso.execute(entorno, arbol)
        return val.getTipo_ofType(int(str(indiceV.data)))