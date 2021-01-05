from Interpreter.Instruction.instruction import Instruction
from Scripts.jsonMode import showDatabases


class UseDataBase(Instruction):
    def __init__(self, db):
        self.db = db

    def execute(self, env):
        print("Se ejecutó la instrucción 'USE DATABASE'")
        dbList = showDatabases()
        if self.db in dbList:
            env.setCurrentDB(self.db)
        else:
            error = ("Semántico", "La base de datos '%s' no existe" %
                     self.db, "--")
            env.ErrorTable.add(error)

    def getGraph(self, graph, idParent):
        _id = str(id(self))
        _label = self.__class__.__name__
        graph.node(_id, label=_label)
        graph.edge(idParent, _id)

        graph.node(self.db, label=self.db)
        graph.edge(_id, self.db)
