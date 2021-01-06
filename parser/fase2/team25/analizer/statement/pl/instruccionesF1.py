from analizer.abstract import instruction

class F1(instruction.Instruction):
    def __init__(self, objeto,cadena , row , column):
        instruction.Instruction.__init__(self, row , column)
        self.objeto = objeto
        self.cadena = cadena

    def execute(self, environment):
        return objeto.execute()

    def dot(self):
        return objeto.dot()

    def generate3d(self, environment, instanciaAux):
        tn = instanciaAux.getNewTemporal()
        if self.cadena != None:
            instruccionC3D = f'\t{tn} = "{self.cadena}"'
            instanciaAux.addToCode(instruccionC3D)
        return  tn # POR SI FUERA UN SELECT