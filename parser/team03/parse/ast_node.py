import abc
import sys

sys.path.append("..")


class ASTNode(abc.ABC):

    # method to implement/execute in every instruction
    @abc.abstractmethod
    def execute(self, table, tree):
        pass

    # attributes to carry in every instruction
    def __init__(self, line, column):
        self.line = line
        self.column = column
