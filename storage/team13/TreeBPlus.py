class TreeBPlus:
    
    def __init__(self, grade):
        if grade < 3:
            self.__grade = 3
        else:
            self.__grade = grade

        self.__root = None
    
    def get_root(self):
        return self.__root

    def add(self, key):
        if self.__root is None:
            self.__root = PageTBPlus(self.__grade)
            self.__root.add_key(NodeTBPlus(key))
        else:
            self.__root = self.__root.add_key(NodeTBPlus(key))
            
    def search(self, key):
        if self.__root is not None:
            return self.__root.search(key).value
    
    def printTree(self):
        return self.__root.callPage()
    
    # Print tree
    def showTree(self):
        self._showTree(self.__root, 0)

    def _showTree(self, tmp, level):
        print("Level", level, ": ", end="")
        tmp.showKeys()
        if not (len(tmp.get_chlds()) == 0):
            for i in range(len(tmp.get_chlds())):
                self._showTree(tmp.get_chlds()[i], level + 1)

    # graph tree
    def graphTree(self):
        if self.__root is not None:
            graph = 'digraph G{\n'
            graph += "node[shape = \"record\"]\n"
            graph += self._graphTree(self.__root, 0)
            graph += "{rank=same;\n"
            graph += self._rankLeaves(self.__root)
            graph += "}"
            graph += '}'
            file = open("ArbolB+.dot", "w")
            file.write(graph)
            file.close()
            os.system('dot -Tpng ArbolB+.dot -o ArbolB+.png')
        else:
            print("No hay Tuplas")

    def _graphTree(self, tmp, level):
        cadena = ""
        cadena += tmp.graphKeys(tmp, level)
        if not (len(tmp.get_chlds()) == 0):
            for i in range(len(tmp.get_chlds())):
                cadena += self._graphTree(tmp.get_chlds()[i], level + 1)
        return cadena
                
    # Rank = same to the nodes (leaves)
    def _rankLeaves(self, tmp):
        cadena = ""
        cadena += tmp.rankLeavesKeys(tmp)
        return cadena

class PageTBPlus:
    
    def __init__(self, grade):
        if grade < 3:
            self.__grade = 3
        else:
            self.__grade = grade

        self.__keys = []
        self.__childs = []
        self.__father = None
        self.__next = None
        self.__previous = None

    def get_keys(self):
        return self.__keys
    
    def get_chlds(self):
        return self.__childs
    
    def get_father(self):
        return self.__father
    
    def get_grade(self):
        return self.__grade
    
    def get_next(self):
        return self.__next
    
    def get_previous(self):
        return self.__previous
    
    def set_keys(self, keys):
        self.__keys = keys
    
    def set_chlds(self, childs):
        self.__childs = childs
    
    def set_father(self, father):
        self.__father = father
    
    def set_grade(self, grade):
        self.__grade = grade
    
    def set_next(self, next):
        self.__next = next
    
    def set_previous(self, previous):
        self.__previous = previous

    def add_chld(self, chld):
        self.__childs.append(chld)
    
    def add_key(self, key):
        if len(self.__keys) == 0:
            self.__keys.append(key)
            return self
        else:
            if len(self.__childs) == 0:
                self.sort(key)
                if len(self.__keys) == (self.__grade):
                    return self.SplitPage()
                return self
            else:
                i = 0
                if key.value < self.__keys[i].value:
                    aux = self.__childs[i].add_key(key)
                    if type(aux) is list:
                        self.__childs.pop(i)
                        for x in range(len(aux) - 1):
                            self.__childs.insert((i + x), aux[x])
                        if len(self.__keys) < self.__grade:
                            self.sort(aux[len(aux) - 1])
                            if len(self.__keys) == (self.__grade):
                                return self.SplitPage()
                            return self
                        else:
                            self.add_key(aux[len(aux) - 1])
                    else:
                        self.__childs[i] = aux
                    return self

                elif (self.__keys[i].value < key.value) and (len(self.__keys) == 1):
                    aux = self.__childs[i + 1].add_key(key)
                    if type(aux) is list:
                        self.__childs.pop(i + 1)
                        for x in range(len(aux) - 1):
                            self.__childs.append(aux[x])
                        if len(self.__keys) < self.__grade:
                            self.sort(aux[len(aux) - 1])
                            if len(self.__keys) == (self.__grade):
                                return self.SplitPage()
                            return self
                        else:
                            self.add_key(aux[len(aux) - 1])
                    else:
                        self.__childs[i + 1] = aux
                    return self

                while i < (len(self.__keys) - 1):
                    if (self.__keys[i].value < key.value) and (key.value < self.__keys[i + 1].value):
                        aux = self.__childs[i + 1].add_key(key)
                        if type(aux) is list:
                            self.__childs.pop(i + 1)
                            for x in range(len(aux) - 1):
                                self.__childs.insert((i + 1) + x, aux[x])
                            if len(self.__keys) < self.__grade:
                                self.sort(aux[len(aux) - 1])
                                if len(self.__keys) == (self.__grade):
                                    return self.SplitPage()
                                return self
                            else:
                                self.add_key(aux[len(aux) - 1])
                        else:
                            self.__childs[i + 1] = aux
                        return self
                    i += 1
                    
                i += 1
                if self.__keys[i - 1].value < key.value:
                    aux = self.__childs[i].add_key(key)
                    if type(aux) is list:
                        self.__childs.pop(i)
                        for x in range(len(aux) - 1):
                            self.__childs.insert((i + x), aux[x])
                        if len(self.__keys) < self.__grade:
                            self.sort(aux[len(aux) - 1])
                            if len(self.__keys) == (self.__grade):
                                return self.SplitPage()
                            return self
                        else:
                            self.add_key(aux[len(aux) - 1])
                    else:
                        self.__childs[i] = aux
                    return self

    def SplitPage(self):
        if (self.__grade % 2) > 0:
            index = int((self.__grade - 1) /2)
        else:
            index = int(self.__grade / 2)
        
        chld1 = PageTBPlus(self.__grade)
        chld2 = PageTBPlus(self.__grade)

        if (self.__father is None) and (len(self.__childs) == 0):
            temp = PageTBPlus(self.__grade)
            temp.add_key(self.__keys[index])

            for i in range(len(self.__keys)):
                if i < index:
                    chld1.__keys.append(self.__keys[i])
                else:
                    chld2.__keys.append(self.__keys[i])

            temp.add_chld(chld1)
            temp.add_chld(chld2)
            chld1.set_father(temp)
            chld2.set_father(temp)
            temp.set_father(self.get_father())
            auxiliar = self.get_previous()
            if auxiliar is not None: 
                auxiliar.set_next(chld1)
            chld1.set_previous(auxiliar)
            chld1.set_next(chld2)
            chld2.set_previous(chld1)
            chld2.set_next(self.get_next())
            if self.get_next() is not None:
                self.get_next().set_previous(chld2)
            return temp

        elif len(self.__childs) == 0:
            for i in range(len(self.__keys)):
                if i < index:
                    chld1.__keys.append(self.__keys[i])
                else:
                    chld2.__keys.append(self.__keys[i])

            chld1.set_father(self.get_father())
            chld2.set_father(self.get_father())
            auxiliar = self.get_previous()
            if auxiliar is not None: 
                auxiliar.set_next(chld1)
            chld1.set_previous(auxiliar)
            chld1.set_next(chld2)
            chld2.set_previous(chld1)
            chld2.set_next(self.get_next())
            if self.get_next() is not None:
                self.get_next().set_previous(chld2)
            temp = []
            temp.extend([chld1, chld2, self.__keys[index]])
            return temp
        else:
            if self.get_father() is not None:
                if len(self.get_father().get_keys()) < self.__grade:
                    for i in range(len(self.__keys)):
                        if i < index:
                            chld1.__keys.append(self.__keys[i])
                        elif i > index:
                            chld2.__keys.append(self.__keys[i])

                    for i in range(len(self.__childs)):
                        aux = self.__childs[i]
                        if i <= index:
                            chld1.add_chld(aux)
                            aux.set_father(chld1)
                        else:
                            chld2.add_chld(aux)
                            aux.set_father(chld2)
                    
                    chld1.set_father(self.get_father())
                    chld2.set_father(self.get_father())
                    temp = []
                    temp.extend([chld1, chld2, self.__keys[index]])
                    return temp
            else:
                temp = PageTBPlus(self.__grade)
                temp.add_key(self.__keys[index])

                for i in range(len(self.__keys)):
                    if i < index:
                        chld1.__keys.append(self.__keys[i])
                    elif i > index:
                        chld2.__keys.append(self.__keys[i])

                for i in range(len(self.__childs)):
                    aux = self.__childs[i]
                    if i <= index:
                        chld1.add_chld(aux)
                        aux.set_father(chld1)
                    else:
                        chld2.add_chld(aux)
                        aux.set_father(chld2)

                temp.add_chld(chld1)
                temp.add_chld(chld2)
                chld1.set_father(temp)
                chld2.set_father(temp)
                return temp

    def sort(self, key):
        for i in range(len(self.__keys)):
            if key.value < self.__keys[i].value:
                self.__keys.insert(i,key)
                break
            elif i == (len(self.__keys) - 1):
                self.__keys.append(key)
        return self
    
    def search(self, key):
        i = 0
        if len(self.__childs) == 0:
            for i in self.__keys:
                if i.value == key:
                    return i
            return NodeTBPlus(-1)

        elif key < self.__keys[i].value:
            return self.__childs[i].search(key)

        elif ((self.__keys[i].value <= key)) and (len(self.__keys) == 1):
            return self.__childs[i + 1].search(key)
        
        while i < (len(self.__keys) - 1):
            if (self.__keys[i].value < key) and (key < self.__keys[i + 1].value):
                return self.__childs[i + 1].search(key)
            i += 1
        
        i += 1
        if self.__keys[i - 1].value < key:
            return self.__childs[i].search(key)

    def callPage(self):
        if (len(self.get_chlds()) == 0) and (self.get_father() is None):
            for i in self.get_chlds():
                print(i.value)
        elif len(self.get_chlds()) == 0:
            return self.printLeaf()
        else:
             return self.get_chlds()[0].callPage()

    def printLeaf(self):
        if self is not None:
            for i in self.get_keys():
                print(i.value, end=" ")
            if self.get_next() is None:
                return -1
            else:
                return self.get_next().printLeaf()
    
    def Travel(self):
        pass

    # Show Keys of Page
    def showKeys(self):
        if not (len(self.__keys) == 0):
            print("[", end=" ")
            for i in range(len(self.__keys)):
                print(self.__keys[i].value, ",", end=" ")
            print("]", end=" ")
            if not (self.__next is None):
                print("[ ", end="")
                for i in range(len(self.__next.__keys)):
                    print(self.__next.__keys[i].value, end=" ")
                print("]", end="")
            else:
                pass
        contador = 0
        if not (len(self.__childs) == 0):
            for x in range(len(self.__childs)):
                contador += 1
        print(" contador hijos: ", contador)

    # Graph and show keys
    def graphKeys(self, tmp, level):
        cadena = ""
        if not (len(self.__keys) == 0):
            keysString = ""
            if level != 0:
                for i in range(len(self.__keys)):
                    if not (i == (len(self.__keys) - 1)):
                        keysString += f"{self.__keys[i].value}, "
                    else:
                        keysString += f"{self.__keys[i].value}"
                cadena += f"{tmp} [label=\"{keysString}\" color=red]\n"

                if len(self.__childs) != 0:
                    for i in range(len(self.__childs)):
                        cadena += f"{tmp} -> {self.__childs[i]}\n"

                if not (self.__next is None):
                    cadena += f"{tmp} -> {self.__next}\n"

            else:
                for i in range(len(self.__keys)):
                    if not (i == (len(self.__keys) - 1)):
                        keysString += f"{self.__keys[i].value}, "
                    else:
                        keysString += f"{self.__keys[i].value}"
                cadena += f"{tmp} [label=\"{keysString}\" color=green]\n"

                if len(self.__childs) != 0:
                    for i in range(len(self.__childs)):
                        cadena += f"{tmp} -> {self.__childs[i]}\n"
        return cadena
                        
    # Rank = same to the nodes (leaves)
    def rankLeavesKeys(self, tmp):
        cadena = ""
        if len(tmp.get_chlds()) != 0:
            cadena += self.rankLeavesKeys(tmp.get_chlds()[0])
        else:
            cadena += f"{tmp};\n"
            if tmp.get_next() is not None:
                cadena += self.rankLeavesKeys(tmp.get_next())
        return cadena    

class NodeTBPlus:

    def __init__(self, value):
        self.value = value
        


    
