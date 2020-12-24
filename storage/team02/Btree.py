import os
class NodeBTree :
    def __init__(self) :
        self.gradeTree = 4
        self.maxKeys = self.gradeTree -1
        self.keys = []
        self.children = []
        self.parentNode = None
class Registro:
    def __init__(self,listRegister):
        self.register = listRegister
        self.idHide = 0

class BTree :
    
    def __init__(self):
        self.root = None
        self.identity = 0
        self.maxColumna = 0
        self.listRegister = []
        self.columPK = [0]
    def isTreeEmpty(self) :
        if self.root is None:
            return True
        else:
            return False
    
    def searchNodeToInsert(self,currentRegister,currentNode) :
        
        maxKeys = len(currentNode.keys)
        i = 0
        while i <  maxKeys and currentNode.keys[i].register[0] < currentRegister.register[0]:
            i += 1
        if i < maxKeys and currentNode.keys[i].register[0] == currentRegister.register[0]:
            return currentNode.keys[i].register
        if len(currentNode.children) == 0:
            return currentNode
        else: 
            return self.searchNodeToInsert(currentRegister,currentNode.children[i])
    
    def changeTypePK(self,currentRegister):
        if currentRegister.register[self.columPK[0]].isdigit():
            currentRegister.register[self.columPK[0]] = int(currentRegister.register[self.columPK[0]])

    def insertSorted(self,register,currentNode,childNode) :
        pivote = 0
        if len(currentNode.keys) == 0:
            currentNode.keys.append(register)
        else:
            # Encuentra la posicion del valor mayor a el
            while currentNode.keys[pivote].register[self.columPK[0]] < register.register[self.columPK[0]] :
                pivote += 1
                #desborda el indice
                if pivote > len(currentNode.keys) -1 :
                    break
            currentNode.keys.append(None)
            #desplaza una pos hacia adelante cada clave
            for i in range( len(currentNode.keys) -1, pivote-1 , -1 ):
                currentNode.keys[i] = currentNode.keys[i-1]
            if childNode is not None:
                currentNode.children.append(None)
                #desplaza una pos hacia adelante cada hijo
                for i in range( len(currentNode.children) -1, pivote , -1 ):
                    currentNode.children[i] = currentNode.children[i-1]
                #agrega un nuevo nodo en una pos ordenada del nodo padre
                currentNode.children[pivote+1] = childNode
            #agrega una nueva clave en una pos ordenada
            currentNode.keys[pivote] = register