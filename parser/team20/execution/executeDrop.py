from .storageManager.jsonMode import dropDatabase,dropTable,dropAll

def executeDropDatabase(self,database):
    if(database.ifExistsFlag):
        return dropDatabase(database.name)
    else:
        return dropDatabase(database.name)

#def executeDropTable(self,):