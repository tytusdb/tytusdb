import os

#definición del objeto nodo para crear el arbol
class Nodo():

    def __init__(self, etiqueta, idnodo):
        self.etiqueta = etiqueta
        self.idnodo = idnodo
        self.hijos = []

    def addNodo(self, hijo):
        self.hijos.append(hijo)
    
    def updateID(self, idnodo):
        self.idnodo = idnodo
    
    def clearHijos(self):
        self.hijos.clear()

#definición del objeto AST
class GraphArbol():

    def __init__(self, raiz):
        self.raiz = raiz
        self.cuerpo = ""
        self.cuerpoaux = ""

    def crearCuerpo(self, raiz):
        if raiz != None:
            self.cuerpo += str(raiz.idnodo) + " [label=\"" + raiz.etiqueta + "\"];\n"
            for hijo in raiz.hijos:
                self.crearCuerpo(hijo)
                self.cuerpoaux += str(raiz.idnodo) + "->" + str(hijo.idnodo) + ";\n"

    def crearArbol(self):
        self.crearCuerpo(self.raiz)
        printCuerpo = "digraph arbolAST{\n" + self.cuerpo + self.cuerpoaux + "}\n"

        try:
            f = open('Arbol.dot','w+')
            f.write(printCuerpo)
            f.close()
        except:
            print("Excepción al dibujar el árbol")
        
        #aquí se deberá sustituir por la ruta en la que se encuentre instalado el Graphviz
        cmd = '"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe"' + " -Tpng Arbol.dot -o Arbol.png"

        try:
            os.system(cmd)
        except:
            print("Excepción al ejecutar el archivo .dot")