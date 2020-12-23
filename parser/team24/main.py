import grammar2 as g
import tablaDGA as TabladeSimbolos
from reportAST import *
from reportError import *
from reportBNF import *
from reportTable import *
default_db = 'DB1'
ts = TabladeSimbolos.Tabla()

def meterSimbolos():
    
    
    ts.agregar(TabladeSimbolos.Simbolo(0,'DB1',TabladeSimbolos.TIPO.DATABASE,None,None, None, None, None, None, None, None,None,None))

    ts.agregar(TabladeSimbolos.Simbolo(1,'tbempleado',TabladeSimbolos.TIPO.TABLE,0,None, None, None, None, None, None, None, None,None))
    ts.agregar(TabladeSimbolos.Simbolo(2,'id',TabladeSimbolos.TIPO.COLUMN,1, None, None, None, None, None, None, None,0,None))
    ts.agregar(TabladeSimbolos.Simbolo(3,'nombre',TabladeSimbolos.TIPO.COLUMN,1,None, None, None, None, None, None, None,1,None))
    ts.agregar(TabladeSimbolos.Simbolo(4,'apellido',TabladeSimbolos.TIPO.COLUMN,1,None, None, None, None, None, None, None,2,None))

    ts.agregar(TabladeSimbolos.Simbolo(5,'tbusuario',TabladeSimbolos.TIPO.TABLE,0,None, None, None, None, None, None, None, None,None))
    
    ts.agregar(TabladeSimbolos.Simbolo(6,'id',TabladeSimbolos.TIPO.COLUMN,5,None, None, None, None, None, None, None,0,None))
    ts.agregar(TabladeSimbolos.Simbolo(7,'nombre',TabladeSimbolos.TIPO.COLUMN,5,None, None, None, None, None, None, None,1,None))
    ts.agregar(TabladeSimbolos.Simbolo(8,'apellido',TabladeSimbolos.TIPO.COLUMN,5,None, None, None, None, None, None, None,2,None))


def analiz(input):
    meterSimbolos()
    raiz = g.parse(input)
    #report_errors()
    #executeGraphTree()
    #graphTable(ts)
    results = []
    for val in raiz:
        if isinstance(val,CError):
            results.append("Error"+ val.tipo+". Descripcion: " +val.descripcion)
        else:
            results.append(val)
    return results
    

    



