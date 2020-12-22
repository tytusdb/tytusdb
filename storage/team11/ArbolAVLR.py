import copy


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


class ArbolAVLR:
    def __init__(self):
        self.root = None
        self.cadena = ""
        self.__list_tables = list()

    def add(self, element):
        self.root = self.__add(self.root, element)

    def __add(self, raiz: NodoAVL, element):
        if raiz is None:
            raiz = NodoAVL(element)
        elif element[0] < raiz.get_element()[0]:
            left = self.__add(raiz.get_left(), element)
            raiz.set_left(left)
        elif element[0] > raiz.get_element()[0]:
            right = self.__add(raiz.get_right(), element)
            raiz.set_right(right)

        raiz.set_factor(1 + max(self.__get_height(raiz.get_left()), self.__get_height(raiz.get_right())))
        balance = self.__get_balance(raiz)
        if balance > 1 and element[0] < raiz.get_left().get_element()[0]:
            return self.__rotacion_right(raiz)

        if balance < -1 and element[0] > raiz.get_right().get_element()[0]:
            return self.__rotacion_left(raiz)

        if balance > 1 and element[0] > raiz.get_left().get_element()[0]:
            rotate = self.__rotacion_left(raiz.get_left())
            raiz.set_left(rotate)
            return self.__rotacion_right(raiz)

        if balance < -1 and element[0] < raiz.get_right().get_element()[0]:
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
            self.cadena += f"node{self.root.get_element()[0]}[color=\"#000000\",label=\"<f0>|<f1> Valor:{self.root.get_element()[0]} |<f2>\" ] \n"
            self.__graficar(self.root, self.get_root().get_left(), True)
            self.__graficar(self.root, self.get_root().get_right(), False)

        self.cadena += "}\n"
        
        return self.cadena

    def get_root(self):
        return self.root

    def __graficar(self, padre, actual, left):
        if actual is not None:
            self.cadena += f"node{actual.get_element()[0]}[color=\"#000000\",label=\"<f0>|<f1> Valor:{actual.get_element()[0]} |<f2>\"] \n"
            if left is True:
                self.cadena += f"node{padre.get_element()[0]}:f0->node{actual.get_element()[0]}:f1 [arrowhead=\"crow\",color=\"#E30101 \"] \n"
            else:
                self.cadena += f"node{padre.get_element()[0]}:f2->node{actual.get_element()[0]}:f1 [arrowhead=\"crow\",color=\"#E30101 \"]  \n"

            self.__graficar(actual, actual.get_left(), True)
            self.__graficar(actual, actual.get_right(), False)

    def __delete_nodo(self, raiz, value):
        if not raiz: return raiz
        if value < str(raiz.get_element()[0]):
            left = self.__delete_nodo(raiz.get_left(), value)
            raiz.set_left(left)
        elif value > str(raiz.get_element()[0]):
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
            small_value = self.__find_nodo(raiz.get_right())
            raiz.set_element(small_value)
            right = self.__delete_nodo(raiz.get_right(), small_value[0])
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

    def __find_nodo(self, raiz=NodoAVL):
        if raiz.get_left() is None:
            return raiz.get_element()
        else:
            return self.__find_nodo(raiz.get_left())

    def __search_value(self, root, name):
        if root is None: return None
        if root.get_element()[0] == name:
            return root
        if root.get_element()[0] > name:
            return self.__search_value(root.get_left(), name)

        return self.__search_value(root.get_right(), name)

    def search_value(self, table_name):
        return self.__search_value(self.root, table_name)

    def __update_table(self, root, table):
        if root is None: return None
        if root.get_element()[0] == table[0]:
            root.set_element(table)
            return root
        if root.get_element()[0] > table[0]:
            return self.__update_table(root.get_left(), table)
        return self.__update_table(root.get_right(), table)

    def update_table(self, table):
        return self.__update_table(self.root, table)

    def get_tables(self):
        self.__inorder(self.root)
        list_aux = self.__list_tables
        self.__list_tables = list()
        return list_aux

    def __inorder(self, nodo):
        if nodo.get_left() is not None:
            self.__inorder(nodo.get_left())
        self.__list_tables.append(nodo.get_element()[0])
        if nodo.get_right() is not None:
            self.__inorder(nodo.get_right())
        return self.__list_tables

    def extra_table(self):
        self.__extract_table(self.root)
        list_aux = self.__list_tables.copy()
        self.__list_tables = list()
        return list_aux

    def __extract_table(self, nodo):
        if nodo.get_left() is not None:
            self.__extract_table(nodo.get_left())
        list_aux = nodo.get_element().copy()
        list_aux.pop(0)
        self.__list_tables.append(list_aux)
        if nodo.get_right() is not None:
            self.__extract_table(nodo.get_right())

    def truncate(self):
        return self.__truncate(self.root)

    def __truncate(self, nodo):
        if nodo.get_left() is not None or nodo.get_right() is not None:
            self.__truncate(self.__delete_nodo(nodo, nodo.get_element()[0]))
        self.delete_nodo(nodo.get_element()[0])
        self.root = None

    def update_node(self, value, register=dict()):
        nodo = self.search_value(value)
        if nodo:
            for key in register.keys():
                nodo.get_element()[key + 1] = register[key]
            return 0
        else:
            return 4

    def extractRangeTable(self, column_number, lower, upper):
        self.__extract_range_table(self.root, column_number, lower, upper)
        list_aux = self.__list_tables.copy()
        self.__list_tables = list()
        return list_aux

    def __extract_range_table(self, nodo: NodoAVL, column_number, lower, upper):
        if nodo.get_left() is not None:
            self.__extract_range_table(nodo.get_left(), column_number, lower, upper)

        data = str(nodo.get_element()[int(column_number + 1)])
        list_aux: list = nodo.get_element().copy()
        list_aux.pop(0)
        if str(lower) <= data <= str(upper):
            self.__list_tables.append(list_aux)

        if nodo.get_right() is not None:
            self.__extract_range_table(nodo.get_right(), column_number, lower, upper)

    def get_rootV2(self):
        return self.root if self.root is not None else None
