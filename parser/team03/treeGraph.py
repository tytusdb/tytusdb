from graphviz import Digraph

dot = Digraph(comment='Team 03 Tree')
dot.node_attr.update(shape='circle')
dot.node_attr.update(fontcolor='black')
dot.node_attr.update(margin='0')
dot.node_attr.update(fontsize='15')
dot.node_attr.update(wgraph_idth='0.5')
dot.node_attr.update(style='filled')
dot.node_attr.update(fillcolor='lightyellow1')

dot.edge_attr.update(color='firebrick')

i = 0
gram="# REPORTE DE GRAMATICA EN EJECUCION \n\n"

def inc():
    global i
    i += 1
    return i


def graph_node(value, child_list=[]):
    graph_id = inc()
    dot.node(str(graph_id), str(value))
    for child in child_list:
        dot.edge(str(graph_id), str(child))
    return graph_id


def createFile():
    archivo = open('reportGrammar.md', 'w')
    archivo.write(gram)
    archivo.close()


def addCad(cadena):
    global gram
    gram = gram + cadena + "\n"+"<br>"+"\n\n" 