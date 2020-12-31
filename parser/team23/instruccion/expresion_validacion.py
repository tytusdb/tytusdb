from abstract.instruccion import *
from tools.tabla_tipos import *

class expresion_validacion(instruccion):
    def __init__(self,comando,dato, line, column, num_nodo):
        super().__init__(line,column)