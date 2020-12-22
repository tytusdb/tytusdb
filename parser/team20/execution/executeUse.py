from .storageManager import jsonMode
from .storageManager.TypeChecker import TCsetDatabase,TCSearchDatabase

def executeUse(self,database):
    
    res=TCSearchDatabase(database.name)
    if(res!= 8):
        return TCsetDatabase(database.name)
    else:
        return 1