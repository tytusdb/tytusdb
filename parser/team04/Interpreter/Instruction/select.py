from Interpreter.Instruction.instruction import Instruction

from Statics.console import Console
from tabulate import tabulate


class Select(Instruction):
    def __init__(self, expression):
        self.expression = expression

    def execute(self, env):
        print("Se ejecutó la instrucción 'SELECT'")
        value = self.expression.getValue(env)
        col = self.getAsColumn(value)

        header = col[0]
        table = [col[1]]
        strTable = tabulate(table, headers=header, tablefmt="psql")

        Console.add(strTable)

    def getAsColumn(self, value):
        if isinstance(value, list):
            return value
        else:
            return [["Columna"], [value]]

    def getGraph(self, graph, idParent):
        _id = str(id(self))
        _label = self.__class__.__name__
        graph.node(_id, label=_label)
        graph.edge(idParent, _id)

        self.expression.getGraph(graph, _id)
