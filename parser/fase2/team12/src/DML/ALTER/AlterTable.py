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

table_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\DDL\\Create')
sys.path.append(table_path)

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
    
    def asignarTipoCol(self,entrada):
        tiposDato = {
            "SMALLINT":1,
            "INTEGER":1,
            "BIGINT":1,
            "DECIMAL":1,
            "NUMERIC":1,
            "REAL":1,
            "DOUBLE PRECISION":1,
            "MONEY":1,
            "CHARACTER VARYING": 2,
            "VARCHAR":2,
            "CHARACTER":2,
            "CHAR":2,
            "TEXT":2,
            "TIME":3,
            "DATE":3,
            "TIME WITH TIME ZONE" : 3,
            "TIME WITHOUT TIME ZONE" : 3,
            "BOOLEAN": 4
        }
        try:
            return tiposDato[entrada]
        except ValueError:
            return 3

class AlterTable():
    def __init__(self):
        self.name = None
        self.traeCols = 0
        self.columnas = []
        self.values = []
        self.checkers = []
        self.listaids = []
        self.addCol = 0
        
    def execute(self, parent, enviroment):
        # OBTENER TABLAS CAMPOS VALORES
        for hijo in parent.hijos:
            if "TABLE" == hijo.nombreNodo:
                self.name = hijo.valor
            elif "ADD" == hijo.nombreNodo:
                nuevaCol = Column()
                self.addCol = 1
                for h in hijo.hijos:
                    if "COLUMN" == h.nombreNodo:
                        nuevaCol.name = h.valor
                    else:
                        print('none ', h.nombreNodo)
                        nuevaCol.type = nuevaCol.asignarTipoCol(h.nombreNodo.upper())
                self.columnas.append(nuevaCol)
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
        
        # INFO A INSERTAR
        print('DB ACTUAL', useDB)
        print('Tabla',self.name)
        
        # VALIDACIONES
        if(self.addCol == 1):
            # INSERTAR NUEVA COL
            res = alterAddColumn(useDB, self.name.upper(), 1)
            res = 0
            print('insert col  :',res)
            if res == 0:
                for columna in self.columnas:
                    tc.CreateColumn(useDB,self.name.upper(), columna)
                resp = Response("00000","Se agrego la columna a la tabla " + self.name.upper())
            else:
                resp = Response("42P12","No se agrego la columna a la tabla " + self.name.upper() )
            self.addCol = 0
            return resp
