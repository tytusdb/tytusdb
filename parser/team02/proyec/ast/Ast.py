class Ast:
    def __init__(self,sentencias):
        self.labels = []
        self.sentencias = sentencias

    def exist_label(self,id):
        for label in self.labels:
            comparacion = label.id == id.id
            if(comparacion):
                return True
        return False

    def nextlabel(self,nombre):
        x = 0
        for label in self.labels:
            if(label.id):
                if(label.id == nombre):
                    if(len(self.labels) > (x+1)):
                     return self.labels[x+1]
                x = x +1

        return None

    def agregarlabel(self,label):
        self.labels.append(label)

    def getlabel(self,nombre):
        for label in self.labels:
            if(label.id == nombre):
                return label

        return None

    def getlabels(self):
        return self.labels
