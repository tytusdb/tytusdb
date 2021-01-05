import copy

from utils.decorators import singleton
from controllers.symbol_table import SymbolTable
from controllers.error_controller import ErrorController


@singleton
class Procedures(object):
    def __init__(self):
        self.__storedProcedure = {}

    def __searchProcedure(self, name: str):
        """
        Method to search a stored procedure in the structure

        :param name: The name of stored procedure
        :return: Returns a stored procedure
        """

        if name in self.__storedProcedure:
            return True
        return False

    def saveProcedure(self, name, tac, line, column):
        """
        Method to create a stored procedure in the structure

        :param name: Stored procedure name
        :param tac: Three-address code of procedure
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        db = SymbolTable().useDatabase
        key = f"{name}{db}"
        if self.__searchProcedure(key):
            desc = f": Function {name} already exists"
            ErrorController().add(38, 'Execution', desc, line, column)
            return False

        newTac = copy.deepcopy(tac)

        self.__storedProcedure[key] = {
            'name': name,
            'database': db,
            'tac': newTac,
            'line': line,
            'column': column
        }
        return True

        # print('PROCEDIMIENTOS Y FUNCIONES ALMACENADAS----------------------')
        # print(self.__storedProcedure)
        # print('------------------------------------------------------------')

    def getProcedure(self, name):
        db = SymbolTable().useDatabase
        key = f"{name}{db}"

        if key in self.__storedProcedure:
            sp = copy.deepcopy(self.__storedProcedure[key]['tac'])
            sp.print(sp.environment)
