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
    
    # metodo para eliminar un nodo
    def delete(self, valor):
        self.__delete(valor, self.root, self.root)

    def __delete(self, value, auxiliar, padre):
        if auxiliar is None:
            return 1
        else:
            if isinstance(auxiliar, LeafNode):
                validando = False
                tmp = None
                for i in auxiliar.values:
                    if i.PK == value:
                        validando = True
                        tmp = auxiliar
                        tmp1 = i
                        break
                    else:
                        validando = False
                if validando:
                    auxiliar.values.remove(tmp1)
                    if len(auxiliar.values) == 0:
                        if isinstance(padre, IndexNode):
                            if auxiliar.next is None:
                                if padre.left == tmp:
                                    padre.left = None
                                elif padre.center == tmp:
                                    padre.center = None
                                elif padre.right == tmp:
                                    padre.right = None
                            else:
                                if padre.left == tmp:
                                    padre.left = auxiliar.next
                                elif padre.center == tmp:
                                    padre.center = auxiliar.next
                                elif padre.right == tmp:
                                    padre.right = auxiliar.next
                        elif isinstance(padre, LeafNode):
                            if auxiliar.next is None:
                                padre.next = None
                            else:
                                temporal1 = auxiliar.next
                                padre.next = temporal1
                    return 0
                else:
                    self.__delete(value, auxiliar.next, auxiliar)
            else:
                validando = False
                tmp = None
                for i in auxiliar.values:
                    if i.PK == value:
                        validando = True
                        tmp = auxiliar
                        tmp1 = i
                        break
                    else:
                        validando = False
                if validando and len(tmp1.data) > 0:
                    tmp1.data.clear()
                else:
                    if len(auxiliar.values) >1:
                        if value < auxiliar.values[0].PK:
                            self.__delete(value, auxiliar.left, auxiliar)
                        elif auxiliar.values[0].PK <= value < auxiliar.values[1].PK:
                            self.__delete(value, auxiliar.center, auxiliar)
                        else:
                            self.__delete(value, auxiliar.right, auxiliar)

# graficar la estructura
    def chart(self):
        file = open('isam.dot', 'w')
        file.write('digraph isam {\n')
        file.write('rankdir=TD;\n')
        file.write('node[shape=box]\n')
        file.close()
        self._chart(self.root, 0)
        file = open('isam.dot', "a")
        file.write('}')
        file.close()
        os.system("dot -Tpng isam.dot -o isam.png")
        os.system("isam.png")

    def _chart(self, tmp, level):
        if tmp:
            file = open('isam.dot', 'a')
            tail = ''
            for i in tmp.values:
                tail += i.PK + ', '
            if level < 2:
                if tmp.left is not None:
                    leftHead = ''
                    for i in tmp.left.values:
                        leftHead += i.PK + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(leftHead)[:-2] + '" \n')
                if tmp.center is not None:
                    centerHead = ''
                    for i in tmp.center.values:
                        centerHead += i.PK + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(centerHead)[:-2] + '" \n')
                if tmp.right is not None:
                    rightHead = ''
                    for i in tmp.right.values:
                        rightHead += i.PK + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(rightHead)[:-2] + '" \n')
                file.close()
                self._chart(tmp.left, level + 1)
                self._chart(tmp.center, level + 1)
                self._chart(tmp.right, level + 1)
            else:
                if tmp.next is not None:
                    nextHead = ''
                    for i in tmp.next.values:
                        nextHead += i.PK + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(nextHead)[:-2] + '" \n')
                file.close()
                self._chart(tmp.next, level + 1)
