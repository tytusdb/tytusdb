import re

class TypeChecker():
    'Esta clase representa el type checker para la comprobación de tipos'

    def __init__(self):
        self.type_checker = {}
        self.database = {}
        self.actual_database = ''

    def createDatabase(self, database: str, mode: int = 1):
        # 0 -> operación exitosa, 
        # 1 -> error en la operación, 
        # 2 -> base de datos existente
        if database not in self.type_checker:
            self.type_checker[database] = {}
            self.database[database] = {}
            return 0
        elif database in self.type_checker:
            return 2
        else:
            return 1

    def showDatabase(self, like: str = ''):
        lista = list(self.type_checker)
        if like == '':
            return lista
        else:
            pattern = '^' + like.replace('%','.+').replace('_','(.){0,1}') + '$'
            filtrada = []
            for base in lista:
                if re.match(pattern, base):
                    filtrada.append(base)
            return filtrada

    def alterDatabase(self, databaseOld: str, databaseNew: str):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> databaseOld no existente
        # 3 -> databaseNew existente
        if databaseOld not in self.type_checker:
            return 2
        elif databaseNew in self.type_checker:
            return 3
        elif databaseOld in self.type_checker:
            self.type_checker[databaseNew] = self.type_checker.pop(databaseOld)
            self.database[databaseNew] = self.database.pop(databaseOld)
            if self.actual_database == databaseOld:
                self.actual_database = databaseNew
            return 0
        else:
            return 1
    
    def dropDatabase(self, database: str):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> base de datos no existente
        if database not in self.type_checker:
            return 2
        elif database in self.type_checker:
            self.type_checker.pop(database)
            self.database.pop(database)
            if self.actual_database == database:
                self.actual_database = ''
            return 0
        else:
            return 1

    def useDatabase(self, database: str):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        if database in self.type_checker:
            self.actual_database = database
            return 0
        else:
            return 1

    def createTable(self, database: str, table: str, numberColumns: int):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> base de datos inexistente
        # 3 -> tabla existente
        if database not in self.type_checker:
            return 2
        elif table in self.type_checker[database]:
            return 3
        elif table not in self.type_checker[database]:
            return 0
        else:
            return 1
        