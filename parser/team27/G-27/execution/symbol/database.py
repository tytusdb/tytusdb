class Database(object):
    def __init__(self, name):
        self.name = name
        self.tables = []
    
    def alterTable(self, name, newName):
        for value in self.tables:
            if value.name == name:
                value.name = name

    def deleteTable(self, name):
        for i in range(0,len(self.tables)):
            if(self.tables[i].name == name):
                del self.tables[i]
                break

    def getTable(self, name):
        for value in self.tables:
            if value.name == name:
                return value
        return None

    def addTable(self, table):
        self.tables.append(table) 
    
    def setName(self,name):
        self.name = name