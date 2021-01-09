import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\AST\\')
sys.path.append(nodo_dir)

storage_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\storageManager\\')
sys.path.append(storage_dir)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

label_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))+"\\C3D\\")
sys.path.append(label_dir)



from Label import *
from Temporal import *
from Nodo import Nodo
from typeChecker.typeChecker import *
from jsonMode import dropDatabase,dropTable
tc = TypeChecker()

class Drop(Nodo):
    def __init__(self, nombreNodo,fila = -1 ,columna = -1 ,valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)


    def compile(self):
        tmp = instanceTemporal.getTemporal()
        dir = f"{tmp} = \"{self.getText()}\"\n"
        dir += f'display[p] = {tmp}\n'
        dir += 'p = p + 1\n'
        return dir

    def getText(self):
        if(self.hijos[1].hijos[0].nombreNodo == "DATABASE"):
        ######### DATABASES
            use_if_exists = len(self.hijos[1].hijos) == 3
            dbname = ""
            if use_if_exists:
                dbname =  " IF EXISTS " + self.hijos[1].hijos[2].valor
            else:
                dbname = self.hijos[1].hijos[1].valor 

            return f'DROP DATABASE {dbname} ;'            
        elif(self.hijos[1].hijos[0].nombreNodo == "TABLE"):
        ######### TABLES
            identificador = self.hijos[1].hijos[1].valor
            return f'DROP TABLE {identificador};'
        elif(self.hijos[1].hijos[0].nombreNodo == "INDEX"):
            pass
            identificador = self.hijos[1].hijos[1].valor
            return f'DROP INDEX {identificador};'  
        elif(self.hijos[1].hijos[0].nombreNodo == "PROCEDURE"):
            pass
            identificador = self.hijos[1].hijos[1].valor
            return f'DROP PROCEDURE {identificador}();'                   


    def execute(self,enviroment = None):
        #Se debe llamar al metodo showDatabases() -> list:
        if(self.hijos[1].hijos[0].nombreNodo == "DATABASE"):
        ######### DATABASES
            use_if_exists = len(self.hijos[1].hijos) == 3
            dbname = ""
            if use_if_exists:
                dbname = self.hijos[1].hijos[2].valor 
            else:
                dbname = self.hijos[1].hijos[1].valor 
            resultado = dropDatabase(dbname)
            if resultado == 0:
                tc.deleteDatabase(dbname)
                return {"Code":"0000","Message": "The database  <"+dbname+"> has been successfully dropped"}
            elif resultado == 1:
                return {"Code":"42602","Message": "invalid_name: The identifier <"+dbname+"> is incorrect"}
            elif resultado == 2:
                return {"Code":"42P12","Message": "invalid_database_definition: The database <"+dbname+"> doesn´t exists"}
        elif(self.hijos[1].hijos[0].nombreNodo == "TABLE"):
        ######### TABLES
            table_name = self.hijos[1].hijos[1].valor
            with open('src/Config/Config.json') as file:
                config = json.load(file)
                dbUse = config['databaseIndex']
                if dbUse == None:
                    return {"Code":"42P12","Message": "invalid_database_definition: There is no selected database "}              
                else:
                    dbUse = config['databaseIndex'].upper()
                    res = dropTable(dbUse,table_name)
                    if res == 0:
                        tc.drop_table(dbUse,table_name)
                        return {"Code":"0000","Message": "The table  <"+table_name+"> has been successfully dropped"}
                    elif res == 1:
                        return {"Code":"42602","Message": "invalid_name: The identifier <"+dbUse+"> is incorrect"}
                    elif res == 2:
                        return {"Code":"42P12","Message": "invalid_database_definition: The database <"+dbUse+"> doesn´t exists"}
                    elif res == 3:
                        return {"Code":"42P01","Message": "undefined_table: The table <"+table_name+"> doesn´t exists"}

        elif(self.hijos[1].hijos[0].nombreNodo == "INDEX"):
            identificador = self.hijos[1].hijos[1].valor                  
            with open('src/Config/Config.json') as file:
                config = json.load(file)
                dbUse = config['databaseIndex']
                if dbUse == None:
                    return {"Code":"42P12","Message": "invalid_database_definition: There is no selected database "}              
                else:
                    dbUse = config['databaseIndex'].upper()
                    resp = tc.drop_index(dbUse, identificador)
                    if resp == None:
                        return {"Code":"42P01","Message": "undefined_index: The index <"+identificador+"> doesn´t exists"}
                    else:
                        return {"Code":"0000","Message": "The index  <"+identificador+"> has been successfully dropped"}
        elif(self.hijos[1].hijos[0].nombreNodo == "PROCEDURE"):  
            identificador = self.hijos[1].hijos[1].valor 
            with open('src/Config/Config.json') as file:
                config = json.load(file)
                dbUse = config['databaseIndex']
                if dbUse == None:
                    return {"Code":"42P12","Message": "invalid_database_definition: There is no selected database "}              
                else:
                    dbUse = config['databaseIndex'].upper()
                    resp = tc.drop_procedure(dbUse,identificador)                       
                    if resp:
                        return {"Code":"0000","Message": "The procedure  <"+identificador+"> has been successfully dropped"}
                    else:
                        return {"Code":"42P12","Message": "invalid_database_definition: There is no procedure to delete "}              







    def addChild(self, node):
        self.hijos.append(node)