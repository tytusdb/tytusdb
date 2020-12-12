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

    def add_chld(self, chld):
        self.__childs.append(chld)
    
    def add_key(self, key):
        if len(self.__keys) == 0:
            self.__keys.append(key)
            return self
        else:
            if self.__childs is None:
                for i in range(len(self.__keys)):
                    if key.value < self.__keys[i].value:
                        self.__keys.insert(i,key)
                        break
                    elif i == (len(self.__keys) - 1):
                        self.__keys.append(key)
                if len(self.__keys) == (self.__grade):
                    return self.SplitPage()
                return self
            else:
                i = 0
                if key.value < self.__keys[i].value:
                    aux = self.__childs[i].add_key(key)
                    if aux is list:
                        for x in range(len(aux) - 1):
                            self.__childs.insert((i + x), aux[x])
                        self.add_key(aux[len(aux) - 1])
                    else:
                        self.__childs[i] = aux
                    return self

                elif self.__keys[i].value < key.value:
                    aux = self.__childs[i].add_key(key)
                    if aux is list:
                        for x in range(len(aux) - 1):
                            self.__childs.insert((i + x), aux[x])
                        self.add_key(aux[len(aux) - 1])
                    else:
                        self.__childs[i] = aux
                    return self

                while i < (len(self.__keys) - 1):
                    if (self.__keys[i].value < key.value) and (key.value < self.__keys[i + 1].value):
                        aux = self.__childs[i].add_key(key)
                    if aux is list:
                        for x in range(len(aux) - 1):
                            self.__childs.insert((i + x), aux[x])
                        self.add_key(aux[len(aux) - 1])
                        return self
                    else:
                        self.__childs[i] = aux
                        return self
                    i += 1
                    
                i += 1
                if self.__keys[i].value < key.value:
                    aux = self.__childs[i].add_key(key)
                    if aux is list:
                        for x in range(len(aux) - 1):
                            self.__childs.insert((i + x), aux[x])
                        self.add_key(aux[len(aux) - 1])
                    else:
                        self.__childs[i] = aux
                    return self
    
    def SplitPage(self):
        if (self.__grade % 2) > 0:
            index = int((self.__grade - 1) /2)
        else:
            index = int(self.__grade / 2)

        if self.__father is None:
            temp = PageTBPlus(self.__grade)
            temp.add_key(NodeTBPlus(self.__keys[index]))
            chld1 = PageTBPlus(self.__grade)
            chld2 = PageTBPlus(self.__grade)

            for i in range(len(self.__keys)):
                if i < index:
                    chld1.add_key(self.__keys[i])
                else:
                    chld2.add_key(self.__keys[i])

            temp.add_chld(chld1)
            temp.add_chld(chld2)
            chld1.set_father(temp)
            chld2.set_father(temp)
            chld1.set_next(chld2)
            return temp
        elif len(self.__childs) == 0:
            chld1 = PageTBPlus(self.__grade)
            chld2 = PageTBPlus(self.__grade)

            for i in range(len(self.__keys)):
                if i < index:
                    chld1.add_key(self.__keys[i])
                else:
                    chld2.add_key(self.__keys[i])
            chld1.set_father(self.get_father())
            chld2.set_father(self.get_father())
            temp = []
            temp.extend([chld1, chld2, self.__keys[index]])
            return temp


class NodeTBPlus:

    def __init__(self, value):
        self.value = value
    
