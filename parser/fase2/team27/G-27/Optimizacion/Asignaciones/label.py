class Label(object):
    def __init__(self,label):
        self.label = label

    def execute(self):
        return {'label': self.label}
    
    def toString(self,tab):
        return '\t'*tab + 'label .' + self.label 
    
    def getLabel(self):
        return self.label