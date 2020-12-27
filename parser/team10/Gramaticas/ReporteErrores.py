from graphviz import Digraph
import lexico
import RevisionTipos

t_lex = Digraph('lexicos', node_attr={'shape': 'plaintext'})
t_sin = Digraph('sintacticos', node_attr={'shape': 'plaintext'})
t_sem = Digraph('semanticos', node_attr={'shape': 'plaintext'})
t_lex.node_attr.update(shape='plaintext')
t_sin.node_attr.update(shape='plaintext')
t_sem.node_attr.update(shape='plaintext')
esin = []


def iniciar_lexico():
    global t_lex
    t_lex = Digraph('lexicos', node_attr={'shape': 'plaintext'})
    t_lex.node_attr.update(shape='plaintext')

def iniciar_semantico():
    global t_sem
    t_sem = Digraph('semanticos', node_attr={'shape': 'plaintext'})
    t_sem.node_attr.update(shape='plaintext')

def iniciar_sintactico():
    global t_sin
    t_sin = Digraph('sintacticos', node_attr={'shape': 'plaintext'})
    t_sin.node_attr.update(shape='plaintext')



def generar_lexico(t):
    global t_lex
    a = '''<
    <TABLE BORDER = "0" CELLBORDER = "1" CELLSPACING = "0">\n'''
    for i in t:
        a = a + '''<TR>\n
        <TD>"'''+i+'''"</TD>\n</TR>'''
    a = a + '''</TABLE>>'''
    t_lex.node('struct1', '''%s''' % (a))

def generar_sintactico(t):
    global t_sin
    a = '''<
    <TABLE BORDER = "0" CELLBORDER = "1" CELLSPACING = "0">\n'''
    for i in t:
        a = a + '''<TR>\n
            <TD>''' + i + '''</TD>\n</TR>'''
    a = a + '''</TABLE>>'''
    t_sin.node('struct1', '''%s''' % (a))

def generar_semantico(t):
    global t_sem
    a = '''<
    <TABLE BORDER = "0" CELLBORDER = "1" CELLSPACING = "0">\n'''
    for i in t:
        a = a + '''<TR>\n
            <TD>''' + i + '''</TD>\n</TR>'''
    a = a + '''</TABLE>>'''
    t_sem.node('struct1', '''%s''' % (a))


# Generar reporte
def ver_lexicos():
    if len(lexico.elex)>0:
        iniciar_lexico()
        generar_lexico(lexico.elex)
        t_lex.view()

def ver_sintacticos():
    if len(esin) > 0:
        iniciar_sintactico()
        generar_sintactico(esin)
        t_sin.view()

def ver_semanticos():
    if len(RevisionTipos.errorsem) > 0:
        iniciar_semantico()
        generar_semantico(RevisionTipos.errorsem)
        t_sem.view()
