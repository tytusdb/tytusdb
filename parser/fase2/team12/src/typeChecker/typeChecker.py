import sys, os.path
import json


class Table():
    def __init__(self):
        self.name = None
        self.isNull = None
        self.columnas = []
        self.checkers = []
        self.listaids = []
        self.listaReferences = []

class Constraints():
    def __init__(self):
        self.nombre = None
        self.listaColumnas = []

class Check():
    def __init__(self):
        self.name = None
        self.checkExp = None

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

class Index():
    def __init__(self):
        self.name = None
        self.table = None
        self.method = None
        self.listaAtribb = []
        self.sentenciaWhere = None

class Atribb():
    def __init__(self):
        self.column = None
        self.order = None
        self.nulls = None

class Procedure:
    def __init__(self):
        self.nombre = None
        self.C3D = None  
        self.parametros = []


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
    def createDatabase(self,database : str,owner : str, mode, indexes = [],procedures = []) -> bool:
        dataFinal = None
        with open(file_dir) as file:
            #Load data as a dictionary
            data = json.load(file)
            if database not in data:
                creacion = {
                    database:{
                        "tables" : {},
                        "owner" : owner,
                        "mode" : mode,
                        "indexes" : indexes,
                        "procedures" : procedures
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


    ######################## CreateProcedure
    def create_procedure(self, database : str, procedure : Procedure):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                procedures = data[database]["procedures"]
                listanombres = []
                for ind in procedures:
                    listanombres.append(ind["nombre"])
                if procedure.nombre not in listanombres:
                    procedures.append({
                        "nombre" : procedure.nombre,
                        "C3D" : procedure.C3D,
                        "parametros" : procedure.parametros
                        })
                    dataFinal = json.dumps(data)
                else:
                    return None
            else:
                return None
        if dataFinal is not None:
            file = open(file_dir,'w')
            file.write(dataFinal)
            file.close()

    def search_procedure(self,database : str, procedure_name : str):
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                procedures = data[database]["procedures"]
                for ind in procedures:
                    if ind["nombre"] == procedure_name:
                        return ind
                return None
            else:
                return None

    def get_all_procedure(self,database : str):
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                procedures = data[database]["procedures"]
                return procedures
            else:
                return None

    ######################## CreateIndex
    def create_index(self, database : str, index : Index):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                indices = data[database]["indexes"]
                listanombres = []
                for ind in indices:
                    listanombres.append(ind["name"])
                if index.name not in listanombres:
                    listaAttribs = []
                    for indice in index.listaAtribb:
                        listaAttribs.append({
                            "column" : str(indice.column),
                            "order" : str(indice.order),
                            "nulls" : str(indice.nulls)
                        })
                    indices.append({
                        "name" : index.name,
                        "table" : index.table,
                        "method" : index.method,
                        "listaAtribb" : listaAttribs,
                        "sentenciaWhere" : index.sentenciaWhere
                        })
                    dataFinal = json.dumps(data)
                else:
                    return None
            else:
                return None
        if dataFinal is not None:
            file = open(file_dir,'w')
            file.write(dataFinal)
            file.close()


    def alter_index(self, database : str,nombre_index,old_column, new_column):
            with open(file_dir) as file:
                data = json.load(file)
                if database in data:
                    indices = data[database]["indexes"]
                    for ind in indices:
                        tabla_actual = ''
                        if nombre_index == ind["name"]:
                            tabla_actual = str(ind["table"]).upper()
                            if tabla_actual not in self.tablename_list(database):
                                return 1 #No existe la tabla

                            l_columns = self.column_list(database,tabla_actual)
                            if old_column.upper() not in l_columns  and new_column.upper() not in l_columns:
                                return 2


                            lista = ind['listaAtribb']
                            for attr in lista:
                                if attr['column'] == old_column:
                                    attr['column'] = new_column
                                    dataFinal = json.dumps(data)
                                    file = open(file_dir,'w')
                                    file.write(dataFinal)
                                    file.close()
                                    return True
                            return None
                    return None
                else:
                    return None


    def return_indexJSON(self, database : str):
        if self.existeDB(database):
            with open(file_dir) as file:
                data = json.load(file)
                return data[database]["indexes"]
        return []        

    def return_indexesObject(self,database : str):
        lista = self.return_indexJSON(database)
        retorno = []
        for indx in lista:
            index_tmp = Index()
            index_tmp.name = indx["name"]
            index_tmp.table = indx["table"]
            index_tmp.method = indx["method"]
            l = []

            for item in indx["listaAtribb"]:
                attr_tmp = Atribb()
                attr_tmp.column = item["column"]
                attr_tmp.order = item["order"]
                attr_tmp.nulls = item["nulls"]
                l.append(attr_tmp)

            index_tmp.listaAtribb = l
            index_tmp.sentenciaWhere = indx["sentenciaWhere"]
            retorno.append(index_tmp)
        return retorno


    #.####################################Creates a table in the database
    def createTable(self,database: str, table: str,columns : list = [],
                    checkers : list = [], listaReferences : list = []):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                tablas = data[database]["tables"]
                if table not in tablas:
                    tablas[table] = {
                        "columnas" : [],
                        "checkers" : [],
                        "listaReferences" : []               
                        }
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
                #Agrega las columnas, checks y references
                self.CreateColumn(database,table,columna)
            for chck in checkers:
                pass
                self.CreateCheck(database,table,chck)
            for ref in listaReferences:
                pass
                self.CreateConstraint(database,table,ref)

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
        try:
            tablas = self.return_tablesJSON(database)
            if table in tablas:
                return tablas[table]["columnas"]
            return []
        except:
            return []

    def return_columnsObject(self,database : str, table : str):
        retorno = []
        lista_columnas = self.return_columnsJSON(database,table)
        for columna in lista_columnas:
            tmp_column = Column()
            tmp_column.name = columna["name"]
            tmp_column.type = columna["type"]
            tmp_column.specificType = columna["specificType"]
            tmp_column.default = columna["default"]
            tmp_column.isNull  = columna["isNull"]
            tmp_column.isUnique = columna["isUnique"]
            tmp_column.uniqueName = columna["uniqueName"]
            tmp_column.size = columna["size"]
            tmp_column.isPrimary = columna["isPrimary"]
            tmp_column.referencesTable = columna["referencesTable"]
            tmp_column.isCheck = columna["isCheck"]
            tmp_column.referenceColumn = columna["referenceColumn"]
            retorno.append(tmp_column)
        return retorno
    ####################################Return checkers
    def return_checksJSON(self,database : str, table : str):
        try:
            tablas = self.return_tablesJSON(database)
            if table in tablas:
                return tablas[table]["checkers"]
            return []
        except:
            return []

    def return_checksObject(self,database : str, table : str):
        retorno = []
        lista_checkers = self.return_checksJSON(database,table)
        for chck in lista_checkers:
            tmp_check = Check()
            tmp_check.name = chck["name"]
            tmp_check.checkExp = chck["checkExp"]
            retorno.append(tmp_check)
        return retorno

    ####################################Return constraints
    def return_constraintsJSON(self,database : str, table : str):
        try:
            tablas = self.return_tablesJSON(database)
            if table in tablas:
                return tablas[table]["listaReferences"]
            return []
        except:
            return []

    def return_constraintsObject(self,database : str, table : str):
        retorno = []
        lista_constr = self.return_constraintsJSON(database,table)
        for constraint in lista_constr:
            tmp_constr = Constraints()
            tmp_constr.nombre = constraint["nombre"]
            tmp_constr.listaColumnas = constraint["listaColumnas"]
            retorno.append(tmp_constr)
        return retorno

    #.##################################Shows the column list
    def column_list(self,database : str, table : str):
        retorno = []
        columns = self.return_columnsJSON(database,table)
        for column in columns:
            retorno.append(column["name"])
        return retorno

    #.######################################## Exists
    def column_exists(self,database : str, table : str, column_name : str):
        with open(file_dir) as file:
            data = json.load(file)
            #Busca la base de datos
            if database in data:
                baseActual = data[database]["tables"]
                #busca la tabla
                if table in baseActual:
                    lista_columnas = baseActual[table]["columnas"]
                    for columna in lista_columnas:
                        if columna["name"] == column_name:
                            return True
                    return False
        return None

    def check_exists(self, database : str, table : str, checkName : str):
        with open(file_dir) as file:
            data = json.load(file)
            #Busca la base de datos
            if database in data:
                baseActual = data[database]["tables"]
                #busca la tabla
                if table in baseActual:
                    lista_checkers = baseActual[table]["checkers"]
                    for chck in lista_checkers:
                        if chck["name"] == checkName:
                            return True
                    return False
        return None

    def constraint_exists(self, database : str, table : str, constraintName : str):
        with open(file_dir) as file:
            data = json.load(file)
            #Busca la base de datos
            if database in data:
                baseActual = data[database]["tables"]
                #busca la tabla
                if table in baseActual:
                    lista_constr = baseActual[table]["listaReferences"]
                    for chck in lista_constr:
                        if chck["nombre"] == constraintName:
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
                            "index" : indice + 1,
                            "name" : column.name,
                            "type" : column.type,
                            "specificType" : column.specificType,
                            "default" : column.default,
                            "isNull" : column.isNull,
                            "isUnique" : column.isUnique,
                            "uniqueName" : column.uniqueName,
                            "size" : column.size,
                            "isPrimary" : column.isPrimary,
                            "referencesTable" : column.referencesTable,
                            "isCheck" : column.isCheck,
                            "referenceColumn" : column.referenceColumn                            
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
    

    def CreateCheck(self, database : str, table : str, check : Check):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            #Busca la base de datos
            if database in data:
                baseActual = data[database]["tables"]
                #busca la tabla
                if table in baseActual:
                    existe = self.check_exists(database,table, check.name)
                    if existe is False and existe is not None:
                        lista_checks = baseActual[table]["checkers"]
                        lista_checks.append(
                            {
                                "name" : check.name,
                                "checkExp" : check.checkExp
                            }
                        )
                        baseActual[table]["checkers"] = lista_checks
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

    def CreateConstraint(self, database : str, table : str, constraint : Constraints):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            #Busca la base de datos
            if database in data:
                baseActual = data[database]["tables"]
                #busca la tabla
                if table in baseActual:
                    existe = self.constraint_exists(database,table,constraint.nombre)
                    if existe is False and existe is not None:
                        lista_constraints = baseActual[table]["listaReferences"]
                        lista_constraints.append(
                            {
                                "nombre" : constraint.nombre,
                                "listaColumnas" : constraint.listaColumnas
                            }
                        )
                        baseActual[table]["listaReferences"] = lista_constraints
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


    #######################################################Replace procedure
    def replace_procedure(self, database : str, procedure : Procedure):
        self.drop_procedure(database,procedure.nombre)
        return self.create_procedure(database,procedure)

    ###################################################### Drop procedure
    def drop_procedure(self,database, procedure_name):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                procedures = data[database]["procedures"]
                l = []
                for inx in procedures:
                    if inx["nombre"].upper() != procedure_name.upper():
                        l.append(inx)
                if len(l) == len(procedures):
                    return None
                else:
                    data[database]["procedures"] = l
                    dataFinal = json.dumps(data)
            else:
                return None
        if dataFinal is not None:
            file = open(file_dir,'w')
            file.write(dataFinal)
            file.close()
            return True
    ###################################################### Drop index
    def drop_index(self,database, index_name):
        dataFinal = None
        with open(file_dir) as file:
            data = json.load(file)
            if database in data:
                indexes = data[database]["indexes"]
                l = []
                for inx in indexes:
                    if inx["name"].upper() != index_name.upper():
                        l.append(inx)
                if len(l) == len(indexes):
                    return None
                else:
                    data[database]["indexes"] = l
                    dataFinal = json.dumps(data)
            else:
                return None
        if dataFinal is not None:
            file = open(file_dir,'w')
            file.write(dataFinal)
            file.close()
            return True

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
            return True

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
        else:
            return False
