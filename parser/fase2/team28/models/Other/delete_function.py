from controllers.error_controller import ErrorController
from models.instructions.shared import Instruction


class DeleteFunction(Instruction):
    
    def __init__(self, id, line, column):
        self.id = id
        self.line = line
        self.column = column
        self._tac = ''

    def __repr__(self):
        return str(vars(self))

    def process(self, environment):
        pass

    def compile(self, environment):
        try:
            pass
        except:
            desc = "FATAL ERROR, No existe la funcion o ya fue eliminada "
            ErrorController().add(34, 'Execution', desc, self.line, self.column)