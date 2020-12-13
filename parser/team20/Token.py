class Token:

    def __init__(self, type, data, row, column):
        self.type = type
        self.data = data
        self.row = row
        self.column = column