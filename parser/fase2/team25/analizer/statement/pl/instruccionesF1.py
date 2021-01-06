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
        tres = instanciaAux.getNewTemporal()#TEMPORAL RESULTANTE
        if self.cadena != None:
            instruccionC3D = f'\t{tn} = "{self.cadena}"'
            instanciaAux.addToCode(instruccionC3D)
            instanciaAux.addToCode(f'\tstack.push({tn})')
            instanciaAux.addToCode(f"\t{tres} = funcionIntermedia()")

        return  tres # POR SI FUERA UN SELECT