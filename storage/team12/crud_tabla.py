from crud_bd import CRUD_DataBase
from crud_tupla import *
import copy

class Tabla():
    def __init__(self, name, numberColumns):
        self.name = name
        self.numberColumns = numberColumns
        self.tuples = None
        self.PK = []

class CRUD_Tabla():
    ##note make validations of pk´s
    def alterAddPK(self, database, table, columns):
        try:
            asd = []
            search = CRUD_DataBase().searchDatabase(database)
            if search:
                search_table = self.extractTable(database, table)
                if search_table is None:
                    return 3
                else:
                    large = search_table.numberColumns
                    # print(large)
                    # print(len(columns))
                    if len(columns) <= large:
                        tmp = CRUD_DataBase().getRoot()
                        if search_table.PK == asd:
                            validation_apoved = self._alterAddPK(database, table, columns, tmp)
                            if validation_apoved:
                                CRUD_DataBase().saveRoot(tmp)
                                return 0
                        else:
                            return 4

                    else:
                        return 5
            else:
                return 2
        except:
            return 1

    def _alterAddPK(self, name, table, columns, tmp):
        ## recursividad para busqueda e insercion de datos
        if tmp is None:
            pass
        elif name == tmp.name:
            id = 0
            for n in tmp.tables:
                if n.name == table:
                    id = tmp.tables.index(n)
                    tmp = self.subalterAddPK(columns, tmp, id)
                    break

        elif name > tmp.name:
            tmp = self._alterAddPK(name, table, columns, tmp.right)
        else:
            tmp = self._alterAddPK(name, table, columns, tmp.left)
        return tmp

    def subalterAddPK(self, keys, tmp, id):

        ## igualamos la lista de pk con keys
        tmp.tables[id].PK = keys
        temp_vals = tmp.tables[id].tuples.takeDates()
        new_tree = CRUD_Tuplas()
        tmp.tables[id].tuples = None
        tmp.tables[id].tuples = new_tree
        tmp.tables[id].tuples.DefinirLlaves(keys)

        if len(tmp.tables[id].PK) > 1:
            ## concatenacion de llaves primarias
            for n in temp_vals:
                tempString = self.sumatoryStringKey(n, keys)
                n.insert(0, tempString)
                tmp.tables[id].tuples.Insertar(n)

        else:
            pk = tmp.tables[id].PK[0]
            # print(pk)

            for n in temp_vals:
                temp_pos = n[pk]
                # print(temp_pos)
                n.insert(0, temp_pos)
                tmp.tables[id].tuples.Insertar(n)

        return tmp

    def sumatoryStringKey(self, values, keys):
        concatenatePK = ""
        # print(values)
        # print(values[2])
        for n in keys:
            asd = values[n]
            concatenatePK += asd
        return concatenatePK

    def alterDropPK(self, database, table):
        try:
            search = CRUD_DataBase().searchDatabase(database)
            if search:
                search_table = self.extractTable(database, table)
                if search_table is None:
                    return 3
                else:
                    temp_pk = search_table.PK
                    if temp_pk[0] is None:
                        return 4
                    else:
                        tmp = CRUD_DataBase().getRoot()
                        validation_aproved = self._alterDropPK(database, table, tmp)
                        if validation_aproved:
                            CRUD_DataBase().saveRoot(tmp)
        except:
            return 1

    def _alterDropPK(self, database, table, tmp):
        if tmp is None:
            pass
        elif database == tmp.name:
            for n in tmp.tables:
                if n.name == table:
                    id = tmp.tables.index(n)
                    pk = []
                    tmp.tables[id].PK = pk
                    tmp.tables[id].tuples.DefinirLlaves([])
                    break
        elif database > tmp.name:
            tmp = self._alterDropPK(database, table, tmp.right)
        else:
            tmp = self._alterDropPK(database, table, tmp.left)
        return tmp

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
            elif name == tmp.name:
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
                # print(item.name)
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
                if tmp.tables[id].tuples == None:
                    tmp.tables[id].tuples = CRUD_Tuplas()
                    tmp.tables[id].tuples.insertar_(tupla)
                else:
                    tmp.tables[id].tuples.insertar_(tupla)
                return tmp

    def update(self, database, table, register,columns):
        self.root = CRUD_DataBase().getRoot()
        self._update(database, self.root, table, register,columns)
        CRUD_DataBase().saveRoot(self.root)

    def _update(self, database, tmp, table, register,columns):
        if tmp is None:
            pass
        elif tmp.name == database:
            self.subUpdate(tmp, table, register, columns)
        elif database > tmp.name:
            tmp = self._update(database, tmp.right, table, register)
        else:
            tmp = self._update(database, tmp.left, table, columns)
        return tmp

    def subUpdate(self, tmp, table, register, columns):
        for n in tmp.tables:
            if n.name == table:
                id = tmp.tables.index(n)
                if tmp.tables[id].tuples == None:
                    return 1
                else:
                    tmp.tables[id].tuples.actualizar(register,columns)
                return tmp

    def delete(self, database, table, tupla):
        self.root = CRUD_DataBase().getRoot()
        self._delete(database, self.root, table, tupla)
        CRUD_DataBase().saveRoot(self.root)

    def _delete(self, database, tmp, table, tupla):
        if tmp is None:
            pass
        elif tmp.name == database:
            self.subDelete(tmp, table, tupla)
        elif database > tmp.name:
            tmp = self._delete(database, tmp.right, table, tupla)
        else:
            tmp = self._delete(database, tmp.left, table, tupla)
        return tmp

    def subDelete(self, tmp, table, tupla):
        for n in tmp.tables:
            if n.name == table:
                id = tmp.tables.index(n)
                if tmp.tables[id].tuples == None:
                    return 1
                else:
                    tmp.tables[id].tuples.Eliminar(tupla)
                return tmp

    def extractRow(self, database, table, tupla):
        self.root = CRUD_DataBase().getRoot()
        self._ext(database, self.root, table, tupla)
        CRUD_DataBase().saveRoot(self.root)

    def _ext(self, database, tmp, table, tupla):
        if tmp is None:
            pass
        elif tmp.name == database:
            self.subExtract(tmp, table, tupla)
        elif database > tmp.name:
            tmp = self._ext(database, tmp.right, table, tupla)
        else:
            tmp = self._ext(database, tmp.left, table, tupla)
        return tmp

    def subExtract(self, tmp, table, tupla):
        for n in tmp.tables:
            if n.name == table:
                id = tmp.tables.index(n)
                if tmp.tables[id].tuples == None:
                    return 1
                else:
                    tmp.tables[id].tuples.ExtraerFila(tupla)
                return tmp

    def truncate(self, database, table):
        self.root = CRUD_DataBase().getRoot()
        self._ext(database, self.root, table)
        CRUD_DataBase().saveRoot(self.root)

    def _trunc(self, database, tmp, table):
        if tmp is None:
            pass
        elif tmp.name == database:
            self.subTrunc(tmp, table)
        elif database > tmp.name:
            tmp = self._trunc(database, tmp.right, table)
        else:
            tmp = self._trunc(database, tmp.left, table)
        return tmp

    def subTrunc(self, tmp, table, tupla):
        for n in tmp.tables:
            if n.name == table:
                id = tmp.tables.index(n)
                if tmp.tables[id].tuples == None:
                    return 1
                else:
                    tmp.tables[id].tuples.Vaciar()
                return tmp

    def loadCSV(self, file, database, table):
        self.root = CRUD_DataBase().getRoot()
        self._load(database, self.root, table, file)
        CRUD_DataBase().saveRoot(self.root)

    def _load(self, database, tmp, table, file):
        if tmp is None:
            pass
        elif tmp.name == database:
            self.subLoad(tmp, table, file)
        elif database > tmp.name:
            tmp = self._load(database, tmp.right, table, file)
        else:
            tmp = self._load(database, tmp.left, table, file)
        return tmp

    def subLoad(self, tmp, table, file):
        for n in tmp.tables:
            if n.name == table:
                id = tmp.tables.index(n)
                if tmp.tables[id].tuples == None:
                    return 1
                else:
                    tmp.tables[id].tuples.loadCSV(file)
                return tmp

    ############################################################################
    def extractRangeTable(self, database, table, columnNumber, lower, upper):
        try:
            search = self.extractTable(database, table)
            if search:
                if search.tuples is None:
                    return None
                else:
                    dates = search.tuples.takeDates()
                    dates = self._extractRangeTables(columnNumber, lower, upper, dates)
                    # print("valores")
                    return dates
            else:
                return None
        except:
            return 1

    ############################################################################

    def _extractRangeTables(self, columnNumber, Lower, upper, dates):
        vals = []
        for n in dates:
            if n[columnNumber] >= Lower and n[columnNumber] <= upper:
                vals.append(n[columnNumber])
        return vals

    def alterDropColumn(self, database, table, columnnumber):
        try:
            search = CRUD_DataBase().searchDatabase(database)
            if search:
                search_table = self.extractTable(database, table)
                if search_table:
                    if columnnumber < search_table.numberColumns - 1:
                        if columnnumber == search_table.numberColumns:
                            return 4
                        else:
                            t = True
                            for n in search_table.PK:
                                if columnnumber == n:
                                    t = False
                            if t == True:
                                tmp = CRUD_DataBase().getRoot()
                                validation_aproved = self._alterDropColumns(database, table, columnnumber, tmp)
                                if validation_aproved:
                                    return 0
                                else:
                                    return 1
                            else:
                                return 4
                    else:
                        return 5

                else:
                    return 3
            else:
                return 2
        except:
            return 1

    def _alterDropColumns(self, name, table, columnumber, tmp):
        if tmp is None:
            pass
        elif name == tmp.name:

            for n in tmp.tables:
                if n.name == table:
                    id = tmp.tables.index(n)
                    tmp = self.newEstructureColumns(tmp, id, columnumber)
                    break

        elif name > tmp.name:
            tmp = self._alterAddPK(name, table, columnumber, tmp.right)
        else:
            tmp = self._alterAddPK(name, table, columnumber, tmp.left)
        return tmp

    def newEstructureColumns(self, tmp, id, columnumber):
        ## igualamos la lista de pk con keys
        temp_vals = tmp.tables[id].tuples.takeDates()
        new_tree = CRUD_Tuplas()
        tmp.tables[id].tuples = None
        tmp.tables[id].tuples = new_tree

        ## concatenacion de llaves primarias
        for n in temp_vals:
            n.pop(columnumber)
            tmp.tables[id].tuples.Insertar(n)

        return tmp

    def alterAddColumn(self, database, table, columns):
        try:
            search = CRUD_DataBase().searchDatabase(database)
            if search:
                search_table = self.extractTable(database, table)
                if search_table is None:
                    return 3
                else:
                    tmp = CRUD_DataBase().getRoot()
                    validation_apoved = self._alterAddColumn(database, table, columns, tmp)
                    if validation_apoved:
                        CRUD_DataBase().saveRoot(tmp)
                        return 0
                    else:
                        return 1
            else:
                return 2
        except:
            return 1

    def _alterAddColumn(self, name, table, columnumber, tmp):
        if tmp is None:
            pass
        elif name == tmp.name:

            for n in tmp.tables:
                if n.name == table:
                    id = tmp.tables.index(n)
                    tmp = self.addcolumn(tmp, id, columnumber)
                    break

        elif name > tmp.name:
            tmp = self._alterAddPK(name, table, columnumber, tmp.right)
        else:
            tmp = self._alterAddPK(name, table, columnumber, tmp.left)
        return tmp

    def addcolumn(self, tmp, id, columnumber):
        temp_vals = tmp.tables[id].tuples.takeDates()
        new_tree = CRUD_Tuplas()
        tmp.tables[id].tuples = None
        tmp.tables[id].tuples = new_tree

        ## concatenacion de llaves primarias
        for n in temp_vals:
            n.append(columnumber)
            tmp.tables[id].tuples.Insertar(n)

        return tmp