import sys
from datetime import datetime

sys.path.append("../../..")
from analizer.abstract import instruction
from analizer.reports.AST import AST
from analizer.symbol.environment import Environment
import analizer.symbol.c3dSymbols as SymbolTable
from analizer.abstract.expression import TYPE
from analizer.reports.Nodo import Nodo

envFunction = Environment(for3d=True)

class Function(instruction.Instruction):
    def __init__(self, name, type_, params, block, row, column) -> None:
        self.params = params
        self.block = block
        self.name = name
        self.type = type_
        super().__init__(row, column)

    def generate3d(self, environment, instanciaAux):
        #Agregacion a la tabla
        for (nombre, tipo) in self.params:
            valores = defaultValues(tipo[0])
            SymbolTable.add_symbol(nombre, valores[0], valores[1], 0,0,None)

        header = f'\n@with_goto\ndef {self.name}(' # solo le quite la f :v
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

    def execute(self, environment):        
        if not envFunction.addFunc(self.name, self):
            instruction.semanticErrors.append(
                ("ERROR: Ya existe la función '%s'" %self.name,self.row)
            )

    def compareParamsTypes(self) -> list:
        types = []

        for param in self.params:
            types.append(param.type)

        return types

    def compareParamsPrimitive(self) -> list:
        types = []

        for param in self.params:
            types.append(defaultValues(param[1][0])[0])

        return types
        
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
                    for dimen in param[1][1]:
                        dim.addNode(Nodo(str(dimen)))
                    tipo.addNode(dim)
                params.addNode(parametro)
            new.addNode(params)

        block = self.block.dot()
        new.addNode(block)
        
        returns = Nodo('RETURNS')
        tipe = Nodo("TIPO")
        tipe.addNode(Nodo(self.type[0]))
        if self.type[1][0] != None:
            dimension = Nodo("DIMENSION")
            dimension.addNode(Nodo(str(self.type[1][0])))
            tipe.addNode(dimension)
        returns.addNode(tipe)
        new.addNode(returns)

        return new

    
def dropFunc(lista, existencia = False):
    print(lista)
    for func in lista:
        if isinstance(func, tuple):
            if func[0] in envFunction.functions:
                actual = envFunction.getFunc(func[0])
                if len(actual.params) != len(func[1]):
                    instruction.semanticErrors.append(
                        ("ERROR: El número de parametros no coincide con la función",0)
                    )
                tipos = []
                for param in func[1]:
                    tipos.append(param[0])
                
                if tipos != actual.compareParamsTypes():
                    instruction.semanticErrors.append(
                        ("ERROR: El tipos de parametros no coincide con la función",0)
                    )

                envFunction.functions.pop(func[0])
            elif not existencia:
                instruction.semanticErrors.append(
                    ("ERROR: La función no existe",0)
                )
        else:
            if func in envFunction.functions:
                envFunction.functions.pop(func)
            elif not existencia:
                instruction.semanticErrors.append(
                    ("ERROR: La función no existe",0)
                )

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