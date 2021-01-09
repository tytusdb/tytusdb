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
    