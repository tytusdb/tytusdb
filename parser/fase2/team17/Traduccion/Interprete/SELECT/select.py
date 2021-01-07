from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from Interprete.SELECT.indexador_auxiliar import indexador_auxiliar
from Interprete.SELECT.indexador_auxiliar import IAT
from Interprete.Primitivos.TIPO import TIPO
from Interprete.simbolo import Simbolo
from Interprete.OperacionesConExpresiones.OperadoresCondicionales import OperadoresCondicionales
from StoreManager import jsonMode as j
from prettytable import PrettyTable
from Interprete.Meta import Meta
from Interprete.Manejo_errores.ReporteTS import ReporteTS

class select(NodoArbol):

    def __init__(self, listavalores, listatablas, listawhere, line, column):
        super().__init__(line, column)
        self.listavalores = listavalores
        self.listatablas = listatablas
        self.listawhere = listawhere
        self.consolaInterna = ""
        self.TablaSelect:Valor
        self.tamFilaTablaSelect = 0

    def execute(self, entorno: Tabla_de_simbolos, arbol:Arbol):

        entorno.NuevoAmbito()

        if self.listawhere == "N/A":
            self.ruta_SelectSimple(entorno, arbol)
            #arbol.console.append(self.consolaInterna)
            entorno.BorrarAmbito()
            return self.TablaSelect
        else:
            self.ruta_SelectComplejo(entorno, arbol)
            #arbol.console.append(self.consolaInterna)
            entorno.BorrarAmbito()
            return self.TablaSelect

    '''
        Ruta: SELECT listavalores FROM listavalores listawhere
    '''

    def ruta_SelectComplejo(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        print("[Select] ruta_SelectComplejo (Go on)")
        V_TablaSelect = Valor(TIPO.MATRIZ, "TablaSelect")
        for i in self.listatablas:
            self.virtualizar_tabla(i, entorno, arbol)

        # ------------------
        j = 0
        for i in self.listavalores:
            if self.obtener_multi(i, entorno, arbol, j):
                break
            j = j + 1
        # ------------------

        V_TablaSelect.inicializarMatrix_boring(self.tamFilaTablaSelect, len(self.listavalores))
        index = 0
        for i in self.listavalores:
            lista: list = self.obtener_columnas(i, entorno, arbol)
            for m in range(len(lista)):
                V_TablaSelect.matriz[m][index] = lista[m]
            index = index + 1
        self.TablaSelect = V_TablaSelect
        # ----------------------------------------------------------------------------------
        TablaSe:Simbolo = Simbolo("TablaResult", 0, self.TablaSelect)
        entorno.insertar_variable(TablaSe)
        for i in self.listawhere:
            i.execute(entorno, arbol)

    '''
        Ruta: SELECT listavalores FROM listavalores
        Ejemplo: select t1.Cod, t2.ciudad, t1.zona from t1, t2;
    '''
    def ruta_SelectSimple(self, entorno: Tabla_de_simbolos, arbol:Arbol):
        print("[Select] ruta_SelectSimple (Go on)")
        V_TablaSelect = Valor(TIPO.MATRIZ, "TablaSelect")
        for i in self.listatablas:
            if i.tipo == IAT.SUBQUERY:
                self.virtualizar_tabla_subquery(i, entorno, arbol)
            else:
                self.virtualizar_tabla(i, entorno, arbol)

        # ------------------
        j = 0
        for i in self.listavalores:
            if self.obtener_multi(i, entorno, arbol, j):
                break
            j = j + 1
        # ------------------

        V_TablaSelect.inicializarMatrix_boring(self.tamFilaTablaSelect, len(self.listavalores))
        index = 0
        for i in self.listavalores:
            lista:list = self.obtener_columnas(i, entorno, arbol)
            for m in range(len(lista)):
                V_TablaSelect.matriz[m][index] = lista[m]
            index = index + 1
        self.TablaSelect = V_TablaSelect
        arbol.console.append("\n" + self.consolaInterna + self.TablaSelect.inicializarPrettybabe() + "\n")
        return self.TablaSelect

    # ==================================================================================================================

    #   Metodo: virtualizar_tabla
    #   sirve para buscar la tabla completa a la BD, obtenerla y posteriormente virtualizarla
    #   al crear un objeto 'Valor' tipo matriz con la tabla dentro. La variable se ingresa a la TS
    def virtualizar_tabla(self, index:indexador_auxiliar, entorno: Tabla_de_simbolos, arbol:Arbol):
        # -----------------------------------------------
        # Codigo para acceder a estructuras de EDD (estan quemados por el momento)
        # basado en el index.origen
        body = j.extractTable(entorno.getBD(),index.origen)
        x = Meta.getNameColumns(body[0])
        body[0] = x
        # body = [['Cod', 'estado', 'ciudad', 'zona'], [1, 'Guatemala', 'Guatemala', 'GTM'], [2, 'Cuilapa', 'Santa Rosa', 'GTM'], [3, 'San Salvador', 'San Salvador', 'SLV']]
        tamFila = len(body)
        tamColumna = len(body[0])
        if tamFila > self.tamFilaTablaSelect:
            self.tamFilaTablaSelect = tamFila
        '''headers:list = ['C_1', 'C_2', 'C_3', 'C_4', 'C_5']
        body:list = [
            '1.1', '2.1', '3.1', '4.1', '5.1',
            '1.2', '2.2', '3.2', '4.2', '5.2',
            '1.3', '2.3', '3.3', '4.3', '5.3'
        ]'''
        # -----------------------------------------------

        nombreTabla = self. definidorDeNombre_deTabla_basadoEnIndexador(index)
        tablaVirtualizada:Valor = Valor(TIPO.MATRIZ, nombreTabla)
        tablaVirtualizada.inicializarMatrix_boring(tamFila, tamColumna)
        tablaVirtualizada.setearMatriz_byJespino(body)
        #tablaVirtualizada.establecer_encabezados(headers)
        #tablaVirtualizada.setear_body_byList_MATRIZ(body)
        # self.consolaInterna = tablaVirtualizada.consola_imprimirMatriz_NERY()
        tablaVirtualizada.consola_imprimirMatriz_NERY()
        newSimbolo:Simbolo = Simbolo(nombreTabla, TIPO.MATRIZ, tablaVirtualizada)
        entorno.insertar_variable(newSimbolo)

        TSreport = ReporteTS(
            nombreTabla, "Tabla", "Select", 1, 1
        )
        arbol.ReporteTS.append(TSreport)
    # ==================================================================================================================

    def virtualizar_tabla_subquery(self, index: indexador_auxiliar, entorno: Tabla_de_simbolos, arbol: Arbol):
        print("virtualiza subquery")
        tablaVirtualizada: Valor = index.origen.execute(entorno, arbol)
        nombreTabla = self.definidorDeNombre_deTabla_basadoEnIndexador(index)
        tablaVirtualizada.consola_imprimirMatriz_NERY()
        newSimbolo: Simbolo = Simbolo(nombreTabla, TIPO.MATRIZ, tablaVirtualizada)
        entorno.insertar_variable(newSimbolo)
    # ==================================================================================================================

    def obtener_columnas(self, index:indexador_auxiliar, entorno: Tabla_de_simbolos, arbol:Arbol):
        campo = self.definidorDeNombre_deTabla_basadoEnIndexador(index)
        tabla = index.origen
        if len(self.listatablas) == 1:
            tabla = self.definidorDeNombre_deTabla_basadoEnIndexador(self.listatablas[0])
        tablaVistualizada:Valor = entorno.obtener_varibale(tabla)
        columna:Valor = Valor(TIPO.LISTA, campo)
        columna.inicizalizar_lista(tablaVistualizada.obtenerColumna_enBase_aEncabezado(campo))
        return  columna.lista
    # ==================================================================================================================

    def obtener_multi(self, index:indexador_auxiliar, entorno: Tabla_de_simbolos, arbol:Arbol, indiceListaValores):
        if index.referencia == "MULTI":
            self.listavalores.pop(indiceListaValores)
            tabla = index.origen
            if len(self.listatablas) == 1:
                tabla = self.definidorDeNombre_deTabla_basadoEnIndexador(self.listatablas[0])
            tablaVistualizada:Valor = entorno.obtener_varibale(tabla)
            encabezados:[] = tablaVistualizada.obtenerEncabezados_soloSTR()
            for i in encabezados:
                ind:indexador_auxiliar = indexador_auxiliar(str(tabla), str(i), 0)
                self.listavalores.append(ind)
            return True
        else:
            return False
    # ==================================================================================================================

    '''
        Funciones auxiliadoras
    '''
    def definidorDeNombre_deTabla_basadoEnIndexador(self, indexador:indexador_auxiliar) -> str:
        if indexador.tipo == IAT.ACCESO_SIN_ALIAS:
            return str(indexador.referencia)
        else:
            return str(indexador.referencia)
    # ==================================================================================================================