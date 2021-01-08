# B+ Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

import os
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.struc = None

class AVLTree:

    def __init__(self):
        self.AVLroot = None

    def add(self, root, key):
        if not root:
            self.AVLroot = TreeNode(key)
            return TreeNode(key)
        elif key.upper() < root.val.upper():
            root.left = self.add(root.left, key)
        else:
            root.right = self.add(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        # Caso 1 - LL
        if balance > 1 and key.upper() < root.left.val.upper():
            return self.rightRotate(root)

        # Caso 2 - RR
        if balance < -1 and key.upper() > root.right.val.upper():
            return self.leftRotate(root)

        # Caso 3 - LR
        if balance > 1 and key.upper() > root.left.val.upper():
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Caso 4 - RL
        if balance < -1 and key.upper() < root.right.val.upper():
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        self.AVLroot = root
        return root

    def delete(self, root, key):

        if not root:
            return root

        elif key.upper() < root.val.upper():
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                self.AVLroot = temp
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                self.AVLroot = temp
                return temp

            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                     temp.val)

        if root is None:
            self.AVLroot = root
            return root

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBalance(root)

        # Caso 1 - LL
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        # Caso 2 - RR
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        # Caso 3 - LR
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Caso 4 - RL
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        self.AVLroot = root
        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        self.AVLroot = y
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        self.AVLroot = y
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def preOrder(self, root, f, nodes):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        name = 'Nodo' + ''.join(str(root.val))
        f.write(name + ' [label = "' + root.val + '"];\n')
        if root.left:
            connection = 'Nodo' + ''.join(str(root.val)) + '->' + 'Nodo' + ''.join(str(root.left.val)) + ';\n'
            nodes.append(connection)
        if root.right:
            connection = 'Nodo' + ''.join(str(root.val)) + '->' + 'Nodo' + ''.join(str(root.right.val)) + ';\n'
            nodes.append(connection)
        self.preOrder(root.left, f, nodes)
        self.preOrder(root.right, f, nodes)

        # List all the keys in postorder
    def postOrder(self, root):
        if root:
            return self.postOrder(root.left).strip() + self.postOrder(root.right).strip() + root.val + "-"
        else:
            return ""

    # Check if the key exists and returns the node
    def search(self, root, key):
        if root:
            if root.val.upper() == key.upper():
                return root
            elif key.upper() < root.val.upper():
                return self.search(root.left, key)
            else:
                return self.search(root.right, key)
        else:
            return None

    def getRoot(self):
        return self.AVLroot

    def graph(self, database):
        nodes = []
        if database == "Databases":
            f = open('bases.dot', 'w', encoding='utf-8')
        else:
            f = open(f'{database}.dot', 'w', encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('graph [ordering="out"];')
        f.write('rankdir=TB;\n')
        f.write('node [shape = box];\n')
        self.preOrder(self.getRoot(), f, nodes)
        for x in nodes:
            f.write(x)
        f.write('}')
        f.close()
        if database == "Databases":
            os.system('dot -Tpng bases.dot -o ./Data/BPlusMode/DataBases.png')
        else:
            os.system(f'dot -Tpng {database}.dot -o ./Data/BPlusMode/{database}/{database}.png')
        # os.system('C:/Users/Marcos/Desktop/Data/DataBases.png')