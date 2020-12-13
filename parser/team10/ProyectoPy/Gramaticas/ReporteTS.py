from graphviz import Digraph

t_lex = Digraph('ts', node_attr={'shape': 'plaintext'})
t_lex.node_attr.update(shape='plaintext')
tsgen = {}


def iniciar():
    global t_lex
    s = Digraph('ts', node_attr={'shape': 'plaintext'})
    s.node_attr.update(shape='plaintext')

def generarts():
    iniciar()
    global t_lex
    a = '''<
    <TABLE BORDER = "4" CELLBORDER = "1" CELLSPACING = "0">\n'''
    a = a + '''<TR>\n
            <TD>Token id</TD><TD>Nombre</TD><TD>Tipo</TD><TD>Dimension</TD><TD>Declarada en</TD>\n</TR>'''
    for i in tsgen:
        a = a + '''<TR>\n
        <TD>'''+i+'''</TD><TD>'''+tsgen[i]['nombre']+'''</TD><TD>'''+tsgen[i]['tipo']+'''</TD><TD>'''+tsgen[i]['dimension']+'''</TD><TD>'''+tsgen[i]['declarada_en']+'''</TD>\n</TR>'''
    a = a + '''</TABLE>>'''
    t_lex.node('struct1','''%s'''%(a))

def verts():
    t_lex.view()
