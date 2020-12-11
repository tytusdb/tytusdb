import re

class TypeChecker():
    'Esta clase representa el type checker para la comprobación de tipos'

    def __init__(self):
        self.type_checker = {}
        self.database = {}

    def createDatabase(self, database: str, mode: int = 1):
        if mode not in [1, 2, 3, 4, 5]:
            return 3
        elif database not in self.type_checker:
            self.type_checker[database] = {}
            self.database[database] = {}
            return 0
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
        # 1 -> existe, 0 -> no existe
        if databaseOld in self.type_checker:
            self.type_checker[databaseNew] = self.type_checker.pop(databaseOld)
            self.database[databaseNew] = self.database.pop(databaseOld)
            return 1
        else:
            return 0
    
    def dropDatabase(self, database: str):
        # 1 -> existe, 0 -> no existe
        if database in self.type_checker:
            self.type_checker.pop(database)
            self.database.pop(database)
            return 1
        else:
            return 0