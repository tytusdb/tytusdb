import AST.Nodo as Node
from TablaSimbolos.Tipos import *
from prettytable import PrettyTable
from Errores.Nodo_Error import *
import data.jsonMode as jm
import os
import json


class Select(Node.Nodo):
    def __init__(self, *args):
        if args[0] == '*':
            self.arguments = None
            self.tables = [args[1]]
            self.line = args[3]
            self.column = args[4]
            self.conditions = args[2]
            self.result_query = PrettyTable()
        else:
            self.arguments = args[0]
            self.tables = args[1]
            self.line = args[3]
            self.column = args[4]
            self.conditions = args[2]
            self.result_query = PrettyTable()

    def ejecutar(self, TS, Errores):
        columnas = []
        result = 'Query from tables: '
        for columna in self.arguments:
            columna.ejecutar(TS, Errores)
            columnas.append(columna.val)
        self.result_query.field_names = columnas
        for obj in self.tables:
            result += str(obj)
        db = os.environ['DB']
        #jm.extractRow(db, self.tables, self.arguments)
        result += '\n' + self.result_query.get_string()
        return result

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


class Delete(Node.Nodo):
    def __init__(self, id, condicion, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.id = id
        self.condicion = condicion

    def ejecutar(self, TS, Errores):
        bd = os.environ['DB']
        columna_id = None  #falta restringir para enviar nombre de columna

        if self.condicion != '':
            jm.delete(bd, self.id, columna_id)
        else: 
            jm.truncate(bd,self.id)

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_TB%s" % self.mi_id, 'id: %s' % self.id)
        grafica.edge(self.mi_id,"nombre_TB" + self.mi_id)

        if self.condicion != '':
            grafica.node("Condicion%s" % self.mi_id, 'where: %s' % self.condicion.val)
            grafica.edge(self.mi_id, "Condicion"+self.mi_id)


class UseDB(Node.Nodo):
    def __init__(self, id, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.id = id

    def ejecutar(self, TS, Errores):
        jm.initCheck()
        dump = False
        with open('data/json/databases') as file:
            data = json.load(file)
            if not self.id in data:
                Errores.insertar(Nodo_Error("TytusDB: 08003", "\'" + str(self.id) + "\' connection_does_not_exist", self.fila, self.columna))
                return 'Error 08003: connection_does_not_exists. Database \'' + str(self.id) + '\' dose not exists.'
            else:
                os.environ['DB'] = str(self.id)
                return 'Base de Datos ' + str(self.id) + ' seleccionada.'

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_DB%s" % self.mi_id, 'id: %s' % self.id)
        grafica.edge(self.mi_id,"nombre_DB" + self.mi_id)