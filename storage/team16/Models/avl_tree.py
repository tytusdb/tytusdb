# # region Code
# from node import Node
# from tree_graph import TreeGraph
# # endregion

# region Pycharm
from Models.node import Node
from Models.tree_graph import TreeGraph


# endregion


class AVLTree:
    def __init__(self, database: str, name: str, numberColumns: int, pklist: list):
        self.root = None
        self.database = database
        self.name = name
        self.numberColumns = int(numberColumns)
        self.pklist = pklist
        # self.columns = self.crearCols(numberColumns)

    def __repr__(self) -> str:
        return str(self.name)

        # En caso sirva:

    # def crearCols(self, numberColumns: int) -> list:
    #     tmp = []
    #     for i in range(numberColumns):
    #         tmp.append(i)
    #     return tmp

    # def agregarCols(self, columns: list):
    #     columns.append(int(columns[-1])+1)

    # def eliminarCol(self, posicion):
    #     self.columns.pop(posicion)

    # region basic methods
    def add(self, index, content):
        self.root = self.__add(index, content, self.root)

    def __add(self, index, content, node):
        if node is None:
            return Node(index, content)
        elif index < node.index:
            node.left = self.__add(index, content, node.left)
            node = self.__balance(node)
        elif index > node.index:
            node.right = self.__add(index, content, node.right)
            node = self.__balance(node)
        return node  # depends of the event returns different node to be the root

    def search(self, index):
        return self.__search(index, self.root)

    def __search(self, index, node):
        if node:
            if node.index == index:
                return node.content
            elif node.index < index:
                content = self.__search(index, node.right)
            else:
                content = self.__search(index, node.left)
            return content
        return None

    def tolist(self) -> list:
        return self.__tolist(self.root, tuples=[]) if self.root is not None else []

    def __tolist(self, node: Node, tuples: list) -> list:
        if node:
            self.__tolist(node.left, tuples)
            tuples.append(node.content)
            self.__tolist(node.right, tuples)
            return tuples

    def massiveupdate(self, action: str, arg):
        self.__massiveupdate(self.root, action, arg)

    def __massiveupdate(self, node, action: str, arg):
        if node:
            if action == "add":
                node.content.append(arg)
            elif action == "drop" and isinstance(arg, int):
                if int(arg) < len(node.content):
                    del node.content[int(arg)]
                else:
                    return
            self.__massiveupdate(node.left, action, arg)
            self.__massiveupdate(node.right, action, arg)

    def delete(self, index):
        self.root = self.__delete(index, self.root)
        self.root = self.__balance(self.root)

    def __delete(self, index, node):
        if node:
            if node.index == index:
                if node.left:
                    tmp, up = self.__rightmost(node.left, node)
                    first = True if tmp == node.left else False
                    node.index = tmp.index
                    node.content = tmp.content

                    if tmp.left:
                        tmp2 = tmp.left
                        tmp.index = tmp2.index
                        tmp.content = tmp2.content
                        tmp.left = tmp2.left
                        tmp.right = tmp2.right
                    else:
                        if first:
                            up.left = None
                        else:
                            up.right = None
                else:
                    return None
            elif node.index < index:
                node.right = self.__delete(index, node.right)
            else:
                node.left = self.__delete(index, node.left)
        return node

    # endregion

    # region other methods
    def __rightmost(self, node, up):
        if node.right:
            return self.__rightmost(node.right, node)
        else:
            return node, up

    def __balance(self, node):
        if node:
            if node.left:
                node.left = self.__balance(node.left)
            if node.right:
                node.right = self.__balance(node.right)

            node.height = self.greater(node.left, node.right) + 1
            if abs(self.difference(node, 'r')) == 2:
                if self.height(node.left) > self.height(node.right):
                    node = self.__DR(node, 'l') if self.height(node.left.left) < \
                                                   self.height(node.left.right) else self.__SR(node, 'l')
                else:
                    node = self.__DR(node, 'r') if self.height(node.right.left) > \
                                                   self.height(node.right.right) else self.__SR(node, 'r')
            return node

    # endregion

    # region calculation methods

    @staticmethod
    def height(temp):
        if temp is None:
            return -1
        else:
            return temp.height

    def difference(self, node, first):
        if first == 'l':
            return self.height(node.left) - \
                   self.height(node.right)
        else:
            return self.height(node.right) - \
                   self.height(node.left)

    def greater(self, left, right):
        left = self.height(left)
        right = self.height(right)
        return (left, right)[right > left]

    # endregion

    # region rotations
    def __SR(self, node, type):
        if type == 'l':
            tmp = node.left
            node.left = tmp.right
            tmp.right = node
            node.height = self.greater(node.left, node.right) + 1
            tmp.height = self.greater(tmp.left, node) + 1
            return tmp
        elif type == 'r':
            tmp = node.right
            node.right = tmp.left
            tmp.left = node
            node.height = self.greater(node.left, node.right) + 1
            tmp.height = self.greater(tmp.right, node) + 1
            return tmp

    def __DR(self, node, type):
        if type == 'l':
            node.left = self.__SR(node.left, 'r')
            return self.__SR(node, 'l')
        elif type == 'r':
            node.right = self.__SR(node.right, 'l')
            return self.__SR(node, 'r')

    # endregion

    # region traversals
    def preorder(self):
        print("Preorder: ")
        self.__preorder(self.root)
        print()

    def __preorder(self, temp):
        if temp:
            print(temp.index, end=' ')
            self.__preorder(temp.left)
            self.__preorder(temp.right)
        # backtracking action

    def inorder(self):
        print("Inorder: ")
        self.__inorder(self.root)
        print()

    def __inorder(self, temp):
        if temp:
            self.__inorder(temp.left)
            print(temp.content, end=' ')
            self.__inorder(temp.right)
        # backtracking action

    def postorder(self):
        print("Postorder: ")
        self.__postorder(self.root)
        print()

    def __postorder(self, temp):
        if temp:
            self.__postorder(temp.left)
            self.__postorder(temp.right)
            print(temp.index, end=' ')
        # backtracking action
    # endregion


t = AVLTree("test", "tst", 5, [])
t.add(57, ["test", "test2"])
t.add(25, ["test", "test2"])
t.add(78, ["test", "test2"])
t.add(17, ["test", "test2"])
t.add(45, ["test", "test2"])
t.add(64, ["test", "test2"])
t.add(97, ["test", "test2"])
t.add(4, ["test", "test2"])
t.add(20, ["test", "test2"])
t.add(43, ["test", "test2"])
t.add(56, ["test", "test2"])
t.add(61, ["test", "test2"])
t.add(68, ["test", "test2"])
t.add(89, ["test", "test2"])
t.add(100, ["test", "test2"])
t.add(1, ["test", "test2"])
t.add(12, ["test", "test2"])
t.add(19, ["test", "test2"])
t.add(23, ["test", "test2"])
t.add(54, ["test", "test2"])
t.add(62, ["test", "test2"])
t.add(66, ["test", "test2"])
t.add(73, ["test", "test2"])
t.add(87, ["test", "test2"])
t.add(90, ["test", "test2"])
t.add(10, ["test", "test2"])
t.add(15, ["test", "test2"])
t.add(58, ["test", "test2"])
t.delete(64)
t.add(9, ["test", "test2"])
t.add(3, ["test", "test2"])
t.delete(9)
t.delete(15)
t.delete(12)
t.delete(57)
t.add(103, ["test", "test2"])
t.add(98, ["test", "test2"])
t.add(102, ["test", "test2"])
t.delete(103)

search = t.search(103)
if search:
    print(search)
else:
    print("empty")

t.tolist()

# t.inorder()
# aa = TreeGraph(t)
# aa.export()


t.massiveupdate("add", "perro")
t.massiveupdate("drop", 2)
t.inorder()
