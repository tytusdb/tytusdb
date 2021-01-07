class Goto_Label(object):
    def __init__(self, label):
        self.label = label

    def execute(self):
        return { 'goto': self.label }