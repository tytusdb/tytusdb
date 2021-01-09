import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

where_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Where')
sys.path.append(where_path)

label_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+"\\C3D\\")
sys.path.append(label_dir)

from Label import *
from Temporal import *

from Where import Where
from typeChecker.typeChecker import *
import json
from Nodo import Nodo
from jsonMode import truncate, showTables, delete,extractTable

class Delete(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)


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


    def compile(self):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = \"{self.getText()}\"\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1\n'
        return dir

    def getText(self):
        table_ =  self.hijos[2].valor.upper()
        if len(self.hijos) < 4:
            
            return f"DELETE FROM {table_};"
        else:
            exp =  self.hijos[3].hijos[0].getText()
            where_body = f" WHERE {exp};"
            return f"DELETE FROM {table_} {where_body}"


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
            tablename = self.hijos[2].valor.upper()
            #Usa hidden pk ["indice"]
            #DELETE WITH WHERE
            parent_node = self.hijos[3]
            raw_matrix = [extractTable(useDB,self.hijos[2].valor.upper())]
            columnas = self.obtenerColumnasDictionary(useDB,tablename)
            tablas = [[self.hijos[2].valor.upper(),self.hijos[2].valor.upper()]]


            nuevoWhere = Where()
            listaResult = nuevoWhere.execute(parent_node, raw_matrix, tablas, columnas,None)
            print(listaResult)
            for elemento in listaResult:
                if elemento[0] is True:
                    print(delete(useDB,tablename,[str(elemento[1])]),"UFF")
        

            return {
                    "Code" : "00000",
                    "Message" : "Data truncated"
                }
