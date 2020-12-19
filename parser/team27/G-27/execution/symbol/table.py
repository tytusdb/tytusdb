class Table(object):
    def __init__(self, name, columns, constraint):
        self.name = name
        self.columns = columns
        self.constraint = constraint
    
    def createColumn(self, column):
        self.columns.append(column)
    
    def readColumn(self, name):
        for value in self.columns:
            if value.name == name:
                return value
    
    def updateColumn(self, name, column):
        for i in range(0,len(self.columns)):
            if self.columns[i].name == name:
                self.columns[i] = column
                break
    
    def deleteColumn(self, name):
        for i in range(0, len(self.columns)):
            if self.columns[i].name == name:
                del self.columns[i]
                break
