class Goto_Label(object):
    def __init__(self, label):
        self.label = label

    def execute(self):
        return { 'goto': self.label }

    def toString(self,tab):
        return '\t'*tab + 'goto .' + self.label

    def getGoto(self):
        return self.label
    def setGoto(self,label):
        self.label = label