from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.DictMode import DictMode as DM
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as j
from storage.Hash import HashMode as Hash
import zlib
import hashlib
import os
# from storage.HashWindows import HashMode as Hash
import Encriptado as E
import BlockChain as Block #IMPOR BASES
saveModo_bandera = True
currentMode,avlList,bList,bplusList,dictList,jsonList,isamList,hashList = [],[],[],[],[],[],[],[]
comp = []
compT,decompT = [],[]
decomp = []
listMode = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
listEncoding = ['ascii', 'iso-8859-1', 'utf8']

global lista
lista = list()

global listados
listados = list()

class controlFK:
    def __init__(self, database, table, indexName, columns, tableRef, columnsRef):
        self.database = database
        self.table = table
        self.indexName = indexName
        self.columns = columns
        self.tableRef = tableRef
        self.columnsRef = columnsRef

class controlUnique:
    def __init__(self, database, table, indexName, columns):
        self.database = database
        self.table = table
        self.indexName = indexName
        self.columns = columns      

# ----------Bases de datos------------------
def createDatabase(database, mode, encoding):
    try:
        if not isValidMode(mode):
            return 3
        elif not isValidEncoding(encoding):
            return 4
        else:    
            currentMode.append(mode)
            #llamar encoding
            return chooseMode(mode,database)
    except:
        return 1

def alterDatabaseMode(database, mode):
    try:
        M = searchInMode(database)
        if  M != None:
            if not isValidMode(mode):
                return 4
            oldReg = []
            oldTables = showTables(database)

            for table in oldTables:
                oldReg.append(extractTable(database,table))
                valCol = len(extractTable(database,table)[0])
            dropDatabase(database)
            if M == 'avl':
                avlList.remove(database)
            elif M == 'b':
                bList.remove(database)
            elif M == 'dict':
                dictList.remove(database)
            elif M == 'bplus':
                dictList.remove(database)
            elif M == 'isam':
                isamList.remove(database)
            elif M == 'json':
                jsontList.remove(database)
            elif M == 'hash':
                hashList.remove(database)
            newBase = createDatabase(database,mode,'ascii')
            if newBase == 0:
                # oldTables = showTables(database)
                
                for table in oldTables:
                    # valCol = len(extractTable(database,table)[0])
                    # oldReg = extractTable(database,table)
                    # newTable = createTable(database,table,valCol)
                    createTable(database,table,valCol)
                # if newTable == 0:
                for i in range(len(oldTables)):
                    for j in range(len(oldReg[i])):
                        insert(database,oldTables[i],oldReg[i][j])
                # for reg in oldReg:
                #     for newReg in reg:
                #         insert(database,table,newReg)
                return 0
                # else:
                #     return newTable
            else:
                return newBase
        else:
            return 2        
    except:
        return 1            

def showDatabases():
    showAvl = avl.showDatabases()
    showB = b.showDatabases()
    showBP = bplus.showDatabases()
    showDict = DM.showDatabases()
    showIsam = isam.showDatabases()
    showHash = Hash.showDatabases()
    showJson = j.showDatabases()
    showALL = 'avl = ' + str(showAvl)+'\n'+'b = ' + str(showB)+'\n'+'bplus = ' + str(showBP)+'\n'+'dict = ' + str(showDict)+'\n'+'isam = ' + str(showIsam)+'\n'+'json = ' + str(showJson) +'\n'+'hash = ' + str(showHash)
                
    return showALL

def alterDatabase(old, new):
    if searchInMode(old) != None:
        currentMode = searchInMode(old)
        if currentMode == 'avl':
            avlList.append(new)
            return avl.alterDatabase(old, new)
        elif currentMode == 'b':
            bList.append(new)
            return b.alterDatabase(old, new)
        elif currentMode == 'bplus':
            bplusList.append(new)
            return bplus.alterDatabase(old, new)
        elif currentMode == 'dict':
            dictList.append(new)
            return DM.alterDatabase(old, new)
        elif currentMode == 'isam':
            isamList.append(new)
            return isam.alterDatabase(old, new)
        elif currentMode == 'json':
            jsonList.append(new)
            return j.alterDatabase(old, new)
        elif currentMode == 'hash':
            hashList.append(new)
            return Hash.alterDatabase(old, new)
        
def dropDatabase(database):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            return avl.dropDatabase(database)
        elif currentMode == 'b':
            return b.dropDatabase(database)
        elif currentMode == 'bplus':
            return bplus.dropDatabase(database)
        elif currentMode == 'dict':
            return DM.dropDatabase(database)
        elif currentMode == 'isam':
            return isam.dropDatabase(database)
        elif currentMode == 'json':
            return j.dropDatabase(database)
        elif currentMode == 'hash':
            return Hash.dropDatabase(database)
    else:
        return 2

def alterTableAddFK(database, table, indexName, columns,  tableRef, columnsRef):  
    Temporal = showTables(database)
    bandera = False
    contador = 0

    if Temporal == 2:
        return 2

    try: 
        for i in Temporal:
            if table == i:
                contador += 1
                if contador >= 1:
                    bandera = True
                

        if len(columns) <= 0 or len(columnsRef) <=0 or len(columns) != len(columnsRef):
            return 4

        elif bandera == False:
            return 3

        else:
            lista.append(controlFK(database,table,indexName,columns,tableRef,columnsRef))
            return 0
    except:
        return 1

def alterTableDropFK(database, table, indexName):
    try:
        for j in range(len(lista)):
            if database == lista[j].database:
                for k in range(len(lista)):
                    if table == lista[k].table:
                        for i in range(len(lista)):
                            if indexName == lista[i].indexName:
                                lista.pop(i)
                                return 0
                            else:
                                return 4
                    else:
                        return 3
            else:
                return 2
    except:
        return 1

def alterTableAddUnique(database, table, indexName, columns):    
    Temporal = showTables(database)
    bandera = False
    bandera2 = False
    contador = 0

    if Temporal == 2:
        return 2

    try:
        for i in Temporal:
            if table == i:
                contador += 1
                if contador >= 1:
                    bandera = True
                
        for j in range(len(listados)):
            if indexName == listados[j].indexName:
                bandera2 = True
            

        if bandera == False:
            return 3
        elif bandera2 == True:
            return 5
        else:
            listados.append(controlUnique(database,table,indexName,columns))
            return 0
    except:
        return 1


def alterTableDropUnique(database, table, indexName):
    try:
        for j in range(len(listados)):
            if database == listados[j].database:
                for k in range(len(listados)):
                    if table == listados[k].table:
                        for i in range(len(listados)):
                            if indexName == listados[i].indexName:
                                listados.pop(i)
                                return 0
                            else:
                                return 4
                    else:
                        return 3
            else:
                return 2
    except:
        return 1

#-------------TABLAS-------------------
def createTable(database, table, numbercolumns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            avlList.append(table)
            return avl.createTable(database, table, numbercolumns)
        elif currentMode == 'b':
            bList.append(table)
            return b.createTable(database, table, numbercolumns)
        elif currentMode == 'bplus':
            bplusList.append(table)
            return bplus.createTable(database, table, numbercolumns)
        elif currentMode == 'dict':
            dictList.append(table)
            return DM.createTable(database, table, numbercolumns)
        elif currentMode == 'isam':
            isamList.append(table)
            return isam.createTable(database, table, numbercolumns)
        elif currentMode == 'json':
            jsonList.append(table)
            return j.createTable(database, table, numbercolumns)
        elif currentMode == 'hash':
            hashList.append(table)
            return Hash.createTable(database, table, numbercolumns)
    else:
        return 2

def alterTableMode(database, table, mode):
    try:
        M = searchInMode(database)
        T = searchInMode(database)
        if  M != None:
            if T != None:
                if not isValidMode(mode):
                    return 4
                oldReg = []
                oldTables = showTables(database)
                valCol = len(extractTable(database,table)[0])
                # for table in oldTables:
                #     oldReg.append(extractTable(database,table))
                #     valCol = len(extractTable(database,table)[0])
                dropDatabase(table)
                if T == 'avl':
                    avlList.remove(table)
                elif T == 'b':
                    bList.remove(table)
                elif T == 'dict':
                    dictList.remove(table)
                elif T == 'bplus':
                    dictList.remove(table)
                elif T == 'isam':
                    isamList.remove(table)
                elif T == 'json':
                    jsontList.remove(table)
                elif T == 'hash':
                    hashList.remove(table)
                newBase = createDatabase(database,mode,'ascii')
                # if newBase == 0:
                #     # oldTables = showTables(database)
                    
                #     for table in oldTables:
                        # valCol = len(extractTable(database,table)[0])
                        # oldReg = extractTable(database,table)
                        # newTable = createTable(database,table,valCol)
                createTable(database,table,valCol)
                if newTable == 0:
                    # for i in range(len(oldTables)):
                    #     for j in range(len(oldReg[i])):
                    #         insert(database,oldTables[i],oldReg[i][j])
                    for reg in oldReg:
                        for newReg in reg:
                            insert(database,table,newReg)
                    return 0
                else:
                    return newTable
                
            else:
                return 3
        else:
            return 2        
    except:
        return 1

def alterTable(database, tableOld, tableNew):
    if searchInMode(tableOld) != None:
        currentMode = searchInMode(tableOld)
        if currentMode == 'avl':
            avlList.append(tableNew)
            return avl.alterTable(database, tableOld, tableNew)
        elif currentMode == 'b':
            bList.append(tableNew)
            return b.alterTable(database, tableOld, tableNew)
        elif currentMode == 'bplus':
            bplusList.append(tableNew)
            return bplus.alterTable(database, tableOld, tableNew)
        elif currentMode == 'dict':
            dictList.append(tableNew)
            return DM.alterTable(database, tableOld, tableNew)
        elif currentMode == 'isam':
            isamList.append(tableNew)
            return isam.alterTable(database, tableOld, tableNew)
        elif currentMode == 'json':
            jsonList.append(tableNew)
            return j.alterTable(database, tableOld, tableNew)
        elif currentMode == 'hash':
            hashList.append(tableNew)
            return Hash.alterTable(database, tableOld, tableNew)
    else:
        return 2

def dropTable(database, table):
    if searchInMode(table) != None:
        currentMode = searchInMode(table)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.dropTable(database, table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.dropTable(database, table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.dropTable(database, table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.dropTable(database, table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.dropTable(database, table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.dropTable(database, table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.dropTable(database, table)
    else:
        return 2

def showTables(database):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.showTables(database)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.showTables(database)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.showTables(database)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.showTables(database)
        elif currentMode == 'isam':
            # isamList.append(database)
            return isam.showTables(database)
        elif currentMode == 'json':
            # jsonList.append(database)
            return j.showTables(database)
        elif currentMode == 'hash':
            # hashList.append(database)
            return Hash.showTables(database)
    else:
        return 2

#--------Registros----------------------
def alterAddPK(database, table, columns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.alterAddPK(database, table, columns)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.alterAddPK(database, table, columns)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.alterAddPK(database, table, columns)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.alterAddPK(database, table, columns)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.alterAddPK(database, table, columns)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.alterAddPK(database, table, columns)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.alterAddPK(database, table, columns)
    else:
        return 2

def alterDropPK(database, table):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.alterDropPK(database, table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.alterDropPK(database, table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.alterDropPK(database, table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.alterDropPK(database, table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.alterDropPK(database, table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.alterDropPK(database, table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.alterDropPK(database, table)
    else:
        return 2

def insert(database, table, register):
    if saveModo_bandera is False:
        Block.activar_SaveModo(register)
        #print("validacion correcta")
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.insert(database, table, register)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.insert(database, table, register)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.insert(database, table, register)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.insert(database, table, register)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.insert(database, table, register)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.insert(database, table, register)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.insert(database, table, register)
    else:
        return 2

def update(database, table, register, columns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.update(database, table, register, columns)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.update(database, table, register, columns)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.update(database, table, register, columns)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.update(database, table, register, columns)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.update(database, table, register, columns)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.update(database, table, register, columns)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.update(database, table, register, columns)
    else:
        return 2

def delete(database, table, columns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.delete(database, table, columns)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.delete(database, table, columns)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.delete(database, table, columns)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.delete(database, table, columns)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.delete(database, table, columns)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.delete(database, table, columns)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.delete(database, table, columns)
    else:
        return 2

def truncate(database, table):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.truncate(database, table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.truncate(database, table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.truncate(database, table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.truncate(database, table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.truncate(database, table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.truncate(database, table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.truncate(database, table)
    else:
        return 2

def alterAddColumn(database,table, default):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.alterAddColumn(database,table, default)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.alterAddColumn(database,table, default)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.alterAddColumn(database,table, default)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.alterAddColumn(database,table, default)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.alterAddColumn(database,table, default)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.alterAddColumn(database,table, default)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.alterAddColumn(database,table, default)
    else:
        return 2

def alterDropColumn(database, table, columnNumber):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.alterDropColumn(database, table, columnNumber)
    else:
        return 2

def extractTable(database, table):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.extractTable(database, table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            #registros = b.extractTable(database, table) -> [reg,reg2,regi]

            return b.extractTable(database, table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.extractTable(database, table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.extractTable(database, table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.extractTable(database, table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.extractTable(database, table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.extractTable(database, table)
    else:
        return 2

def extractRangeTable(database, table, columnNumber, lower, upper):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.extractRangeTable(database, table, lower, upper)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.extractRangeTable(database, table, columnNumber, lower, upper)
    else:
        return 2

def extractRow(database, table, columns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.extractRow(database, table, columns)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.extractRow(database, table, columns)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.extractRow(database, table, columns)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.extractRow(database, table, columns)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.extractRow(database, table, columns)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.extractRow(database, table, columns)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.extractRow(database, table, columns)
    else:
        return 2

def loadCSV(file,database,table):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.loadCSV(file,database,table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.loadCSV(file,database,table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.loadCSV(file,database,table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.loadCSV(file,database,table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.loadCSV(file,database,table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.loadCSV(file,database,table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.loadCSV(file,database,table)
    else:
        return 2

#----------------------------------------------------
def isValidMode(mode):
    listMode = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
    for check in listMode:
        if check == mode:
            return True
    return False

def isValidEncoding(encoding):
    listEncoding = ['ascii', 'iso-8859-1', 'utf8']
    for check in listEncoding:
        if check == encoding:
            return True
    return False

def chooseMode(mode,database):
    if mode == 'avl':
        if avl.createDatabase(database) == 0:
            avlList.append(database)
            return 0
        else:
            return avl.createDatabase(database)
    elif mode == 'b':
        if b.createDatabase(database) == 0:
            bList.append(database)
            return 0
        else:
            return b.createDatabase(database)
    elif mode == 'bplus':
        if bplus.createDatabase(database) == 0:
            bplusList.append(database)
            return 0
        else:
            return bplus.createDatabase(database)
    elif mode == 'dict':
        if DM.createDatabase(database) == 0:
            dictList.append(database)
            return 0
        else:
            return DM.createDatabase(database)
    elif mode == 'isam':
        if isam.createDatabase(database) == 0:
            isamList.append(database)
            return 0
        else:
            return isam.createDatabase(database)
    elif mode == 'json':
        if j.createDatabase(database) == 0:
            jsonList.append(database)
            return 0
        else:
            return j.createDatabase(database)
    elif mode == 'hash':
        if Hash.createDatabase(database) == 0:
            hashList.append(database)
            return 0
        else:
            return Hash.createDatabase(database)

def searchInMode(value):
    if value in avlList:
        return 'avl'
    elif value in bList:
        return 'b'
    elif value in bplusList:
        return 'bplus'
    elif value in dictList:
        return 'dict'
    elif value in jsonList:
        return 'json'
    elif value in isamList:
        return 'isam'
    elif value in hashList:
        return 'hash'
    else:
        return None

def alterDataBaseEncoding(database, codificacion):
    try:
        if codificacion == '' or codificacion == None:
            codificacion ='ascii'
        key = []
        #vamos a recorrer las bases, empezando por ver si existe la base 
        for i in listMode:
            if searchInMode(database)!= None :  #Buscamos la base 
                if  listEncoding(codificacion):
                   # tabla = showTables(database, i) #Verificamos si hay tablas en la BD
                    if showTables(database, i):#tabla != []:
                        for j in showTables : #La codificaci[on de las tablas] \
                            tupla = extractTable(database, j)   
                            if tupla !=[]:
                                llave = currentMode[i][database][0][j][1]
                                for n in range (0,len(tupla)):
                                    Tup = []
                                    for l in tupla[n]:
                                        if type(l) is bytes: 
                                            var1 = l.decode(currentMode[i][database][0][j][2])
                                            Tup += [str(var1).encode(encoding = codificacion ,errors= 'backslashreplace' )]
                                        else: 
                                            Tup += [str(l).encode(encoding = codificacion ,errors= 'backslashreplace' )]
                                    for x in llave:
                                            key.append(tupla[n][x])
                                            tuplaNew = {}
                                    for f in range(0,len(Tup)):
                                            tuplaNew[f] = Tup[f]
                                    update(database,j,tuplaNew,key)
                                    key = []
                        currentMode[i][dataBase][0][j][2] = codificacion
            return 0 
                    
            return 3
        return 2
    except:
        return 1         

def alterDatabaseCompress(database: str, level: int) :
    try:
        baseexist = searchInMode(database)
        if baseexist != None:
            if not level > -1 and level < 10:
                return 3
            oldReg = []
            # comp = []
            oldTables = showTables(database)

            for table in oldTables:
                oldReg.append(extractTable(database,table))
                valCol = len(extractTable(database,table)[0])
            
            for reg in oldReg:
                for newReg in reg:
                    compressed = zlib.compress(bytes(str(newReg),encoding = "utf-8"),level)
                    comp.append(compressed)
            print(comp)
            return 0
            
        else:
            return 2
    except:
        return 1

def alterDatabaseDecompress(database: str) :
    try:
        baseexist = searchInMode(database)
        if baseexist != None:
            if len(comp) == 0:
                return 3
            oldReg = []
            # comp = []
            oldTables = showTables(database)

            for table in oldTables:
                oldReg.append(extractTable(database,table))
                valCol = len(extractTable(database,table)[0])
            
            for c in comp:
                decompressed = zlib.decompress(c)
                decomp.append(decompressed)
            print(decomp)
            # print(comp)
            return 0
        else:
            return 2       
    except:
        return 1

def alterTableCompress(database: str, table: str, level: int):
    try:
        baseexist = searchInMode(database)
        if baseexist != None:
            if not level > -1 and level < 10:
                return 4
            if searchInMode(table) == None:
                return 3
            oldReg = []
            # comp = []
            oldTables = showTables(database)

            for table in oldTables:
                oldReg.append(extractTable(database,table))
                valCol = len(extractTable(database,table)[0])
            
            for reg in oldReg:
                for newReg in reg:
                    compressedT = zlib.compress(bytes(str(newReg),encoding = "utf-8"),level)
                    compT.append(compressedT)
            print(compT)
            return 0
        else:
            return 2       
    except:
        return 1

def alterTableDecompress(database: str, table: str):
    try:
        baseexist = searchInMode(database)
        if baseexist != None:
            if len(compT) == 0:
                return 4
            if searchInMode(table) == None:
                return 3
            oldReg = []
            # comp = []
            oldTables = showTables(database)

            for table in oldTables:
                oldReg.append(extractTable(database,table))
                valCol = len(extractTable(database,table)[0])
            
            for c in comp:
                decompressedT = zlib.decompress(c)
                decompT.append(decompressedT)
            print(decompT)
            # print(comp)
            return 0
        else:
            return 2       
    except:
        return 1

def checksumDatabase(database, mode):
    MegaCadena = ""

    try:
        lista = showTables(database)
        MegaCadena = MegaCadena + database

        for i in lista:
            MegaCadena = MegaCadena + i

            for j in extractTable(database, i):
                MegaCadena = MegaCadena + str(j)
        if mode == "MD5":
            return CodMD5(MegaCadena)
        else:
            return CodSHA256(MegaCadena)
    
    except:
        return None

def checksumTable(database, table, mode):
    MegaCadena = ""

    try:
        lista = showTables(database)

        for i in lista:
            if i == table:
                MegaCadena = MegaCadena + i
            
            for j in extractTable(database, i):
                if i == table:
                    MegaCadena = MegaCadena + str(j)

        
        if mode == "MD5":
            return CodMD5(MegaCadena)
        else:
            return CodSHA256(MegaCadena)

    except:
        return None

        
# ------------------ 8. Grafos ------------------

#def graphDSD(database: str) -> str:
#Relacion de tablas con respecto a las FK en una BD             #no son utiles todavia, al no usar fk no funcionan
def graphDSD(database: str) :
    l=[]
    l.append(showTables(database))
    print(l[0][2])
    return GDSD(database,l)

def CodMD5(Entrada):
    MD5Codigo = hashlib.md5()
    MD5Codigo.update(Entrada.encode('utf8'))
    Proceso = MD5Codigo.hexdigest()
    return Proceso

def CodSHA256(Entrada):
    SHACodigo = hashlib.sha256()
    SHACodigo.update(Entrada.encode('utf8'))
    Proceso = SHACodigo.hexdigest()
    return Proceso

def GDSD(baseDatos, lista: list) :
    try:
        f = open("GrafoBD.dot","w")
        f.write("digraph g {\n")
        f.write("node [shape=record]\n")
        f.write("subgraph cluster_0 {\n")
        f.write("\""+str(lista[0][0])+"\";\n")
        for i in range(len(lista[0][0])):
            #if i >= len(lista[0][0]):
               # break
            f.write("\""+str(lista[0][i+1])+"\";\n") 
            
        f.write("label=\""+baseDatos+"\";")
        f.write("color=blue;\n")
        f.write("}")
        for i in range(len(lista[0][0])):
            f.write(lista[0][0]+"->"+lista[0][i]+"\n")
        f.write("}")
        f.close()
        os.system("dot -Tjpg GrafoBD.dot -o GrafoBD.png")
        return 0
    except Exception as e:
        print(e)
        return None

#def graphDF(database: str, table: str) -> str:
#Relacion de registros de 1 tabla con repecto a la PK e indices unicos        #no trabaja con indices todavia
def graphDF(database: str, table: str) :
    l=[] 
    l.append(extractTable(database,table))
    return GDF(table,l)

def GDF(tabla, lista: list) :
    try:
        f = open("GrafoT.dot","w")
        f.write("digraph g {\n")
        f.write("node [shape=record]\n")
        f.write("subgraph cluster_0 {")
        f.write("\""+str(lista[0][0][0])+"\";\n")
        for i in range(len(lista[0][0][0])):
            f.write("\""+str(lista[0][i+1][0])+"\";\n") 
        f.write("label=\""+tabla+"\";")
        f.write("color=blue;\n")
        f.write("}")
        for i in range(len(lista[0][0][0])):
            f.write(lista[0][0][0]+"->"+lista[0][i+1][0]+"\n")
        f.write("}")
        f.close()
        os.system("dot -Tjpg GrafoT.dot -o GrafoT.png")
        return 0
    except:
        return None

def safeModeOn(database, table):
    global saveModo_bandera
                
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            if avl.verificar_avl(database,table) == 0:
                saveModo_bandera = not saveModo_bandera
                return 0
            elif avl.verificar_avl(database,table) == 2:
                return 2
            elif avl.verificar_avl(database,table) == 1:
                return 1   
            return 1  
        elif currentMode == 'b':
            if b.verificar_B(database,table) == 0:
                saveModo_bandera = not saveModo_bandera
                return 0
            elif b.verificar_B(database,table) == 1:
                return 1
            return 1
        elif currentMode == 'bplus':
            if bplus.verificar_Bplus(database,table) == 0:
                saveModo_bandera = not saveModo_bandera
                return 0
            elif bplus.verificar_Bplus(database,table) == 1:
                return 1
            elif bplus.verificar_Bplus(database,table) == 2:
                return 2
            elif bplus.verificar_Bplus(database,table) == 3:
                return 3
            return 1
        elif currentMode == 'dict':
            if DM.verificar_DictMode(database,table) == 0:
                saveModo_bandera = not saveModo_bandera
                return 0
            elif DM.verificar_DictMode(database,table) == 1:
                return 1
            elif DM.verificar_DictMode(database,table) == 2:
                return 2
            elif DM.verificar_DictMode(database,table) == 3:
                return 3
        elif currentMode == 'isam':
            if isam.verificar_Isam(database,table)== 0:
                saveModo_bandera = not saveModo_bandera
                return 0
            elif isam.verificar_Isam(database,table) == 1:
                return 1
            elif isam.verificar_Isam(database,table) == 2:
                return 2
            elif isam.verificar_Isam(database,table) == 3:
                return 3
            return 1
        elif currentMode == 'json':
            if j.verificar_Json(database,table) == 0:
                saveModo_bandera = not saveModo_bandera
                return 0
            elif j.verificar_Json(database,table) == 1:
                return 1
            elif j.verificar_Json(database,table) == 2:
                return 2
            elif j.verificar_Json(database,table) == 3:
                return 3
            return 1
        elif currentMode == 'hash':
            if Hash.verificar_Hash(database,table) == 0:
                saveModo_bandera = not saveModo_bandera
                return 0
            elif Hash.verificar_Hash(database,table) == 1:
                return 1
            elif Hash.verificar_Hash(database,table) == 2:
                return 2
            elif Hash.verificar_Hash(database,table) == 3:
                return 3
            return 1
    else:
        return 2


def safeModeOff(database, table):
    global saveModo_bandera
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            if avl.verificar_avl(database,table) == 0:
                
                saveModo_bandera = True
                return 0
            elif avl.verificar_avl(database,table) == 2:
                return 2
            elif avl.verificar_avl(database,table) == 1:
                return 1   
            return 1  
        elif currentMode == 'b':
            if b.verificar_B(database,table) == 0:
                saveModo_bandera = True
                return 0
            elif b.verificar_B(database,table) == 1:
                return 1
            return 1
        elif currentMode == 'bplus':
            if bplus.verificar_Bplus(database,table) == 0:
                saveModo_bandera = True
                return 0
            elif bplus.verificar_Bplus(database,table) == 1:
                return 1
            elif bplus.verificar_Bplus(database,table) == 2:
                return 2
            elif bplus.verificar_Bplus(database,table) == 3:
                return 3
            return 1
        elif currentMode == 'dict':
            if DM.verificar_DictMode(database,table) == 0:
                saveModo_bandera = True
                return 0
            elif DM.verificar_DictMode(database,table) == 1:
                return 1
            elif DM.verificar_DictMode(database,table) == 2:
                return 2
            elif DM.verificar_DictMode(database,table) == 3:
                return 3
        elif currentMode == 'isam':
            if isam.verificar_Isam(database,table)== 0:
                saveModo_bandera = True
                return 0
            elif isam.verificar_Isam(database,table) == 1:
                return 1
            elif isam.verificar_Isam(database,table) == 2:
                return 2
            elif isam.verificar_Isam(database,table) == 3:
                return 3
            return 1
        elif currentMode == 'json':
            if j.verificar_Json(database,table) == 0:
                saveModo_bandera = True
                return 0
            elif j.verificar_Json(database,table) == 1:
                return 1
            elif j.verificar_Json(database,table) == 2:
                return 2
            elif j.verificar_Json(database,table) == 3:
                return 3
            return 1
        elif currentMode == 'hash':
            if Hash.verificar_Hash(database,table) == 0:
                saveModo_bandera = True
                return 0
            elif Hash.verificar_Hash(database,table) == 1:
                return 1
            elif Hash.verificar_Hash(database,table) == 2:
                return 2
            elif Hash.verificar_Hash(database,table) == 3:
                return 3
            return 1
    else:
        return 2

def abrir_archivoImage():
    Block.abrir()

def modificarBloque(indice, registro):
    Block.modificar_cadena(indice,registro)

#---------metodo para validar saveModo---------------------
def validarSaveModo(database,table):
    global saveModo_bandera
    saveModo_bandera = not saveModo_bandera
    return saveModo_bandera

#----------------SEGURIDAD------------------------------------------------
#----------------CIFRADO--------------------------------------------------
def encrypt(backup: str, password: str) -> str:
    res_1 = E.encriptar_Backup(backup, password)
    return res_1

def decrypt(cipherBackup: str, password: str) -> str:
    res_2 = E.desencriptar_Backup(cipherBackup, password)
    return res_2