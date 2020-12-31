class Table(object):
    def __init__(self, name, columns, constraint):
        self.name = name
        self.columns = columns
        self.constraint = constraint
        self.alias = None
        self.herencia = None
    
    def createColumn(self, column):
        self.columns.append(column)
    
    def readColumn(self, name):
        for value in self.columns:
            if value.name == name:
                return value
        return None
    
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
    
    def deleteConstraint(self, name):
        i = 0
        exist = False
        for item in self.constraint:
            if item['type'] != 'check':
                if item['value'] == name:
                    del self.constraint[i]
                    exist = True
                    break
            i=i+1
        return exist

    def eliminar_Constraint(self, name):
        i = 0
        exist = False
        for item in self.constraint:
            if item['name'] == name:
                del self.constraint[i]
                exist = True
                break
            i=i+1
        return exist

    def readConstraint(self, name):
        for value in self.constraint:
            if value['name'] == name:
                return value
        return None
    
    def createConstraint(self, constr):
        self.constraint.append(constr)
