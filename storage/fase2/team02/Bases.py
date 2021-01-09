from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.DictMode import DictMode as DM
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as j
from storage.Hash import HashMode as Hash
import zlib
# from storage.HashWindows import HashMode as Hash

currentMode,avlList,bList,bplusList,dictList,jsonList,isamList,hashList = [],[],[],[],[],[],[],[]
comp = []
compT,decompT = [],[]
decomp = []

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