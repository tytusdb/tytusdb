
from analizer.abstract import instruction
from analizer.reports import Nodo
class Raise(instruction.Instruction):
    def __init__(self, string1 ,string2 , row , column ,notice = None):
        instruction.Instruction.__init__(self, row , column)
        self.string1 = string1
        self.string2 = string2
        self.notice = notice

    def execute(self, environment):
        pass

    def dot(self):
        new = Nodo.Nodo("RAISE")
        string1 = Nodo.Nodo("STRING")
        string2 = Nodo.Nodo(self.string2.dot())
        if self.notice:
            notice_ = Nodo.Nodo("NOTICE")
            new.addNode(notice_)
        new.addNode(string1)
        new.addNode(string2)
        return new
    def generate3dToMain(self, environment, instanciaAux):# solo porque este puede venir en el main :v
        try:
            instanciaAux.addToMain(f"\tprint('{self.string1}',{(self.string2.value)})") # en el main no podria generar temporales
        except:
            instanciaAux.addToMain(f"\tprint('{self.string1}',{str(self.string2)})")

    def generate3d(self, environment, instanciaAux):
        instanciaAux.addToCode(f"\tprint('{self.string1}' , {self.string2.generate3d(environment,instanciaAux)})") # en el main no podria generar temporales