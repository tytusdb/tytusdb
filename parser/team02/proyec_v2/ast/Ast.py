class Ast:
    def __init__(self,sentencias):
        self.labels = []
        self.sentencias = sentencias
        self.nodos = []

    def exist_label(self,id):
        for label in self.labels:
            #print("ava a comparar  ",label.id," con ",id.id)

            comparaciontype =True
            comparacion =True

            try:
               
                if(label.id == id.id):
                      comparacion=False
                
            except:
                pass
            try:
               
                if(label.type == label.type):
                      comparaciontype=False
                
            except:
                pass

            if(comparacion and comparaciontype):
                #print("k ")
                return True
            #print("y ")

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
        print("va a append  ")
        print(label)

        self.labels.append(label)

    def getlabel(self,nombre):
        for label in self.labels:
            if(label.id == nombre):
                return label

        return None

    def getlabels(self):
        return self.labels

    def agregarnodos(self,label):        
        self.nodos.append(label)

    def getnodos(self):
        return self.nodos
