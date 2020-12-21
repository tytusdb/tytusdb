import sys, os.path
import json


class Table():
    def __init__(self):
        self.name = None
        self.isNull = None
        self.columnas = []
        self.checkers = []
        self.listaids = []

class Constraints():
    def __init__(self):
        self.nombre = None
        self.listaColumnas = []

class Column():
    def __init__(self):
        self.name = None
        self.type = None
        self.default = None
        self.isNull = None
        self.isUnique = None
        self.uniqueName = None
        self.size = None
        self.isPrimary = None
        self.referencesTable = None
        self.isCheck = None

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
                        indice = -1
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
            file = open(file_dir,'w')
            file.write(dataFinal)
            file.close()

    #######################################################Alter database (rename)
    def rename_database(self,old_db_name : str, new_db_name : str):
        if self.existeDB(new_db_name) or not self.existeDB(old_db_name):
            return False
        with open(file_dir) as file:
            data = json.load(file)
            data[new_db_name] = data[old_db_name]
            data.pop(old_db_name)
            file = open(file_dir,'w')
            file.write(json.dumps(data))
            return True   

    ########################################################Alter table (rename)         
    def rename_table(self):
        pass

    ########################################################Get column index
    def get_column_index(self,database : str, table : str, column : str):
        lista = self.return_columnsJSON(database,table)
        for columna in lista:
            if column == columna["name"]:
                return columna["index"]
        return None
    ########################################################################
    def update_indexes(self, database : str, table : str):
        lista = self.return_columnsJSON(database,table)
        i = 0
        for columna in lista:
            columna["index"] = i
            i = i + 1
        return lista       

    ##########################################################Delete a column
    def delete_column(self,database : str, table : str,column : str):
        if self.column_exists(database,table,column):
            lista = []
            dicc = self.return_columnsJSON(database,table)
            for columna in dicc:
                if columna["name"] != column:
                    lista.append(columna)
            #Deletes the column
            with open(file_dir) as file:
                data = json.load(file)
                data[database]["tables"][table]["columnas"] = lista
                file = open(file_dir,'w')
                file.write(json.dumps(data))
            with open(file_dir) as file:
                data = json.load(file)
                data[database]["tables"][table]["columnas"] = self.update_indexes(database,table)
                file = open(file_dir,'w')
                file.write(json.dumps(data))
            return True                
            #Updates indexes     
                    
        else:
            return False
