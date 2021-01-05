class Error():

    def __init__(self, type, detail, row, column):
        self.type = type
        self.detail = detail
        self.row = row
        self.column = column

    def toString(self):
        return str(self.type) + "Error : " + self.detail + ". In row  " + str(self.row) + ", column " + str(self.column)
