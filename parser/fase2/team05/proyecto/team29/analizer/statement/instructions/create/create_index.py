from analizer.abstract import instruction
from analizer.typechecker import Checker
from analizer.typechecker.Metadata import Struct
from analizer.reports import Nodo
from storage.storageManager import jsonMode


class CreateIndex(instruction.Instruction):
    def __init__(self, unique, idIndex, idTable, usingHash, whereCl, optList=[]):
        self.unique = unique 
        self.idIndex = idIndex 
        self.idTable = idTable
        self.optList = optList
        self.whereCl = whereCl
        self.usingHash = usingHash
        

    def execute(self):
        #return self.dot()
        pass
    def dot(self):
        new = Nodo.Nodo("CREATE_INDEX")
        if self.unique:
            uniqueNode = Nodo.Nodo("UNIQUE")
            new.addNode(uniqueNode)
        if self.usingHash:
            uhNode = Nodo.Nodo("USING_HASH")
            new.addNode(uhNode)
        id1 = Nodo.Nodo(str(self.idIndex))
        id2 = Nodo.Nodo(str(self.idTable))
        new.addNode(id1)
        new.addNode(id2)

        listNode = Nodo.Nodo("INDEX_LIST")
        new.addNode(listNode)
        print(self.optList)
        for l in self.optList:
           
            if l[0] != None:
                l1 = Nodo.Nodo(str(l[0]))
                listNode.addNode(l1)
            if l[1] != None:
                l2 = Nodo.Nodo(str(l[1])) 
                listNode.addNode(l2)
            if l[2]:
                l3 = Nodo.Nodo("NULL")
                listNode.addNode(l3)
            if l[3] != None:
                l4 = Nodo.Nodo(str(l[3])) 
                listNode.addNode(l4)

        if self.whereCl != None:
            new.addNode(self.whereCl.dot())
        return new