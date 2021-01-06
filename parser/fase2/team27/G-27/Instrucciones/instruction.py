class Instruccion(object):
    def __init__(self,row,column):
        self.row = row
        self.column = column

    def Traduct(self):
        raise NotImplementedError