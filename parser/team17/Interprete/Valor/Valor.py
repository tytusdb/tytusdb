from Interprete.Primitivos.TIPO import TIPO
from prettytable import PrettyTable
from prettytable import ORGMODE

class Valor():

    def __init__(self, tipo, data:object):
        self.tipo = tipo
        self.data = data
        self.matriz = []
        self.lista = []
        self.prettyGirl = PrettyTable() # <--- la pretty table
        self.filasPareas = []
        self.filasPareas_internacional = []

    def getTipo(self):
        return self.tipo

    '''
    ------------------------------------------------------------------------------------
    CODIGO PARA MATRICES:
    ------------------------------------------------------------------------------------
    '''

    def consola_imprimirMatriz_NERY(self):
        photon = str(self.data) + ": \n-------------------------\n"
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

    def setear_body_byList_MATRIZ(self, body:list):
        indiceBody = 0
        for item_1 in range(len(self.matriz)):
            if item_1 != 0:
                for item_2 in range(len(self.matriz[item_1])):
                    val:Valor = Valor(TIPO.CADENA, str(body[indiceBody]))
                    self.matriz[item_1][item_2] = val
                    indiceBody = indiceBody + 1

    def setearMatriz_byJespino(self, body):
        newBody = []
        for i in range(len(body)):
            newBody.append([])
            for j in range(len(body[i])):
                data = body[i][j]
                value:Valor = Valor(TIPO.CADENA, str(data))
                body[i][j] = value

        self.matriz = body

    def obtenerEncabezados_soloSTR(self) -> []:
        encabezados = []
        for item_2 in range(len(self.matriz[0])):
            val:Valor = self.matriz[0][item_2]
            encabezados.append(str(val.data))
        return encabezados

    '''
    ------------------------------------------------------------------------------------
    CODIGO PARA LISTAS:
    ------------------------------------------------------------------------------------
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

    def preparadoBasico_list(self):
        encabezado = ""
        cuerpo = []
        for item in range(len(self.lista)):
            value: Valor = self.lista[item]
            if item == 0:
                encabezado = str(value.data)
            else:
                cuerpo.append(str(value.data))
        retorno = [ encabezado, cuerpo ]
        return retorno

    '''
    ------------------------------------------------------------------------------------
    CODIGO PARA prettytable:
    ------------------------------------------------------------------------------------
    '''
    def inicializarPrettybabe(self):
        self.prettyGirl.set_style(ORGMODE)
        self.prettyGirl.clear()
        i = 0
        for item_1 in range(len(self.matriz)):
            recolector = []
            for item_2 in range(len(self.matriz[item_1])):
                value: Valor = self.matriz[item_1][item_2]
                recolector.append(value.data)
            if i == 0:
                self.prettyGirl.field_names = recolector
                i = i + 1
                recolector.clear()
            else:
                if self.elRowesValido(item_1):
                    self.prettyGirl.add_row( recolector )
                    recolector.clear()
                else:
                    recolector.clear()
        print(self.prettyGirl)
        self.filasPareas = [] # < --- libero a las filas Pareas
        return self.prettyGirl.get_string()

    def getPrettyGirl(self):
        return self.prettyGirl.get_string()

    def inicializarPrettybabe_experimental(self):
        self.prettyGirl.set_style(ORGMODE)
        self.prettyGirl.clear()
        i = 0
        for item_1 in range(len(self.matriz)):
            recolector = []
            for item_2 in range(len(self.matriz[item_1])):
                value: Valor = self.matriz[item_1][item_2]
                recolector.append(value.data)
            if i == 0:
                self.prettyGirl.field_names = recolector
                i = i + 1
                recolector.clear()
            else:
                if self.elRowesValido_experimental(item_1):
                    self.prettyGirl.add_row( recolector )
                    recolector.clear()
                else:
                    recolector.clear()
        print(self.prettyGirl)
        self.filasPareas = [] # < --- libero a las filas Pareas
        return self.prettyGirl.get_string()

    def inicializarPrettybabe_experimental_invertido(self):
        self.prettyGirl.set_style(ORGMODE)
        self.prettyGirl.clear()
        i = 0
        for item_1 in range(len(self.matriz)):
            recolector = []
            for item_2 in range(len(self.matriz[item_1])):
                value: Valor = self.matriz[item_1][item_2]
                recolector.append(value.data)
            if i == 0:
                self.prettyGirl.field_names = recolector
                i = i + 1
                recolector.clear()
            else:
                if self.elRowesValido_experimental(item_1):

                    recolector.clear()
                else:
                    self.prettyGirl.add_row(recolector)
                    recolector.clear()
        print(self.prettyGirl)
        self.filasPareas = [] # < --- libero a las filas Pareas
        return self.prettyGirl.get_string()

    '''
    ------------------------------------------------------------------------------------
    CODIGO PARA WHERE:
    ------------------------------------------------------------------------------------
    '''

    def filtrarWhere(self, tipo, encabezado, filtro):
        indexEncabezado = self.noDeEncabezado(encabezado)
        for item_1 in range(len(self.matriz)):
            if item_1 == 0:
                pass
            else:
                value: Valor = self.matriz[item_1][indexEncabezado]
                if str(value.data) == str(filtro):
                    pass
                else:
                    self.filasPareas.append(item_1)
        self.filasPareas_internacional = self.filasPareas

    def filtrarWhere_experimental(self, tipo, encabezado, filtro):
        indexEncabezado = self.noDeEncabezado(encabezado)
        for item_1 in range(len(self.matriz)):
            if item_1 == 0:
                pass
            else:
                value: Valor = self.matriz[item_1][indexEncabezado]
                if str(value.data) == str(filtro):
                    self.filasPareas.append(item_1)
                    pass
                else:
                    pass


    def elRowesValido(self, index):
        for i in self.filasPareas:
            if i == index:
                return False
            else:
                pass
        return True

    def elRowesValido_experimental(self, index):
        for i in self.filasPareas:
            if i == index:
                return True
            else:
                pass
        return False

    def elRowesValido_internacional(self, index):
        for i in self.filasPareas_internacional:
            if i == index:
                return False
            else:
                pass
        return True

    def matriResult_isEmpty(self):
        if len(self.matriz) == (len(self.filasPareas) + 1):
            return True
        else:
            return False

    def getLista_sinPareas(self):
        print("holaaa " + str(self.filasPareas_internacional))
        for i in range(len(self.lista)):
            if self.elRowesValido_internacional(i):
                pass
            else:
                self.lista.pop(i)
        return self.lista

    '''
    ------------------------------------------------------------------------------------
    CODIGO PARA ORDER:
    ------------------------------------------------------------------------------------
    '''
    def order(self, encabezdo, orientacion):
        if str(orientacion) == "ASC":
            return self.prettyGirl.get_string(sortby=encabezdo)
        else:
            self.prettyGirl.reversesort = True
            return self.prettyGirl.get_string(sortby=encabezdo)

    '''
    ------------------------------------------------------------------------------------
    CODIGO PARA LIMIT:
    ------------------------------------------------------------------------------------
    '''
    def limit(self, limit:int):
        return self.prettyGirl.get_string(start = 0, end = limit)

    '''
    ------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------
    CODIGO PARA TYPES:
    ------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------
    '''
    def insert_tipo_toType(self, elemento):
        val:Valor = Valor(TIPO.CADENA, str(elemento))
        self.lista.append(val)

    def getTipo_ofType(self, index):
        val:Valor = self.lista[index]
        return str(val.data)

    '''
    ------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------
    CODIGO PARA UNION:
    ------------------------------------------------------------------------------------
    ------------------------------------------------------------------------------------
    '''

    '''
    algoritomo:
        01. obtener en forma de lista la "n" columna de tablaExtranjera
        02. fusionar la lista a self.tabla
        03. n + 1 y volver a paso 01
    '''
    def union(self, tablaExtra):
        self.inicializarPrettybabe()
        tablaExtranjera:Valor = tablaExtra
        noColumnas_en_tablaExtranjera = len(tablaExtranjera.matriz[0])
        for i in range(noColumnas_en_tablaExtranjera):
            columna: Valor = Valor(TIPO.LISTA, '')
            columna.inicizalizar_lista(tablaExtranjera.obtenerColumna_enBase_aIndice(i))
            preparado = columna.preparadoBasico_list()
            self.prettyGirl.add_column(preparado[0], preparado[1])
        return self.getPrettyGirl()

















