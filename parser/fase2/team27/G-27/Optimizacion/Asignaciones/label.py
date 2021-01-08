class Label(object):
    def __init__(self,label):
        self.label = label

    def execute(self):
        return {'label': self.label}
    
    def toString(self,tab):
        return '\t'*tab + 'Label .' + self.label 
    
    def getLabel(self):
        return self.label