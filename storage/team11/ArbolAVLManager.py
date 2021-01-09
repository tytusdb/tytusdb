class NodoAVL:
    def __init__(self, element):
        self.__element = element
        self.__right = None
        self.__left = None
        self.__factor = 1

    def set_left(self, left):
        self.__left = left

    def get_left(self):
        return self.__left

    def set_right(self, right):
        self.__right = right

    def get_right(self):
        return self.__right

    def set_element(self, element):
        self.__element = element

    def get_element(self):
        return self.__element

    def set_factor(self, factor):
        self.__factor = factor

    def get_factor(self):
        return self.__factor


class ArbolAVLDB:
    def __init__(self):
        self.root = None
        self.name = ""
        self.__list_databases = list()

    def add(self, element):
        self.root = self.__add(self.root, element)

    def __add(self, raiz: NodoAVL, element):
        if raiz is None:
            raiz = NodoAVL(element)
        elif element.get_database() < raiz.get_element().get_database():
            left = self.__add(raiz.get_left(), element)
            raiz.set_left(left)
        elif element.get_database() > raiz.get_element().get_database():
            right = self.__add(raiz.get_right(), element)
            raiz.set_right(right)

        raiz.set_factor(1 + max(self.__get_height(raiz.get_left()), self.__get_height(raiz.get_right())))
        balance = self.__get_balance(raiz)
        if balance > 1 and element.get_database() < raiz.get_left().get_element().get_database():
            return self.__rotacion_right(raiz)

        if balance < -1 and element.get_database() > raiz.get_right().get_element().get_database():
            return self.__rotacion_left(raiz)

        if balance > 1 and element.get_database() > raiz.get_left().get_element().get_database():
            rotate = self.__rotacion_left(raiz.get_left())
            raiz.set_left(rotate)
            return self.__rotacion_right(raiz)

        if balance < -1 and element.get_database() < raiz.get_right().get_element().get_database():
            rotate = self.__rotacion_right(raiz.get_right())
            raiz.set_right(rotate)
            return self.__rotacion_left(raiz)

        return raiz

    def __get_height(self, root: NodoAVL):
        if not root:
            return 0
        return root.get_factor()

    def __rotacion_left(self, z: NodoAVL):
        y: NodoAVL = z.get_right()
        t2: NodoAVL = y.get_left()

        y.set_left(z)
        z.set_right(t2)

        z.set_factor(1 + max(self.__get_height(z.get_left()), self.__get_height(z.get_right())))
        y.set_factor(1 + max(self.__get_height(y.get_left()), self.__get_height(y.get_right())))
        return y

    def __rotacion_right(self, z: NodoAVL):
        y: NodoAVL = z.get_left()
        t3 = y.get_right()

        y.set_right(z)
        z.set_left(t3)

        z.set_factor(1 + max(self.__get_height(z.get_left()), self.__get_height(z.get_right())))
        y.set_factor(1 + max(self.__get_height(y.get_left()), self.__get_height(y.get_right())))
        return y

    def __get_balance(self, raiz: NodoAVL):
        if not raiz:
            return 0
        return self.__get_height(raiz.get_left()) - self.__get_height(raiz.get_right())

    def grafica(self):
        self.cadena = "digraph G{\n"
        self.cadena += "node[shape=\"record\"]\n"
        if self.root is not None:
            self.cadena += f"node{self.root.get_element().get_database()}[color=\"#000000\",label=\"<f0>|<f1> Valor:{self.root.get_element().get_database()} |<f2>\" ] \n"
            self.__graficar(self.root, self.get_root().get_left(), True)
            self.__graficar(self.root, self.get_root().get_right(), False)

        self.cadena += "}\n"
        print(self.cadena)
        return self.cadena

    def get_root(self):
        return self.root

    def __graficar(self, padre, actual, left):
        if actual is not None:
            self.cadena += f"node{actual.get_element().get_database()}[color=\"#000000\",label=\"<f0>|<f1> Valor:{actual.get_element().get_database()} |<f2>\"] \n"
            if left is True:
                self.cadena += f"node{padre.get_element().get_database()}:f0->node{actual.get_element().get_database()} \n"
            else:
                self.cadena += f"node{padre.get_element().get_database()}:f2->node{actual.get_element().get_database()} \n"

            self.__graficar(actual, actual.get_left(), True)
            self.__graficar(actual, actual.get_right(), False)

    def __delete_nodo(self, raiz, value):
        if not raiz:
            return raiz
        if value < str(raiz.get_element().get_database()):
            left = self.__delete_nodo(raiz.get_left(), value)
            raiz.set_left(left)
        elif value > str(raiz.get_element().get_database()):
            right = self.__delete_nodo(raiz.get_right(), value)
            raiz.set_right(right)
        else:
            if raiz.get_left() is None:
                temp = raiz.get_right()
                raiz = None
                return temp
            elif raiz.get_right() is None:
                temp = raiz.get_left()
                raiz = None
                return temp
            lower_value = self.__find_nodo(raiz.get_right())
            raiz.set_element(lower_value)
            right = self.__delete_nodo(raiz.get_right(), lower_value.get_database())
            raiz.set_right(right)

        if raiz is None:
            return raiz

        raiz.set_factor(1 + max(self.__get_height(raiz.get_left()), self.__get_height(raiz.get_right())))
        balance = self.__get_balance(raiz)

        if balance > 1 and self.__get_balance(raiz.get_left()) >= 0:
            return self.__rotacion_right(raiz)
        if balance < -1 and self.__get_balance(raiz.get_right()) <= 0:
            return self.__rotacion_left(raiz)

        if balance > 1 and self.__get_balance(raiz.get_left()) < 0:
            left = self.__rotacion_left(raiz.get_left())
            raiz.set_left(left)
            return self.__rotacion_right(raiz)

        if balance < -1 and self.__get_balance(raiz.get_right()) > 0:
            right = self.__rotacion_right(raiz.get_right())
            raiz.set_right(right)
            return self.__rotacion_left(raiz)
        return raiz

    def delete_nodo(self, value):
        self.root = self.__delete_nodo(self.root, value)

    def __find_nodo(self, raiz: NodoAVL):
        if raiz.get_left() is None:
            return raiz.get_element()
        else:
            return self.__find_nodo(raiz.get_left())

    def __search_value(self, root, name):
        if root is None:
            return None
        if root.get_element().get_database() == name:
            return root
        if root.get_element().get_database() > name:
            return self.__search_value(root.get_left(), name)
        return self.__search_value(root.get_right(), name)

    def search_value(self, db_name):
        return self.__search_value(self.root, db_name)

    def __update_db(self, root, db):
        if root is None: return None
        if root.get_element().get_database() == db.get_database():
            root.set_element(db)
            return root
        if root.get_element().get_database() > db.get_database():
            return self.__update_db(root.get_left(), db)
        return self.__update_db(root.get_right(), db)

    def update_db(self, db):
        return self.__update_db(self.root, db)

    def get_databases(self):
        self.__inorder(self.root)
        list_aux = self.__list_databases
        self.__list_databases = list()
        return list_aux

    def __inorder(self, nodo):
        if nodo.get_left() is not None:
            self.__inorder(nodo.get_left())
        self.__list_databases.append(nodo.get_element().get_database())

        if nodo.get_right() is not None:
            self.__inorder(nodo.get_right())

