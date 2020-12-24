# File:         B+ Mode File for EDD
# License:      Released under MIT License
# Notice:       Copyright (c) 2020 TytusDB Team
# Developer:    Virginia Sarai Gutierrez Depaz


import math
import os
from storageManager.Clave import Clave
from storageManager.Pagina import Pagina

class ArbolBmas:
    def __init__(self):
        self.raiz = None
        self.Dato = []
        self.retorno = 1 

    def insertar(self, clave, data):
        if self.estaVacio():
            self.raiz = Pagina([None, Clave(clave, data), None])
        else:
            valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                clave, data, self.raiz)
            if seDividio:
                self.raiz = Pagina([self.raiz, valorMediana, nuevaPagina])

    def insertarRecursivo(self, clave, data, paginaTemporal):
        if paginaTemporal.esHoja():
            return paginaTemporal.insertarEnPagina(clave, data)
        else:
            if clave > paginaTemporal.contenido[-2].clave:
                valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                    clave, data, paginaTemporal.contenido[-1])
            else:
                i = 1
                while i < len(paginaTemporal.contenido) and clave > paginaTemporal.contenido[i].clave:
                    i += 2
                valorMediana, nuevaPagina, seDividio = self.insertarRecursivo(
                    clave, data, paginaTemporal.contenido[i-1])
            if seDividio:
                return paginaTemporal.insertarEnPagina(valorMediana.clave, valorMediana.data, nuevaPagina)
            else:
                return None, None, False

                #[apuntador, Clave, Apuntador]

    def estaVacio(self):
        return self.raiz == None

    def recorrer(self):
        self.recorrerRecursivo(self.raiz, 0)

    def recorrerRecursivo(self, pagina, level):
        if not pagina.esHoja():
            # [puntero, clave, puntero, clave2, puntero, clave3]
            for x in pagina.contenido[::2]:
                self.recorrerRecursivo(x, level+1)
        #print("Level: "+str(level))
        for x in pagina.contenido[1::2]:
            print(x.data)

    def imprimirLista(self, pagina):
        if pagina.esHoja():
            aux = pagina
            i = 0
            while aux:
                #print("Pagina: " + str(i))
                for x in aux.contenido[1::2]:
                    #print(x.data)
                    ''''''
                aux = aux.paginaSiguiente
                i += 1
        else:
            self.imprimirLista(pagina.contenido[0])

    # contador de F = level + 1
    def graphviz(self):
        self.hojas = []
        archivo = open('archivo.dot', 'w', encoding='utf-8')
        archivo.write('digraph structs {\n')
        archivo.write('node [shape=record];\n')
        self.contPag = 0
        self.graficarEncabezado(self.raiz, 0, archivo)
        self.contPag = 0
        self.graficarEnlace(self.raiz, 0, archivo, None)
        tmp = self.hojas[0]
        ant = tmp
        for x in self.hojas[1::1]:
            ant = tmp
            tmp = x
            archivo.write('{0} -> {1};\n'.format(ant, tmp))
        archivo.write('{rank=same; ')
        for x in self.hojas[::1]: archivo.write('{0}; '.format(x))
        archivo.write('}\n}\n')
        archivo.close()
        os.system('dot -Tpng archivo.dot -o salida.png')
        #os.system('salida.png')

    def graficarEncabezado(self, pagina, level, archivo):
        f = ''
        for x in range(level + 1):
            f += 'f'

        nombre = 'pagina{0}'.format(self.contPag)
        archivo.write('{0} [label="'.format(nombre))
        self.contPag += 1

        pos = 0  # posicion actual del arreglo
        bandera = True
        for x in pagina.contenido[::1]:
            if bandera:
                # puntero
                archivo.write('<{0}{1}> '.format(f, pos))
            else:
                # clave
                archivo.write('|<{0}{1}> {2} |'.format(f, pos, x.data))
            bandera = not bandera
            pos += 1
        archivo.write('"];\n')

        if not pagina.esHoja():
            for x in pagina.contenido[::2]:
                self.graficarEncabezado(x, level+1, archivo)
        else:
            self.hojas += [nombre]

    def graficarEnlace(self, pagina, level, archivo, padre):
        f = ''
        for x in range(level + 1):
            f += 'f'

        if not (padre is None):
            self.contPag += 1
            archivo.write('{0} -> pagina{1};\n'.format(padre, self.contPag))

        pos = 0  # posicion actual del arreglo
        bandera = True
        nombre = 'pagina' + str(self.contPag)
        for x in pagina.contenido[::1]:  # pagina0
            if bandera:
                # puntero
                if not pagina.esHoja():
                    # no es Hoja
                    self.graficarEnlace(x, level+1, archivo,
                                        '{0}:{1}{2}'.format(nombre, f, pos))
            bandera = not bandera
            pos += 1

    def eliminar(self, clave):
        if  self.raiz is None:
            return False
        seElimino, esHoja = self.raiz.eliminar(clave, None, self.raiz)
        if seElimino == True:
            '''print(str(clave) + ' eliminado.')'''
        else:
            '''print('Error: La clave ' + str(clave) + ' no se eliminó.')'''
        return seElimino

    def truncateRoot(self):
        self.raiz = None
