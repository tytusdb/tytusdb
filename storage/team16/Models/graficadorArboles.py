import os


class Graficador:
    def __init__(self, arbol, tipo):
        self.contenido = ""
        self.arbol = arbol
        self.tipo = tipo
        if tipo == 'bs':
            self.titulo = 'Arbol Binario De Busqueda BS'
        elif tipo == 'avl':
            self.titulo = 'Arbol Binario Balanceado AVL'

    def __graficar(self):
        self.__contenidoRecursivo(self.arbol.raiz)

    def __contenidoRecursivo(self, aux):
        if aux.izquierdo is not None:
            if self.tipo == 'avl':
                self.contenido = self.contenido + "\"" + aux.getDato() + "\n" + str(aux.peso) + "\"" \
                                    " -> \"" + aux.izquierdo.getDato() + "\n" + str(aux.izquierdo.peso) + "\" \n"
            else:
                self.contenido = self.contenido + aux.getDato() + " -> " + aux.izquierdo.getDato() + "\n"
            self.__contenidoRecursivo(aux.izquierdo)
        if aux.derecho is not None:
            if self.tipo == 'avl':
                self.contenido = self.contenido + "\"" + aux.getDato() + "\n" + str(aux.peso) + "\"" \
                                            " -> \"" + aux.derecho.getDato() + "\n" + str(aux.derecho.peso) + "\" \n"
            else:
                self.contenido = self.contenido + aux.getDato() + " -> " + aux.derecho.getDato() + "\n"
            self.__contenidoRecursivo(aux.derecho)
        if aux.izquierdo is None or aux.derecho is None:
            if aux.dato == self.arbol.raiz.dato and self.tipo == "avl":
                self.contenido = self.contenido + "\"" + aux.getDato() + "\n" + str(aux.peso) + "\""
            return

    def exportar(self):
        archivo = open('Resultado/GraficaArbol.dot', 'w')
        archivo.write('digraph D{\n')
        archivo.write("node [shape=circle style=filled ] \n")
        archivo.write("label= \" Grafico del " + self.titulo + " \" \n")

        # llenamos el contenido alv
        self.__graficar()

        # se agrega el contenido al dot
        archivo.write(self.contenido)

        # cerramos el archivo . dot y el de python
        archivo.write('\n}')
        archivo.close()

        # exportamos
        os.system('dot -Tpdf Resultado/GraficaArbol.dot -o Grafico.pdf')
        print('Generado con exito')