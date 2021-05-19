from team29.analizer.abstract import instruction
from team29.analizer.typechecker.Metadata import Struct
from team29.analizer.reports import Nodo
import requests
import json
# from storage.storageManager import jsonMode


class CreateDatabase(instruction.Instruction):
    """
    Clase que representa la instruccion CREATE DATABASE
    Esta instruccion es la encargada de crear una nueva base de datos en el DBMS
    """

    def __init__(self, replace, exists, name, owner, mode, row, column):
        instruction.Instruction.__init__(self, row, column)
        self.exists = exists
        self.name = name
        self.mode = mode
        self.owner = owner
        self.replace = replace

    def execute(self, environment):
        Struct.load()
        form_data = {'nameDB': self.name}
        resp = requests.post('http://127.0.0.1:9998/DB/CreateDB', json=form_data)
        """
        0: insert
        1: error
        2: exists
        """
        json1 = json.loads(resp.text)
        result = json1["code"]
        if self.mode == None:
            self.mode = 1
        if result == 0:
            Struct.createDatabase(self.name, self.mode, self.owner)
            report = "Base de datos: " + self.name + " insertada."
        elif result == 1:
            instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
            report = "Error al insertar la base de datos: " + self.name
        elif result == 2 and self.replace:
            Struct.replaceDatabase(self.name, self.mode, self.owner)
            form_data = {'nameDB': self.name}
            resp = requests.post('http://127.0.0.1:9998/DB/dropDatabase', json=form_data)
            form_data = {'nameDB': self.name}
            resp = requests.post('http://127.0.0.1:9998/DB/CreateDB', json=form_data)
            report = "Base de datos '" + self.name + " ' reemplazada."
        elif result == 2 and self.exists:
            report = "Base de datos no insertada, " + self.name + " ya existe."
        else:
            instruction.semanticErrors.append(
                ["La base de datos " + str(self.name) + " ya existe", self.row]
            )
            instruction.syntaxPostgreSQL.append(
                "Error: 42P04: La base de datos  " + str(self.name) + " ya existe"
            )
            report = "Error: La base de datos ya existe"
        return report

    def dot(self):
        new = Nodo.Nodo("CREATE_DATABASE")
        if self.exists:
            ex = Nodo.Nodo("EXISTS")
            new.addNode(ex)

        n = Nodo.Nodo(self.name)
        new.addNode(n)
        if self.owner != None:
            ow = Nodo.Nodo("OWNER")
            own = Nodo.Nodo(self.owner)
            ow.addNode(own)
            new.addNode(ow)
        if self.mode != None:
            mod = Nodo.Nodo("MODE")
            mod2 = Nodo.Nodo(str(self.mode))
            mod.addNode(mod2)
            new.addNode(mod)
        return new