from .storageManager.jsonMode import createDatabase
def executeCreateDatabase(self, database):
    # crear en base a la condicion
    if(database.ifexistsNotFlag):
        return createDatabase(database.name)#0 Created, 2 It exists, 1 not created
    else:
        if(createDatabase(database.name) == 0):
            return 0
    return 1
def executeCreateTable(self, database):
    return 0