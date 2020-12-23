import json
import sys, os.path
import os

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\storageManager')
sys.path.append(storage)

error_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\ERROR')
sys.path.append(error_path)

response_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\Response')
sys.path.append(response_path)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker\\')
sys.path.append(storage)


from jsonMode import * 

from typeChecker.typeChecker import *
from Error import Error
from Response.Response import Response

tc = TypeChecker()


class Column():
    def __init__(self):
        self.name = None
        self.type = None
        self.default = None
        self.isNull = None
        self.isUnique = None
        self.uniqueName = None
        self.size = None
        self.isPrimary = None
        self.referencesTable = None
        self.isCheck = None

    def crearColumna(self, parent, checkers, enviroment, listaids):
        
        self.name = parent.hijos[0].valor
        self.type = parent.hijos[1].hijos[0].nombreNodo
        #Inicia la verificación de cada uno de los nodos.
        #Valor Default
        for hijo in parent.hijos:
            if hijo.nombreNodo == "OPCIONALES_ATRIBUTO_DEFAULT":
                if self.default == None:
                    if self.isPrimary ==None:
                        self.default = hijo.hijos[0].execute(enviroment)
                    else:
                        respError = Error(3,"La clave primaria no puede tener un valor por defecto", -1)
                        responseMessage = Response("20000", respError)
                        return responseMessage
                else: 
                    respError = Error(3,"Ya se declaró un default para la columna " + self.name, -1)
                    responseMessage = Response("42710", respError)
                    return responseMessage
            elif hijo.nombreNodo == "OPCIONALES_NOT_NULL":
                if self.isNull == None : 
                    self.isNull = False
                else:
                    respError = Error(3,"Ya se declaró un valor para null para la columna " + self.name, -1)
                    responseMessage = Response("42710", respError)
                    return responseMessage
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_NULL":
                if self.isNull == None: 
                    if self.isPrimary == None:
                        self.isNull = True
                    else:
                        respError = Error(3,"Una clave primaria no puede ser null para la columna " + self.name, -1)
                        responseMessage = Response("20000", respError)
                        return responseMessage
                else:
                    respError = Error(3,"Ya se declaro un valor null para la columna " + self.name, -1)
                    responseMessage = Response("20000", respError)
                    return responseMessage
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_UNIQUE":
                if self.isUnique == None : 
                    self.isUnique = True
                    if len(hijo.hijos) == 2:
                        self.uniqueName = hijo.hijos[0].hijos[0].valor
                else:
                    respError = Error(3,"Ya se declaro un constraint unique para la columna " + self.name, -1)
                    responseMessage = Response("20000", respError)
                    return responseMessage
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_CHECK":
                if self.isCheck == None : 
                    newCheck = Check()
                    if len(hijo.hijos) == 1:
                        newCheck.checkExp = self.construirUnique(hijo.hijos[0], listaids)
                    elif len(hijo.hijos) == 2:
                        newCheck.checkExp = self.construirUnique(hijo.hijos[1], listaids)
                        newCheck.name = hijo.hijos[0].hijos[0].valor
                    checkers.append(newCheck)
                else:
                    respError = Error(3,"Ya se declaro una constraint check para la columna " + self.name, -1)
                    responseMessage = Response("20000", respError)
                    return responseMessage
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_PRIMARY":
                if self.isPrimary == None : 
                    self.isPrimary = True
                else:
                    respError = Error(3,"Ya se la colum " + self.name+ " como primaria", -1)
                    responseMessage = Response("20000", respError)
                    return responseMessage
            elif hijo.nombreNodo == "OPCIONALES_ATRIBUTO_REFERENCES":
                if self.referencesTable == None : 
                    # Se debe verificar que exista la tabla y la columna con el mismo nombre
                    self.referencesTable = hijo.hijos[0].nombreNodo
                else:
                    respError = Error(3,"Ya se declaro una referencia para la columna " + self.name, -1)
                    responseMessage = Response("20000", respError)
                    return responseMessage
        responseMessage = Response("00000","Se creó la columna correctamente")
        return responseMessage

    def construirUnique(self, parent, listaids):
        if len(parent.hijos) == 3 :
            obj1 = self.construirUnique(parent.hijos[0], listaids)
            obj2 = self.construirUnique(parent.hijos[2], listaids)
            jsonExpresion = {
                'E0' : obj1,
                'operador' : parent.hijos[1].nombreNodo,
                'E1' : obj2
            }
            return jsonExpresion
        elif len(parent.hijos) == 2:
            jsonExpresion = {
                'nodo0' : self.construirUnique(parent.hijos[0], listaids),
                'nodo1' : self.construirUnique(parent.hijos[1], listaids)
            }
            return jsonExpresion
        elif len(parent.hijos) == 1:
            jsonExpresion = {
                'nombre' : parent.hijos[0].nombreNodo,
                'valor' : parent.hijos[0].valor
            }
            if parent.hijos[0].nombreNodo.upper() == "IDENTIFICADOR":
                listaids.append(parent.hijos[0].valor)
            return jsonExpresion

class Check():
    def __init__(self):
        self.name = None
        self.checkExp = None

class InsertTable():
    def __init__(self):
        self.name = None
        self.traeCols = 0
        self.columnas = []
        self.values = []
        self.checkers = []
        self.listaids = []
        
    def execute(self, parent, enviroment):
        # OBTENER TABLAS CAMPOS VALORES
        for hijo in parent.hijos:
            if "Tabla" == hijo.nombreNodo:
                self.name = hijo.valor
            elif "L_COLUMN" == hijo.nombreNodo:
                self.traeCols = 1
                for h in hijo.hijos:
                    self.columnas.append(h)
            elif "PARAM_INSERT" == hijo.nombreNodo:
                for h1 in hijo.hijos:
                    self.values.append(h1)
        
        # VALIDACIONES
        # Mismo # de cols y valores
        if self.traeCols == 1:
            if not(len(self.values) == len(self.columnas)):
                print("no tiene la misma cantidad de columnas y valores")   
        #
           
        # INSERTAR 
        print('Tabla',self.name)
        valoresI = []
        for h in self.columnas:
            print('Columnas', h.valor)
        for h in self.values:
            valoresI.append(h.valor)
            
        insert(database: str, self.name, valoresI)
        print('Values', valoresI)
        
         

    def buscarColumna(self,nombre):
        for column in self.columnas:
            if column.name.upper() == nombre.upper():
                return True
        return False