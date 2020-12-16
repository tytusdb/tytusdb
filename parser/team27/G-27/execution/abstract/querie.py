class Querie(object):
    def __init__(self,row,column):
        self.row = row
        self.column = column

    def execute(self, environment):
        raise NotImplementedError