from analizer.abstract.expression import Expression, TYPE
from analizer.abstract import expression
from analizer.symbol.environment import Environment
from analizer.reports import Nodo
import analizer.symbol.c3dSymbols as SymbolTable


class Identifiers(Expression):
    """
    Esta clase representa los nombre de columnas
    """

    def __init__(self, table, name, row, column):
        super().__init__(row, column)
        self.table = table
        self.name = name
        if table == None:
            self.temp = name
        else:
            self.temp = table + "." + name
        self.type = None

    def execute(self, environment):
        if isinstance(environment,Environment) and not environment.for3d:
            print('Probando...')
            if not self.table:
                table = environment.ambiguityBetweenColumns(self.name)
                if table[0]:  # Si existe ambiguedad
                    return
                else:
                    if table[1]:
                        self.table = table[1]
                        col = self.table + "." + self.name
                        self.value = environment.dataFrame[col]
                    else:
                        x = environment.getVar(self.name)
                        if not x:
                            expression.list_errors.append(
                                "Error: 42703: columna  "
                                + str(self.name)
                                + " no existe \n En la linea: "
                                + str(self.row)
                            )
                            self.table = ""
                            self.name = ""
                            self.value = ""
                        else:
                            self.table = x[0]
                            self.name = x[1]
                            self.value = environment.getColumn(self.table, self.name)
            else:
                self.value = environment.getColumn(self.table, self.name)
            type_ = environment.getType(self.table, self.name)
            self.type = type_
            return self
        else:
            if not SymbolTable.search_symbol(self.name)==0:
                nombre,tipo,valor=SymbolTable.search_symbol(self.name)
                while not SymbolTable.search_symbol(valor)==0:
                    nombre,tipo,valor=SymbolTable.search_symbol(valor)
                self.type=tipo
                self.value=valor
                print(self.type, self.value)
                return self
            else:
                expression.list_errors.append(
                    "Error: 42703: la variable  "
                    + str(self.name)
                    + " no existe \n En la linea: "
                    + str(self.row)
                )

    def dot(self):
        nod = Nodo.Nodo(self.name)
        return nod

    def generate3d(self,environment, instanciaAux , fase =2):
        return str(self.name) # TANTO PARA FASE 1 O FASE 2 SE RETORNA LO MISMO