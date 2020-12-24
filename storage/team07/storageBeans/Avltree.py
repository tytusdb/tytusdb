
import os
import platform
import subprocess
class Nodo:
    def __init__(self, valor, lista):
        self.izquierda = None
        self.derecha = None
        self.valor = valor
        self.tupla = lista
        self.altura = 0


#
#
# def toASCII2(cadena):
#     cadena = str(cadena)
#     resultado = 0
#     for i in cadena:
#         i = str(i)
#         resultado += ord(i)
#     return resultado


class arbolAVL(object):
    def __init__(self, noColumnas):
        self.valor = 0  # sera el numero que genere su codigo ascci
        self.raiz = None
        self.pk = None
        self.noColumnas = noColumnas
        self.grafo = ""

    def agregar(self, lista):  # metodo que mandare a llamar para hacer el insert,
        # asumiendo que la lista contiene la cantidad de elementos necesarios

        if self.pk is None:
            self.raiz = self.agregar1(self.raiz, self.valor, lista)
            self.valor += 1
            # self.preorden()
        else:
            indiceCompleto = 0
            for i in self.pk:
                indiceCompleto += toASCII2(lista[i])
            self.raiz = self.agregar1(self.raiz, indiceCompleto, lista)
            # self.preorden()

    def agregar1(self, aux, valor, lista):
        if aux is None:
            return Nodo(valor, lista)
        elif valor > aux.valor:
            aux.derecha = self.agregar1(aux.derecha, valor, lista)
            if (self.altura1(aux.derecha) - self.altura1(aux.izquierda)) == 2:
                if valor > aux.derecha.valor:
                    aux = self.srr(aux)
                else:
                    aux = self.drr(aux)
        else:
            aux.izquierda = self.agregar1(aux.izquierda, valor, lista)
            if (self.altura1(aux.izquierda) - self.altura1(aux.derecha)) == 2:
                if valor < aux.izquierda.valor:
                    aux = self.srl(aux)
                else:
                    aux = self.drl(aux)
        dere = self.altura1(aux.derecha)
        izq = self.altura1(aux.izquierda)
        m = self.maxi(dere, izq)
        aux.altura = m + 1
        return aux

    def altura1(self, aux):
        if aux is None:
            return -1
        else:
            return aux.altura

    def maxi(self, dere, izq):
        return (izq, dere)[dere > izq]

    def srl(self, aux1):
        aux2 = aux1.izquierda
        aux1.izquierda = aux2.derecha
        aux2.derecha = aux1
        aux1.altura = self.maxi(self.altura1(aux1.izquierda), self.altura1(aux1.derecha)) + 1
        aux2.altura = self.maxi(self.altura1(aux2.izquierda), aux1.altura) + 1
        return aux2

    def srr(self, aux1):
        aux2 = aux1.derecha
        aux1.derecha = aux2.izquierda
        aux2.izquierda = aux1
        aux1.altura = self.maxi(self.altura1(aux1.izquierda), self.altura1(aux1.derecha)) + 1
        aux2.altura = self.maxi(self.altura1(aux2.izquierda), aux1.altura) + 1
        return aux2

    def drl(self, aux):
        aux.izquierda = self.srr(aux.izquierda)
        return self.srl(aux)

    def drr(self, aux):
        aux.derecha = self.srl(aux.derecha)
        return self.srr(aux)

    # def eliminar(self, valor):
    #     self.raiz = self.eliminar1(self.raiz, valor)
    #
    # def eliminar1(self, aux: object, valor):
    #     if aux is None:
    #         print("Nodo no encontrado")
    #     elif valor > aux.valor:
    #         # nodo por la derecha
    #         aux.derecha = self.eliminar1(aux.derecha, valor)
    #     elif valor < aux.valor:
    #         # nodo por la izquierda
    #         aux.izquierda = self.eliminar1(aux.izquierda, valor)
    #     else:
    #         aux1 = aux
    #         if (aux1.derecha is None):
    #             aux = aux1.izquierda
    #         elif (aux1.izquierda is None):
    #             aux = aux1.derecha
    #         else:
    #             self.aux1 = self.Elimina(aux1)
    #         self.aux1 = None
    #     return aux
    #
    # def Elimina(self, aux):
    #     aux1 = aux  # p
    #     aux2 = aux.izquierda  # a
    #     while (aux2.derecha is not None):
    #         aux1 = aux2
    #         aux2 = aux2.derecha
    #     aux.valor = aux2.valor
    #     if (aux1 == aux):
    #         aux1.izquierda = aux2.izquierda
    #     else:
    #         aux1.derecha = aux2.derecha

    def preorden(self):
        self.preorden1(self.raiz)

    def preorden1(self, aux):
        if aux:
            cadena = "["
            for i in aux.tupla:
                cadena += str(i) + " , "
            cadena += "]"
            print(cadena)
    def Grafo(self):
        f = open('Avl.txt','w')
        self.grafo+= "digraph G { \n rankdir=LR; style=filled \n size=\"8,5\" \n	node [shape = rectangle];\n"
        self.Grafo1(self.raiz)
        self.grafo+="}"
        f.write(self.grafo)
        f.close()

        commandfile = 'dot -Tpng Avl.txt -o Avl.png'

        path = 'Avl.png'

        self.start_file(commandfile)
        self.open_file(path)
        print(self.grafo)

    def open_file(self,path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def start_file(self,commandfile):
        if platform.system() == "Windows":
           os.system(commandfile)
        elif platform.system() == "Darwin":
           subprocess.call(commandfile, shell=True)
        else:
           os.system(commandfile)


    def Grafo1(self, aux):
        if (aux != None):
             if(aux.izquierda != None):
                self.grafo +="\""+ str(aux.tupla)+"\"" + "->" +"\"" +str(aux.izquierda.tupla) +"\""+";\n"
                self.Grafo1(aux.izquierda)
             if(aux.derecha != None):
                self.grafo += "\""+str(aux.tupla)+"\"" + "->" + "\""+str(aux.derecha.tupla) +"\""+ ";\n"
                self.Grafo1(aux.derecha)




    def getTuplas(self):
        self.listamoment = []
        self._getTuplas(self.raiz)
        return self.listamoment

    def _getTuplas(self, aux):
        if aux:
            self.listamoment.append(aux.tupla)
            # print(aux.valor, end=' ')
            self._getTuplas(aux.izquierda)
            self._getTuplas(aux.derecha)


    def addNewColumna(self,newAtributo):
        self._addNewColumna(self.raiz, newAtributo)

    def _addNewColumna(self, aux, newAtributo):
        if aux:
            aux.tupla.append(newAtributo)
            self._addNewColumna(aux.izquierda, newAtributo)
            self._addNewColumna(aux.derecha, newAtributo)

    def eliminarColumna(self, noColumna):
        self._eliminarColumna(self.raiz, noColumna)

    def _eliminarColumna(self, aux, noColumna):
        if aux:
            aux.tupla.pop(noColumna)
            self._eliminarColumna(aux.izquierda, noColumna)
            self._eliminarColumna(aux.derecha, noColumna)




t = arbolAVL(3)

for i in range(20):
    t.agregar(["algo",i,"ultimo"])

#t.preorden()
t.Grafo()
print()

#Eliminar
#t.eliminar(1)
