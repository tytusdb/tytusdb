from graphviz import Digraph

from tablaDGA import Tabla

def graphTable(tabla : Tabla):
    s = Digraph('structs', filename='reporteTabla.gv', node_attr={'shape': 'plaintext'})
    c = 'lista [label =  <<TABLE> \n <TR><TD>ID</TD><TD>Tipo</TD><TD>Valor</TD><TD>Ambito</TD></TR> '
    for x in tabla.simbolos.values():
        c+= '<TR>\n'
        c+= '<TD>\n'
        c+= str(x.id)
        c+= '\n</TD><TD>'
        c+= str(x.tipo)
        c+= '\n</TD><TD>'
        c+= str(x.nombre)
        c+= '\n</TD><TD>'
        c+= str(x.ambito)
        c+= '\n</TD></TR>'
    c += '</TABLE>>, ];'
    s.body.append(c)
    s.view()