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
        self.specificType = None
        self.default = None
        self.isNull = None
        self.isUnique = None
        self.uniqueName = None
        self.size = None
        self.isPrimary = None
        self.referencesTable = None
        self.isCheck = None
        self.referenceColumn = None

class UpdateTable():
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
            if "TABLE" == hijo.nombreNodo:
                self.name = hijo.valor
            elif "LISTA_UPDATE" == hijo.nombreNodo:
                self.traeCols = 1
                for h in hijo.hijos:
                    for i in h.hijos:
                        if "COL" == i.nombreNodo:
                            self.columnas.append(i)
                        else:
                            self.values.append(i)
        # INFO DB ACTUAL
        with open('src/Config/Config.json') as file:
            config = json.load(file)

        if config['databaseIndex'] == None:
            err_resp = Error(3,"No se ha seleccionado ninguna base de datos.",-1)
            resp = Response("42P12",err_resp)
            return resp
        listTables = showTables(config['databaseIndex'].upper())
        useDB = config['databaseIndex'].upper()
        
        if not(self.name.upper() in listTables) :
            err_resp = Error(3,"No existe la tabla en la DB.",-1)
            resp = Response("42P12",err_resp)
            return resp        
        print('2')
        # INFO A INSERTAR
        columnasI = []
        valoresI = []
        l_col = tc.return_columnsObject(useDB,self.name.upper())
        for h in self.columnas:
            columnasI.append(h.valor)
        for h in self.values:
            valoresI.append(h.valor)
        print('DB ACTUAL', useDB)
        print('Tabla Update',self.name)
        print('Values Update', valoresI)
        print('Columns Update', columnasI)  
        print('L_col', len(l_col))
        
        valores_insertar = []
        contador = 0
        keywords = {
            'seno' : 23,
            'coseno' : 23
        }
        # VALIDACIONES

        # INSERTAR 
        '''print('update code: ',update(useDB, self.name.upper(), keywords, columnasI) )
        resp = Response("00000","Se actualizo el valor en la tabla")
        return resp'''
        
        
    def validar_tipo(self, tipo: str, variable: str):
        print('Variable ', variable, ' tipo ', tipo)
        variable = str(variable)
        try:
            if tipo == 1:
                variable = variable.replace(" ","")
                variable = variable.replace(",","")
                int(variable)
            elif tipo == 2:
                print('caracter')
            elif tipo == 4:
                if not(variable.upper() == 'TRUE' or variable.upper() == 'FALSE'):
                    return 0
            else:
                print('No tiene validacion')
            return 1 
        except:
            print('La variable ', variable, ' no coincide con el tipo ',tipo)
            return 0
        
