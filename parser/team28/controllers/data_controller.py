from controllers.error_controller import ErrorController
from controllers.symbol_table import SymbolTable
from controllers import data_mode


class DataController(object):
    def __init__(self):
        pass

    def showDatabases(self) -> list:
        databases = []
        for i in range(1, 6):
            mode = data_mode.mode(i)
            if mode:
                databases += mode.showDatabases()
        return databases
