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

where_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Where')
sys.path.append(where_path)

from jsonMode import * 

from typeChecker.typeChecker import *
from Error import Error
from Response.Response import Response
from Where import Where

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
    
    def obtenerColumnasDictionary(self,dbUse, tabla):
            # Se obtiene el diccionario de columnas para la tabla del Storage,
            # Solo se utiliza para selects de tablas, hay casos en los que se pueden
            # Recibir tablas como parámetros, en las subconsultas, por ejemplo.
            tc = TypeChecker()
            listTemp = tc.return_columnsJSON(dbUse, tabla.upper())
            listaCols = []
            if listTemp != None:
                for col in listTemp:
                    listaCols.append([col['name'], col['type']])
                return [listaCols]
            return [[]]
        
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
        useDB = config['databaseIndex'].upper()
        listTables = showTables(useDB)
        
        if not(self.name.upper() in listTables) :
            err_resp = Error(3,"No existe la tabla en la DB.",-1)
            resp = Response("42P12",err_resp)
            return resp        
                                      
        # INFO A INSERTAR
        tablename = self.name.upper()      
        print('DB ACTUAL', useDB)        
        print('Tabla Update',tablename)
        
        columnasI = []
        valoresI = []
        val_update = {}
        l_col = tc.return_columnsObject(useDB,tablename)
        for h in self.columnas:
            columnasI.append(h.valor.upper())
        for h in self.values:
            valoresI.append(h.valor)
        
        contador = 0
        contador2 = 0
        for h in l_col:
            for j in columnasI:
                if h.name.upper() == j:
                    val_update[contador] = valoresI[contador2]
                contador2 = contador2 + 1
            contador2 = 0
            contador = contador + 1   
        
        # VALIDACIONES
        if len(parent.hijos) <  4:
            #Update sin where
            res = update(useDB, tablename, val_update,['0'])
            print('update code: ', res )
            if res == 0:
                resp = Response("00000","Se actualizo el valor en la tabla")
            else:
                err_resp = Error(3,"No se logro actualizar el valor",-1)
                resp = Response("42P12",err_resp)
            return resp          
        else:
            #update con where
            parent_node = parent.hijos[3]
            raw_matrix = [extractTable(useDB,tablename)]
            columnas = self.obtenerColumnasDictionary(useDB,tablename)
            tablas = [[tablename,tablename]]

            nuevoWhere = Where()
            listaResult = nuevoWhere.execute(parent_node, raw_matrix, tablas, columnas,None)
            print('listaREsult ', listaResult)
            res = ""
            for elemento in listaResult:
                if elemento[0] is True:
                    res = update(useDB, tablename, val_update, [str(elemento[1])])
                    print('update code: ',res)
                    
            if res == 0:
                resp = Response("00000","Se actualizo el valor en la tabla")
            else:
                err_resp = Error(3,"No se logro actualizar el valor",-1)
                resp = Response("42P12",err_resp)
            return resp                                            
        
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
        
