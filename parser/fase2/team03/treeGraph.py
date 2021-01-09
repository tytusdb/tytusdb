from graphviz import Digraph
import subprocess

s = "\n"
i = 0
gram = ""
childslist = "inicio -> {"


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

    padre = "A" + str(graph_id) + '[label = "' + str(
        value) + '" width = 1.5 style = filled, fillcolor = lightskyblue]; \n'
    listahijos = "A" + str(graph_id) + ' ->{'

    allhijos = ""

    for child in arreglo:
        if existelement(child, child_indices):
            listahijos = listahijos + child.graph_ref + ","
        else:
            if child != None:
                idhijo = inc()
                listahijos = listahijos + "A" + str(idhijo) + ","
                hijo = "A" + str(idhijo) + '[label = "' + str(
                    child) + '" width = 1.5 style = filled, fillcolor = lightskyblue];\n'
                allhijos = allhijos + hijo
    temp = len(listahijos)
    if listahijos[temp - 1] == ",":
        listahijos = listahijos[:temp - 1]
        listahijos = listahijos + "}\n"
    elif listahijos[temp - 1] == "{":
        listahijos = listahijos + "}\n"

    if len(arreglo) == 0:
        s = padre + s
        return "A" + str(graph_id)
    else:
        s = padre + listahijos + allhijos + s
        return "A" + str(graph_id)


def createFile():
    global gram
    gram = "# REPORTE DE GRAMATICA EN EJECUCION \n\n" + gram
    archivo = open('reportGrammar.md', 'w')
    archivo.write(gram)
    archivo.close()


def creategrafo():
    global s
    global childslist
    temp = len(childslist)
    if childslist[temp - 1] == ",":
        childslist = childslist[:temp - 1]
        childslist = childslist + "}\n"
    elif childslist[temp - 1] == "{":
        childslist = childslist + "}\n"
    s = "digraph Matrix { graph [dpi=300]; \n node [shape=box] e0[ shape = point, width = 0 ];\n inicio[label = \"Inicio\" width = 1.5 style = filled, fillcolor = firebrick1];  " + childslist + s + "}"

    archivo = open('grap.dot', 'w')
    archivo.write(s)
    archivo.close()

    comando = "dot -Tpng " + "grap" + ".dot -o " + "grap" + ".png"
    resultado = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)  # manda a consola la instruccion
    for salida in resultado.stdout:
        print(salida.decode(sys.getdefaultencoding()).rstrip())  # imprime algun posible error que pueda suceder

    comando2 = "start " + "grap" + ".png"
    resultado2 = subprocess.Popen(comando2, shell=True, stdout=subprocess.PIPE)
    for salida2 in resultado2.stdout:
        print(salida2.decode(sys.getdefaultencoding()).rstrip())


def punteroinicio(nombre):
    global childslist
    childslist = childslist + nombre + ","


def addCad(cadena):
    global gram
    gram = cadena + "\n" + "<br>" + "\n\n" + gram


# recibo un arreglo y devuelve solamento los indices que quiero
def addChild(arregloT, cualesNecesito=[]):
    childs = []
    for i in cualesNecesito:
        childs.append(arregloT[i])
    return childs


# recibo un arreglo y devuelvo cuales no son None, indices que recibe tienen que ser producciones
def addNotNoneChild(arregloT, cualesVerifico=[]):
    childs = []
    for i in cualesVerifico:
        if arregloT[i] != None:
            childs.append(str(arregloT[i].graph_ref))
    return childs


def generateReports():
    createFile()
    creategrafo()
    global s
    s = "\n"
    global i
    i = 0
    global gram
    gram = ""
    global childslist
    childslist = "inicio -> {"


##solo es para sintetizar el id de los nodos,,, borrar cuando ya no se use
class upNodo:
    def __init__(self, val, line, column, graph_ref):
        self.line = line
        self.column = column
        self.val = val
        self.graph_ref = graph_ref

    def execute(self, table, tree):
        pass

    def generate(self, table, tree):
        raise Exception('¡¡¡You are trying to generate TAC for an Non value AS node!!!') 
