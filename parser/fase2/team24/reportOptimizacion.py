from graphviz import Digraph

from OptimizarObjetos import Optimizado
from tablaDGA import Tabla

def graphTable(Obj):
    s = Digraph('structs', filename='reporteOptimizacion.gv', node_attr={'shape': 'plaintext'})
    c = 'lista [label =  <<TABLE> \n <TR><TD>Regla</TD><TD>Orignal</TD><TD>Optimizado</TD></TR> '
    for x in Obj:
        if isinstance(x, Optimizado):
            c+= '<TR>\n'
            c+= '<TD>\n'
            c+= str(validarNull(x.regla))
            c+= '\n</TD><TD>'
            c+= str(validarNull(x.original))
            c+= '\n</TD><TD>'
            c+= str(validarNull(x.resultado))
            c+= '\n</TD></TR>'

    c += '</TABLE>>, ];'
    s.body.append(c)
    s.view()

def validarNull(x):
    try:
        if x is not None:
            return str(x)
        else:
            return ''
    except:
        return ''