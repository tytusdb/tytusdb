import sys, os.path

where_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Where')
sys.path.append(where_path)

select_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Select')
sys.path.append(select_path)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

variables_globales = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')))
sys.path.append(variables_globales)

response_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\Response')
sys.path.append(response_path)

from Response.Response import Response
from jsonMode import *
from typeChecker.typeChecker import *
tc = TypeChecker()

from VariablesGlobales import *
from Where import Where
from Where import Info_Tabla
from Where import Info_Column
from Cartesiano import Cartesiano


class TableResult():
    def __init__(self):
        self.nombre = None
        self.tipoUnico = None
        self.valorUnico = None
        self.alias = None
        self.columnas = []
        self.noColumnas = 0
        self.data = None
        self.noFilas = 0
        self.listaEncabezados = []

class EncabResult():
    def __init__(self):
        self.nombre = None
        self.tipo = None

class Select():

    def __init__(self):
        self.dbUse = None
        self.matriz3DData = []
        self.listaTablas = []
        self.listaColumnas = []
        self.listaEstructuras = {}
        self.resultEncabezado = []
        self.listaTiposColumnas = []
        self.tableResultData = []
        self.tablaRetorno = []
        self.encabezadoRetorno = []
        self.listaTablasExpresion = []
        self.seLlenaEncabezado = True
        self.listaColumnasWhere = []
        self.enviroment = None
        

    #region Llenado de variables iniciales
    def verificarDBActiva(self):
        # Verifica si hay una base de datos activa, se utiliza para cualquier instrucción
        with open('src/Config/Config.json') as file:
            config = json.load(file)
        dbUse = config['databaseIndex']
        if dbUse == None:
            print("Se debe seleccionar una base de datos")
            return None
        return dbUse.upper()

    def obtenerColumnasDictionary(self, tabla):
        # Se obtiene el diccionario de columnas para la tabla del Storage,
        # Solo se utiliza para selects de tablas, hay casos en los que se pueden
        # Recibir tablas como parámetros, en las subconsultas, por ejemplo.
        listTemp = tc.return_columnsJSON(self.dbUse, tabla.upper())
        listaCols = []
        if listTemp != None:
            for col in listTemp:
                listaCols.append([col['name'], col['type']])
            return listaCols
        return []

    

    #endregion

    #region Inicia Algoritmo Select
    def procesarIdentificadorTable(self, parent, alias = None):
        # Siempre se recibe un nodo Identificador
        nuevaTabla = TableResult()
        nuevaTabla.nombre = parent.valor
        nuevaTabla.alias = parent.valor if alias == None else alias
        columnas = self.obtenerColumnasDictionary(parent.valor)
        if not columnas:
            return Response("22222","No existe la tabla referenciada")
        nuevaTabla.columnas = columnas
        self.listaColumnasWhere.append(columnas)
        nuevaTabla.data =  extractTable(self.dbUse, parent.valor.upper())
        nuevaTabla.noFilas = len(nuevaTabla.data)
        self.listaTablas.append(nuevaTabla)
        
    def procesarTable(self, parent):
        # Siempre se recibe un nodo TABLE
        self.procesarIdentificadorTable(parent.hijos[0],parent.hijos[1].valor)

    def procesarSentenciaSelect(self, resultado):
        resu = []
        for encabezado in resultado.listaEncabezados:
            resu.append([encabezado.nombre,encabezado.tipo])
        resultado.columnas = resu
        self.listaTablas.append(resultado)

    def procesarSentenciaSubquery(self, resultado, alias):
        resu = []
        for encabezado in resultado.listaEncabezados:
            resu.append([encabezado.nombre,encabezado.tipo])
        resultado.columnas = resu
        resultado.alias = alias.valor
        resultado.nombre = alias.valor
        self.listaTablas.append(resultado)

    def procesarTableExpresion(self, parent):
        for hijo in parent.hijos:
            if hijo.nombreNodo == "TABLE":
                self.procesarTable(hijo)
            elif hijo.nombreNodo == "SUBQUERY_TABLE":
                nuevoSelect = Select()
                resultadoSubquery = nuevoSelect.execute(hijo.hijos[0])
                self.procesarSentenciaSubquery(resultadoSubquery, hijo.hijos[1])
            elif hijo.nombreNodo == "SENTENCIA_SELECT":
                nuevoSelect = Select()
                resultadoSubquery = nuevoSelect.execute(hijo)
                self.procesarSentenciaSelect(resultadoSubquery)
            elif hijo.nombreNodo == "Identificador":
                self.procesarIdentificadorTable(hijo)
        producto = Cartesiano()
        self.tableResultData = producto.cartesiano(self.listaTablas)

        for tabla in self.listaTablas:
            for columna in tabla.columnas:
                nuevoEncabezado = EncabResult()
                nuevoEncabezado.nombre = columna[0]
                nuevoEncabezado.tipo = columna[1]
                tabla.listaEncabezados.append(nuevoEncabezado)
                self.encabezadoRetorno.append(nuevoEncabezado)
            

        
    #endregion
    

    #region Ejecución Select
    def ejecutarSelect(self, nodoListaEspresion):

        self.llenarEstructura(self.listaTablas)
        for fila in self.tableResultData:
            if fila[0]:
                self.ejecutarListExpresionSelect(nodoListaEspresion, fila)


        
    def ejecutarListExpresionSelect(self, nodoLista, fila):
        if nodoLista.nombreNodo == "*":
            self.llenarConAsterisco(fila)
        elif nodoLista.nombreNodo == "LISTA_EXP":
            self.llenarConExpresiones(nodoLista,fila)
        
    def llenarConAsterisco(self, fila):
        if self.seLlenaEncabezado:
            self.encabezadoRetorno.clear()
            for tabla in self.listaTablas:
                for columna in tabla.columnas:
                    nuevoEncabezado = EncabResult()
                    nuevoEncabezado.nombre = columna[0]
                    nuevoEncabezado.tipo = columna[1]
                    tabla.listaEncabezados.append(nuevoEncabezado)
                    self.encabezadoRetorno.append(nuevoEncabezado)
            self.seLlenaEncabezado = False
        resultado = []
        for i in range(0,len(self.listaTablas)):
            resultado = resultado + self.listaTablas[i].data[fila[i+1]]
        self.tablaRetorno.append(resultado)

    def llenarConExpresiones(self,nodoLista,fila):
        
        resultado = []
        for i in range(0,len(self.listaTablas)):
            for j in range(0,len(self.listaTablas[i].data[0])):
                nomTabla = self.listaTablas[i].nombre.upper()
                nomColumna = self.listaTablas[i].listaEncabezados[j].nombre.upper()
                valColumna = self.listaTablas[i].data[fila[i+1]][j]
                self.listaEstructuras[nomTabla].lista[nomColumna].valueColumn = valColumna
        
        encabezados = []
        for hijo in nodoLista.hijos:
            global selectAgregate
            selectAgregate.append(None)
            if hijo.nombreNodo == "E":
                respuesta = hijo.execute(self.listaEstructuras)
                resultado.append(respuesta)
                encabezados.append(["?column?", hijo.tipo.data_type])
            elif hijo.nombreNodo == "ALIAS":
                resultado.append(hijo.hijos[0].execute(self.listaEstructuras))
                encabezados.append([hijo.hijos[1].valor, hijo.hijos[1].tipo.value])
        self.tablaRetorno.append(resultado)
        if self.seLlenaEncabezado:
            self.encabezadoRetorno.clear()
            for encabezado in encabezados:
                nuevoEncabezado = EncabResult()
                nuevoEncabezado.nombre = encabezado[0]
                nuevoEncabezado.tipo = encabezado[1]
                self.encabezadoRetorno.append(nuevoEncabezado)                    
            self.seLlenaEncabezado = False
            #resultado = resultado + self.listaTablas[i].data[fila[i+1]]
        #self.tablaRetorno.append(resultado)
    
    #endregion

    def execute(self, parent, enviroment = None):
        global selectAgregate
        selectAgregate.clear()
        self.enviroment = enviroment
        # Se verifican las variables, si esta seleccionada la base de datos 
        self.dbUse = self.verificarDBActiva()
        if self.dbUse == None:
            return Response("22222","La base de datos no está seleccionada")
        # Se recibe como parámetro en nodo SENTENCIA_SELECT
        # Se visita al nodo TABLE_EXPRESION
        self.procesarTableExpresion(parent.hijos[1])



        stringName = ""        
        for tab in self.listaTablas:
            stringName = stringName + tab.alias

        if len(parent.hijos) == 3:
            listaDataTemp = []
            listaColumnasTemp = []
            listaTablasTemp = []
            for tabla in self.listaTablas:
                listaDataTemp.append(tabla.data)
                for columna in tabla.columnas:
                    listaColumnasTemp.append(columna)
                listaTablasTemp.append([tabla.nombre, tabla.alias])
            #print(listaDataTemp)
            #print(listaColumnasTemp)
            #print(listaTablasTemp)
            #print(self.tableResultData)
            nuevoFiltro = Where()
            resultado =  nuevoFiltro.execute(parent.hijos[2],listaDataTemp,listaTablasTemp,self.listaColumnasWhere,self.tableResultData)
            
        
        
        self.ejecutarSelect(parent.hijos[0])

                
        
        

        #region Agregacion
        dataTemporalAgregacion = []
        dataTemporalGlobal = []
        #Inicia el pocedimiento de funciones de agregación
        hayNoAgregate = False
        hayAgregate = False
        if len(selectAgregate)>= len(self.encabezadoRetorno):
            for i in range(0,len(self.encabezadoRetorno)):
                #selectAgregate
                if selectAgregate[i] == "AVG":
                    hayAgregate = True
                    dataTemporalAgregacion.append(self.realizarAVG(i,self.tablaRetorno))
                elif selectAgregate[i] == "COUNT":
                    hayAgregate = True
                    dataTemporalAgregacion.append(self.realizarCount(i,self.tablaRetorno))
                elif selectAgregate[i] == "MAX":
                    hayAgregate = True
                    dataTemporalAgregacion.append(self.realizarMax(i,self.tablaRetorno))
                elif selectAgregate[i] == "MIN":
                    hayAgregate = True
                    dataTemporalAgregacion.append(self.realizarMin(i,self.tablaRetorno))
                elif selectAgregate[i] == "SUM":
                    hayAgregate = True
                    dataTemporalAgregacion.append(self.realizarSum(i,self.tablaRetorno))
                elif selectAgregate[i] == None:
                    hayNoAgregate = True
        if hayAgregate and not hayNoAgregate:
            dataTemporalGlobal.append(dataTemporalAgregacion)
        else:
            dataTemporalGlobal = self.tablaRetorno
        #endregion
        
        numeroFilas = len(dataTemporalAgregacion)
        numeroColumnas = len(self.encabezadoRetorno)
        tipoUnico = None
        valorUnico = None

        if numeroFilas == 1 and numeroColumnas == 1 :
            tipoUnico = self.encabezadoRetorno[0].tipo
            valorUnico = dataTemporalAgregacion[0]
        
        
        tablaResultado = TableResult()
        tablaResultado.nombre = stringName
        tablaResultado.alias = stringName
        tablaResultado.columnas = self.encabezadoRetorno
        tablaResultado.noColumnas = len(self.encabezadoRetorno)
        tablaResultado.data = dataTemporalGlobal
        tablaResultado.noFilas = len(dataTemporalGlobal)
        tablaResultado.listaEncabezados = self.encabezadoRetorno
        tablaResultado.valorUnico = valorUnico
        tablaResultado.tipoUnico = tipoUnico
        return tablaResultado


    def llenarEstructura(self, listaTablas):
        for i in range(0,len(listaTablas)):
            infTab = Info_Tabla(listaTablas[i].nombre.upper(),listaTablas[i].alias.upper())
            for j in range(0,len(listaTablas[i].listaEncabezados)):
                infCol = Info_Column(listaTablas[i].listaEncabezados[j].nombre.upper(),listaTablas[i].listaEncabezados[j].tipo)
                infTab.lista[listaTablas[i].listaEncabezados[j].nombre.upper()] = infCol
            self.listaEstructuras[listaTablas[i].nombre.upper()] = infTab
        
    def realizarAVG(self, indice, data):
        dividendo = len(data)
        
        temporal = 0
        for fila in data:
            temporal = temporal + fila[indice]
        return temporal/dividendo

    def realizarCount(self, indice, data):
        dividendo = len(data)
        return dividendo

    def realizarMax(self, indice, data):
        temporal = None
        for fila in data:
            print(fila[indice])
            if temporal == None:
                temporal = fila[indice]
            elif fila[indice]>temporal:
                temporal = fila[indice]
        return temporal

    def realizarMin(self, indice, data):
        temporal = None
        for fila in data:
            if temporal == None:
                temporal = fila[indice]
            elif fila[indice]<temporal:
                temporal = fila[indice]
        return temporal

    def realizarSum(self, indice, data):
        temporal = 0
        for fila in data:
            temporal = temporal + fila[indice]
        return temporal