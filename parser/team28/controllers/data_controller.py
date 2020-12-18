from controllers.error_controller import ErrorController
from controllers.symbol_table import SymbolTable
from controllers import data_mode


class DataController(object):
    def __init__(self):
        pass

    def showDatabases(self) -> list:
        """
        Method to show all databases

        :return: Returns list of databases
        """
        databases = []
        for i in range(1, 6):
            mode = data_mode.mode(i)
            if mode:
                databases.extend(mode.showDatabases())
        return databases

    def showTables(self, line, column) -> list:
        """
        Method to show all tables in a database

        :return: Returns list of tables
        """
        database = SymbolTable().useDatabase
        if not database:
            desc = f": Database not selected"
            ErrorController().addExecutionError(4, 'Execution', desc,
                                                line, column)
            return None

        tables = data_mode.mode(database.mode).showTables(database.name)

        if tables == None:
            desc = f": Database {database.name} does not exist"
            ErrorController().addExecutionError(35, 'Execution', desc, line, column)
            return None

        return tables
