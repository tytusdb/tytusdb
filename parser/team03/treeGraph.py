from graphviz import Digraph
import subprocess


s="\n"
i = 0
gram="# REPORTE DE GRAMATICA EN EJECUCION \n\n"

def inc():
    global i
    i += 1
    return i

def existelement(value, ray=[]):
    try:
        if value.graph_ref in ray:
            return True
        else:
            return False
    except:
        pass


def graph_node(value, arreglo=[], child_indices=[]):
    global s 
    graph_id = inc()

    padre = "A"+str(graph_id)+'[label = "'+str(value) +'" width = 1.5 style = filled, fillcolor = lightskyblue]; \n'
    listahijos = "A"+str(graph_id) +' ->{'

    allhijos=""
   
    for child in arreglo:
        if existelement(child,child_indices):
            listahijos = listahijos + child.graph_ref +","
        else:
            if child != None:
                idhijo = inc()
                listahijos=listahijos +"A"+ str(idhijo) + ","
                hijo= "A"+str(idhijo)+'[label = "'+str(child)+'" width = 1.5 style = filled, fillcolor = lightskyblue];\n'
                allhijos = allhijos + hijo
    temp = len(listahijos)        
    listahijos = listahijos[:temp - 1]
    listahijos = listahijos +"}\n"
    if len(arreglo) ==0:
        s = padre +s
        return "A"+str(graph_id)
    else:
        s =  padre + listahijos + allhijos+s 
        return "A"+str(graph_id)



def createFile():
    archivo = open('reportGrammar.md', 'w')
    archivo.write(gram)
    archivo.close()

def creategrafo():
    global s
    s="digraph Matrix { node [shape=box] e0[ shape = point, width = 0 ];\n"+s+"}"
    archivo = open('grap.txt', 'w')
    archivo.write(s)
    archivo.close()

    comando = "dot -Tpng "+ "grap" +".txt -o "+ "grap" +".png"
    resultado = subprocess.Popen(comando,shell=True,stdout=subprocess.PIPE)   #manda a consola la instruccion
    for salida in resultado.stdout:
        print(salida.decode(sys.getdefaultencoding()).rstrip())            #imprime algun posible error que pueda suceder

    comando2 = "start "+ "grap" +".png"
    resultado2 = subprocess.Popen(comando2,shell=True,stdout=subprocess.PIPE)
    for salida2 in resultado2.stdout:
        print(salida2.decode(sys.getdefaultencoding()).rstrip())



def addCad(cadena):
    global gram
    gram = gram + cadena + "\n"+"<br>"+"\n\n" 


#recibo un arreglo y devuelve solamento los indices que quiero
def addChild(arregloT, cualesNecesito=[]):
    childs=[]
    for i in cualesNecesito:
        childs.append(arregloT[i])
    return childs        

#recibo un arreglo y devuelvo cuales no son None, indices que recibe tienen que ser producciones
def addNotNoneChild(arregloT, cualesVerifico=[]):
    childs=[]
    for i in cualesVerifico:         
        if arregloT[i] != None :
            childs.append(str(arregloT[i].graph_ref))
    return childs        









##solo es para sintetizar el id de los nodos,,, borrar cuando ya no se use
class upNodo:
    def __init__(self, val, line, column, graph_ref):
        self.val = val
        self.graph_ref = graph_ref

    def execute(self,val,line):
        pass
