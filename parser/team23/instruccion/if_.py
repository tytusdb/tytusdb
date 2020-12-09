from abstract.instruccion import *
from tools.tabla_tipos import *
from error.errores import *

class if_(instruccion):
    def __init__(self, condicion, code, else_, line, column):
        super().__init__(line, column)
        self.condicion = condicion
        self.code = code
        self.else_ = else_
    
    def ejecutar(self, ambiente):
        try:
            condition = self.condicion.ejecutar(ambiente)

            if condition.tipo != tipo_primitivo.BOOLEAN:
                errores.append(nodo_error(self.line, self.column, 'Semántico', 'La condición debe ser de tipo boolean'))
                return 
            
            if condition.valor == True:
                self.code.ejecutar(ambiente)
            else:
                if self.else_ != None:
                    self.else_.ejecutar(ambiente)
                return

        except:
            pass