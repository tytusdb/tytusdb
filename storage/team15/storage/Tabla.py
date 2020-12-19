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
        os.system('hash.png')

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


tabla = Tabla('Integrantes', 2)
tabla.alterAddPK([0])
tabla2 = Tabla('Integrantes2', 3)
tabla2.alterAddPK([0])

tabla2.insertar(['aa', 'Dato1', 45])
tabla2.insertar(['aa', 'Dato1 Repetido', 8])
tabla2.insertar(['ab', 'Dato1', 9])
tabla2.insertar(['ba', 'Dato2 invertido', 10])
tabla2.insertar(['aab', 'Dato3', 11])
tabla2.insertar(['aba', 'Dato3 modificado', 12])
tabla2.insertar(['ac', 'Dato4', 13])
tabla2.insertar(['ad', 'Dato5', 14])
tabla2.insertar(['ae', 'Dato6', 15])
tabla2.insertar(['af', 'Dato7', 16])
tabla2.insertar(['aggg', 'Dato8', 489])
tabla2.insertar(['abc', 'Dato9', 789])
tabla2.insertar(['arr', 'Dato11', 87])
tabla2.insertar(['acc', 'Dato10', 756])

print()
tabla2.imprimir()
print()
print('Quito la primaria')
print(tabla2.alterDropPK())
print('Pongo la segunda me dara error')
print(tabla2.alterAddPK([1]))
print('La 0 me dara exito')
print(tabla2.alterAddPK([0]))
print('Update erroneo por llave')
print(tabla2.ExtraerTupla(['aa']))
print(tabla2.update(['aa'], {0:'af', 1:'Me modificaron'}))
print(tabla2.ExtraerTupla(['aa']))
print(tabla2.ExtraerTupla(['af']))
print('Update exitoso con llave')
print(tabla2.ExtraerTupla(['aa']))
print(tabla2.update(['aa'], {0:'Nuevo'}))
print(tabla2.ExtraerTupla(['aa']))
print(tabla2.ExtraerTupla(['Nuevo']))

print()
tabla2.imprimir()
print()

print(tabla2.extractTable())
print('Rango de tabla')
print(tabla2.extractRangeTable(2, 8, 15))

tabla2.imprimir()
print('Probando add column')
print(tabla2.alterAddColumn('Agregada1'))
print(tabla2.alterAddColumn('Agregada2'))
print()
tabla2.imprimir()
print(tabla2.alterDropColumn(5))
print(tabla2.alterDropColumn(0))
print(tabla2.alterDropColumn(3))
tabla2.imprimir()

tabla.insertar([65, 'Primer65'])
tabla.insertar([1, 'Welmann', 'Paniagua'])
tabla.insertar([2, 'Welmann1'])
tabla.insertar([3, 'unico 3'])
tabla.insertar([4, 'Welmann3'])
tabla.insertar([5, 'Welmann4'])
print(tabla.insertar([6, 'Welmann5']))
print(tabla.insertar([6, 'No se debe agregar']))
tabla.insertar(['hola', 'Welmann6'])
tabla.insertar([8, 'Welmann7'])
tabla.insertar([9, 'Welmann8'])
tabla.insertar([10, 'Welmann9'])
tabla.insertar([11, 'Welmann10'])
tabla.insertar([12, 'Welmann21'])
tabla.insertar([13, 'Welmann41'])
tabla.insertar([14, 'Welmann51'])
tabla.insertar([15, 'Welmann61'])
tabla.insertar([16, 'Welmann71'])
tabla.insertar([17, 'Welmann81'])
tabla.insertar([18, 'Welmann91'])
tabla.insertar([100, 'Welmann91'])
tabla.insertar([55, 'Welmann91'])
tabla.insertar([50, 'Welmann9'])
tabla.insertar([51, 'Welmann10'])
tabla.insertar([52, 'Welmann21'])
tabla.insertar([53, 'Primer53'])
tabla.insertar([54, 'Welmann51'])
tabla.insertar([95, 'Welmann61'])
tabla.insertar([56, 'Welmann71'])
tabla.insertar([57, 'Welmann81'])
tabla.insertar([58, 'Welmann91'])
tabla.insertar([120, 'Welmann91'])
tabla.insertar([65, 'Welmann91'])
tabla.insertar([16, 'Welmann71 no se debe insertar'])
tabla.insertar([1, 'Welmann'])
tabla.insertar([53342, 'unico 53342'])
tabla.insertar([12343, 'Welmann41'])
tabla.insertar([14324, 'Welmann51'])
tabla.insertar([143245, 'Welmann61'])
tabla.insertar([13246, 'Welmann71'])
tabla.insertar([14327, 'Welmann81'])
tabla.insertar([13238, 'Welmann91'])
tabla.insertar([10430, 'Welmann91'])
tabla.insertar([5345, 'Welmann91'])
tabla.insertar([53430, 'Welmann9'])
tabla.insertar([5334, 'Welmann41'])
tabla.insertar([1243, 'Welmann41'])
tabla.insertar([4324, 'Welmann51'])
tabla.insertar([14324, 'Welmann61'])
tabla.insertar([1346, 'Welmann71'])
tabla.insertar([1432, 'Welmann81'])
tabla.insertar([138, 'Welmann91'])
tabla.insertar([1043, 'Welmann91'])
tabla.insertar([545, 'Welmann91'])
tabla.insertar([530, 'Welmann9'])
tabla.insertar([53342, 'repetido'])
tabla.insertar([3, 'Welmann2'])
tabla.imprimir()
input('stop')
print('Probando updates de ints, falla por primaria')
print(tabla.ExtraerTupla([5345]))
print(tabla.update([5345], {0: 53430}))
print(tabla.ExtraerTupla([5345]))
print(tabla.ExtraerTupla([53430]))
print('Probando updates de ints, modifica por primaria')
print(tabla.ExtraerTupla([5345]))
print(tabla.update([5345], {0: 777}))
print(tabla.ExtraerTupla([5345]))
print(tabla.ExtraerTupla([777]))
input('stop')

print('Extrayendo parte de la tabla')
print(tabla.extractRangeTable(0, 8, 13))
print('Extrayendo parte string')
print(tabla.extractRangeTable(1, 'Welmann1', 'Welmann9'))

print('Tabla entera:')

# tabla.Grafico()

print(tabla.extractTable())

tabla.imprimir()
print('Tratando de redefinir PK')
print(tabla.alterAddPK([0, 1]))
print('Quitando PK')
print(tabla.alterDropPK())
print('Volviendo a poner PK')
print(tabla.alterAddPK([0, 1]))

tabla.imprimir()
# tabla.Grafico()
tabla.alterAddColumn('Agregada3')
print('Probando updates compuestas')
print(tabla.update([666], {1: 'hola', 2: 'puto'}))
print(tabla.update([12], {1: 'hola', 2: 'Me modificaron'}))
print(tabla.update([12, 'Welmann21'], {1: 'hola', 2: 'Me modificaron'}))
print(tabla.update([12, 'Welmann7777'], {1: 'hola', 2: 'Me modificaron'}))
print('Probando deletes compuestos')
print(tabla.deleteTable([12, 'jojojojo']))
print(tabla.deleteTable([545, 'Welmann91']))
tabla.imprimir()
print('Extraer tupla compuesta')
print(tabla.ExtraerTupla([3, 'unico 3']))

print('')
print('Quitando PK')
print(tabla.alterDropPK())
print('Volviendo a poner PK')
print(tabla.alterAddPK([0]))
tabla.alterAddColumn('OtraAgregada')

print(tabla.update([666], {1: 'hola', 2: 'puto'}))
print(tabla.update([12], {1: 'hola', 2: 'Me modificaron'}))
tabla.imprimir()
print('Delete de valor no existente')
print(tabla.deleteTable([666]))
print('Delete exitoso')
print(tabla.deleteTable([2]))
print('Extraer tupla normal')
print(tabla.ExtraerTupla([1346]))
tabla.imprimir()

tablaFloat = Tabla('Float', 4)
print(tablaFloat.alterAddPK([0]))
print(tablaFloat.insertar([1.4, 5, 8, 48]))
print(tablaFloat.insertar([1.8, 10, 8, 478]))
print(tablaFloat.insertar([1.9, 58, 8, 56]))
print(tablaFloat.insertar([1.45, 58, 8, 256]))
print(tablaFloat.insertar([10.5, 74, 8, 47]))
print(tablaFloat.insertar([1, 78, 89, 789]))
print(tablaFloat.insertar([489.45, 45, 8, 25]))
print(tablaFloat.insertar([48.14, 795, 8, 48789]))
print(tablaFloat.insertar([1.4, 52, 8, 741]))
print(tablaFloat.insertar([1.48, 45, 8, 4789]))
print('Rango de 1.4 a 1.9')
print(tablaFloat.extractRangeTable(0, 1.4, 1.9))
print('Update de tabla float')
print(tablaFloat.update([1.4], {1:'modificado', 2:'Siu'}))
print('Extract Row')
print(tablaFloat.ExtraerTupla([1.4]))
print('Delete de tabla float')
print(tablaFloat.deleteTable([1.48]))
print('Extract Row')
print(tablaFloat.ExtraerTupla([1.48]))
print('Retirando primaria')
print(tablaFloat.alterDropPK())
print('Haciendo cosas sin la primaria')
print('Insertar')
print(tablaFloat.insertar([1,1,1,1]))
tablaFloat.imprimir()
print('Extraer')
print(tablaFloat.ExtraerTupla([1.4]))
print('Eliminar')
print(tablaFloat.deleteTable([1.4]))
print('Extraer')
print(tablaFloat.ExtraerTupla([1.4]))
tablaFloat.imprimir()
print('Colocando primaria falla')
print(tablaFloat.alterAddPK([1, 2]))
print('Colocando primaria exitosa')
print(tablaFloat.alterAddPK([2, 3]))
tablaFloat.imprimir()
'''
print()
print()

pruebaBusqueda = [65, 17, 8, 4, 121, 2000, 896]
BusquedaASCII = ['aa', 'aba', 'arr', 'hola', 'puto', 50, 1]

print('BUSQUEDA EN TABLA ENTEROS')
for i in pruebaBusqueda:
    print('Resultado de buscar la llave:', i)
    print(tabla.ExtraerTupla(i))

print()
print('BUSQUEDA EN TABLA STRING')
for i in BusquedaASCII:
    print('Resultado de buscar la llave:', i)
    print(tabla2.ExtraerTupla(i))

print()
print(tabla.ExtraerTupla(52))
tabla.deleteTable(52)
print(tabla.ExtraerTupla(52))

print()
print(tabla.ExtraerTupla(11))
print(tabla.update(11, 1, 'NuevoValor'))
print(tabla.ExtraerTupla(11))

tabla.truncate()
tabla.imprimir()
tabla.insertar([4, 'Holuuuuu'])
tabla.imprimir()
tabla.deleteTable(4)
tabla.imprimir()

print(tabla.extractTable())
print(type(45))

tablaAleaoria = Tabla('Aleatoria', 3)

for i in range(200):
    tablaAleaoria.insertar([random.randint(1, 10000), random.randint(1, 100000), random.randint(1, 10000)])

print(tablaAleaoria.tamano)

'''
