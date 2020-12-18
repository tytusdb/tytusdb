import sys, os.path
import json


table_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\DDL\\Create\\')
sys.path.append(table_dir)
from Table import * 

file_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))+ '\\estructura.json')


class TypeChecker():
    def existeDB(self,database: str):
        with open(file_dir) as file:
            #Load data as a dictionary
            data = json.load(file)
            if database not in data:
                return False
            return True

    def UseDB(self,database : str):
        return self.existeDB(database)

            
    #.#############################################Adds a new database
    def createDatabase(self,database : str,owner : str, mode) -> bool:
        dataFinal = None
        with open(file_dir) as file:
            #Load data as a dictionary
            data = json.load(file)
            if database not in data:
                creacion = {
                    database:{
                        "tables" : {},
                        "owner" : owner,
                        "mode" : mode
                    }   
                }
                data.update(creacion)
                dataFinal = json.dumps(data)
        if dataFinal is not None:
            file = open(file_dir,'w')
            file.write(dataFinal)
            return True
        else:
            return False

    #.##################################################Delete database
    def deleteDatabase(self,database : str):
        dataFinal = None
        if self.existeDB(database):
           with open(file_dir) as file:
                data = json.load(file)
                data.pop(database)
                dataFinal = data
        if dataFinal is not None:
            file = open(file_dir,'w')
            file.write(json.dumps(dataFinal))
            return True
        else:
            return False

    #.##################################################Replace database
    def replaceDatabase(self,database : str, owner : str = None, mode : str = None):
        return self.deleteDatabase(database) and self.createDatabase(database,owner,mode)


    #.####################################Creates a table in the database
    def createTable(self,database: str, table: str,columns):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                tablas = data[database]["tables"]
                if table not in tablas:
                    tablas[table] = {"columnas" : []}
                    dataFinal = json.dumps(data)
                else:
                    return None
            else:
                return None
        if dataFinal is not None:
            print("alv")
            file = open(file_dir,'w')
            file.write(dataFinal)
            file.close()
            for columna in columns:
                self.CreateColumn(database,table,columna)


    #.###############################################Shows the tables name list
    def tablename_list(self,database : str):
        if self.existeDB(database):
            with open(file_dir) as file:
                data = json.load(file)
                return list(data[database]["tables"].keys())
        return []
        
    #.##################################Returns the tables from a database    
    def return_tablesJSON(self,database : str):
        if self.existeDB(database):
            with open(file_dir) as file:
                data = json.load(file)
                return data[database]["tables"]
        return {}
        
    def return_tablesObject(self,database : str):
        table_list = []
        tablas = self.return_tablesJSON(database)
        table_names = self.tablename_list(database)
        for tabla in table_names:
            tmp_table = Table()
            tmp_table.name = tabla
            tmp_table.columnas = self.return_columnsObject(database,tabla)
            table_list.append(tmp_table)
        return table_list


    #.##################################Returns the columns from a table
    def return_columnsJSON(self,database : str, table : str):
        tablas = self.return_tablesJSON(database)
        if table in tablas:
            return tablas[table]["columnas"]
        return {}

    def return_columnsObject(self,database : str, table : str):
        retorno = []
        lista_columnas = self.return_columnsJSON(database,table)
        for columna in lista_columnas:
            tmp_column = Column()
            tmp_column.name = columna["name"]
            tmp_column.type = columna["type"]
            tmp_column.default = columna["default"]
            tmp_column.isNull = columna["isNull"]
            tmp_column.isUnique = columna["isUnique"]
            tmp_column.uniqueName = columna["uniqueName"]
            tmp_column.checkExp = columna["checkExp"]
            tmp_column.checkName = columna["checkName"]
            tmp_column.size = columna["size"]
            tmp_column.isPrimary = columna["isPrimary"]
            tmp_column.referencesTable = columna["referencesTable"]
            retorno.append(tmp_column)
        return retorno

    #.##################################Shows the column list
    def column_list(self,database : str, table : str):
        retorno = []
        columns = self.return_columnsJSON(database,table)
        for column in columns:
            retorno.append(column["name"])
        return retorno

    #.########################################
    def column_exists(self,database : str, table : str, column_name : str):
        with open(file_dir) as file:
            data = json.load(file)
            #Busca la base de datos
            if database in data:
                baseActual = data[database]["tables"]
                #busca la tabla
                if table in baseActual:
                    #Crea la tabla
                    lista_columnas = baseActual[table]["columnas"]
                    for columna in lista_columnas:
                        if columna["name"] == column_name:
                            return True
                    return False
        return None


    #.##################################Creates a column in a table
    def CreateColumn(self,database: str, table: str,column : Column):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            #Busca la base de datos
            if database in data:
                baseActual = data[database]["tables"]
                #busca la tabla
                if table in baseActual:
                    existe = self.column_exists(database,table, column.name)
                    if existe is False and existe is not None:
                        lista_columnas = baseActual[table]["columnas"]
                        indice = 0
                        if len(lista_columnas) > 0:
                            ultima = lista_columnas[-1]
                            indice = ultima["index"]
                        lista_columnas.append({
                            "name" : column.name,
                            "index" : indice + 1,
                            "type"  : column.type,
                            "default" : column.default,
                            "isNull" : column.isNull,
                            "isUnique" : column.isUnique,
                            "uniqueName" : column.uniqueName,
                            "checkExp" : column.checkExp,
                            "checkName" : column.checkName,
                            "size" : column.size,
                            "isPrimary" : column.isPrimary,
                            "referencesTable" : column.referencesTable
                        })
                        baseActual[table]["columnas"] = lista_columnas
                        dataFinal = json.dumps(data)
                    else:
                        return None
                else:
                    return None
            else:
                return None
        if dataFinal is not None:
            file = open(file_dir,'w')
            file.write(dataFinal)
            return table
    
    ###################################################### Drop table
    def drop_table(self, database : str, table_name : str):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                tablas = data[database]["tables"]
                if table_name in tablas:
                    tablas.pop(table_name)
                    dataFinal = json.dumps(data)
                else:
                    return None
            else:
                return None
        if dataFinal is not None:
            print("alv")
            file = open(file_dir,'w')
            file.write(dataFinal)
            file.close()
