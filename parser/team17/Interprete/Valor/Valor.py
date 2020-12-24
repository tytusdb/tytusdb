class Valor():

    def __init__(self, tipo, data:object):
        self.tipo = tipo
        self.data = data
        self.matriz = []

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

    def obtenerColumna_enBase_aIndice(self):
        '''
        Retorna una lista con los valores de la columna
        '''
        columna = []
