import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

where_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Where')
sys.path.append(where_path)

from Where import Where
from typeChecker.typeChecker import *
import json
from Nodo import Nodo
from jsonMode import truncate, showTables, delete,extractTable

class Delete(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)

    def execute(self,enviroment = None):
        useDB = None
        with open('src/Config/Config.json') as file:
            config = json.load(file)
            useDB = config['databaseIndex']

        if useDB == None:
            return {
                "Code" : "42P12",
                "Message" : "No se ha seleccionado ninguna base de datos."
            }
        else:
            useDB = useDB.upper()

        listTables = showTables(useDB)
        for i in self.hijos:
            print(i.valor)
        if not(self.hijos[2].valor.upper() in listTables) :
            return {
                "Code" : "42P12",
                "Message" : "No existe la tabla <<"+ self.hijos[2].valor.upper()+">> en  la DB.."
                }
            
        if len(self.hijos) < 4:
            #Delete without where
            resp = truncate(useDB,self.hijos[2].valor.upper())
            if resp == 0:
                return {
                    "Code" : "00000",
                    "Message" : "Data truncated"
                }
            else: 
                return {
                    "Code" : "42P12",
                    "Message" : "Error"
                }   
        else:
            #Usa hidden pk ["indice"]
            #DELETE WITH WHERE
            raw_matrix = extractTable(useDB,self.hijos[2].valor.upper())
            parent_node = self.hijos[3]
            lista_tabla = [[self.hijos[2].valor.upper(),self.hijos[2].valor.upper()]]
            lista_columns = []
            tc = TypeChecker()

            dictionar = tc.return_columnsJSON(useDB,self.hijos[2].valor.upper())
            for elemento in dictionar:
                lista_columns.append([elemento['name'],elemento['type']])
            lista_columns = [lista_columns]

            print("PARENT")
            print(type(parent_node))
            
            print("MATRIZ3D")
            print(raw_matrix)

            print("LISTATABLA")
            print(lista_tabla)

            print("LISTA COLUMNAS")
            print(lista_columns)


            nuevoWhere = Where()
            listaResult = nuevoWhere.execute(parent_node,raw_matrix,lista_tabla,lista_columns)

            return {
                    "Code" : "00000",
                    "Message" : "Data truncated"
                }
