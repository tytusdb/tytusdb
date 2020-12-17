import os


class IndexNode:
    def __init__(self):
        self.values = []
        self.left = None
        self.center = None
        self.right = None


class LeafNode:
    def __init__(self):
        self.values = []
        self.next = None


class Tuple:
    def __init__(self, PK, data):
        self.PK = PK
        self.data = data


class ISAM:
    def __init__(self):
        self.root = None
        
    # inserta un registro en la estructura ISAM
    def insert(self, data):
        self.root = self._insert(data, self.root, 0)

    def _insert(self, data, tmp, level):
        if tmp is None:
            if level < 2:
                node = IndexNode()
                node.values.append(data)
                return node
            elif level >= 2:
                node = LeafNode()
                node.values.append(data)
                return node
        else:
            if len(tmp.values) < 2:
                tmp.values.append(data)
                tmp.values = self.sort(tmp.values)
                return tmp
            else:
                if level < 2:
                    if level == 1:
                        if tmp.center is None:
                            tmp.center = self._insert(self.makeIndexLeaf(tmp.values[0]), tmp.center, level + 1)
                            tmp.values[0].data.clear()
                        if tmp.right is None:
                            tmp.right = self._insert(self.makeIndexLeaf(tmp.values[1]), tmp.right, level + 1)
                            tmp.values[1].data.clear()
                        if tmp.left is None:
                            if self.root.values[0].PK < data.PK < self.root.values[1].PK:
                                tmp.left = self._insert(self.makeIndexLeaf(self.root.values[0]), tmp.left, level + 1)
                                self.root.values[0].data.clear()
                            elif data.PK > self.root.values[1].PK:
                                tmp.left = self._insert(self.makeIndexLeaf(self.root.values[1]), tmp.left, level + 1)
                                self.root.values[1].data.clear()
                    if data.PK < tmp.values[0].PK:
                        tmp.left = self._insert(data, tmp.left, level + 1)
                    elif tmp.values[0].PK < data.PK < tmp.values[1].PK:
                        tmp.center = self._insert(data, tmp.center, level + 1)
                    elif tmp.values[1].PK < data.PK:
                        tmp.right = self._insert(data, tmp.right, level + 1)
                else:
                    tmp.next = self._insert(data, tmp.next, level + 1)
                return tmp
    
    # envia los valores de una pagina indice a una pagina hoja
    def makeIndexLeaf(self, register):
        newList = register.data[:]
        newPK = register.PK
        return Tuple(newPK, newList)
    
    # ordena los valores dentro de pagina
    def sort(self, array):
        aux = array
        for i in range(len(aux)):
            for j in range(len(aux)):
                if aux[i].PK < aux[j].PK:
                    temporal = aux[i]
                    aux[i] = aux[j]
                    aux[j] = temporal
        return aux
