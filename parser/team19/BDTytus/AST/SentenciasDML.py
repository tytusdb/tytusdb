import AST.Nodo as Node
from TablaSimbolos.Tipos import *
from Errores.Nodo_Error import *


class Select(Node.Nodo):
    def __init__(self, *args):
        if args[0] == '*':
            self.arguments = None
            self.tables = args[1]
            self.line = args[3]
            self.column = args[4]
            self.conditions = args[2]
        else:
            self.arguments = args[0]
            self.tables = args[1]
            self.line = args[3]
            self.column = args[4]
            self.conditions = args[2]


    def ejecutar(self, TS, Errores):
        return 1

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        return 1


class Insert(Node.Nodo):
    def __init__(self, table_id, values, file, col):
        self.table_id = table_id
        self.values = values
        self.fila = file
        self.columna = col

    def ejecutar(self, TS, Errores):
        return 1

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        return 1


class Update(Node.Nodo):
    def __init__(self, table_id, list_id, list_values, file, col):
        self.table_id = table_id
        self.list_id = list_id
        self.values = list_values
        self.fila = file
        self.columna = col

    def ejecutar(self, TS, Errores):
        return 1

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        return 1



