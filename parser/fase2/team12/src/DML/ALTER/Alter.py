import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\typeChecker\\')
sys.path.append(storage_dir)
label_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+"\\C3D\\")
sys.path.append(label_dir)

from Label import *
from Temporal import *



from typeChecker.typeChecker import *
from Nodo import Nodo
from jsonMode import showDatabases
import json
class Alter(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)

    def execute(self,enviroment = None):
        print('Llamar al Alter')
        print(self.compile())
        if self.nombreNodo == 'SENTENCIA_ALTER_INDEX':
            id1 = self.hijos[0].valor
            id2 = self.hijos[1].valor
            id3 = self.hijos[2].valor
            with open('src/Config/Config.json') as file:
                config = json.load(file)
                dbUse = config['databaseIndex']            
                tc = TypeChecker()
                if tc.alter_index(dbUse,id1,id2,id3):
                    return {"Code":"0000","Message": "Succesful altered index <"+id1+">", "Data" : ""}
                
        return {"Code":"42P01","Message": "undefined_index: The index <"+id1+"> doesn´t exists"}
            
        
    def compile(self):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = \"{self.getText()}\"\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1'
        return dir

    def getText(self):
        if self.hijos[1].nombreNodo == "DATABASE":
            table_ =  self.hijos[1].valor.upper()
            return f"ALTER DATABASE {table_};"
        elif self.hijos[0].nombreNodo == "TABLE":
            table_ =  self.hijos[0].valor.upper()
            #exp =  self.hijos[3].hijos[0].getText()
            #where_body = f" WHERE {exp};"
            return f"ALTER TABLE {table_}"
        elif self.nombreNodo == 'SENTENCIA_ALTER_INDEX':
            id1 = self.hijos[0].valor
            id2 = self.hijos[1].valor
            id3 = self.hijos[2].valor
            return f'ALTER INDEX IF EXISTS {id1} {id2} {id3};'
