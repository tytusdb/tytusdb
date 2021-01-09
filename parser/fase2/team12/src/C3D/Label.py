class Label(object):    

    def __init__(self):
        self.labelActual = 1
    
    def getLabel(self):
        getLabelActual = '.L' + str(self.labelActual)
        self.labelActual += 1
        return getLabelActual

instanceLabel = Label()