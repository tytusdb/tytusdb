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
    