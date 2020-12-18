import grammar as g
import tabla as ts
from graphQueries import graphTree
default_db = ''


TS = ts.Tabla()

if __name__ == '__main__':
    f = open("./entrada.txt", "r")
    input = f.read()
    print(input)
    root = g.parse(input)
    graphTree(root)


