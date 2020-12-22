from crud_bd import CRUD_DataBase
import copy

class Tabla():
    def __init__(self, name, numberColumns):
        self.name = name
        self.numberColumns = numberColumns
        self.tuples = None
        self.PK=[]

class CRUD_Tabla():
    """def Buscar2(self, Clave, Actual):
        if Actual != None:
            Aux = Actual.Valores
            if Clave < Aux[0][0]:
                return self.Buscar2(Clave, Actual.Hijos[0])
            elif Clave == Aux[0][0]:
                return Aux[0]
            elif Aux[1][0] != -1 and Clave > Aux[1][0]:
                return self.Buscar2(Clave, Actual.Hijos[2])
            elif Aux[1][0] != -1 and Clave == Aux[1][0]:
                return Aux[1]
            else:
                return self.Buscar2(Clave, Actual.Hijos[1])
        else:
            return None

    def Buscar(self, Clave):
        if self.Raiz == None:
            return None
        else:
            return self.Buscar2(Clave, self.Raiz)"""

    def alterAddPK(self,database,table,keys):
        Pk = keys
        datos = []
        ## busqueda tabla
        temp = self.extractTable(database,table)
        ## asignacion de valores para uso posterior del ordenamiento
        datos =  temp.Tomar_Datos()
        print(Pk)

    def extractTable(self, database, table):
        temp = CRUD_DataBase().searchDatabase(database)
        try:
            tablas = temp.tables
            for i in tablas:
                if i.name == table:
                    return i
        except:
            return None

    def createTable(self, database, table, numberColumns):
        
        r_basededatos = CRUD_DataBase().searchDatabase(database)
        if r_basededatos:
            r_tabla = self.extractTable(database, table)
            if r_tabla is None:
                tmp = CRUD_DataBase().getRoot()
                table_temp = Tabla(table, numberColumns)
                r_value = self._createTable(database, tmp, table_temp)
                if r_value:
                    CRUD_DataBase().saveRoot(tmp)
                    return 0
                else:
                    return 1
            else:
                return 3
        else:
            return 2  

    def _createTable(self, name, tmp, table_temp):
        try:
            if tmp is None:
                pass
            elif name == tmp.name :
                tmp.tables.append(table_temp)
            elif name > tmp.name:
                tmp = self._createTable(name, tmp.right, table_temp)
            else:
                tmp = self._createTable(name, tmp.left, table_temp)
            return tmp
        except:
            return 1   

    def shownTables(self, database):
        try:
            temp = CRUD_DataBase().searchDatabase(database)
            lista_retorno = []
            for item in temp.tables:
                lista_retorno.append(item.name)
            return lista_retorno
        except:
            return None

    def dropTable(self, database, table):
        try:
            temp = CRUD_DataBase().searchDatabase(database)
            if temp:
                tmp = CRUD_DataBase().getRoot()
                existencia_tabla = self.extractTable(database, table)
                if existencia_tabla:
                    self._dropTable(database, tmp, table)
                    CRUD_DataBase().saveRoot(tmp)
                    return 0
                else:
                    return 3 
            else:
                return 2
        except:
            return 1

    def _dropTable(self, name, tmp, table):
        if tmp is None:
            pass
        elif name == tmp.name:
            id = 0
            for n in tmp.tables:
                if n.name == table:
                    id = tmp.tables.index(n)
                    break
            tmp.tables.pop(id)
        elif name > tmp.name:
            tmp = self._dropTable(name, tmp.right, table)
        else:
            tmp = self._dropTable(name, tmp.left, table)
        return tmp

    def alterTable(self, database, tableOld, tableNew):
        
        existe_database = CRUD_DataBase().searchDatabase(database)
        if existe_database:
            existe_tableOld = copy.deepcopy(self.extractTable(database, tableOld))
            if existe_tableOld:
                existe_tableNew = self.extractTable(database, tableNew)
                if existe_tableNew is None:
                    
                    existe_tableOld.name = tableNew
                    val_drop = self.dropTable(database, tableOld)

                    if val_drop == 0:
                        val_assign = self.createTable_Object(database, tableNew, existe_tableOld)
                        return val_assign
                    elif val_drop == 2:
                        return 2
                    else:
                        return 1
                else:
                    return 4
            else:
                return 3
        else:
            return 2
            
    def createTable_Object(self, database, table, object_table):
        
        r_basededatos = CRUD_DataBase().searchDatabase(database)
        if r_basededatos:
            r_tabla = self.extractTable(database, table)
            if r_tabla is None:
                tmp = CRUD_DataBase().getRoot()
                r_value = self._createTable(database, tmp, object_table)
                if r_value:
                    CRUD_DataBase().saveRoot(tmp)
                    return 0
                else:
                    return 1
            else:
                return 3
        else:
            return 2  
           
    def extractRangeTable(self,database,table,columnNumber,lower,upper):
        valores = []
        i = lower
        temp = self.extractTable(database,table)
        while i <= upper:
            i += 1
            valores.append(temp[i])
        return valores

    def insert(self,database,table,tupla):
        self.root = CRUD_DataBase().getRoot()
        self._insert(database, self.root, table,tupla)
        CRUD_DataBase().saveRoot(self.root)

    def _insert(self,database,tmp,table,tupla):
        if tmp is None:
            pass
        elif tmp.name == database:
            self.subinsert(tmp,table,tupla)
        elif database > tmp.name:
            tmp = self._insert(database, tmp.right, table,tupla)
        else:
            tmp = self._insert(database, tmp.left, table, tupla )
        return tmp

    def subinsert(self,tmp,table,tupla):
        for n in tmp.tables:
            if n.name == table:
                id = tmp.tables.index(n)
                if tmp.tables[id].Tuplas == None:
                    tmp.tables[id].Tuplas = []
                    tmp.tables[id].Tuplas.insertar_(tupla)
                else:
                    tmp.tables[id].Tuplas.insertar_(tupla)
                return tmp
