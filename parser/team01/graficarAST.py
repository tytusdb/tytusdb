import sys 
import ts as TS
from graphviz import *
import tempfile
from datetime import datetime
  

dot = Digraph(comment='The Round Table')
contador = 1
x = 0

def inc():
    global x
    x += 1
    return x

def recorrer(arbol, ts):

    if arbol is not None:
        for i in range(0,len(arbol)):
            global contador 
            contador += 1
            valor = calcular(arbol[i],ts)

            now = datetime.now()
            dt_string = now.strftime("%d_%m_%Y %H_%M_%S") # dd/mm/YY H:M:S

            dot.attr(splines='true',ordering="out")
            dot.node_attr.update(shape='circle')
            #dot.edge_attr.update(color='blue4')
            dot.render('.\\tempPDF\\'+dt_string+'.gv', view=False)  # doctest: +SKIP
            '.\\tempPDF\\'+dt_string+'.gv.pdf'
        #--fin recorrer

def calcular(arbol,ts):
    global contador
    contador += 1
    print("===============================================================")
    print("--#Iniciando calcular[" + str(contador)+"]"+"["+str(arbol)+"]")
    print("                                             [\'\'\'"+str(arbol.etiqueta)+"]")
    print("===============================================================")

    #if arbol.hijos is None or arbol.esHoja == 'S':
    if arbol.esHoja == 'S':
        if len(arbol.hijos) == 1:
            id = inc()
            dot.node(str(id),str(arbol.etiqueta))
            dot.attr('node', style='filled', shape='doublecircle', fillcolor='LimeGreen')
            dot.edge(str(id),'#'+str(id)+'[' +str(arbol.lexema)+']')
            #dot.attr('node', shape='circle',color="orange")                
            dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')

            simbolo = TS.Simbolo(str(arbol.etiqueta), TS.TIPO_DATO.ETIQUETA, str(arbol.lexema))      # inicializamos con 0 como valor por defecto
            ts.agregar(simbolo)   

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
        valorRetorno = str(calcular(arbol.hijos[0],ts))
        dot.edge(str(id),valorRetorno)     
        return id
    
    elif len(arbol.hijos) == 2:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        return id

    elif len(arbol.hijos) == 3:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        valorRetorno3 = str(calcular(arbol.hijos[2],ts))
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        return id

    elif len(arbol.hijos) == 4:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        valorRetorno3 = str(calcular(arbol.hijos[2],ts))
        valorRetorno4 = str(calcular(arbol.hijos[3],ts))
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        dot.edge(str(id),valorRetorno4)     
        return id

    elif len(arbol.hijos) == 5:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        valorRetorno3 = str(calcular(arbol.hijos[2],ts))
        valorRetorno4 = str(calcular(arbol.hijos[3],ts))
        valorRetorno5 = str(calcular(arbol.hijos[4],ts))
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        dot.edge(str(id),valorRetorno4)     
        dot.edge(str(id),valorRetorno5)     
        return id



    elif len(arbol.hijos) == 6:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        valorRetorno3 = str(calcular(arbol.hijos[2],ts))
        valorRetorno4 = str(calcular(arbol.hijos[3],ts))
        valorRetorno5 = str(calcular(arbol.hijos[4],ts))
        valorRetorno6 = str(calcular(arbol.hijos[5],ts))
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        dot.edge(str(id),valorRetorno4)     
        dot.edge(str(id),valorRetorno5)     
        dot.edge(str(id),valorRetorno6)     
        return id


    elif len(arbol.hijos) == 7:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        valorRetorno3 = str(calcular(arbol.hijos[2],ts))
        valorRetorno4 = str(calcular(arbol.hijos[3],ts))
        valorRetorno5 = str(calcular(arbol.hijos[4],ts))
        valorRetorno6 = str(calcular(arbol.hijos[5],ts))       
        valorRetorno7 = str(calcular(arbol.hijos[6],ts))      
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        dot.edge(str(id),valorRetorno4)     
        dot.edge(str(id),valorRetorno5)     
        dot.edge(str(id),valorRetorno6)        
        dot.edge(str(id),valorRetorno7)  
        return id


    elif len(arbol.hijos) == 8:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        valorRetorno3 = str(calcular(arbol.hijos[2],ts))
        valorRetorno4 = str(calcular(arbol.hijos[3],ts))
        valorRetorno5 = str(calcular(arbol.hijos[4],ts))
        valorRetorno6 = str(calcular(arbol.hijos[5],ts))     
        valorRetorno7 = str(calcular(arbol.hijos[6],ts))
        valorRetorno8 = str(calcular(arbol.hijos[7],ts))        
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        dot.edge(str(id),valorRetorno4)     
        dot.edge(str(id),valorRetorno5)     
        dot.edge(str(id),valorRetorno6)     
        dot.edge(str(id),valorRetorno7)   
        dot.edge(str(id),valorRetorno8)           
        return id


    elif len(arbol.hijos) == 9:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        valorRetorno3 = str(calcular(arbol.hijos[2],ts))
        valorRetorno4 = str(calcular(arbol.hijos[3],ts))
        valorRetorno5 = str(calcular(arbol.hijos[4],ts))
        valorRetorno6 = str(calcular(arbol.hijos[5],ts))        
        valorRetorno7 = str(calcular(arbol.hijos[6],ts)) 
        valorRetorno8 = str(calcular(arbol.hijos[7],ts)) 
        valorRetorno9 = str(calcular(arbol.hijos[8],ts)) 
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        dot.edge(str(id),valorRetorno4)     
        dot.edge(str(id),valorRetorno5)     
        dot.edge(str(id),valorRetorno6)     
        dot.edge(str(id),valorRetorno7)     
        dot.edge(str(id),valorRetorno8)     
        dot.edge(str(id),valorRetorno9)     
        return id

    elif len(arbol.hijos) == 10:
        id = inc()
        dot.attr('node', style='filled', shape='circle', fillcolor='NavajoWhite')
        dot.node(str(id),str(arbol.etiqueta))
        valorRetorno1 = str(calcular(arbol.hijos[0],ts))
        valorRetorno2 = str(calcular(arbol.hijos[1],ts))
        valorRetorno3 = str(calcular(arbol.hijos[2],ts))
        valorRetorno4 = str(calcular(arbol.hijos[3],ts))
        valorRetorno5 = str(calcular(arbol.hijos[4],ts))
        valorRetorno6 = str(calcular(arbol.hijos[5],ts))        
        valorRetorno7 = str(calcular(arbol.hijos[6],ts)) 
        valorRetorno8 = str(calcular(arbol.hijos[7],ts)) 
        valorRetorno9 = str(calcular(arbol.hijos[8],ts)) 
        valorRetorno10 = str(calcular(arbol.hijos[9],ts)) 
        dot.edge(str(id),valorRetorno1)     
        dot.edge(str(id),valorRetorno2)     
        dot.edge(str(id),valorRetorno3)     
        dot.edge(str(id),valorRetorno4)     
        dot.edge(str(id),valorRetorno5)     
        dot.edge(str(id),valorRetorno6)     
        dot.edge(str(id),valorRetorno7)  
        dot.edge(str(id),valorRetorno8)     
        dot.edge(str(id),valorRetorno9)  
        dot.edge(str(id),valorRetorno10)                
        return id                                                
