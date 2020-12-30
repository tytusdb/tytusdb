import abc
import sys

#sys.path.append("..")


class ASTNode(abc.ABC):

    # method to implement/execute in every instruction
    @abc.abstractmethod
    def execute(self, table, tree):
        # Adding print all node values for debug purposes
        # print(f'{self.__class__.__name__} - {self.additional_args}. Linea: {self.line} columna:  {self.column}')
        pass

    # method to allow generation of C3D in every instruction
    @abc.abstractmethod
    def generate(self, table, tree):
        pass

    # attributes to carry in every instruction
    def __init__(self, line, column, additional_args='Undefined value to report'):
        self.line = line
        self.column = column
        self.additional_args = additional_args
