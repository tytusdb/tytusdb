from graphviz import Digraph

s = Digraph('ts', node_attr={'shape': 'plaintext'})
s.node_attr.update(shape='plaintext')
tsgen = {}


def iniciar():
    global s
    s = Digraph('ts', node_attr={'shape': 'plaintext'})
    s.node_attr.update(shape='plaintext')


def generarts():
    iniciar()
    global s
    a = '''<
    <TABLE BORDER = "4" CELLBORDER = "1" CELLSPACING = "0">\n'''
    a = a + '''<TR>\n
            <TD>Token id</TD><TD>Nombre</TD><TD>Tipo</TD><TD>Declarada en</TD><TD>Ambito</TD>\n</TR>'''
    for i in tsgen:
        a = a + '''<TR>\n
        <TD>''' + i + '''</TD><TD>''' + tsgen[i]['nombre'] + '''</TD><TD>''' + tsgen[i]['tipo'] + '''</TD><TD>''' + tsgen[i]['declarada_en'] + '''</TD><TD>''' + tsgen[i]['ambito'] + '''</TD>\n</TR>'''
    a = a + '''</TABLE>>'''
    s.node('struct1', '''%s''' % (a))


def verts():
    s.view()
