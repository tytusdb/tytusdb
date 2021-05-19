from  Fase1.analizer.abstract import instruction
from  Fase1.analizer.typechecker.Metadata import Struct
from  Fase1.analizer.reports import Nodo
from  Fase1.storage.storageManager import storage


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
        
        """
        0: insert
        1: error
        2: exists
        """

        if self.mode == None:
            self.mode = 'avl'
        elif self.mode == 1:
            self.mode = 'avl'
        elif self.mode == 2:
            self.mode = 'b'
        elif self.mode == 3:
            self.mode = 'bplus'
        elif self.mode == 4: 
            self.mode = 'dict'
        elif self.mode == 5:
            self.mode = 'isam'
        elif self.mode == 6:
            self.mode = 'json'
        elif self.mode == 7:
            self.mode = 'hash'
            
        result = storage.createDatabase(self.name, self.mode)
        if result == 0:
            Struct.createDatabase(self.name, self.mode, self.owner)
            report = "Base de datos: " + self.name + " insertada."
        elif result == 1:
            instruction.syntaxPostgreSQL.append("Error: XX000: Error interno")
            report = "Error al insertar la base de datos: " + self.name
        elif result == 2 and self.replace:
            Struct.replaceDatabase(self.name, self.mode, self.owner)
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