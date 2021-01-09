from analizer.reports.Nodo import Nodo
from analizer.reports.AST import AST
from analizer.abstract import instruction

class f2Statement(instruction.Instruction):
    def __init__(self, row, column, statement) -> None:
        super().__init__(row, column)
        self.statement = statement
    
    def dot(self):
        nuevo_nodo = Nodo("PL STATEMENT")
        nuevo_nodo.addNode(self.statement.dot())
        return nuevo_nodo