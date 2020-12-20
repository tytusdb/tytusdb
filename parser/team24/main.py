import grammar as g
import tabla as TabladeSimbolos
from graphQueries import graphTree
default_db = 'DB1'
ts = TabladeSimbolos.Tabla()

def meterSimbolos():
    ts.agregar(TabladeSimbolos.Simbolo(0,TabladeSimbolos.TIPO.DATABASE,'DB1',None,None))
    ts.agregar(TabladeSimbolos.Simbolo(1,TabladeSimbolos.TIPO.TABLE,'tbempleado',0,None))
    ts.agregar(TabladeSimbolos.Simbolo(2,TabladeSimbolos.TIPO.COLUMN,'id',1,0))
    ts.agregar(TabladeSimbolos.Simbolo(3,TabladeSimbolos.TIPO.COLUMN,'nombre',1,1))
    

if __name__ == '__main__':
    f = open("./entrada.txt", "r")
    input = f.read()
    #print(input)
    meterSimbolos()
    root = g.parse(input)
    results = []
    for query in root:
        results.append(query.ejecutar())
    print(results)
    #graphTree(root)



