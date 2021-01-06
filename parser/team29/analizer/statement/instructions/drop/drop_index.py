from analizer.abstract import instruction
from analizer.typechecker.Metadata import File
from analizer.reports import Nodo


class Drop(instruction.Instruction):

    def __init__(self, exists, names, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.names = names
        self.exists = exists

    def execute(self, environment):
        Index = File.importFile("Index")
        result = []
        for name in self.names:
            exists = Index.get(name)
            if not exists:
                if self.exists:
                    result.append("El INDEX : " + name + " no existe")
                else:
                    result.append("Error: El INDEX : " + name + " no existe")
            else:
                Index.pop(name)
                result.append("INDEX : " + name + " eliminado")
        
        File.exportFile(Index,"Index")
        return result


    def dot(self):
        pass