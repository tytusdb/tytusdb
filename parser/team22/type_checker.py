import re
from ts import Simbolo
from storageManager import jsonMode as jsonMode
from tabla_errores import *

class TypeChecker():
    'Esta clase representa el type checker para la comprobación de tipos'

    def __init__(self, tabla_simbolos, tabla_errores, consola, salida):
        self.type_checker = {}
        self.actual_database = ''
        self.tabla_simbolos = tabla_simbolos
        self.tabla_errores = tabla_errores
        self.consola = consola
        self.salida = salida

    def createDatabase(self, database: str, line: int, mode: int = 1):
        # 0 -> operación exitosa, 
        # 1 -> error en la operación, 
        # 2 -> base de datos existente
        query_result = jsonMode.createDatabase(database)
        if query_result == 0:
            self.type_checker[database] = {}
            self.tabla_simbolos.agregar(Simbolo(database, 'DATABASE', '', line))
            self.consola.append(Codigos().database_successful_completion(database))
        elif query_result == 1:
            error = Codigos().database_internal_error(database)
            self.consola.append(error)
            self.tabla_errores.agregar(Error('Semántico', error, line))
        else:
            error = Codigos().database_duplicate_database(database)
            self.consola.append(error)
            self.tabla_errores.agregar(Error('Semántico', error, line))

    def showDatabase(self, like: str = ''):
        query_result = jsonMode.showDatabases()
        if like == '':
            self.salida.append(query_result)
        else:
            pattern = '^' + like.replace('%','.+').replace('_','(.){0,1}') + '$'
            filtrada = []
            for base in query_result:
                if re.match(pattern, base):
                    filtrada.append(base)
            self.salida.append(filtrada)
        self.consola.append(Codigos().successful_completion('SHOW DATABASE'))

    def alterDatabase(self, databaseOld: str, databaseNew: str, line: int):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> databaseOld no existente
        # 3 -> databaseNew existente
        query_result = jsonMode.alterDatabase(databaseOld, databaseNew)
        if query_result == 0:
            self.consola.append(Codigos().successful_completion('ALTER DATABASE'))
            self.type_checker[databaseNew] = self.type_checker.pop(databaseOld)
            self.tabla_simbolos.simbolos[databaseNew] = self.tabla_simbolos.simbolos.pop(databaseOld)
        elif query_result == 1:
            error = Codigos().database_internal_error(databaseOld)
            self.consola.append(error)
            self.tabla_errores.agregar(Error('Semántico', error, line))
        elif query_result == 2:
            error = Codigos().database_undefined_object(databaseOld)
            self.consola.append(error)
            self.tabla_errores.agregar(Error('Semántico', error, line))
        else:
            error = Codigos().database_duplicate_database(databaseNew)
            self.consola.append(error)
            self.tabla_errores.agregar(Error('Semántico', error, line))
    
    def dropDatabase(self, database: str, line: int):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> base de datos no existente
        query_result = jsonMode.dropDatabase(database)
        if query_result == 0:
            self.consola.append(Codigos().successful_completion('DROP DATABASE'))
            self.type_checker.pop(database)
            self.tabla_simbolos.simbolos.pop(database)
            if self.actual_database == database:
                self.actual_database = ''
        elif query_result == 1:
            error = Codigos().database_internal_error(database)
            self.consola.append(error)
            self.tabla_errores.agregar(Error('Semántico', error, line))
        else:
            error = Codigos().database_undefined_object(database)
            self.consola.append(error)
            self.tabla_errores.agregar(Error('Semántico', error, line))

    def useDatabase(self, database: str, line: int):
        if database in self.type_checker:
            self.actual_database = database
            self.consola.append(Codigos().successful_completion('USE DATABASE'))
        else:
            error = Codigos().database_undefined_object(database)
            self.consola.append(error)
            self.tabla_errores.agregar(Error('Semántico', error, line))

    def createTable(self, database: str, table: str, numberColumns: int):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> base de datos inexistente
        # 3 -> tabla existente



        '''if database not in self.type_checker:
            return 2
        elif table in self.type_checker[database]:
            return 3
        elif table not in self.type_checker[database]:
            return 0
        else:
            return 1'''
        