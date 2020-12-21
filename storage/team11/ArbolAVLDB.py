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


class ArbolAVLT:
    def __init__(self):
        self.root: NodoAVL = None
        self.cadena = ""
        self.__list_tables = list()

    def add(self, element):
        self.root = self.__add(self.root, element)

    def __add(self, raiz: NodoAVL, element):
        if raiz is None:
            raiz = NodoAVL(element)
        elif element.get_table_name() < raiz.get_element().get_table_name():
            left = self.__add(raiz.get_left(), element)
            raiz.set_left(left)
        elif element.get_table_name() > raiz.get_element().get_table_name():
            right = self.__add(raiz.get_right(), element)
            raiz.set_right(right)

        raiz.set_factor(1 + max(self.__get_height(raiz.get_left()), self.__get_height(raiz.get_right())))
        balance = self.__get_balance(raiz)
        if balance > 1 and element.get_table_name() < raiz.get_left().get_element().get_table_name():
            return self.__rotacion_right(raiz)

        if balance < -1 and element.get_table_name() > raiz.get_right().get_element().get_table_name():
            return self.__rotacion_left(raiz)

        if balance > 1 and element.get_table_name() > raiz.get_left().get_element().get_table_name():
            rotate = self.__rotacion_left(raiz.get_left())
            raiz.set_left(rotate)
            return self.__rotacion_right(raiz)

        if balance < -1 and element.get_table_name() < raiz.get_right().get_element().get_table_name():
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
            self.cadena += f"node{self.root.get_element().get_table_name()}[color=\"#000000\",label=\"<f0>|<f1> Valor:{self.root.get_element().get_table_name()} |<f2>\" ] \n"
            self.__graficar(self.root, self.get_root().get_left(), True)
            self.__graficar(self.root, self.get_root().get_right(), False)

        self.cadena += "}\n"
        print(self.cadena)
        return self.cadena

    def get_root(self):
        return self.root

    def __graficar(self, padre, actual, left):
        if actual is not None:
            self.cadena += f"node{actual.get_element().get_table_name()}[color=\"#000000\",label=\"<f0>|<f1> Valor:{actual.get_element().get_table_name()} |<f2>\"] \n"
            if left is True:
                self.cadena += f"node{padre.get_element().get_table_name()}:f0->node{actual.get_element().get_table_name()}:f1 [arrowhead=\"crow\",color=\"#E30101 \"] \n"
            else:
                self.cadena += f"node{padre.get_element().get_table_name()}:f2->node{actual.get_element().get_table_name()}:f1 [arrowhead=\"crow\",color=\"#E30101 \"]  \n"

            self.__graficar(actual, actual.get_left(), True)
            self.__graficar(actual, actual.get_right(), False)

    def __delete_nodo(self, raiz, value):
        if not raiz: return raiz
        if value < str(raiz.get_element().get_table_name()):
            left = self.__delete_nodo(raiz.get_left(), value)
            raiz.set_left(left)
        elif value > str(raiz.get_element().get_table_name()):
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
            right = self.__delete_nodo(raiz.get_right(), small_value.get_table_name())
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
        if root.get_element().get_table_name() == name:
            return root
        if root.get_element().get_table_name() > name:
            return self.__search_value(root.get_left(), name)

        return self.__search_value(root.get_right(), name)

    def search_value(self, table_name):
        return self.__search_value(self.root, table_name)

    def update_table_pk(self, table_name, columns):
        aux: NodoAVL = self.root
        modify = False
        while not modify:
            if table_name == aux.get_element().get_table_name():
                aux.get_element().define_pk(columns)
                modify = True
                return True
            if table_name < aux.get_element().get_table_name():
                aux = aux.get_left()
            if table_name > aux.get_element().get_table_name():
                aux = aux.get_right()

        return False

    def __update_table_pk_r(self, root: NodoAVL, table_name, columns):
        if root is None: return None
        if root.get_element().get_table_name() == table_name:
            return root.get_element().define_pk(columns)
        if root.get_element().get_table_name() > table_name:
            return self.__update_table_pk_r(root.get_left(), table_name, columns)

        return self.__update_table_pk_r(root.get_right(), table_name, columns)

    def update_table_pk_r(self, table_name, columns):
        return self.__update_table_pk_r(self.root, table_name, columns)

    def update_alter_add_column(self, table_name):
        return self.__update_alter_add_column(self.root, table_name)

    def __update_alter_add_column(self, root, table_name):
        if root is None: return None
        if root.get_element().get_table_name() == table_name:
            root.get_element().add_column()
            return True
        if root.get_element().get_table_name() > table_name:
            return self.__update_alter_add_column(root.get_left(), table_name)

        return self.__update_alter_add_column(root.get_right(), table_name)

    def insert_tupla(self, table_name, register):
        return self.__insert_tupla(self.root, table_name, register)

    def __insert_tupla(self, root: NodoAVL, table_name, register):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            status = root.get_element().insert(register)
            return status
        if root.get_element().get_table_name() > table_name:
            return self.__insert_tupla(root.get_left(), table_name, register)

        return self.__insert_tupla(root.get_right(), table_name, register)

    def extract_row(self, table_name, columns):
        return self.__extract_row(self.root, table_name, columns)

    def __extract_row(self, root: NodoAVL, table_name, columns):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            return root.get_element().extractRow(columns)
        if root.get_element().get_table_name() > table_name:
            return self.__extract_row(root.get_left(), table_name, columns)

        return self.__extract_row(root.get_right(), table_name, columns)

    def get_tables(self):
        self.__inorder(self.root)
        list_aux = self.__list_tables
        self.__list_tables = list()
        return list_aux

    def __inorder(self, nodo):
        if nodo.get_left() is not None:
            self.__inorder(nodo.get_left())

        self.__list_tables.append(nodo.get_element().get_table_name())

        if nodo.get_right() is not None:
            self.__inorder(nodo.get_right())

    def load_csv(self, table_name, file):
        return self.__load_csv(self.root, table_name, file)

    def __load_csv(self, root: NodoAVL, table_name, file):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            return root.get_element().loadCSV(file)
        if root.get_element().get_table_name() > table_name:
            return self.__load_csv(root.get_left(), table_name, file)

        return self.__load_csv(root.get_right(), table_name, file)

    def update(self, table_name, register, columns):
        return self.__update(self.root, table_name, register, columns)

    def __update(self, root: NodoAVL, table_name, register, columns):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            return root.get_element().update(register, columns)
        if root.get_element().get_table_name() > table_name:
            return self.__update(root.get_left(), table_name, register, columns)

        return self.__update(root.get_right(), table_name, register, columns)

    def delete_register(self, table_name, columns):
        return self.__delete_register(self.root, table_name, columns)

    def __delete_register(self, root: NodoAVL, table_name, columns):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            return root.get_element().delete(columns)
        if root.get_element().get_table_name() > table_name:
            return self.__delete_register(root.get_left(), table_name, columns)

        return self.__delete_register(root.get_right(), table_name, columns)

    def truncate(self, table_name):
        return self.__truncate(self.root, table_name)

    def __truncate(self, root: NodoAVL, table_name):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            root.get_element().truncate()
            return True
        if root.get_element().get_table_name() > table_name:
            return self.__truncate(root.get_left(), table_name)

        return self.__truncate(root.get_right(), table_name)

    def alter_drop_pk(self, table_name):
        return self.__alter_drop_pk(self.root, table_name)

    def __alter_drop_pk(self, root: NodoAVL, table_name):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            return root.get_element().alterDropPK()
        if root.get_element().get_table_name() > table_name:
            return self.__alter_drop_pk(root.get_left(), table_name)

        return self.__alter_drop_pk(root.get_right(), table_name)

    def alterAddColumn(self, table_name, default):
        return self.__alterAddColumn(self.root, table_name, default)

    def __alterAddColumn(self, root: NodoAVL, table_name, default):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            status = root.get_element().alterAddColumn(default)
            return status
        if root.get_element().get_table_name() > table_name:
            return self.__alterAddColumn(root.get_left(), table_name, default)

        return self.__alterAddColumn(root.get_right(), table_name, default)

    def alterDropColumn(self, table_name, columnNumber):
        return self.__alterDropColumn(self.root, table_name, columnNumber)

    def __alterDropColumn(self, root: NodoAVL, table_name, columnNumber):
        if root is None: return None
        if table_name == root.get_element().get_table_name():
            status = root.get_element().alterDropColumn(columnNumber)
            return status
        if root.get_element().get_table_name() > table_name:
            return self.__alterDropColumn(root.get_left(), table_name, columnNumber)

        return self.__alterDropColumn(root.get_right(), table_name, columnNumber)
