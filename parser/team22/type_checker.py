import re
import os 
import json
from ts import Simbolo
from storageManager import jsonMode as jsonMode
from tabla_errores import *
from columna import *
import math 
import numpy as np
from random import random

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
            sal = [['DATABASES']]
            for base in query_result:
                sal.append([base])
            self.salida.append(sal)
        else:
            pattern = '^' + like.replace('%','.+').replace('_','(.){0,1}') + '$'
            filtrada = [['DATABASES']]
            for base in query_result:
                if re.match(pattern, base):
                    filtrada.append([base])
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
            symbol = self.tabla_simbolos.simbolos.pop(databaseOld)
            symbol.id = databaseNew
            self.tabla_simbolos.simbolos[databaseNew] = symbol
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

    def showTables(self, line: int):
        query_result = jsonMode.showTables(self.actual_database)
        print("====> ", query_result)

    


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
            self.tabla_simbolos.agregar(Simbolo(self.actual_database + '.' + table, 'TABLE', '', line))
            self.type_checker[self.actual_database][table] = {}
            for columna in columns:
                if 'nombre' in columna:
                    self.type_checker[self.actual_database][table][columna['nombre']] = columna['col']
                    self.tabla_simbolos.agregar(Simbolo(self.actual_database + '.' + table + '.' + columna['nombre'], 'COLUMN', columna['col'].tipo['tipo'].name, columna['col'].line))
                elif 'primary' in columna:
                    for primaria in columna['primary']:
                        const = self.type_checker[self.actual_database][table][primaria].addPrimaryKey(1)
                        self.tabla_simbolos.agregar(Simbolo(const.name, 'CONSTRAINT', '', const.line))
                elif 'foreign' in columna:
                    temp = 0
                    for foranea in columna['foreign']:
                        const = self.type_checker[self.actual_database][table][foranea].addReference(columna['table'] + '.' + columna['references'][temp])
                        temp += 1
                        self.tabla_simbolos.agregar(Simbolo(const.name, 'CONSTRAINT', '', const.line))
                elif 'unique' in columna:
                    for unique in columna['unique']:
                        const = self.type_checker[self.actual_database][table][unique].addUnique(1)
                        self.tabla_simbolos.agregar(Simbolo(const.name, 'CONSTRAINT', '', const.line))

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
            self.tabla_simbolos.simbolos.pop(self.actual_database + '.' + table)
            delete = []
            for symbol in self.tabla_simbolos.simbolos:
                array = symbol.split('.')
                if len(array) > 1 and array[1] == table:
                    delete.append(symbol)
            for element in delete:
                self.tabla_simbolos.simbolos.pop(element)
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
        self.tabla_errores.agregar(Error('Semántico', error, line))
    

    def Validando_Operaciones_Aritmeticas(self, valor1, valor2, operando):
        v1 = float(valor1)
        v2 = float(valor2)
        
        if operando == '+':
            self.consola.append(Codigos().successful_completion(' SUMA (' + str(v1) + ', ' + str(v2) + ')'))
            val = v1 + v2
            return val

        elif operando == '-':
            self.consola.append(Codigos().successful_completion(' RESTA (' + str(v1) + ', ' + str(v2) + ')'))
            val = v1 - v2
            return val

        elif operando == '*':
            self.consola.append(Codigos().successful_completion(' MULTIPLICACION (' +str(v1) + ', ' + str(v2) + ')'))
            val = v1 * v2
            return val

        elif operando == '/':
            self.consola.append(Codigos().successful_completion(' DIVISION (' + str(v1) + ', ' + str(v2)+ ')'))
            val = v1 / v2
            return val

        elif operando == '%':
            self.consola.append(Codigos().successful_completion(' MODULO (' + str(v1) + ', ' + str(v2) + ')'))
            val = v1 % v2
            return val

        elif operando == '^':
            self.consola.append(Codigos().successful_completion(' POTENCIA (' + str(v1) + ', ' + str(v2) + ')'))
            val = v1 ** v2
            return val

        elif operando == 'NEGATIVO':
            self.consola.append(Codigos().successful_completion(' NEGATIVO (' + str(v1) + ', ' + str(v2) + ')'))
            val = -1 * v1
            return val

    def Funciones_Trigonometricas_1(self, funcion, valor, line: int):
        val = float(valor)

        if funcion == 'ACOS':
            if val >=-1 and val <=1:
                self.consola.append(Codigos().successful_completion('SELECT ACOS(' + str(val) + ')'))
                return math.acos (val)
            else:
                return self.addError(Codigos().trigonometric_function_out_of_range('ACOS', str(val), '-1, 1'), line)

        elif funcion == 'ASIN':
            if val >=-1 and val <=1:
                self.consola.append(Codigos().successful_completion('SELECT ASIN(' + str(val) + ')'))
                return math.asin (val)
            else:
                return self.addError(Codigos().trigonometric_function_out_of_range('ACOS', str(val), '-1, 1'), line)

        elif funcion == 'ATAN':
            self.consola.append(Codigos().successful_completion('SELECT ASIN(' + str(val) + ')'))
            return math.asin (val)

        elif funcion == 'COS':
            self.consola.append(Codigos().successful_completion('SELECT COS(' + str(val) + ')'))
            return math.cos (val)

        elif funcion == 'COT':
            self.consola.append(Codigos().successful_completion('SELECT COT(' + str(val) + ')'))
            result = math.tan (val) ** -1 
            return result       

        elif funcion == 'SIN':
            self.consola.append(Codigos().successful_completion('SELECT SIN(' + str(val) + ')'))
            return math.sin (val)
            
        elif funcion == 'TAN':
            self.consola.append(Codigos().successful_completion('SELECT TAN(' + str(val) + ')'))
            return math.tan (val)

        elif funcion == 'ASIND':
            if val >=-1 and val <=1:
                self.consola.append(Codigos().successful_completion('SELECT ASIND(' + str(val) + ')'))
                return math.asin(math.radians(val)) 
            else:
                return self.addError(Codigos().trigonometric_function_out_of_range('ASIND', str(val), '-1, 1'), line)


        elif funcion == 'ACOSD':
            if val >=-1 and val <=1:
                self.consola.append(Codigos().successful_completion('SELECT ACOSD(' + str(val) + ')'))
                return math.acos(math.radians(val))        #   <= no esta la funcion
            else:
                return self.addError(Codigos().trigonometric_function_out_of_range('ACOSD', str(val), '-1, 1'), line)

        elif funcion == 'ATAND':
            self.consola.append(Codigos().successful_completion('SELECT ATAND(' + str(val) + ')'))
            return math.atan(math.radians(val))        #   <= no esta la funcion

        elif funcion == 'COSD':
            self.consola.append(Codigos().successful_completion('SELECT COSD(' + str(val) + ')'))
            return math.cos(math.radians(val))        #   <= no esta la funcion

        elif funcion == 'COTD':
            self.consola.append(Codigos().successful_completion('SELECT COTD(' + str(val) + ')'))
            return math.tan (math.radians(val)) ** -1         #   <= no esta la funcion

        elif funcion == 'SIND':
            self.consola.append(Codigos().successful_completion('SELECT SIND(' + str(val) + ')'))
            return math.sin (math.radians(val))        #   <= no esta la funcion

        elif funcion == 'TAND':
            self.consola.append(Codigos().successful_completion('SELECT TAND(' + str(val) + ')'))
            return math.tan(math.radians(val))        #   <= no esta la funcion
        
        elif funcion == 'SINH':
            self.consola.append(Codigos().successful_completion('SELECT SINH(' + str(val) + ')'))
            return math.sinh (val)

        elif funcion == 'COSH':
            self.consola.append(Codigos().successful_completion('SELECT COSH(' + str(val) + ')'))
            return math.cosh (val)

        elif funcion == 'TANH':
            self.consola.append(Codigos().successful_completion('SELECT TANH(' + str(val) + ')'))
            return math.tanh (val)

        elif funcion == 'ASINH':
            self.consola.append(Codigos().successful_completion('SELECT ASINH(' + str(val) + ')'))
            return math.asinh (val)

        elif funcion == 'ACOSH':
            if val >= 1:
                self.consola.append(Codigos().successful_completion('SELECT ACOSH(' + str(val) + ')'))
                return math.acosh (val)
            else:
                return self.addError(Codigos().trigonometric_function_out_of_range('ACOSH', str(val), '1, infinit'), line)

        elif funcion == 'ATANH':
            if val >-1 and val <1:
                self.consola.append(Codigos().successful_completion('SELECT ATANH(' + str(val) + ')'))
                return math.atanh (val)
            else:
                return self.addError(Codigos().trigonometric_function_out_of_range('ATANH', str(val), '-1, 1'), line)
        
    def Funciones_Trigonometricas_2(self, funcion, valor1, valor2, line: int):
        val1 = float(valor1)
        val2 = float(valor2)
        if funcion == 'ATAN2D':          #   <= 2 parametros
            return math.atan2 (math.radians(val1), math.radians(val2))
        elif funcion == 'ATAN2':          #   <= 2 parametros
            return math.atan2 (val1, val2)


    def Funciones_Matematicas_1(self, funcion, valor, line: int):
        val = float(valor)

        if funcion == 'COUNT':          #   <= FALTA
            return 1
        elif funcion == 'SUM':          #   <= FALTA
            return 1
        elif funcion == 'AVG':          #   <= FALTA
            return 1
        
        elif funcion == 'ABS':
            self.consola.append(Codigos().successful_completion('ABS (' + str(val) + ')'))
            return abs(val)
        elif funcion == 'CBRT': 
            self.consola.append(Codigos().successful_completion('CBRT (' + str(val) + ')'))
            return val ** (1/3)
        elif funcion == 'CEIL': 
            self.consola.append(Codigos().successful_completion('CEIL (' + str(val) + ')'))    
            return round(val)
        elif funcion == 'CEILING':
            self.consola.append(Codigos().successful_completion('CEILING (' + str(val) + ')'))          
            return math.ceil(val)
        elif funcion == 'DEGREES':  
            self.consola.append(Codigos().successful_completion('DEGREES (' + str(val) + ')'))        
            return math.degrees(val)
        elif funcion == 'EXP': 
            self.consola.append(Codigos().successful_completion('EXP (' + str(val) + ')'))
            return math.e ** val
        elif funcion == 'FACTORIAL': 
            self.consola.append(Codigos().successful_completion('FACTORIAL (' + str(val) + ')'))         
            return math.factorial(val)
        elif funcion == 'FLOOR':  
            self.consola.append(Codigos().successful_completion('FLOOR (' + str(val) + ')'))        
            return math.floor(val)
        elif funcion == 'LN':   
            self.consola.append(Codigos().successful_completion('LN (' + str(val) + ')'))       
            return math.log(val)
        elif funcion == 'LOG': 
            self.consola.append(Codigos().successful_completion('LOG (' + str(val) + ')'))       
            return math.log(val)
        elif funcion == 'PI':  
            self.consola.append(Codigos().successful_completion('PI ()'))        
            return math.pi
        elif funcion == 'RADIANS':     
            self.consola.append(Codigos().successful_completion('RADIANS (' + str(val) + ')'))     
            return math.radians(val)
        elif funcion == 'ROUND':      
            self.consola.append(Codigos().successful_completion('ROUND (' + str(val) + ')'))    
            return round(val)
        elif funcion == 'SIGN':  
            self.consola.append(Codigos().successful_completion('SIGN (' + str(val) + ')'))        
            return np.sign(val)
        elif funcion == 'SQRT': 
            if val >= 0:         
                self.consola.append(Codigos().successful_completion('SQRT (' + str(val) + ')'))
                return val ** (1/2)
            else:
                return self.addError(Codigos().trigonometric_function_out_of_range('SQRT', str(val), '0, infinit'), line)

        elif funcion == 'TRUNC':  
            self.consola.append(Codigos().successful_completion('TRUNC (' + str(val) + ')'))        
            return math.trunc(val)
        elif funcion == 'RANDOM':     
            self.consola.append(Codigos().successful_completion('RANDOM ()'))     
            return random()


    def Funciones_Matematicas_2(self, funcion, valor1, valor2, line: int):
        val1 = float(valor1)
        val2 = float(valor2)

        if funcion == 'MOD':
            self.consola.append(Codigos().successful_completion('MOD ('+ str(val1) +',' + str(val2)+ ')'))     
            return val1 % val2
        elif funcion == 'POWER':
            self.consola.append(Codigos().successful_completion('POWER ('+ str(val1) +',' + str(val2)+ ')')) 
            return math.pow(val1, val2)
        elif funcion == 'DIV':
            self.consola.append(Codigos().successful_completion('DIV ('+ str(val1) +',' + str(val2)+ ')')) 
            return val1 // val2
        elif funcion == 'GCD':
            self.consola.append(Codigos().successful_completion('GCD ('+ str(val1) +',' + str(val2)+ ')')) 
            return math.gcd(val1, val2)