from .storageManager.jsonMode import createDatabase
from .storageManager.TypeChecker import TCcreateDatabase,TCSearchDatabase,TCdropDatabase

def executeCreateDatabase(self, database):
    # crear en base a la condicion FALTA AGREGAR REPLACE Y OWNERMODE
    if(database.ifNotExistsFlag and not(database.OrReplace)):
        return createDatabase(database.name)
    elif(database.ifNotExistsFlag and database.OrReplace):
        res=TCSearchDatabase(database.name)
        if(res==1):
            TCdropDatabase(database.name)
            dropDatabase(database.name)
            return createDatabase(database.name)
        else:
            return createDatabase(database.name)

    elif(not(database.ifNotExistsFlag) and not(database.OrReplace)):
        return createDatabase(database.name)#0 Created, 2 It exists, 1 not created
    else:
        res=TCSearchDatabase(database.name)
        if(res==1):
            TCdropDatabase(database.name)
            dropDatabase(database.name)
            return createDatabase(database.name)
        else:
            return createDatabase(database.name)
    return 1
def executeCreateTable(self, database):
    return 0