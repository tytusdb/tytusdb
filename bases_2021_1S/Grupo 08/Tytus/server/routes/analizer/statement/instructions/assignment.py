from routes.analizer.reports import Nodo
from routes.analizer.abstract import instruction
from routes.analizer.abstract.expression import Expression


class Assignment(instruction.Instruction):
    def __init__(self, id, value, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.id = id
        self.value = value

    def execute(self, environment):
        if self.value != "DEFAULT":
            self.value = self.value.execute(environment).value
        return self

    def dot(self):
        new = Nodo.Nodo("=")
        idNode = Nodo.Nodo(str(self.id))
        new.addNode(idNode)
        new.addNode(self.value.dot())
        return new
