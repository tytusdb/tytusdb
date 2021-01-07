from analizer.abstract import instruction
from analizer.statement.instructions.select.select import Select
from analizer.statement.instructions.insert import InsertInto
class F1(instruction.Instruction):
    def __init__(self, objeto,cadena_tn , row , column):
        instruction.Instruction.__init__(self, row , column)
        self.objeto = objeto
        self.cadena = cadena_tn[0]
        self.tn = cadena_tn[1]

    def execute(self, environment):
        return self.objeto.execute()

    def dot(self):
        return self.objeto.dot()

    def generate3d(self, environment, instanciaAux):
        instanciaAux.addToCode(self.cadena)
        # VALIDACION DE TIPOS Y EXISTENCIA DE FUNCIONES EN LE INSERT Y EN EL SELECT
        if isinstance(self.objeto , Select):
            self.objeto.validaFuncionesFase2()
        elif isinstance(self.objeto,  InsertInto):
            self.objeto.validaFuncionesFase2()
        return  self.tn # POR SI FUERA UN SELECT