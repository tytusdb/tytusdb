class Label(object):
    def __init__(self,label):
        self.label = label

    def execute(self):
        return {'label': self.label}