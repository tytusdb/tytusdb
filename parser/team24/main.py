import grammar as g
import tabla as TabladeSimbolos
from graphQueries import graphTree
default_db = ''


ts = TabladeSimbolos.Tabla()

if __name__ == '__main__':
    f = open("./entrada.txt", "r")
    input = f.read()
    #print(input)
    root = g.parse(input)
    results = []
    for query in root:
        results.append(query.ejecutar())
    print(results)
    #graphTree(root)


