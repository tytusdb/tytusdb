from graphviz import Digraph

from tablaDGA import Tabla
from tablaDGA import Simbolo

def graphTable(tabla : Tabla):
    s = Digraph('structs', filename='reporteTabla.gv', node_attr={'shape': 'plaintext'})
    c = 'lista [label =  <<TABLE> \n <TR><TD>ID</TD><TD>Nombre</TD><TD>Tipo</TD><TD>Ambito</TD><TD>ColTab</TD><TD>TipoCol</TD>' \
        '<TD>LlaveCol</TD><TD>RefCol</TD><TD>DefCol</TD><TD>NullCol</TD><TD>ContsCol</TD><TD>NumCol</TD><TD>Registro</TD></TR> '
    for x in tabla.simbolos.values():
        if isinstance(x,Simbolo):
            c+= '<TR>\n'
            c+= '<TD>\n'
            c+= str(x.id)
            c+= '\n</TD><TD>'
            c+= str(x.nombre)
            c+= '\n</TD><TD>'
            c+= str(x.tipo)
            c+= '\n</TD><TD>'
            c+= str(x.ambito)
            c+= '\n</TD><TD>'
            c+= str(x.coltab)
            c+= '\n</TD><TD>'
            c+= str(x.tipocol)
            c+= '\n</TD><TD>'
            c+= str(x.llavecol)
            c+= '\n</TD><TD>'
            c+= str(x.refcol)
            c+= '\n</TD><TD>'
            c+= str(x.defcol)
            c+= '\n</TD><TD>'
            c+= str(x.nullcol)
            c+= '\n</TD><TD>'
            c+= str(x.constcol)
            c+= '\n</TD><TD>'
            c+= str(x.numcol)
            c+= '\n</TD><TD>'
            c+= str(x.registro)
            c+= '\n</TD></TR>'
    c += '</TABLE>>, ];'
    s.body.append(c)
    s.view()