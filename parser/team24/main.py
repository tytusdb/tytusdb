import grammar2 as g
import tabla as TabladeSimbolos
from reportAST import *
from reportError import *
from reportBNF import *
from reportTable import *
#from graphQueries import graphTree
default_db = 'DB1'
ts = TabladeSimbolos.Tabla()

def meterSimbolos():
    ts.agregar(TabladeSimbolos.Simbolo(0,TabladeSimbolos.TIPO.DATABASE,'DB1',None,None))
    ts.agregar(TabladeSimbolos.Simbolo(1,TabladeSimbolos.TIPO.TABLE,'tbempleado',0,None))
    ts.agregar(TabladeSimbolos.Simbolo(2,TabladeSimbolos.TIPO.COLUMN,'id',1,0))
    ts.agregar(TabladeSimbolos.Simbolo(3,TabladeSimbolos.TIPO.COLUMN,'nombre',1,1))
    ts.agregar(TabladeSimbolos.Simbolo(4,TabladeSimbolos.TIPO.COLUMN,'apellido',1,2))
    ts.agregar(TabladeSimbolos.Simbolo(5,TabladeSimbolos.TIPO.TABLE,'tbusuario',0,None))
    ts.agregar(TabladeSimbolos.Simbolo(6,TabladeSimbolos.TIPO.COLUMN,'id',5,0))
    ts.agregar(TabladeSimbolos.Simbolo(7,TabladeSimbolos.TIPO.COLUMN,'nombre',5,1))
    ts.agregar(TabladeSimbolos.Simbolo(8,TabladeSimbolos.TIPO.COLUMN,'apellido',5,2))

if __name__ == '__main__':
    f = open("./entrada.txt", "r")
    input = f.read()
    #print(input)
    meterSimbolos()
    root = g.parse(input)

    for val in root:
        print(val.ejecutar())
    



