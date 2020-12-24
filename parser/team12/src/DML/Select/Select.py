import sys, os.path

where_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\Where')
sys.path.append(where_path)

storage = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..\..')) + '\\typeChecker')
sys.path.append(storage)

from jsonMode import *
from typeChecker.typeChecker import *
tc = TypeChecker()


from Where import Where
from Where import Info_Tabla
from Where import Info_Column



class Select():
    
    def insertaDatos(self):
        truncate(self.dbUse,'EMPLEADO')
        truncate(self.dbUse,'PUESTO')
        truncate(self.dbUse,'EMPLEADO_PUESTO')
        db="EMPLEADO"
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])
        insert(self.dbUse,db,[1,"Juan Perez"])
        insert(self.dbUse,db,[2,"Daniel Perez"])
        insert(self.dbUse,db,[3,"Daniel Gonzales"])
        insert(self.dbUse,db,[4,"Esbin Perez"])
        insert(self.dbUse,db,[5,"Esbin Gonzales"])
        insert(self.dbUse,db,[6,"Walter Perez"])
        insert(self.dbUse,db,[7,"Josue Perez"])
        insert(self.dbUse,db,[8,"Eduardo Perez"])
        insert(self.dbUse,db,[9,"Edilson Perez"])

        db = "PUESTO"
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        insert(self.dbUse,db,[1,"Operador"])
        insert(self.dbUse,db,[2,"Vendedor"])
        insert(self.dbUse,db,[3,"Jefe"])
        insert(self.dbUse,db,[4,"Sistemas"])
        insert(self.dbUse,db,[5,"Otro Jefe"])
        

        db = "EMPLEADO_PUESTO"
        insert(self.dbUse,db,[1,1])
        insert(self.dbUse,db,[2,2])
        insert(self.dbUse,db,[3,1])
        insert(self.dbUse,db,[4,2])
        insert(self.dbUse,db,[5,1])


    def __init__(self):
        self.dbUse = None
        self.matriz3DData = []
        self.listaTablas = []
        self.listaColumnas = []
        self.listaEstructuras = {}
        self.resultEncabezado = []
        self.listaTiposColumnas = []
        
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
        listTemp = tc.return_columnsJSON(self.dbUse, tabla)
        listaCols = []
        if listTemp != None:
            for col in listTemp:
                listaCols.append([col['name'], col['type']])
            return listaCols
        return []
    
    def llenarListaTablaDatosStorage(self, listaTablas):
        # Este método se llama para llenar la matriz de matrices de datos
        # Solo se utiliza para el storage también.
        listaTablasDatos=[]
        for tab in listaTablas:
            listaTablasDatos.append(extractTable(self.dbUse, tab[0]))
        return listaTablasDatos

    def llenarListadoTablasAlias(self,parent, listaTablasStorage):
        # Se llena un listado de tablas que vienen del storage
        listaTablas=[]
        for hijo in parent.hijos:
            if hijo.nombreNodo == "TABLE":
                if not  (hijo.hijos[0].valor.upper() in listaTablasStorage):
                    print("Error, no se encuentra en la DB")
                    return None
                listaTablas.append([hijo.hijos[0].valor.upper(),hijo.hijos[1].valor.upper()])
            elif hijo.nombreNodo == "Identificador":
                if not  (hijo.valor.upper() in listaTablasStorage):
                    print("Error, no se encuentra en la DB")
                    return None
                listaTablas.append([hijo.valor.upper(),hijo.valor.upper()])
        return listaTablas

    def llenarTablasStorage(self):
        return showTables(self.dbUse)

    def llenarDataNormal(self, parent):
        # Pasos para llenar las tablas con los datos del storage (Forma Normal)
        # 1. Obtener todas las tablas del storage.
        # 2. Obtener todas las tablas involucradas
        # 3. Obtener todas las columnas de las tablas involucradas
        # 4. Obtener toda la data del storage.
        for hijo in parent.hijos:
            if hijo.nombreNodo == "TABLE_EXPRESION":
                # 1.
                listaTablas = self.llenarTablasStorage()
                # 2.
                listaTablasInvolucradas = self.llenarListadoTablasAlias(hijo,listaTablas)
                # 3.
                listaColumnas = []
                for tabla in listaTablasInvolucradas:
                    listaColumnas.append(self.obtenerColumnasDictionary(tabla[0]))
                cuboStorage = self.llenarListaTablaDatosStorage(listaTablasInvolucradas)
                self.listaTablas = listaTablasInvolucradas
                self.listaColumnas = listaColumnas
                self.matriz3DData = cuboStorage

    def llenarDataSubConsulta(self, enviroment):
        print("Subconsulta")
    #endregion

    #region Filtrado de datos
    def llenarEstructura(self, listaEncabezados):
        for encabezado in listaEncabezados:
            infoT = Info_Tabla(encabezado[0],encabezado[1])
            self.listaEstructuras[encabezado[0]]=infoT
        for encabezado in listaEncabezados:
            infoC = Info_Column(encabezado[2],encabezado[3])
            self.listaEstructuras[encabezado[0]].lista[encabezado[2]]=infoC
        

    
    def executeSelect(self, parent, listaEncabezados, listaDatos):
        self.llenarEstructura(listaEncabezados)
        listaResultado = []
        validaLlenar = True
        for dato in listaDatos:
            for i in range(0,len(listaEncabezados)):
                self.listaEstructuras[listaEncabezados[i][0]].lista[listaEncabezados[i][2]].valueColumn = dato[i]
            rowResult = []
            for exp in parent.hijos:
                if exp.nombreNodo == 'E':
                    rowResult.append(exp.execute(self.listaEstructuras))
                    if validaLlenar :
                        self.resultEncabezado.append('?columna?')
                elif exp.nombreNodo == 'ALIAS':
                    if validaLlenar :
                        self.resultEncabezado.append(exp.hijos[1].valor)
                    rowResult.append(exp.hijos[0].execute(self.listaEstructuras))
            listaResultado.append(rowResult)
            validaLlenar = False
        return listaResultado

    def extractEncabezadosAll(self, listaEncabezados):
        listaRetorno = []
        for enc in listaEncabezados:
            listaRetorno.append(enc[1]+"."+enc[2])
        self.resultEncabezado = listaRetorno
    
    def construirEncabezadosSelectSinWhere(self, listaTablas, listaColumnas):
        listCols = []
        for i in range(0,len(listaTablas)):
            for j in range(0,len(listaColumnas[i])):
                listCols.append([listaTablas[i][0],listaTablas[i][1],listaColumnas[i][j][0],listaColumnas[i][j][1]])

        return listCols
        # Se arma la matriz con los resultados obtenidos  

    #endregion
    
    def execute(self, parent, enviroment = None):
        # Se verifican las variables, si esta seleccionada la base de datos 
        # Se llenan las tablas del storage, serán utilizadas mas adelante para
        # busquedas.
        self.dbUse = self.verificarDBActiva()
        if self.dbUse == None:
            print("Error, db no seleccionada")
            return
        # Datos de Prueba
        #self.insertaDatos()

        # Llena dependiendo del modo en el que sea invocado
        if enviroment == None : #Select normal
            self.llenarDataNormal(parent)
        else: #Subconsulta
            self.llenarDataSubConsulta(enviroment)

        listaResult = None
        listaEncabezados = None
        esWhere = False
        # Recorre
        for hijo in parent.hijos:
            if hijo.nombreNodo == "SENTENCIA_WHERE":
                esWhere =True
                nuevoWhere = Where()
                listaResult = nuevoWhere.execute(hijo,self.matriz3DData, self.listaTablas, self.listaColumnas)
                listaEncabezados = nuevoWhere.matEncabezados
        
        if not esWhere:
            wr = Where()
            listaEncabezados = self.construirEncabezadosSelectSinWhere(self.listaTablas, self.listaColumnas)
            listaResult = wr.execute(None,self.matriz3DData,self.listaTablas,self.listaColumnas)

        for hijo in parent.hijos:
            if hijo.nombreNodo == "LISTA_EXP":
                if listaResult!= None:
                    result = self.executeSelect(hijo,listaEncabezados, listaResult)
                    if len(result)>0:
                        return result
            if hijo.nombreNodo == "*":
                if listaResult!=None:
                    self.extractEncabezadosAll(listaEncabezados)
                    return listaResult
                    

    
                
