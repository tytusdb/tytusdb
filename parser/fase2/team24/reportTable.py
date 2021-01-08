from graphviz import Digraph

from tablaDGA import Tabla
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)


def graphTable(tabla : Tabla):
    s = Digraph('structs', filename=str(get_random_string(8))+'.gv', node_attr={'shape': 'plaintext'})
    c = 'lista [label =  <<TABLE> \n <TR><TD>ID</TD><TD>Tipo</TD><TD>Nombre</TD>' \
        '<TD>Ambito</TD><TD>tablaind</TD><TD>tipoind</TD><TD>ordenind</TD><TD>valor</TD><TD>columnaind</TD></TR> '
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
        c+= '\n</TD><TD>'
        c+= str(validarNull(x.tablaind))
        c+= '\n</TD><TD>'
        c+= str(validarNull(x.tipoind))
        c+= '\n</TD><TD>'
        c+= str(validarNull(x.ordenind))
        c+= '\n</TD><TD>'
        c+= str(validarNull(x.valor))
        
        c+= '\n</TD><TD>'
        c+= str(validarNull(x.columnaind))
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