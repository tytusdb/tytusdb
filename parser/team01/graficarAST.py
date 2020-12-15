import sys 
from graphviz import *
import tempfile
from datetime import datetime
  

dot = Digraph(comment='The Round Table')
x = 0

def inc():
    global x
    x += 1
    return x

def recorrer(arbol):

    if arbol is not None:
        for i in range(0,len(arbol)):
            valor = calcular(arbol[i])

            now = datetime.now()
            dt_string = now.strftime("%d_%m_%Y %H_%M_%S") # dd/mm/YY H:M:S

            dot.attr(splines='true',ordering="out")
            dot.node_attr.update(shape='circle')
            #dot.edge_attr.update(color='blue4')
            dot.render('.\\tempPDF\\'+dt_string+'.gv', view=False)  # doctest: +SKIP
            '.\\tempPDF\\'+dt_string+'.gv.pdf'
        #--fin recorrer

def calcular(arbol):
    print("--#Iniciando calcular")
    #if arbol.hijos is None or arbol.esHoja == 'S':
    if arbol.esHoja == 'S':
        if len(arbol.hijos) == 1:
            id = inc()
            dot.node(str(id),str(arbol.etiqueta))
            dot.attr('node', style='filled', shape='doublecircle', fillcolor='LimeGreen')
            dot.edge(str(id),'#'+str(id)+'[' +str(arbol.lexema)+']')
            #dot.attr('node', shape='circle',color="orange")                
            dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
            return id
        elif len(arbol.hijos) > 1:
            id = inc()
            dot.node(str(id),str(arbol.etiqueta))
            for x in range(0,len(arbol.hijos)):
                #valor = self.calcular(arbol[i])
                dot.attr('node', style='filled', shape='doublecircle', fillcolor='LimeGreen')
                dot.edge(str(id),'#'+str(id)+'[' +str(arbol.hijos[x])+']')
                #dot.attr('node', shape='circle',color="orange")                
                dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
            return id            
    elif len(arbol.hijos) == 1:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno = str(calcular(arbol.hijos[0]))
        dot.edge(str(id),valorRetorno)     
        return id
    
    elif len(arbol.hijos) == 2:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0]))
        valorRetorno2 = str(calcular(arbol.hijos[1]))
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        return id

    elif len(arbol.hijos) == 3:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0]))
        valorRetorno2 = str(calcular(arbol.hijos[1]))
        valorRetorno3 = str(calcular(arbol.hijos[2]))
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        return id

    elif len(arbol.hijos) == 4:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0]))
        valorRetorno2 = str(calcular(arbol.hijos[1]))
        valorRetorno3 = str(calcular(arbol.hijos[2]))
        valorRetorno4 = str(calcular(arbol.hijos[3]))
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        dot.edge(str(id),valorRetorno4)     
        return id
