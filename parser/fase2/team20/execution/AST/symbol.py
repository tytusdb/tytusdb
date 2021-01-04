  
class Symbol():

    def __init__(self,id,type,value,row,column):
        self.id = id
        self.type = type
        self.value = value
        self.row = row
        self.column = column
        self.op = ''
        self.references = []