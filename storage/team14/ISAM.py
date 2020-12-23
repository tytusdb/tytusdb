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
        duplicated = []
        self.root = self._insert(data, self.root, 0, duplicated)
        return duplicated

    def _insert(self, data, tmp, level, duplicated):
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
                if tmp.values[0].PK == data.PK and len(tmp.values[0].data) > 0:
                    duplicated.append(data)
                    return tmp
                elif tmp.values[0].PK == data.PK and len(tmp.values[0].data) == 0:
                    tmp.values[0].data = data.data
                    tmp.values[0].PK = data.PK
                    return tmp
                else:
                    tmp.values.append(data)
                    tmp.values = self.sort(tmp.values)
                    return tmp
            else:
                for i in tmp.values:
                    if i.PK == data.PK and len(self.search(data.PK)) == 0:
                        i.data = data.data
                        i.PK = data.PK
                        return tmp
                    elif i.PK == data.PK:
                        duplicated.append(data)
                        return tmp
                if level < 2:
                    if level == 1:
                        if tmp.center is None:
                            tmp.center = self._insert(self.makeIndexLeaf(tmp.values[0]), tmp.center, level + 1,
                                                      duplicated)
                            tmp.values[0].data.clear()
                        if tmp.right is None:
                            tmp.right = self._insert(self.makeIndexLeaf(tmp.values[1]), tmp.right, level + 1,
                                                     duplicated)
                            tmp.values[1].data.clear()
                        if tmp.left is None:
                            if self.root.values[0].PK < data.PK < self.root.values[1].PK:
                                tmp.left = self._insert(self.makeIndexLeaf(self.root.values[0]), tmp.left, level + 1,
                                                        duplicated)
                                self.root.values[0].data.clear()
                            elif data.PK > self.root.values[1].PK:
                                tmp.left = self._insert(self.makeIndexLeaf(self.root.values[1]), tmp.left, level + 1,
                                                        duplicated)
                                self.root.values[1].data.clear()
                    if data.PK < tmp.values[0].PK:
                        tmp.left = self._insert(data, tmp.left, level + 1, duplicated)
                    elif tmp.values[0].PK < data.PK < tmp.values[1].PK:
                        tmp.center = self._insert(data, tmp.center, level + 1, duplicated)
                    elif tmp.values[1].PK < data.PK:
                        tmp.right = self._insert(data, tmp.right, level + 1, duplicated)
                else:
                    isTwice = False
                    for i in tmp.values:
                        if i.PK == data.PK:
                            duplicated.append(data)
                            isTwice = True
                    if not isTwice:
                        tmp.next = self._insert(data, tmp.next, level + 1, duplicated)
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
        return self.__delete(valor, self.root, self.root)

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
                    return self.__delete(value, auxiliar.next, auxiliar)
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
                    return 0
                else:
                    if len(auxiliar.values) > 1:
                        if value < auxiliar.values[0].PK:
                            return self.__delete(value, auxiliar.left, auxiliar)
                        elif auxiliar.values[0].PK <= value < auxiliar.values[1].PK:
                            return self.__delete(value, auxiliar.center, auxiliar)
                        else:
                            return self.__delete(value, auxiliar.right, auxiliar)
                    else:
                        return 1

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

    def _chart(self, tmp, level):
        if tmp:
            file = open('isam.dot', 'a')
            tail = ''
            for i in tmp.values:
                tail += str(i.PK) + ', '
            if level < 2:
                if tmp.left is not None:
                    leftHead = ''
                    for i in tmp.left.values:
                        leftHead += str(i.PK) + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(leftHead)[:-2] + '" \n')
                if tmp.center is not None:
                    centerHead = ''
                    for i in tmp.center.values:
                        centerHead += str(i.PK) + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(centerHead)[:-2] + '" \n')
                if tmp.right is not None:
                    rightHead = ''
                    for i in tmp.right.values:
                        rightHead += str(i.PK) + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(rightHead)[:-2] + '" \n')
                if tmp.left is None and tmp.right is None and tmp.center is None and level == 0:
                    head = ''
                    for i in tmp.values:
                        head += i.PK + ', '
                    head = head[:-2]
                    file.write(' " ' + head + '"' + '[shape=box] \n')
                file.close()
                self._chart(tmp.left, level + 1)
                self._chart(tmp.center, level + 1)
                self._chart(tmp.right, level + 1)
            else:
                if tmp.next is not None:
                    nextHead = ''
                    for i in tmp.next.values:
                        nextHead += str(i.PK) + ', '
                    file.write('"' + str(tail)[:-2] + '" -> "' + str(nextHead)[:-2] + '" \n')
                file.close()
                self._chart(tmp.next, level + 1)
    
    #Metodo que busca el valor especificado
    def search(self, value):
        return self._search(value, self.root, 0)

    def _search(self, value, tmp, level):
        if tmp:
            if level < 2:
                for i in tmp.values:
                    if i.PK == value and len(i.data) > 0:
                        return i.data
                if value < tmp.values[0].PK:
                    return self._search(value, tmp.left, level + 1)
                elif len(tmp.values) > 1:
                    if tmp.values[0].PK <= value < tmp.values[1].PK:
                        return self._search(value, tmp.center, level + 1)
                    elif value >= tmp.values[1].PK:
                        return self._search(value, tmp.right, level + 1)
            else:
                for i in tmp.values:
                    if i.PK == value and len(i.data) > 0:
                        return i.data
                return self._search(value, tmp.next, level + 1)
        else:
            return []
       
    # extrae todos los registros de una estructura ISAM y los devuelve en una lista
    def extractAll(self):
        tuples = []
        self._extractAll(self.root, 0, tuples)
        return tuples

    def _extractAll(self, tmp, level, tuples):
        if tmp:
            if level < 2:
                self._extractAll(tmp.left, level + 1, tuples)
                for i in tmp.values:
                    if len(i.data) > 0:
                        tuples.append(i.data)
                self._extractAll(tmp.center, level + 1, tuples)
                self._extractAll(tmp.right, level + 1, tuples)
            else:
                for i in tmp.values:
                    if len(i.data) > 0:
                        tuples.append(i.data)
                self._extractAll(tmp.next, level + 1, tuples)
    
    #Metodo que extrae informacion entre los limites especificados
    def extractRange(self, lower, upper, column):
        tuples = []
        self._extractRange(self.root, column, upper, lower, 0, tuples)
        return tuples

    def _extractRange(self, tmp, column, upper, lower, level, tuples):
        if tmp:
            if level < 2:
                self._extractRange(tmp.left, column, upper, lower, level + 1, tuples)
                for i in tmp.values:
                    if len(i.data) > 0 and lower <= i.data[column] <= upper:
                        tuples.append(i.data)
                self._extractRange(tmp.center, column, upper, lower, level + 1, tuples)
                self._extractRange(tmp.right, column, upper, lower, level + 1, tuples)
            else:
                for i in tmp.values:
                    if len(i.data) > 0 and lower <= i.data[column] <= upper:
                        tuples.append(i.data)
                self._extractRange(tmp.next, column, upper, lower, level + 1, tuples)
                
    # extrae todos los objetos almacenados en ISAM
    def extractAllObject(self):
        tuples = []
        self._extractAllObject(self.root, 0, tuples)
        return tuples

    def _extractAllObject(self, tmp, level, tuples):
        if tmp:
            if level < 2:
                self._extractAllObject(tmp.left, level + 1, tuples)
                for i in tmp.values:
                    if len(i.data) > 0:
                        tuples.append(i)
                self._extractAllObject(tmp.center, level + 1, tuples)
                self._extractAllObject(tmp.right, level + 1, tuples)
            else:
                for i in tmp.values:
                    if len(i.data) > 0:
                        tuples.append(i)
                self._extractAllObject(tmp.next, level + 1, tuples)

    # define una nueva PK
    def newPK(self, PKs):
        self._newPK(self.root,0, PKs)

    def _newPK(self, tmp, level, PKs):
        if tmp:
            for i in tmp.values:
                newPK = ''
                for j in PKs:
                    if j == PKs[len(PKs) - 1]:
                        if len(i.data) > 0:
                            newPK = newPK + str(i.data[j])
                    else:
                        if len(i.data) > 0:
                            newPK = newPK + str(i.data[j])+ '_'
                i.PK = newPK
            if level < 2:
                self._newPK(tmp.left, level + 1, PKs)
                self._newPK(tmp.center, level + 1, PKs)
                self._newPK(tmp.right, level + 1, PKs)
            else:
                self._newPK(tmp.next, level + 1, PKs)
                
    def update(self, register, cols, PKCols):
        lists = ''
        for ip in cols:
            lists += str(ip) + '_'
        lists = lists[:-1]
        return self.__update(register, self.root, lists, PKCols)

    def __update(self, register, auxiliar, cols, PKCols):
        if auxiliar is None:
            return 1
        else:
            if isinstance(auxiliar, LeafNode):
                validando = False
                tmp1 = None
                for i in auxiliar.values:
                    if i.PK == cols:
                        validando = True
                        tmp = auxiliar
                        tmp1 = i
                        break
                    else:
                        validando = False
                if validando:
                    aux = Tuple(tmp1.PK, tmp1.data[:])
                    aux2 = Tuple(tmp1.PK, tmp1.data[:])
                    x = register.keys()
                    for i in x:
                        aux.data[i] = register[i]
                    new_PK = ''
                    if isinstance(PKCols, list):
                        for i in PKCols:
                            new_PK += str(aux.data[i]) + '_'
                        new_PK = new_PK[:-1]
                    else:
                        new_PK = str(PKCols)
                    self.delete(tmp1.PK)
                    if len(self.insert(Tuple(new_PK, aux.data))) == 0:
                        return 0
                    else:
                        self.insert(Tuple(aux2.PK, aux2.data))
                        return 2
                else:
                    return self.__update(register, auxiliar.next, cols, PKCols)
            else:
                validando = False
                tmp1 = None
                lists = ''
                for ip in cols:
                    lists += ip
                for i in auxiliar.values:
                    if i.PK == lists:
                        validando = True
                        tmp = auxiliar
                        tmp1 = i
                        break
                    else:
                        validando = False
                if validando and len(tmp1.data) > 0:
                    aux = Tuple(tmp1.PK, tmp1.data[:])
                    aux2 = Tuple(tmp1.PK, tmp1.data[:])
                    x = register.keys()
                    for i in x:
                        aux.data[i] = register[i]
                    new_PK = ''
                    if isinstance(PKCols, list):
                        for i in PKCols:
                            new_PK += str(aux.data[i]) + '_'
                        new_PK = new_PK[:-1]
                    else:
                        new_PK = str(PKCols)
                    self.delete(tmp1.PK)
                    if len(self.insert(Tuple(new_PK, aux.data))) == 0:
                        return 0
                    else:
                        self.insert(Tuple(aux2.PK, aux2.data))
                        return 2
                else:
                    if len(auxiliar.values) > 1:
                        if cols < auxiliar.values[0].PK:
                            return self.__update(register, auxiliar.left, cols, PKCols)
                        elif auxiliar.values[0].PK <= cols < auxiliar.values[1].PK:
                            return self.__update(register, auxiliar.center, cols, PKCols)
                        else:
                            return self.__update(register, auxiliar.right, cols, PKCols)
                    else:
                        return 1
                    
    # agrega un dato a cada uno de los registros de la estructura ISAM
    def addAtEnd(self, default):
        self._addAtEnd(self.root, default, 0)

    def _addAtEnd(self, tmp, default, level):
        if tmp:
            if level < 2:
                self._addAtEnd(tmp.left, default, level + 1)
                for i in tmp.values:
                    if len(i.data) > 0:
                        i.data.append(default)
                self._addAtEnd(tmp.center, default, level + 1)
                self._addAtEnd(tmp.right, default, level + 1)
            else:
                for i in tmp.values:
                    if len(i.data) > 0:
                        i.data.append(default)
                self._addAtEnd(tmp.next, default, level + 1)

    # elimina un dato de todos los registros de la estructura ISAM
    def deleteColumn(self, n):
        self._deleteColumn(self.root, 0, n)

    def _deleteColumn(self, tmp, level, n):
        if tmp:
            if level < 2:
                for i in tmp.values:
                    if len(i.data) > 0:
                        i.data.pop(n)
                self._deleteColumn(tmp.left, level + 1, n)
                self._deleteColumn(tmp.center, level + 1, n)
                self._deleteColumn(tmp.right, level + 1, n)
            else:
                for i in tmp.values:
                    if len(i.data) > 0:
                        i.data.pop(n)
                self._deleteColumn(tmp.next, level + 1, n)
                
    # elimina todos los nodos de la estrucutura ISAM
    def truncate(self):
        self.root = None
