import sys

sys.path.append("../../..")
from analizer.abstract import instruction
from analizer.reports import Nodo
from analizer.symbol.environment import Environment

indexEnv = Environment(None,for3d=True)
indicesReg = dict()

class Index(instruction.Instruction):
    def __init__(self, indice, tabla, campos, tipo, row, column) -> None:
        self.index = indice
        self.table = tabla
        self.fields = campos
        self.type = tipo
        super().__init__(row, column)

    def execute(self, environment):
        if not indexEnv in instruction.envVariables:
            instruction.envVariables.append(indexEnv)

        campos = 'Campos: '
        if isinstance(self.fields, list):
            for index in range(len(self.fields)):
                if index == len(self.fields) - 1:
                    campos += self.fields[index] + ';'
                else:
                    campos += self.fields[index] + ', '
        else:
            campos += self.fields +';'

        valor = 'Tabla: ' + self.table + '; ' + campos
        tipo = 'INDEX' if not self.type else 'UNIQUE INDEX'
        if indexEnv.addVar(self.index,  valor, tipo, self.row, self.column):
            indicesReg[self.index] = self
        else:
            pass

    def dot(self):
        texto = "CREATE_INDEX"

        if self.type:
            texto = self.type + "_" + texto

        new = Nodo.Nodo(texto)
        indice = Nodo.Nodo("INDEX")
        nombre = Nodo.Nodo(self.index)
        indice.addNode(nombre)
        
        tabla = Nodo.Nodo("TABLE")
        tNombre = Nodo.Nodo(self.table)
        tabla.addNode(tNombre)

        fields = Nodo.Nodo("FIELDS")
        if isinstance(self.fields, list):
            for campo in self.fields:
                field = Nodo.Nodo(campo)
                fields.addNode(field)
        else:
            field = Nodo.Nodo(self.fields)
            fields.addNode(field)


        new.addNode(indice)
        new.addNode(tabla)
        new.addNode(fields)

        return new

    def __str__(self) -> str:
        return 'Index: ' + self.index

#TODO Implementar errores semanticos
def dropIndex(id):
    if not indexEnv in instruction.envVariables:
        instruction.envVariables.append(indexEnv)

    if id in indexEnv.variables:
        indexEnv.variables.pop(id)
        return indicesReg.pop(id)
    else:
        pass

def alterIndex(id, indice):
    if not indexEnv in instruction.envVariables:
        instruction.envVariables.append(indexEnv)

    if id in indexEnv.variables:
        mod = dropIndex(id)
        try:
            mod.fields.pop(indice)
            mod.execute(None)
        except:
            pass 
    else:
        pass