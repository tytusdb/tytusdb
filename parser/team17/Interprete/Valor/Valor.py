class Valor():

    def __init__(self, tipo, data:object):
        self.tipo = tipo
        self.data = data
        self.matriz = []
        self.lista = []

    def getTipo(self):
        return self.tipo

    '''
    ESTILO DE NERY (osea el estilo neutron):
    Codigo para matrices
    '''

    def consola_imprimirMatriz_NERY(self):
        photon = ""
        for item_1 in range(len(self.matriz)):
            photon += "|   "
            for item_2 in range(len(self.matriz[item_1])):
                value:Valor = self.matriz[item_1][item_2]
                photon += value.data + "   "
            photon += "| \n"
        print(photon)
        return photon

    def inicializarMatrix_boring(self, tamFila, tamColumna):
        matrix = []
        value:Valor = Valor(2, 'NULL')
        for item in range(tamFila):
            tupla = [value] * tamColumna
            matrix.append(tupla)
        self.matriz = matrix

    def ingresar_aMatriz_boring(self, value, linea, columna):
        val:Valor = Valor(value.tipo, str(value.data))
        self.matriz[linea][columna] = val

    def establecer_encabezados(self, encabezados:list):
        if len(self.matriz[0]) == len(encabezados):
            for item_2 in range(len(self.matriz[0])):
                val: Valor = Valor(2, str(encabezados[item_2]))
                self.matriz[0][item_2] = val
            pass
            return True
        else:
            return False

    def obtenerColumna_enBase_aIndice(self, indice) -> list:
        '''
        Retorna una lista con los valores de la columna
        '''
        columna = []
        for item_1 in range(len(self.matriz)):
            value:Valor = self.matriz[item_1][indice]
            columna.append(value)
        return columna

    def obtenerColumna_enBase_aEncabezado(self, encabezado) -> list:
        '''
        Retorna una lista con los valores de la columna
        '''
        columna = []
        indice = self.noDeEncabezado(encabezado)
        for item_1 in range(len(self.matriz)):
            value:Valor = self.matriz[item_1][indice]
            columna.append(value)
        return columna

    def noDeEncabezado(self, encabezado):
        no = -1
        for item_2 in range(len(self.matriz[0])):
            val:Valor = self.matriz[0][item_2]
            if str(val.data) == str(encabezado):
                no = item_2
                break
        return no

    '''
    ESTILO DE NERY (osea el estilo neutron):
    Codigo para listas
    '''
    def inicizalizar_lista(self, lista_:list):
        self.lista = lista_

    def imprimir_lista(self):
        photon = "Columna: \n---------------------\n"
        for item in range(len(self.lista)):
            value: Valor = self.lista[item]
            photon += value.data + "\n"
            if item == 0:
                photon += "---------------------\n"
        photon += "---------------------"
        print(photon)
        return photon