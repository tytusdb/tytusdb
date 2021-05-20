from abc import abstractmethod

from utilities.storage import avlMode
from utilities.analisys_parser.analizer.typechecker.Metadata import Struct
from utilities.analisys_parser.analizer.typechecker import Checker
from utilities.analisys_parser.analizer.reports import Nodo
from utilities.analisys_parser.analizer.reports import AST

ast = AST.AST()
root = None

envVariables = []


# carga de datos
Struct.load()

# variable encargada de almacenar la base de datos a utilizar
dbtemp = ""
# listas encargadas de almacenar los errores semanticos
syntaxPostgreSQL = list()
semanticErrors = list()


def makeAst(root):
    ast.makeAst(root)


class Instruction:
    """
    Esta clase representa una instruccion
    """

    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

    @abstractmethod
    def execute(self, environment):
        """
        Metodo que servira para ejecutar las expresiones
        """


class useDataBase(Instruction):
    def __init__(self, db, row, column):
        Instruction.__init__(self, row, column)
        self.db = db

    def execute(self, environment):
        dbs = avlMode.showDatabases()
        #dbs = jsonMode.showDatabases()
        if self.db in dbs:
            global dbtemp
            dbtemp = self.db
            return "Se cambio la base de datos a: " + dbtemp
        syntaxPostgreSQL.append(
            "Error: 42000: La base de datos " + self.db + " no existe"
        )
        semanticErrors.append(
            ["La base de datos " + str(self.db) + " no existe", self.row]
        )
        return "La base de datos: " + self.db + " no existe."

    def dot(self):
        new = Nodo.Nodo("USE_DATABASE")
        n = Nodo.Nodo(self.db)
        new.addNode(n)

        return new


def returnErrors():
    list_ = list()
    list_ = Checker.returnErrors()
    list_ += syntaxPostgreSQL
    return list_


def returnSemanticErrors():
    return semanticErrors