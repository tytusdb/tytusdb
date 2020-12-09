from abstract.instruccion import *
from tools.tabla_tipos import * 
from error.errores import *

class while_(instruccion):
    def __init__(self, condicion, code, line, column):
        super().__init__(line, column)
        self.condicion = condicion
        self.code = code

    def ejecutar(self, ambiente):
        try:
            condition = self.condicion.ejecutar(ambiente)

            if condition.tipo != tipo_primitivo.BOOLEAN:
                errores.append(nodo_error(self.line, self.column, 'Semántico', 'La condición debe ser de tipo boolean'))
                return 

            while(condition):
                self.code.ejecutar(ambiente)
                condition = self.condicion.ejecutar(ambiente)

        except:
            pass