import re
import json
from graphviz import Digraph

graph2 = Digraph('structs', filename='tree.gv', node_attr={'shape': 'record'})


# *** Tree representation ***
class Node(object):
    def __init__(self, title):
        self.title = title
        self.parent = None
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.parent = self


# *** Node insertion logic ***
class Inserter(object):
    def __init__(self, node, depth=0):
        self.node = node
        self.depth = depth

    def __call__(self, title, depth):
        newNode = Node(title)
        if (depth > self.depth):
            self.node.add(newNode)
            self.depth = depth
        elif (depth == self.depth):
            if isinstance(self.node.parent, Node):
                self.node.parent.add(newNode)
        else:
            parent = self.node.parent
            for i in range(0, self.depth - depth):
                if isinstance(parent, Node):
                    parent = parent.parent
            if isinstance(parent, Node):
                parent.add(newNode)
            self.depth = depth
        self.node = newNode


def print_tree(node):
    global graph2
    graph2.node(str(node), '{' + str(node.title) + '}')
    if node is not None and node.parent is not None:
        graph2.edge(str(node.parent), str(node))
    for child in node.children:
        print_tree(child)


# *** File iteration logic ***

def tos_string(d, depth=0):
    if not isinstance(d, (dict, list)):
        return f"{' ' * (depth * 5)}{d}"
    if isinstance(d, list):
        return '\n'.join(f'{" " * (depth * 5)}{i}\n{tos_string(a, depth + 1)}' for i, a in enumerate(d, 1))
    return '\n'.join(f'{" " * (depth * 5)}{a}\n{tos_string(b, depth + 1)}' for a, b in d.items())


inputFile = r'entrada2.txt'
outputFile = r'salida.dot'


def executeGraphTree(data):
    global graph2
    json_data = json.dumps({'raiz': data}, default=lambda o: o.__dict__, indent=4)
    json_data = json_data.replace("[]", "null")
    json_data = json_data.replace(">", "MAYOR")
    json_data = json_data.replace("<", "MENOR")
    #print(json_data)
    with open('entrada2.txt', 'w') as f:
        stringNew = ''
        tempstr = tos_string(json.loads(json_data)).replace('     ', '\t')
        x = tempstr.split('\n')
        count = 0
        for y in x:
            if (count + 1) == len(x):
                stringNew += y + '_' + str(count)
            else:
                stringNew += y + '_' + str(count) + '\n'
            count = count + 1
        f.write(tempstr)
        f.close()

    with open(inputFile, 'r') as f:
        radice = f.readline().rstrip('\n')
        #print(radice)
        tree = Node(radice)
        inserter = Inserter(tree)
        #print(inserter)
        if inserter == None:
            #print('caxxo')
            pass
        for line in f:
            line = line.rstrip('\n')
            #print(line)
            # note there's a bug with your original tab parsing code:
            # it would count all tabs in the string, not just the ones
            # at the beginning
            tabs = re.match('\t*', line).group(0).count('\t')
            title = line[tabs:]
            inserter(title, tabs)

    graph2 = Digraph('structs', filename='tree.gv', node_attr={'shape': 'record'})
    print_tree(tree)
    graph2.view()