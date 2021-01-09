import os
import nodoGeneral

class GraphArbol():
    

    def __init__(self,raiz):
        self.raiz = raiz
        self.cuerpo = ""
        self.cuerpoaux = ""

    def crearCuerpo(self, raiz):
        if raiz !=None:
            if isinstance(raiz,nodoGeneral.NodoGeneral):                            
                
                for hijo in raiz.hijos:
                    if isinstance(hijo,nodoGeneral.NodoGeneral):
                        self.cuerpo += "\"" + str(raiz.numeroNodo) + "_" + raiz.nombreNodo + " -> " + str(raiz.valor) + "\"->\"" + str(hijo.numeroNodo) + "_" + hijo.nombreNodo + " -> " + str(hijo.valor) + "\"\n"
                        self.crearCuerpo(hijo)
                        
        



    def crearArbol(self):
        self.crearCuerpo(self.raiz)
        printCuerpo="digraph G {node[shape=box, style=filled, color=blanchedalmond]; edge[color=chocolate3];rankdir=UD \n"
        printCuerpo += self.cuerpo
        printCuerpo += "\n}"

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
            print("Ejecutado")
        except: 
            print("An exception ocurred")
