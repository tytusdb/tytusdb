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
        # INFO DB ACTUAL
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        
        useDB = config['databaseIndex'].upper()
        
        if config['databaseIndex'] == None:
            err_resp = Error(3,"No se ha seleccionado ninguna base de datos.",-1)
            resp = Response("42P12",err_resp)
            return resp
        listTables = showTables(config['databaseIndex'].upper())
        
        if not(self.name.upper() in listTables) :
            err_resp = Error(3,"No existe la tabla en la DB.",-1)
            resp = Response("42P12",err_resp)
            return resp        
        
        # INFO A INSERTAR
        columnasI = []
        valoresI = []
        l_col = tc.return_columnsObject(useDB,self.name.upper())
        for h in self.columnas:
            columnasI.append(h.valor)
        for h in self.values:
            valoresI.append(h.valor)
        print('DB ACTUAL', useDB)
        print('Tabla',self.name)
        print('Values', valoresI)
        print('Columns', columnasI)  
        print('L_col', len(l_col))
        
        valores_insertar = []
        contador = 0
        # VALIDACIONES
        if self.traeCols == 1:
            # Mismo # de cols y valores
            if not(len(self.values) == len(self.columnas)):
                print("no tiene la misma cantidad de columnas y valores") 
                err_resp = Error(3,"No tiene la misma cantidad de columnas a insertar y valores a insertar.",-1)
                resp = Response("42P12",err_resp)
                return resp                 
            # cols a insertar <=  cols existentes
            if not(len(l_col) >=  len(self.columnas)):
                print("El numero de columnas a insertar es a mayor a las existentes") 
                err_resp = Error(3,"El numero de columnas a insertar es a mayor a las existentes.",-1)
                resp = Response("42P12",err_resp)
                return resp      
            # cols existentes >=  valores a insertar
            if not(len(l_col) >=  len(self.values)):
                print("El numero de valores a insertar es mayor a la cantidad de columnas existentes") 
                err_resp = Error(3,"El numero de valores a insertar es mayor a la cantidad de columnas existentes.",-1)
                resp = Response("42P12",err_resp)
                return resp      
            for h in l_col:
                tmp_col_actual = Column()
                if len(columnasI) > contador:
                    tmp_col_insert = columnasI[contador].upper()
                    tmp_valor = valoresI[contador]
                tmp_col_actual = h

                # Validar que sea la misma columna
                if tmp_col_actual.name == tmp_col_insert:
                    contador = contador + 1
                    # Validar tipo de datos
                    if self.validar_tipo( tmp_col_actual.type, tmp_valor) == 1:
                        valores_insertar.append(tmp_valor)
                    else:
                        print("El tipo de dato no coincide con la variable " + tmp_valor)
                        err_resp = Error(3,"El tipo de dato no coincide con la variable " + tmp_valor,-1)
                        resp = Response("42P12",err_resp)
                        return resp   
                else:
                    valores_insertar.append(None)
        # Solo vienes valores
        else:
            for h in l_col:
                tmp_col_actual = Column()
                tmp_col_actual = h
                if not(contador == len(valoresI)):
                    tmp_valor = valoresI[contador]

                # Validar tipo de datos
                if self.validar_tipo( tmp_col_actual.type, tmp_valor) == 1 and contador < len(valoresI) :
                    contador = contador + 1
                    valores_insertar.append(tmp_valor)
                else:
                    valores_insertar.append(None)
            if not(contador == len(valoresI)):
                print("El tipo de dato no coincide con la variable ")
                err_resp = Error(3,"Los valores a ingresar no coinciden con los valores de la tabla",-1)
                resp = Response("42P12",err_resp)
                return resp             
           
        # INSERTAR 
        print('Se va a insertar', valores_insertar)
        print('insert code :',insert(useDB, self.name.upper(), valores_insertar))
        resp = Response("00000","Se inserto el valor en la tabla")
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
            elif tipo == 3:
                print('validacion Fecha')
            elif tipo == 4:
                if not(variable.upper() == 'TRUE' or variable.upper() == 'FALSE'):
                    return 0
            else:
                print('No tiene validacion')
            return 1 
        except:
            print('La variable ', variable, ' no coincide con el tipo ',tipo)
            return 0