import copy
import pickle

from parserT28.views.data_window import DataWindow
from parserT28.utils.decorators import singleton
from parserT28.controllers.symbol_table import SymbolTable
from parserT28.controllers.error_controller import ErrorController


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

    def saveProcedure(self, name, tac, _return, line, column):
        """
        Method to create a stored procedure in the structure

        :param name: Stored procedure name
        :param tac: Three-address code of procedure
        :param line: The instruction line
        :param column: The instruction column
        :return: Returns nothing
        """
        self.loadFile()

        db = SymbolTable().useDatabase
        # if not db:
        #    desc = f": Database not selected"
        #    ErrorController().add(4, 'Execution', desc,
        #                          line, column)
        #    return

        key = f"{name}"
        if self.__searchProcedure(key):
            desc = f": Function {name} already exists"
            ErrorController().add(38, 'Execution', desc, line, column)
            return False

        newTac = copy.deepcopy(tac)

        if _return is not None:
            _return = _return.compile()

        self.__storedProcedure[key] = {
            'name': name,
            'database': db,
            'tac': newTac,
            'line': line,
            'column': column,
            'return': _return
        }

        self.writeFile()
        return True

    def getReturnType(self, id):
        return self.__storedProcedure[id]['return']

    def getProcedure(self, name, params, line, column):
        self.loadFile()

        # db = SymbolTable().useDatabase
        # if not db:
        #    desc = f": Database not selected"
        #    ErrorController().add(4, 'Execution', desc,
        #                          line, column)
        #    return

        # key = f"{name}{db}"
        key = f"{name}"
        if key in self.__storedProcedure:
            if params == len(self.__storedProcedure[key]['tac'].params):
                sp = copy.deepcopy(self.__storedProcedure[key]['tac'])
                return sp.print(sp.environment)

        desc = f": Function {name} does not exist"
        ErrorController().add(39, 'Execution', desc, line, column)
        return None

    def getParams(self, name):
        self.loadFile()
        db = SymbolTable().useDatabase
        key = f"{name}{db}"

        if key in self.__storedProcedure:
            return self.__storedProcedure[key]['tac'].params

        return []

    def getProceduresIDs(self):
        return self.__storedProcedure.keys()

    def dropProcedure(self, name, line, column):
        self.loadFile()

        # db = SymbolTable().useDatabase
        # if not db:
        #    desc = f": Database not selected"
        #    ErrorController().add(4, 'Execution', desc,
        #                          line, column)
        #    return

        # key = f"{name}{db}"
        key = f"{name}"
        if key in self.__storedProcedure:
            DataWindow().consoleText('Query returned successfully: Function deleted')
            self.__storedProcedure.pop(key)
            self.writeFile()
            return True

        return False

    def loadFile(self):
        try:
            with open('data/json/functionsAndProcedures.pkl', 'rb') as input:
                self.__storedProcedure = pickle.load(input)
                print(self.__storedProcedure)
        except IOError:
            # print('Error: File does not appear to exist.')
            pass

    def writeFile(self):
        try:
            with open('data/json/functionsAndProcedures.pkl', 'wb') as output:
                pickle.dump(self.__storedProcedure, output,
                            pickle.HIGHEST_PROTOCOL)
        except IOError:
            # print('Error: File does not appear to exist.')
            pass
