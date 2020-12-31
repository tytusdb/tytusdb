# AVL Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team
# Developers: SG#16


from ..Models.node import Node


class AVLTree:
    def __init__(self, database: str, name: str, numberColumns: int, pklist: list = []):
        self.root = None
        self.database = database
        self.name = name
        self.numberColumns = int(numberColumns)
        self.pklist = pklist
        self.hidden = 1

    def __repr__(self) -> str:
        return str(self.name)

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

    def update(self, index, content):
        self.root = self.__update(index, content, self.root)

    def __update(self, index, content, node):
        if node:
            if node.index == index:
                node.content = content
                return node
            elif node.index < index:
                node.right = self.__update(index, content, node.right)
            else:
                node.left = self.__update(index, content, node.left)
            return node
        return None

    def tolist(self) -> list:
        return self.__tolist(self.root, tuples=[]) if self.root is not None else []

    def __tolist(self, node: Node, tuples: list) -> list:
        if node:
            tuples.append(node.content)
            self.__tolist(node.left, tuples)
            self.__tolist(node.right, tuples)
            return tuples

    def indexes(self) -> list:
        return self.__indexes(self.root, indexes=[]) if self.root is not None else []

    def __indexes(self, node: Node, indexes: list) -> list:
        if node:
            indexes.append(node.index)
            self.__indexes(node.left, indexes)
            self.__indexes(node.right, indexes)
            return indexes

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

    def range(self, columnNumber: int, lower: any, upper: any) -> list:
        tuples = []
        return self.__range(self.root, tuples, columnNumber, lower, upper) if self.root is not None else []

    def __range(self, node: Node, tuples: list, columnNumber: int, lower: any, upper: any) -> list:
        if node:
            if isinstance(node.content[columnNumber], int):
                if int(lower) <= node.content[columnNumber] <= int(upper):
                    tuples.append(node.content)
            elif isinstance(node.content[columnNumber], str):
                if str(lower) <= node.content[columnNumber] <= str(upper):
                    tuples.append(node.content)
            elif isinstance(node.content[columnNumber], float):
                if float(lower) <= node.content[columnNumber] <= float(upper):
                    tuples.append(node.content)
            elif isinstance(node.content[columnNumber], bool):
                if bool(lower) <= node.content[columnNumber] <= bool(upper):
                    tuples.append(node.content)
            self.__range(node.left, tuples, columnNumber, lower, upper)
            self.__range(node.right, tuples, columnNumber, lower, upper)
            return tuples

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
