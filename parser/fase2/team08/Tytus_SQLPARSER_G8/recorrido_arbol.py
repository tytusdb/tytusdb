import os

class recorrido_arbol():
    def __init__(self, nodo_arbol):
        self.nodo_arbol = nodo_arbol
        self.cadena = ""
        self.cadenaAux = ""
        self.id_n = 0
    
    def recorrer_arbolito(self,nodo):
        if nodo.id==0:
            nodo.id = self.id_n
            self.id_n = self.id_n+1

        if nodo != None:
            val = str(nodo.id) + " [label=\"" + nodo.valor + "\"];\n"
            self.cadena += val
            for x in nodo.hijos:
                self.cadenaAux += str(nodo.id) + "->" + str(self.id_n) + ";\n"
                self.recorrer_arbolito(x)
    

    def imprimir(self):
        self.recorrer_arbolito(self.nodo_arbol)
        printCuerpo = "digraph arbolAST{\n" + self.cadena + self.cadenaAux + "}\n"

        try:
            f = open('Digraph.dot','w+')
            f.write(printCuerpo)
            f.close()
        except:
            print("No se pudo dibujar el árbol")
        
        #aquí se deberá sustituir por la ruta en la que se encuentre instalado el Graphviz
        cmd = '"D:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe"' + " -Tpng Digraph.dot -o Digraph.png"

        try:
            os.system(cmd)
        except:
            print("Excepción al ejecutar el archivo .dot")