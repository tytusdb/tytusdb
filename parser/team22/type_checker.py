import re
import os 
import json
from ts import Simbolo
from storageManager import jsonMode as jsonMode
from tabla_errores import *
from columna import *

class TypeChecker():
    'Esta clase representa el type checker para la comprobación de tipos'

    def __init__(self, tabla_simbolos, tabla_errores, consola, salida):
        self.type_checker = {}
        self.actual_database = ''
        self.tabla_simbolos = tabla_simbolos
        self.tabla_errores = tabla_errores
        self.consola = consola
        self.salida = salida
        jsonMode.dropAll()
        self.initCheck()

    def createDatabase(self, database: str, line: int, mode: int = 1):
        # 0 -> operación exitosa, 
        # 1 -> error en la operación, 
        # 2 -> base de datos existente
        query_result = jsonMode.createDatabase(database)
        if query_result == 0:
            self.type_checker[database] = {}
            self.tabla_simbolos.agregar(Simbolo(database, 'DATABASE', '', line))
            self.consola.append(Codigos().database_successful_completion(database))
            #self.saveTypeChecker()
        elif query_result == 1:
            self.addError(Codigos().database_internal_error(database), line)
        else:
            self.addError(Codigos().database_duplicate_database(database), line)

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
            #self.saveTypeChecker()
        elif query_result == 1:
            self.addError(Codigos().database_internal_error(databaseOld), line)
        elif query_result == 2:
            self.addError(Codigos().database_undefined_object(databaseOld), line)
        else:
            self.addError(Codigos().database_duplicate_database(databaseNew), line)
    
    def dropDatabase(self, database: str, line: int):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> base de datos no existente
        query_result = jsonMode.dropDatabase(database)
        if query_result == 0:
            self.consola.append(Codigos().successful_completion('DROP DATABASE «' + database + '»'))
            self.type_checker.pop(database)
            self.tabla_simbolos.simbolos.pop(database)
            if self.actual_database == database:
                self.actual_database = ''
            #self.saveTypeChecker()
        elif query_result == 1:
            self.addError(Codigos().database_internal_error(database), line)
        else:
            self.addError(Codigos().database_undefined_object(database), line)

    def useDatabase(self, database: str, line: int):
        if database in self.type_checker:
            self.actual_database = database
            self.consola.append(Codigos().successful_completion('USE DATABASE «' + database + '»'))
        else:
            self.addError(Codigos().database_undefined_object(database), line)

    def createTable(self, table: str, columns: [], line: int):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> base de datos inexistente
        # 3 -> tabla existente
        contador = 0
        for columna in columns:
            if 'nombre' in columna: contador += 1
        query_result = jsonMode.createTable(self.actual_database, table, contador)
        if query_result == 0:
            self.consola.append(Codigos().table_successful(table))
            self.tabla_simbolos.agregar(Simbolo(self.actual_database + '.' +table, 'TABLE', '', line))
            self.type_checker[self.actual_database][table] = {}
            for columna in columns:
                print(columna)
                if 'nombre' in columna:
                    self.type_checker[self.actual_database][table][columna['nombre']] = columna['col']
                elif 'primary' in columna:
                    for primaria in columna['primary']:
                        self.type_checker[self.actual_database][table][primaria['valor']].addPrimaryKey(1)
                elif 'foreign' in columna:
                    temp = 0
                    for foranea in columna['foreign']:
                        self.type_checker[self.actual_database][table][foranea['valor']].addReference(columna['table'] + '.' + columna['references'][temp]['valor'])
                        temp += 1
                        self.type_checker[self.actual_database][table][foranea['valor']].printCol()

            #self.saveTypeChecker()
        elif query_result == 1:
            self.addError(Codigos().database_internal_error(table), line)
        elif query_result == 2:
            self.addError(Codigos().database_undefined_object(self.actual_database), line)
        else:
            self.addError(Codigos().table_duplicate_table(table), line)


    def dropTable(self, table:str, line: int):
        # 0 -> operación exitosa
        # 1 -> error en la operación
        # 2 -> base de datos inexistente
        # 3 -> tabla inexistente
        query_result = jsonMode.dropTable(self.actual_database, table)
        if query_result == 0:
            self.consola.append(Codigos().successful_completion('DROP TABLE «' + table + '»'))
            self.type_checker[self.actual_database].pop(table)
        elif query_result == 1:
            self.addError(Codigos().database_internal_error(table), line)
        elif query_result == 2:
            self.addError(Codigos().database_undefined_object(self.actual_database), line)
        else:
            self.addError(Codigos().table_undefined_table(table), line)

    def initCheck(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        if not os.path.exists('data/json'):
            os.makedirs('data/json')
        if not os.path.exists('data/json/type_check'):
            data = {}
            with open('data/json/type_check', 'w') as file:
                json.dump(data, file)    
        else:
            with open('data/json/type_check') as file:
                data = json.load(file)
                '''for database in data:
                    for tabla in data[database]:
                        for columna in data[database][tabla]:
                            data[database][tabla][columna] = Columna(
                                tipo = data[database][tabla][columna]['tipo'], 
                                default = data[database][tabla][columna]['default'],
                                is_null = TipoNull[data[database][tabla][columna]['is_null']],
                                is_primary = data[database][tabla][columna]['is_primary'],
                                references = data[database][tabla][columna]['references'],
                                is_unique = data[database][tabla][columna]['is_unique'],
                                constraints = data[database][tabla][columna]['constraints']
                                )'''
                # self.type_checker = data

    def saveTypeChecker(self):
        with open('data/json/type_check', 'w') as file:
            data = self.type_checker
            for database in data:
                for tabla in data[database]:
                    for columna in data[database][tabla]:
                        data[database][tabla][columna] = data[database][tabla][columna].json()
            json.dump(data, file)
                
    def addError(self, error, line):
        self.consola.append(error)
        self.tabla_errores.agregar(Error('Semántico', error, line))