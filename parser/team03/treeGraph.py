from graphviz import Digraph

dot = Digraph(comment='The Round Table')
dot.node_attr.update(shape='circle')
dot.node_attr.update(fontcolor='black')
dot.node_attr.update(margin='0')
dot.node_attr.update(fontsize='15')
dot.node_attr.update(width='0.5')
dot.node_attr.update(style='filled')
dot.node_attr.update(fillcolor='lightyellow1')

dot.edge_attr.update(color='firebrick')




i =0

def inc():
    global i
    i +=1
    return i

def nodoHoja(valor):
    id= inc()
    dot.node(str(id),str(valor))
    return id

def nodoDosAristas(valor,izquierda,derecha):
    id= inc()
    dot.node(str(id),str(valor))
    dot.edge(str(id),str(izquierda))
    dot.edge(str(id),str(derecha))
    return id
    
def nodoTresAristas(valor,izquierda,derecha,medio):
    id= inc()
    dot.node(str(id),str(valor))
    dot.edge(str(id),str(izquierda))
    dot.edge(str(id),str(medio))    
    dot.edge(str(id),str(derecha))
    return id

    