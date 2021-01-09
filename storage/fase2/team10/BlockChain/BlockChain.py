import random
import time
import string
import json as Json

class Node:
    def _init_(self, previousKey, value):
        self.previousKey = previousKey
        self.value = value
        self.nextKey = self.generateKey(value)
        self.trust = True

    def generateKey(self, value):
        chars = ''.join(random.sample(string.ascii_letters, 15))
        return chars + str(len(value)) + str(time.strftime("%j")) + str(random.choice(string.ascii_letters)) + str(random.randint(0, 100)) + time.strftime("%M") + time.strftime("%S") + str(value[0])

    def getPreviousKey(self):
        return self.previousKey

    def setPreviousKey(self, key):
        self.previousKey = key

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value
        self.nextKey = self.generateKey(value)

    def getNextKey(self):
        return self.nextKey  

    def setNextKey(self, key):
        self.nextKey = key  

    def getStatus(self):
        return self.trust

    def setStatus(self, status):
        self.trust = status
   
class BlockChain:
    
    def _init_(self, name):
        self.listNodes = []
        self.secureMode = False
        self.name = name

    def getName(self):
        return self.name
    
    def getListValues(self):
        values = []
        for i in self.listNodes:
            values.append(i.getValue())
        return values

    def getListNodes(self):
        return self.listNodes
    
    def setName(self, name):
        self.name = name

    def enabledSafeMode(self):
        self.secureMode = True
    
    def disabledSafeMode(self):
        self.secureMode = False

    def getStatusSafeMode(self):
        return self.secureMode

    def addNode(self, value):
        if len(self.listNodes) == 0:
            node = Node(None, value)
            self.listNodes.append(node)
        else:
            if len(self.listNodes) > 1:
                previousNode = self.listNodes[len(self.listNodes) - 1]
            else:
                previousNode = self.listNodes[0]
            node = Node(previousNode.getNextKey(), value)
            self.listNodes.append(node)

    def addNodeNoSecure(self, value):
        if len(self.listNodes) == 0:
            node = Node(None, value)
            self.listNodes.append(node)
        else:
            if len(self.listNodes) > 1:
                previousNode = self.listNodes[len(self.listNodes) - 1]
            else:
                previousNode = self.listNodes[0]
            node = Node(previousNode.generateKey(value), value)
            self.listNodes.append(node)

    def alterValueNode(self, value, index):
        self.listNodes[index].setValue(value)
        if self.secureMode and (index < (len(self.listNodes) - 1)):
            self.listNodes[index + 1].setPreviousKey(self.listNodes[index].getNextKey())
        
    def printList(self):
        for i in self.listNodes:
            print("_______Node_______")
            print("LLAVE ANTERIOR:")
            print(i.getPreviousKey())
            print("VALOR:")
            print(i.getValue())
            print("SIGUIENTE LLAVE:")
            print(i.getNextKey())

    def generateGraph(self): 
        graph = "digraph G{\n"
        graph += "rankdir=LR;"
        graph += "node [shape=box, style=filled, color=\"green\"];\n"
        i = 0
        while i < (len(self.listNodes) - 1):
            if self.listNodes[i].getNextKey() != self.listNodes[i+1].getPreviousKey():
                graph += "\""
                graph += str(self.listNodes[i+1].getValue())
                graph += "\""
                graph += " [color=\"red\"]\n"
            graph += "\""
            graph += str(self.listNodes[i].getValue())
            graph += "\""
            graph += "->"
            graph += "\""
            graph += str(self.listNodes[i+1].getValue())
            graph += "\""
            graph += ";\n"
            i += 1
        graph += "}\n"
        return graph
        
    def generateJsonSafeMode(self):
        try:
            data = {}
            data[self.name] = []
            for node in self.listNodes:
                data[self.name].append(
                    {
                        "PreviousKey": node.getPreviousKey(),
                        "Tuple" : node.getValue(),
                        "NextKey": node.getNextKey()
                    }
                )
            with open('BlockChain\\'+str(self.name)+'.json', 'w') as file:
                Json.dump(data, file, indent=4)
        except Exception as e:
            print("Error al generar JSON")
            print(e)
