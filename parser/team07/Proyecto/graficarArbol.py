import os

class GraphArbol():
    

    def __init__(self,raiz):
        self.raiz = raiz
        self.cuerpo = ""
        self.cuerpoaux = ""

    def crearCuerpo(self, raiz):
        if raiz !=None:
            self.cuerpo += str(raiz.idnodo)+" [label=\""+raiz.etiqueta + "\"];\n"
            for hijo in raiz.hijos:
                self.crearCuerpo(hijo)
                self.cuerpoaux += str(raiz.idnodo)+"->"+str(hijo.idnodo)+";\n"
        



    def crearArbol(self):
        self.crearCuerpo(self.raiz)
        printCuerpo="digraph arbolAST{\n"+self.cuerpo+self.cuerpoaux+"}\n"
        #print(printCuerpo)

        try:
            f= open('Arbol.dot','w+')
            f.write(printCuerpo)
            f.close()
        except: 
            print("An exception ocurred")

        cmd ='"C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe"' + " -Tpng Arbol.dot -o Arbol.png"
        try:
            os.system(cmd)
        except: 
            print("An exception ocurred")
