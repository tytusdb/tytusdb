from .storageManager import jsonMode
from .storageManager.TypeChecker import TCsetDatabase,TCSearchDatabase

def executeUse(self,database):
    
    res=TCSearchDatabase(database.name)
    if(res!= 8):
        return TCsetDatabase(database.name)
    else:
        return 1

#Si se realiza un alter database rename, cambiar nombre en use
def executeUseAlter(self,name):
    
    res=TCSearchDatabase(name)
    if(res!= 8):
        return TCsetDatabase(name)
    else:
        return 1