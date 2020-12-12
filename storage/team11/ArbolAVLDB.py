class NodoAVL:
    def __init__(self, element):
        self.element = element
        self.right = None
        self.left = None
        self.factor = 0

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right

    def set_element(self, element):
        self.element = element

    def get_element(self):
        return self.element

    def set_factor(self, factor):
        self.factor = factor

    def get_factor(self):
        return self.factor


class ArbolAVLT:
    def __init__(self):
        self.root = None
        self.cadena = ""
        self.scape = False

    def add(self, element):
        # b = False
        self.root = self.__add(self.root, element)

    def __add(self, raiz, elemeneto):
        if raiz is None:
            raiz = NodoAVL(elemeneto)
            self.scape = True
        elif elemeneto < raiz.get_element():
            izq = self.__add(raiz.get_left(), elemeneto)
            raiz.set_left(izq)
            if self.scape is True:
                if raiz.get_factor() == 1:
                    raiz.set_factor(0)
                    self.scape = False
                elif raiz.get_factor() == 0:
                    raiz.set_factor(-1)
                elif raiz.get_factor() == -1:
                    n1 = raiz.get_left()
                    if n1.get_factor() == -1:
                        raiz = self.__rotacion_ii(raiz, n1)
                    else:
                        raiz = self.__rotacion_id(raiz, n1)
                    self.scape = False
        elif elemeneto > raiz.get_element():
            der = self.__add(raiz.get_right(), elemeneto)
            raiz.set_right(der)
            if self.scape:
                if raiz.get_factor() == 1:
                    n1 = raiz.get_right()
                    if n1.get_factor() == 1:
                        raiz = self.__rotacion_dd(raiz, n1)
                    else:
                        raiz = self.__rotacion_di(raiz, n1)
                    self.scape = False
                elif raiz.get_factor() == 0:
                    raiz.set_factor(1)
                elif raiz.get_factor() == -1:
                    raiz.set_factor(0)
                    self.scape = False

        return raiz

    def __rotacion_ii(self, n, n1):
        n.set_left(n1.get_right())
        n1.set_right(n)

        if n1.get_factor() == -1:
            n.set_factor(0)
            n1.set_factor(0)
        else:
            n.set_factor(-1)
            n1.set_factor(1)

        return n1

    def __rotacion_dd(self, n, n1):
        n.set_right(n1.get_left())
        n1.set_left(n)

        if n1.get_factor() == 1:
            n.set_factor(0)
            n1.set_factor(0)
        else:
            n.set_factor(1)
            n1.set_factor(-1)

        return n1

    def __rotacion_id(self, n, n1):
        n2 = n1.get_right()
        n.set_left(n2.get_right())
        n2.set_right(n)
        n1.set_right(n2.get_left())
        n2.set_left(n1)

        if n2.get_factor() == 1:
            n1.set_factor(-1)
        else:
            n1.set_factor(0)

        if n2.get_factor() == -1:
            n.set_factor(1)
        else:
            n.set_factor(0)

        n2.set_factor(0)
        return n2

    def __rotacion_di(self, n, n1):
        n2 = n1.get_left()
        n.set_right(n2.get_left())
        n2.set_left(n)
        n1.set_left(n2.get_right())
        n2.set_right(n1)

        if n2.get_factor() == 1:
            n.set_factor(-1)
        else:
            n.set_factor(0)

        if n2.get_factor() == -1:
            n1.set_factor(1)
        else:
            n1.set_factor(0)

        n2.set_factor(0)
        return n2
