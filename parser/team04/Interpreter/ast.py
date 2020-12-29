from Interpreter.environment import Environment
from Interpreter.Expression.native import *
from Statics.errorTable import ErrorTable
from Statics.symbolTable import SymbolTable
from graphviz import Digraph


class Ast:
    def __init__(self, root):
        self.root = root

    def execute(self):
        print("Ejecutando el AST...")
        env = Environment(functions=getNativeFuncs())

        for inst in self.root:
            inst.execute(env)

        ErrorTable.clear()
        ErrorTable.load()
        SymbolTable.clear()
        SymbolTable.load()

    def getGraph(self):
        print("Generando el grafo")

        u = Digraph('unix', filename='unix.gv',
                    node_attr={'color': 'lightblue2', 'style': 'filled'})
        u.attr(size='6,6')
        _id = str(id(self))
        _label = self.__class__.__name__
        u.node(_id, label=_label)

        for inst in self.root:
            inst.getGraph(u, _id)

        u.view()
