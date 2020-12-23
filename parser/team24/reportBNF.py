from graphviz import Digraph

lista_gramatica = []
reglas_gramaticales = []

def insertProduction(listaP, rango):
    c = str(listaP[0]) + ' :: = '
    for x in range(1, rango):
        c += str(listaP[x].type) + ' '
    lista_gramatica.append(c)
    insertRegla(c)

def insertRegla(regla):
    reglas_gramaticales.append(str(regla))

def report_BNF():
    global lista_gramatica
    global reglas_gramaticales
    l = len(lista_gramatica)
    s = Digraph('structs', filename='reporteBNF.gv', node_attr={'shape': 'plaintext'})
    c = 'lista [label =  <<TABLE> \n <TR><TD>Producciones</TD><TD>Regla</TD></TR> '
    for x in range(0, l):
        c+= '<TR>\n'
        c+= '<TD>\n'
        c+= str(lista_gramatica.pop())
        c+= '\n</TD><TD>'
        c+= str(reglas_gramaticales.pop())
        c+= '\n</TD></TR>'
    c += '</TABLE>>, ];'
    s.body.append(c)
    s.view()