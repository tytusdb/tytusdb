from abc import ABC, abstractmethod
from Interpreter.node import Node


class Instruction(Node):
    def execute(self, env):
        pass

    def getGraph(self, graph, idParent):
        _id = str(id(self))
        _label = self.__class__.__name__
        graph.node(_id, label=_label)
        graph.edge(idParent, _id)
