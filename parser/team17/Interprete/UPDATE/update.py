from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor

#############################
# Patrón intérprete: UPDATE #
#############################

# UPDATE: modificar atributos de una tabla


class Update(NodoArbol):
    def __init__(self, bd_, tabla_, listaexp_, line, column, condicion_=None):
        super().__init__(line, column)
        self.bd = bd_
        self.tabla = tabla_
        self.listaexp = listaexp_
        self.condicion = condicion_

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        if self.condicion is None:
            pass
            # SET columna1 = 1 + 1
