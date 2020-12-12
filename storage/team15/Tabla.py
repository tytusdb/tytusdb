class Nodo(object):
    def __init__(self, datos):
        self.datos = datos
        self.primaria = datos[0]
        if type(self.primaria) is str:
            self.tipo = 'str'
        else:
            self.tipo = 'int'


class Tabla(object):
    def __init__(self, nombre, columnas):
        self.nombre = nombre
        self.columnas = columnas
        self.vector = []
        self.tamano = 15
        self.elementos = 0
        self.factorCarga = 0
        self.tipoPrimaria = None
        for i in range(15):
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
            nuevo = Nodo(datos)
            if self.elementos == 0:
                self.tipoPrimaria = nuevo.tipo
            else:
                if self.tipoPrimaria != nuevo.tipo:
                    return False
            posicion = self.funcionHash(nuevo.primaria)
            # Ahora se verificara si la posicion ya tiene una lista o esta vacia
            if self.vector[posicion] is None:
                self.vector[posicion] = []

            self.vector[posicion].append(nuevo)
            '''self.vector[posicion] = self.OrdenarAnidado(self.vector[posicion])'''
            self.elementos += 1
            self.factorCarga = self.elementos / self.tamano

            if self.factorCarga > 0.8:
                self.rehashing()

            return True
        else:
            return False

    def rehashing(self):
        while not (self.factorCarga < 0.5):
            self.tamano += 1
            self.factorCarga = self.elementos / self.tamano

        nuevosEspacios = self.tamano - len(self.vector)
        for i in range(nuevosEspacios):
            self.vector.append(None)

    def funcionHash(self, primaria):
        if self.tipoPrimaria == 'str':
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


tabla = Tabla('Integrantes', 2)

tabla.insertar([10, 'Welmann'])
tabla.insertar([20, 'Welmann1'])
tabla.insertar([16, 'Welmann2'])
tabla.insertar([50, 'Welmann3'])
tabla.insertar([12, 'Welmann4'])
tabla.insertar([18, 'Welmann5'])
tabla.insertar([78, 'Welmann6'])
tabla.insertar([13, 'Welmann7'])
tabla.insertar([72, 'Welmann8'])
tabla.insertar([80, 'Welmann9'])
tabla.insertar([100, 'Welmann10'])
tabla.insertar([160, 'Welmann21'])
tabla.insertar([120, 'Welmann41'])
tabla.insertar([180, 'Welmann51'])
tabla.insertar([780, 'Welmann61'])
tabla.insertar([130, 'Welmann71'])
tabla.insertar([720, 'Welmann81'])
tabla.insertar([800, 'Welmann91'])

tabla.imprimir()
