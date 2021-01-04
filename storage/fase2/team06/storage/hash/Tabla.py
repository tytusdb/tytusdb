# HASH Mode Package
# Released under MIT License
# Copyright (c) 2020 TytusDb Team


import os
import subprocess


class Nodo(object):
    
    def __init__(self, datos, primaria, posicion):
        self.primaria = ''
        self.datos = datos
        if primaria is None:
            self.primaria = posicion
        elif len(primaria) == 1:
            self.primaria = datos[primaria[0]]
        else:
            contador = 0
            for i in primaria:
                if contador == len(primaria) - 1:
                    self.primaria += str(datos[i])
                else:
                    self.primaria += str(datos[i]) + '-'
                contador += 1

        if type(self.primaria) is int:
            self.tipo = 'int'
        else:
            self.tipo = 'str'
            self.primaria = str(self.primaria)


class Tabla(object):
    def __init__(self, nombre, columnas):
        self.nombre = nombre
        self.columnas = columnas
        self.vector = []
        self.tamano = 13
        self.elementos = 0
        self.factorCarga = 0
        self.tipoPrimaria = None
        self.PK = None
        self.contadorPK = 0
        for i in range(self.tamano):
            self.vector.append(None)

    '''
    En caso de que la llave primaria sea una cadena este metodo me devolvera un numerico para
    lograr indexarla
    '''

    def toASCII(self, cadena):
        result = 0
        for char in cadena:
            result += ord(char)
        return result

    '''
    Metodo correspondiente al metodo insert(database, table, columns)
    sin embargo desde a esta clase solo llega el columns, que es una lista de 
    datos
    '''

    def insertar(self, datos):
        if len(datos) == self.columnas:
            nuevo = Nodo(datos, self.PK, self.contadorPK)
            if self.elementos == 0:
                self.tipoPrimaria = nuevo.tipo
            else:
                if self.tipoPrimaria is None:
                    '''No hace nada'''
                elif self.tipoPrimaria != nuevo.tipo:
                    return 1
            posicion = self.funcionHash(nuevo.primaria)
            # Ahora se verificara si la posicion ya tiene una lista o esta vacia
            if self.vector[posicion] is None:
                self.vector[posicion] = []
                self.vector[posicion].append(nuevo)
                self.elementos += 1
                self.contadorPK += 1
                return 0

            '''
            Aqui se verifica que no existan valores repetidos ya que estamos hablando de llaves primarias,
            sin embargo se divide en caso de se primarias string o enteras 
            '''
            if self.tipoPrimaria == 'int':
                if self.Existe(self.vector[posicion], nuevo.primaria):
                    return 4
            elif self.tipoPrimaria is None:
                '''No se hacce nada'''
            else:
                if self.ExisteToAscii(self.vector[posicion], nuevo.primaria):
                    return 4

            self.vector[posicion].append(nuevo)  # Se agrega el dato a la lista

            '''
            Se va a verificar el tipo de ordenamiento, si sera por int o para string
            '''
            if self.tipoPrimaria == 'int':
                self.vector[posicion] = self.OrdenarBurbuja(self.vector[posicion])
            else:
                self.vector[posicion] = self.OrdenarBurbujaToAscii(self.vector[posicion])

            self.factorCarga = self.elementos / self.tamano

            if self.factorCarga > 0.9:
                self.rehashing()

            self.contadorPK += 1
            return 0
        else:
            return 5

    def rehashing(self):
        while not (self.factorCarga < 0.3):
            self.tamano += 1
            self.factorCarga = self.elementos / self.tamano

        lista = []
        for i in self.vector:
            if i is None:
                '''No hace nada'''
            else:
                for j in i:
                    lista.append(j)

        self.vector = []
        for tamaño in range(self.tamano):
            self.vector.append(None)

        self.contadorPK = 0
        for nodo in lista:
            self.insertar(nodo.datos)

    def funcionHash(self, primaria):
        if type(primaria) is str:
            primaria = self.toASCII(primaria)
        index = primaria % self.tamano
        return index

    def imprimir(self):
        indice = 0
        print('Contenido de la tabla:', self.nombre)
        for i in self.vector:
            if i is None:
                print('Indice:', indice, 'Contenido:', i)
            else:
                print('Indice:', indice, 'Contenido:', end=' ')
                for j in i:
                    print('{Primaria:', j.primaria, 'Tupla:', str(j.datos) + '}', end=' ')
                print('')
            indice += 1

    '''
    Para Hacer una  busqueda mas efectiva se implementara el algoritmo de busqueda binaria
    '''

    def Existe(self, lista, dato):
        if len(lista) == 0:
            return False
        else:
            medio = len(lista) // 2
            if lista[medio].primaria == dato:
                return True
            else:
                if dato < lista[medio].primaria:
                    return self.Existe(lista[:medio], dato)
                else:
                    return self.Existe(lista[medio + 1:], dato)

    def ExisteToAscii(self, lista, dato):
        for i in lista:
            if str(i.primaria) == str(dato):
                return True
        return False

    def BuscandoNodoToAscii(self, lista, dato):
        for i in lista:
            if str(i.primaria) == str(dato):
                return i
        return False

    '''
    Ordenamiento de la lista, el metodo a utilizar sera el ordenamiento de burbuja
    '''

    def OrdenarBurbuja(self, vector):
        for i in range(1, len(vector)):
            for j in range(0, len(vector) - 1):
                if vector[j].primaria > vector[j + 1].primaria:
                    aux = vector[j + 1]
                    vector[j + 1] = vector[j]
                    vector[j] = aux
        return vector

    def OrdenarBurbujaToAscii(self, vector):
        for i in range(1, len(vector)):
            for j in range(0, len(vector) - 1):
                if self.toASCII(str(vector[j].primaria)) > self.toASCII(str(vector[j + 1].primaria)):
                    aux = vector[j + 1]
                    vector[j + 1] = vector[j]
                    vector[j] = aux
        return vector

    def BusquedaBinariaDevlviendoNodo(self, lista, dato):
        if len(lista) == 0:
            return False
        else:
            medio = len(lista) // 2
            if lista[medio].primaria == dato:
                return lista[medio]
            else:
                if dato < lista[medio].primaria:
                    return self.BusquedaBinariaDevlviendoNodo(lista[:medio], dato)
                else:
                    return self.BusquedaBinariaDevlviendoNodo(lista[medio + 1:], dato)

    '''
    Retorna el nodo para mostrar la informacion
    Representa la funcion ExtractRow()
    '''

    def ExtraerTupla(self, primaria):
        try:
            if len(primaria) > 1:
                primaria = self.UnirLlave(primaria)
            else:
                primaria = primaria[0]

            if not (type(primaria) is int):
                primaria = str(primaria)

            if self.tipoPrimaria == 'int':
                if type(primaria) is str:
                    return []
                indice = self.funcionHash(primaria)
                casilla = self.vector[indice]
                if casilla is None:
                    return []  # Llave primaria no existe
                nodo = self.BusquedaBinariaDevlviendoNodo(casilla, primaria)
            else:
                indice = self.funcionHash(primaria)
                casilla = self.vector[indice]
                if casilla is None:
                    return []  # Llave primaria no existe
                nodo = self.BuscandoNodoToAscii(casilla, primaria)

            if type(nodo) == bool:
                return []
            else:
                return nodo.datos
        except:
            return []

    '''
    Truncate, metodo para vaciar la tabla totalmente 
    '''

    def truncate(self):
        try:
            self.vector = []
            self.tamano = 13
            self.contadorPK = 0
            self.elementos = 0
            self.factorCarga = 0
            for i in range(self.tamano):
                self.vector.append(None)
            return 0
        except:
            return 1

    '''
    deleteTable, elimina un registro de la tabla
    '''

    def deleteTable(self, primaria):
        try:
            if len(primaria) > 1:
                primaria = self.UnirLlave(primaria)
            else:
                primaria = primaria[0]

            if not (type(primaria) is int):
                primaria = str(primaria)

            if (type(primaria) is str) or (type(primaria) is int):
                indice = self.funcionHash(primaria)
                if self.vector[indice] is None:
                    return 4
                elif len(self.vector[indice]) == 1:
                    if self.vector[indice][0].primaria == primaria:
                        self.vector[indice] = None
                        self.elementos -= 1
                        return 0
                    else:
                        return 4
                nuevo = self._delete(self.vector[indice], primaria)
                if type(nuevo) == bool:
                    return 4
                else:
                    self.vector[indice] = nuevo
                    return 0
            else:
                return 1
        except:
            return 1

    def _delete(self, lista, primaria):
        if self.tipoPrimaria == 'int':
            elemento = self.BusquedaBinariaDevlviendoNodo(lista, primaria)
            if type(elemento) == bool:
                return False
            else:
                lista.remove(elemento)
                return lista
        else:
            for i in lista:
                if str(i.primaria) == str(primaria):
                    lista.remove(i)
                    return lista
            return False

    def update(self, primaria, registro):
        try:
            if len(primaria) > 1:
                primaria = self.UnirLlave(primaria)
            else:
                primaria = primaria[0]

            if not (type(primaria) is int):
                primaria = str(primaria)

            keys = registro.keys()
            for i in keys:
                if i >= self.columnas:
                    return 1

            if self.tipoPrimaria == 'int':
                if not (type(primaria) is int):
                    return 1
                indice = self.funcionHash(primaria)
                if self.vector[indice] is None:
                    return 4
                if not self.Existe(self.vector[indice], primaria):
                    return 4
                elemento = self.BusquedaBinariaDevlviendoNodo(self.vector[indice], primaria)
                indiceInterno = self.vector[indice].index(elemento)
                listaNueva = elemento.datos[:]
                for i in keys:
                    listaNueva[i] = registro[i]
                for i in keys:
                    if i in self.PK:
                        return self.CambioPrimaria(listaNueva, indice, indiceInterno)
                elemento.datos = listaNueva
                self.vector[indice][indiceInterno] = elemento
                return 0
            else:

                indice = self.funcionHash(primaria)
                if self.vector[indice] is None:
                    return 4
                if not self.ExisteToAscii(self.vector[indice], primaria):
                    return 4
                elemento = self.BuscandoNodoToAscii(self.vector[indice], primaria)
                indiceInterno = self.vector[indice].index(elemento)
                listaNueva = elemento.datos[:]
                for i in keys:
                    listaNueva[i] = registro[i]
                for i in keys:
                    if i in self.PK:
                        return self.CambioPrimaria(listaNueva, indice, indiceInterno)
                elemento.datos = listaNueva
                self.vector[indice][indiceInterno] = elemento
                return 0
        except:
            return 1

    def CambioPrimaria(self, datos, indice, indiceInterno):
        retorno = self.insertar(datos)
        if retorno != 0:
            return 1
        else:
            self.vector[indice].pop(indiceInterno)
            if len(self.vector[indice]) == 0:
                self.vector[indice] = None
                self.elementos -= 1
            return retorno


    def extractTable(self):
        lista = []
        for i in self.vector:
            if i is None:
                '''No hace nada'''
            else:
                for j in i:
                    lista.append(j)
        if len(lista) > 0:
            if self.tipoPrimaria == 'int':
                lista = self.OrdenarBurbuja(lista)
            else:
                lista = self.OrdenarBurbujaToAscii(lista)
            ListaDeListas = []
            for i in lista:
                ListaDeListas.append(i.datos)
            return ListaDeListas
        else:
            return []

    def alterTable(self, name):
        try:
            self.nombre = name
            return 0
        except:
            return 1

    def Grafico(self):
        file = open('hash.dot', "w")
        file.write("digraph grafica{" + os.linesep)
        file.write('graph [pad="0.5"];' + os.linesep)
        file.write("nodesep=.05;" + os.linesep)
        file.write("rankdir=LR;" + os.linesep)
        file.write("node [shape=record,width=.1,height=.1];" + os.linesep)

        for i in range(self.tamano):
            if i == 0:
                file.write('vector [label = "<f0> 0|' + os.linesep)
            elif i == self.tamano - 1:
                file.write(
                    '<f' + str(i) + '> ' + str(i) + '",height=' + str(self.tamano / 2) + ', width=.8];' + os.linesep)
            else:
                file.write('<f' + str(i) + '> ' + str(i) + '|' + os.linesep)

        contador = 0
        for listaNodos in self.vector:
            if not listaNodos is None:
                for nodo in listaNodos:
                    file.write('node' + str(nodo.primaria).replace(' ', '').replace('-', 'y') + '[label = "{<n> ' + str(
                        nodo.primaria).replace(' ', '').replace('-', 'y') + '| <p> }"];' + os.linesep)
                file.write(
                    'vector:f' + str(contador) + ' -> node' + str(listaNodos[0].primaria).replace(' ', '').replace('-',
                                                                                                                   'y') + ':n;' + os.linesep)
                if len(listaNodos) > 1:
                    for i in range(len(listaNodos)):
                        if not i == len(listaNodos) - 1:
                            file.write('node' + str(listaNodos[i].primaria).replace(' ', '').replace('-',
                                                                                                     'y') + ':p -> node' + str(
                                listaNodos[i + 1].primaria).replace(' ', '').replace('-', 'y') + ':n;' + os.linesep)

            else:
                file.write('nodeNone' + str(contador) + ' [shape=plaintext, label="None", width=0.5]' + os.linesep)
                file.write('vector:f' + str(contador) + ' -> nodeNone' + str(contador) + os.linesep)
            contador += 1

        file.write(' }' + os.linesep)
        file.close()
        subprocess.call('dot -Tpng hash.dot -o hash.png')

    def alterAddColumn(self, default):
        try:
            for i in self.vector:
                if i is None:
                    '''No hace nada'''
                else:
                    for j in i:
                        j.datos.append(default)
            self.columnas += 1
            return 0
        except:
            return 1

    def alterDropColumn(self, numero):
        try:
            if self.columnas == 1:
                return 4
            if numero in self.PK:
                return 4
            if numero >= self.columnas:
                return 5
            if not (self.PK is None):
                count = 0
                for i in self.PK:
                    if i > numero:
                        self.PK[count] -= 1
                    count += 1

            for i in self.vector:
                if i is None:
                    '''No hace nada'''
                else:
                    for j in i:
                        j.datos.pop(numero)
            self.columnas -= 1
            return 0
        except:
            return 1

    def alterAddPK(self, referencias):
        try:
            if not (self.PK is None):
                return 4
            for i in referencias:
                if i >= self.columnas:
                    return 5
            temporal = self.PK
            self.PK = referencias
            if self.elementos > 0:
                retorno = self.RestructuracionPorLlavePrimaria()
                if not retorno:
                    self.PK = temporal
                    return 1
            return 0
        except:
            return 1

    def alterDropPK(self):
        try:
            if self.PK is None:
                return 4
            self.PK = None
            self.tipoPrimaria = None
            return 0
        except:
            return 1

    def RestructuracionPorLlavePrimaria(self):
        lista = []
        for i in self.vector:
            if i is None:
                '''No hace nada'''
            else:
                for j in i:
                    lista.append(j)

        comprobacion = self.ComprobarReestructuracion(lista)

        if not comprobacion:
            return False

        self.elementos = 0
        self.factorCarga = 0
        self.tamano = 13
        self.contadorPK = 0
        self.tipoPrimaria = None

        self.vector = []
        for i in range(13):
            self.vector.append(None)
        for nodo in lista:
            self.insertar(nodo.datos)
        return True

    def ComprobarReestructuracion(self, lista):
        tablaPrueba = Tabla('prueba', self.columnas)
        tablaPrueba.alterAddPK(self.PK)
        for nodo in lista:
            retorno = tablaPrueba.insertar(nodo.datos)
            if not (retorno == 0):
                return False
        return True

    def UnirLlave(self, primaria):
        combinada = ''
        contador = 0
        for i in primaria:
            if contador == len(primaria) - 1:
                combinada += str(i)
            else:
                combinada += str(i) + '-'
            contador += 1
        return combinada

    def extractRangeTable(self, numeroColumna, lower, upper):
        try:
            if (not (type(lower) is int)) or (not (type(upper) is int)):
                lower = str(lower)
                upper = str(upper)

            lista = []
            for i in self.vector:
                if i is None:
                    '''No hace nada'''
                else:
                    for j in i:
                        lista.append(j)

            listaRetorno = []
            if not (type(lower) is int):
                for nodo in lista:
                    if lower <= str(nodo.datos[numeroColumna]) <= upper:
                        listaRetorno.append(nodo.datos)
                return listaRetorno

            for nodo in lista:
                if lower <= nodo.datos[numeroColumna] <= upper:
                    listaRetorno.append(nodo.datos)
            return listaRetorno
        except:
            return []


