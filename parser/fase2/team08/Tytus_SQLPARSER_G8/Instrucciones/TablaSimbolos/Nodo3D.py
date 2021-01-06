class Nodo3D():
    def __init__(self):
        self.temporalAnterior = ""
        self.etiquetaTrue = ""
        self.etiquetaFalse = ""

    
    def imprimirEtiquetDestino(self, arbol, etiquetas):
        if(etiquetas == ""):
            return
        lista = etiquetas.split(",")
        for i in range(0,len(lista)):
            arbol.addc3d("label ."+lista[i])

    def imprimirEtiquetOrigen(self, arbol, etiquetas):
        if(etiquetas == ""):
            return
        lista = etiquetas.split(",")
        for i in range(0,len(lista)):
            arbol.addc3d("goto ."+lista[i]+"")
    