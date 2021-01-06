import json
import sys, os.path
import os

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

from typeChecker.typeChecker import *

tc = TypeChecker()



class Atribb():
    def __init__(self):
        self.column = None
        self.order = None
        self.nulls = None

    
    def execute(self, parent):
        # Se recibe ATRIB_E
        for hijo in parent.hijos:
            if hijo.nombreNodo == "IDENTIFICADOR":
                self.column = hijo.valor.upper()
            elif hijo.nombreNodo == "OPC_ORDER":
                self.order = hijo.hijos[0].nombreNodo.upper()
            elif hijo.nombreNodo == "OPC_NULLS":
                self.nulls = hijo.hijos[0].nombreNodo.upper()
        if self.order == None:
            self.order = "DESC"

class Index():
    def __init__(self):
        self.name = None
        self.table = None
        self.method = "BTREE"
        self.listaAtribb = []
        self.sentenciaWhere = None

    def setMethod(self, parent):
        self.method = parent.hijos[0].value



    def execute(self, parent):
        # Se recibe una sentencia CREATE INDEX
        self.name = parent.hijos[0].valor
        self.table = parent.hijos[1].valor
        for hijo in parent.hijos[2].hijos:
            if hijo.nombreNodo == "ATRIB_E":
                nuevaCol = Atribb()
                nuevaCol.execute(hijo)
                self.listaAtribb.append(nuevaCol)
            elif hijo.nombreNodo == "SENTENCIA_METHOD_INDEX":
                self.setMethod(hijo)
        if self.method == None:
            self.method = "BTREE"
        if len(parent.hijos) == 4:#Where
            self.sentenciaWhere = self.construirExpresionJSON(parent.hijos[3])
        
        #Se agrega a typeChecker
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        
        if config['databaseIndex'] == None:
            print("DATABASE NONE")
            err_resp = Error(3,"No se ha seleccionado ninguna base de datos.",-1)
            resp = Response("42P12",err_resp)

        indexI = Index()
        indexI.listaAtribb = self.listaAtribb
        indexI.name = self.name
        indexI.table = self.table
        indexI.method = self.method
        tc.create_index(config['databaseIndex'].upper(),indexI)
        print("Llego al final")
        






    def construirExpresionJSON(self, parent):
        if len(parent.hijos) == 3 :
            obj1 = self.construirExpresionJSON(parent.hijos[0])
            obj2 = self.construirExpresionJSON(parent.hijos[2])
            jsonExpresion = {
                'E0' : obj1,
                'operador' : parent.hijos[1].nombreNodo,
                'E1' : obj2
            }
            return jsonExpresion
        elif len(parent.hijos) == 2:
            jsonExpresion = {
                'nodo0' : self.construirExpresionJSON(parent.hijos[0]),
                'nodo1' : self.construirExpresionJSON(parent.hijos[1])
            }
            return jsonExpresion
        elif len(parent.hijos) == 1:
            jsonExpresion = {
                'nombre' : parent.hijos[0].nombreNodo,
                'valor' : parent.hijos[0].valor
            }
            return jsonExpresion
