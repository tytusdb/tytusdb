import grammar2 as g
import tabla as TabladeSimbolos
from reportAST import *
from reportError import *
from reportBNF import *
#from graphQueries import graphTree
default_db = 'DB1'
ts = TabladeSimbolos.Tabla()

def meterSimbolos():
    ts.agregar(TabladeSimbolos.Simbolo(0,TabladeSimbolos.TIPO.DATABASE,'DB1',None,None))
    ts.agregar(TabladeSimbolos.Simbolo(1,TabladeSimbolos.TIPO.TABLE,'tbempleado',0,None))
    ts.agregar(TabladeSimbolos.Simbolo(2,TabladeSimbolos.TIPO.COLUMN,'id',1,0))
    ts.agregar(TabladeSimbolos.Simbolo(3,TabladeSimbolos.TIPO.COLUMN,'nombre',1,1))
    ts.agregar(TabladeSimbolos.Simbolo(4,TabladeSimbolos.TIPO.COLUMN,'apellido',1,2))

if __name__ == '__main__':
    f = open("./entrada.txt", "r")
    input = f.read()
    #print(input)
    meterSimbolos()
    root = g.parse(input)
    #ejemplo para sacar el arbol
    executeGraphTree(root)
    #ejemplo para sacar los errores, cada vez que se ejecuta se limpia la lista al final
    # es decir que si se ejecuta dos veces seguidas sin ejecuciones de por medio, el segundo reporte estaria vacio
    report_errors()
    report_BNF()

    #for val in root:
        #print(val.ejecutar())
    #graphTree(root)



