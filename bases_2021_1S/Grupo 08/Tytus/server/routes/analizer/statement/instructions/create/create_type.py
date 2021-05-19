from routes.analizer.abstract import instruction
from routes.analizer.typechecker.Metadata import Struct
from routes.analizer.reports import Nodo


class CreateType(instruction.Instruction):
    def __init__(self, exists, name, row, column, values=[]):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.values = values

    def execute(self, environment):
        Struct.load()
        lista = []
        for value in self.values:
            lista.append(value.execute(environment).value)
        result = Struct.createType(self.exists, self.name, lista)
        if result == None:
            report = "Type creado"
        else:
            report = result
        return report

    def dot(self):
        new = Nodo.Nodo("CREATE_TYPE")
        if self.exists:
            exNode = Nodo.Nodo("IF_NOT_EXISTS")
            new.addNode(exNode)
        idNode = Nodo.Nodo(self.name)
        new.addNode(idNode)
        paramsNode = Nodo.Nodo("PARAMS")
        new.addNode(paramsNode)
        for v in self.values:
            paramsNode.addNode(v.dot())
        return new
