class node():
    def __init__(self, padre, hijo,  valor):
        self.padre = padre
        self.hijo = hijo
        self.valor = valor





class nodeGramatical():
    def __init__(self, produccion, reglas):
        self.produccion = produccion
        self.reglas = reglas



class genera() :
    def add(self, nodo):
        Grafica = open('../Reportes/AST.dot','a')     #creamos el archivo

        Grafica.write(f"n00{str(nodo.padre)} -- n00{str(nodo.hijo)};\n")
        Grafica.write(f"n00{str(nodo.hijo)} [label=\"{nodo.valor}\"] ;\n")

        Grafica.close()