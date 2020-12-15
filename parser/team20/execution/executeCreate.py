from .storageManager.jsonMode import createDatabase,showDatabases
def executeCreateDatabase(self, database):
    # crear en base a la condicion FALTA AGREGAR REPLACE Y OWNERMODE
    if(database.ifNotExistsFlag):
        return createDatabase(database.name)#0 Created, 2 It exists, 1 not created
    else:
        if(createDatabase(database.name) == 0):
            return 0
    return 1
def executeCreateTable(self, database):
    return 0
def executeShowDatabases(self):
    print(showDatabases())