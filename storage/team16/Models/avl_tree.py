from Models.node import Node
from Models.tree_graph import TreeGraph


class AVLTree:
    def __init__(self, database: str, name: str, numberColumns: int):
        self.root = None
        self.database = str(database)
        self.name = str(name)
        self.numberColumns = numberColumns
        self.pk = []

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
            print(temp.index, end=' ')
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


t = AVLTree("test", "tst", 5)
t.add(57, "as")
t.add(25, "as")
t.add(78, "as")
t.add(17, "as")
t.add(45, "as")
t.add(64, "as")
t.add(97, "as")
t.add(4, "as")
t.add(20, "as")
t.add(43, "as")
t.add(56, "as")
t.add(61, "as")
t.add(68, "as")
t.add(89, "as")
t.add(100, "as")
t.add(1, "as")
t.add(12, "as")
t.add(19, "as")
t.add(23, "as")
t.add(54, "as")
t.add(62, "as")
t.add(66, "as")
t.add(73, "as")
t.add(87, "as")
t.add(90, "as")
t.add(10, "as")
t.add(15, "as")
t.add(58, "as")
t.delete(64)
t.add(9, "as")
t.add(3, "as")
t.delete(9)
t.delete(15)
t.delete(12)
t.delete(57)
t.add(103, "as")
t.add(98, "as")
t.add(102, "as")
t.delete(103)

t.inorder()
aa = TreeGraph(t)
aa.export()
