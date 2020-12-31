from Statics.errorTable import ErrorTable


class Environment:
    def __init__(self, parent=None, functions=None):
        self.parent = parent
        self.functions = functions
        self.ErrorTable = ErrorTable
        self.currentDB = None
        self.dbs = {}

    def setCurrentDB(self, db):
        self.currentDB = db

    def addTable(self, db, tabla):
        if not db in self.dbs:
            self.dbs[db] = {}
        self.dbs[db].update(tabla)
