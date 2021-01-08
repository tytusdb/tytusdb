from datetime import datetime
import sys

sys.path.append("../../..")
from analizer.abstract import instruction
from analizer.reports.Nodo import Nodo
from analizer.symbol.environment import Environment
import analizer.symbol.c3dSymbols as SymbolTable
from analizer.abstract.expression import TYPE

envProcedure = Environment(for3d=True)

class Procedure(instruction.Instruction):
    def __init__(self, name, params, block, row, column) -> None:
        self.params = params
        self.block = block
        self.name = name
        super().__init__(row, column)

    def generate3d(self, environment, instanciaAux):
        for (nombre, tipo) in self.params:
            valores = defaultValues(tipo[0])
            SymbolTable.add_symbol(nombre, valores[0], valores[1], 0,0,None)

        header = f'\n@with_goto\ndef p{self.name}('
        for param in range(len(self.params)):
            header += self.params[param][0]
            if param != len(self.params) -1:
                header += ","
        header += '):'

        eFinal = instanciaAux.getNewLabel()
        newEnv = Environment(environment)
        newEnv.addVar('eFinal',eFinal, 'Etiqueta', self.row, self.column)

        instanciaAux.addToCode(header)

        self.block.generate3d(newEnv, instanciaAux)
        SymbolTable.symbolTable.clear()

        instanciaAux.addToCode(f'\tlabel .{eFinal}')

    def compareParamsTypes(self) -> list:
        types = []

        for param in self.params:
            types.append(param[1])

        return types

    def compareParamsPrimitive(self) -> list:
        types = []

        for param in self.params:
            types.append(defaultValues(param[1][0])[0])

        return types

    def execute(self, environment):        
        if not envProcedure.addProc(self.name, self):
            instruction.semanticErrors.append(
                ("ERROR: Ya existe procedimiento '%s'" %self.name,self.row)
            )
            

    def dot(self):
        new = Nodo('CREATE FUNCTION')
        nombre_func = Nodo("IDENTIFICADOR DE FUNCION")
        nombre_func.addNode(Nodo(self.name))
        new.addNode(nombre_func)
        if len(self.params) > 0:
            params = Nodo('PARAMETROS')
            for param in self.params:
                parametro = Nodo("PARAMETRO")
                id = Nodo("IDENTIFICADOR")
                identi = Nodo(param[0])
                id.addNode(identi)
                parametro.addNode(id)
                tipo = Nodo("TIPO")
                type_node = Nodo(param[1][0])
                tipo.addNode(type_node)
                parametro.addNode(tipo)
                if param[1][1][0] != None:
                    dim = Nodo("DIMENSION")
                    dim.addNode(Nodo(str(param[1][1][0])))
                    tipo.addNode(dim)
                params.addNode(parametro)
            new.addNode(params)
        block = self.block.dot()
        new.addNode(block)

        return new

def defaultValues(type_) -> tuple:
    if type_ in ('DECIMAL', 'INTEGER', 'INT', 'SMALLINT', 'BIGINT', 'DECIMAL', 'NUMERIC', 'REAL', 'DOUBLE', 'MONEY'):
        return (TYPE.NUMBER, 1)
    elif type_ in ('TEXT', 'VARCHAR', 'CHAR', 'CHARACTER', 'VARYING'):
        return (TYPE.STRING, "")
    elif type_ == 'DATE':
        return (TYPE.DATE, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    elif type_ == 'TIMESTAMP':
        return (TYPE.TIMESTAMP,datetime.now().strftime("%Y-%m-%d"))
    elif type_ == 'TIME':
        return (TYPE.TIME,datetime.now().strftime("%H:%M:%S"))
    else:
        return (TYPE.BOOLEAN, False)

    
def dropProc(lista, existencia = False):
    for proc in lista:
        if isinstance(proc, tuple):
            if proc[0] in envProcedure.procedures:
                actual = envProcedure.getProc(proc[0])
                if len(actual.params) != len(proc[1]):
                    instruction.semanticErrors.append(
                        ("ERROR: El número de parametros no coincide con el procedimiento",0)
                    )
                tipos = []
                for param in proc[1]:
                    tipos.append(param[0])
                
                if tipos != actual.compareParamsTypes():
                    instruction.semanticErrors.append(
                        ("ERROR: El tipo de parametros no coincide con el procedimiento",0)
                    )
                
                envProcedure.procedures.pop(proc[0])
            elif not existencia:
                instruction.semanticErrors.append(
                    ("ERROR: El procedimiento no existe",0)
                )
        else:
            if proc in envProcedure.procedures:
                envProcedure.procedures.pop(proc)
            elif not existencia:
                instruction.semanticErrors.append(
                    ("ERROR: El procedimiento no existe",0)
                ) 