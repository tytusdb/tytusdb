import AST.Nodo as Node
from TablaSimbolos.Tipos import *
from Errores.Nodo_Error import *


class Select(Node.Nodo):
    def __init__(self, Exp1, Exp2, op, fila, col):
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        self.op = op
        self.fila = fila
        self.columna = col

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



