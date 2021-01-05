class Nodo:
    def __init__(self, nombreBase=None, nombre=None, columna=0, datos=None, sig=None):
        self.nombreBase = nombreBase
        self.nombre = nombre
        self.columna = columna
        self.datos = datos
        self.sig = sig
    
    def __str__(self):
        return "%s %s %s %s" %(self.nombreBase, self.nombre, self.columna, self.datos)

class listaS:
   
    
    #complementos a utilizaar
    listaRegistros = []
    ListaRegistroTabla = []
    lista = []
    
    def __init__(self):
        self.cabeza = None
        self.cola = None #guardar  ultimo elemento
    
    def agregar(self, element ): #creando un nodo
        if self.cabeza == None:
            self.cabeza = element

        if self.cola != None: #vesrificando si la lista esta vacia
            self.cola.sig = element

        self.cola = element
        def listar(self):
        aux = self.cabeza 
        while aux != None:
            print(aux)
            aux = aux.sig

    def verificando(self):
        if self.cola != None: #vesrificando si la lista esta vacia
             return True
        else:
            return False
     
    def buscar(self, nombre):
        aux = self.cabeza 
        while aux != None:
            if aux.nombre == nombre:
                return aux.nombre
            aux = aux.sig
        return None

    def buscarBase(self, baseDatos):
        
        aux = self.cabeza 
        while aux != None:
            if aux.nombreBase == baseDatos:
                return aux.nombreBase
            aux = aux.sig
        return None
    
    def buscarcolumna(self, tabla):
        aux = self.cabeza 
        while aux != None:
            if aux.nombre == tabla:
                return aux.columna
            aux = aux.sig
        return None
    
    def buscando(self, table):
        aux = self.cabeza 
        while aux != None:
            if aux.nombre == table:
                return aux.nombreBase
            aux = aux.sig
        return None
    def buscandoelemento(self, tabla):
        aux = self.cabeza 
        while aux != None:
            if aux.nombre == tabla:
                return aux.datos
            aux = aux.sig
        return None

    def imprimirLista(self, base):
        aux = self.cabeza 
        while aux != None:
            if aux.nombreBase == base:
                print(aux.nombre)
            aux = aux.sig
        return None
    
    def imprimirRegistros(self,table):
        aux = self.cabeza 
        while aux != None:
            if aux.nombre == table:
                print(aux.datos)
            aux = aux.sig
        return None

    def eliminar(self, nombre):
        if self.cabeza.nombre == nombre:
            self.cabeza = self.cabeza.sig #inicializando con el siguiente registro
            return True

        else:
            aux = self.cabeza
            anterior = aux # objetivo de recorrer para encontrar
            while aux != None:
                if aux.nombre == nombre:
                    anterior.sig = aux.sig #desvinculando nodo
                    return True
                anterior = aux
                aux= aux.sig
            return False
    
    def modificar(self, nombre, elemento):
        if self.cabeza.nombre == nombre:
            elemento.sig = self.cabeza.sig
            self.cabeza = elemento
            return True
        
        else:
            aux = self.cabeza
            anterior = aux
            while aux != None:
                if aux.nombre == nombre:
                    elemento.sig = aux.sig #modificando elemento que estamos recibiendo
                    anterior.sig = elemento
                    #return True
                anterior = aux
                aux = aux.sig
        #return False

    #FUNCIONES DE TABLA
    def createTable(self, basedatos, tabla, Ncolumna):
        try:
            if basedatos in self.listabase:
                #data = t.getDataBase(basedatos)  # get the database
                buscandoTabla = self.buscar(tabla)
                if buscandoTabla is not None:
                    return 3 # tabla existente
                else:
                    columna = int(Ncolumna)
                    registros = [] 
                    nod = Nodo(basedatos, tabla, columna, registros)
                    self.agregar(nod)
                    self.imprimirLista(basedatos)
                    return 0 #operacion existosa
            else:
                return 2 #basa de datos no existente
        
        except:
            return 1 #Error en la operacion
    
    def extractTable(self, database, table):
        try:
            verificar =0
            if database in self.listabase:
                buscandobase = self.buscarBase(database) #buscando base
                #print(buscandobase)
                if buscandobase != None:
                    buscandotabla = self.buscar(table)
                    #print(buscandotabla)
                    if buscandotabla != None:
                        #self.insertandodatos()
                            almacenandodatos=[]
                            print(self.listaRegistros)
                       
                            for j in range(len(self.listaRegistros)): 
                                
                                Verificartabla = self.listaRegistros[j][0]
                                
                                if table == Verificartabla:
                                    buscandoColumna = self.buscarcolumna(table)
                                    verificar=1
                                    almacenandodatos.append(self.listaRegistros[j])
                                    nod = Nodo(database, table, buscandoColumna,almacenandodatos)
                                    self.modificar(buscandotabla, nod)
                                    
                                    
                                else:
                                    print("no hay tabla registro")
                                    listaVacia=[]
                                    f=listaVacia
                                    print(f)
                            for k in range(len(almacenandodatos)):
                                print(almacenandodatos[k][1:len(almacenandodatos[k])])
                        
                    else:
                        return None # tabla no existe
                else:
                    return None
            else:
                return None #base no existente
        except:
            return None #Error en la operacion

    def alterTable(self, database, tableOld, tableNew):
        try:
            if database in self.listabase:
                buscandobase = self.buscarBase(database) #buscando base
                if buscandobase != None: 
                    buscandotabla = self.buscar(tableOld) #buscando vieja tabla
                    if buscandotabla != None:
                        buscandotablaNew = self.buscar(tableNew) #buscando si existe el nuevo nombre
                        if buscandotablaNew != None:
                            return 4 #nuevatabla existente
                        else:
                            buscandocolum = self.buscarcolumna(tableOld) #buscando vieja tabla
                            if buscandocolum != None:
                                buscandoelementos = self.buscandoelemento(tableOld)
                                nod = Nodo(database, tableNew, buscandocolum,buscandoelementos)
                                self.modificar(tableOld, nod)
                                return 0 #operacion exitosa
                    else:
                        return 3 # viejatabla no existe               
            else:
                return 2 #base no existente                             
        except:
           return 1 #Error en la operacion
    
    def showTables(self,basedatos):
        try:
            if basedatos in self.listabase:
       #         data = t.getDataBase(basedatos)  # get the database
                resultado = self.buscarBase(basedatos)
                if resultado != None: #vesrificando si la lista esta vacia
                   self.imprimirLista(basedatos)
                else:
                   print()
              
            else:
               return None #basa de datos no existente
        
        except:
           return None
    #Error en la operacion
    
    def extractRangeTable(self,database, table, columnNumber, lower, upper):
        try:
            verificar=0
            datoscolumna = []
            if database in self.listabase:
                buscandobase = self.buscarBase(database) #buscando base
                if buscandobase != None:
                    buscandotabla = self.buscar(table)
                    if buscandotabla != None:
                            for j in range(len(self.listaRegistros)): 
                                Verificartabla = self.listaRegistros[j][0]
                                if table == Verificartabla:
                                    columnaa=int(columnNumber)
                                    Acolumna= columnaa+1
                                    Adatoscolumna = self.listaRegistros[j][Acolumna]
                                    datoscolumna.append(Adatoscolumna)
                                    verificar=1
                                else:
                                    
                                    listaVacia=[]
                                    f=listaVacia
                                    print(f)
                            if verificar ==1:
                                inferior=int(lower) 
                                superior=int(upper)
                                superiorF= superior+1
                                for m in range (inferior,superiorF):
                                    print(datoscolumna[m])
                    else:
                        return None # tabla no existe
                else:
                    return None
            else:
                return None #base no existente
        except :
             return None #Error en la operacion
    def alterAddColumn(self,database, table, default):
        try:
            verificar=0
            if database in self.listabase:
                buscandobase = self.buscarBase(database) #buscando base
                if buscandobase != None:
                    buscandotabla = self.buscar(table)
                    if buscandotabla != None:
                         buscandoColumna = int(self.buscarcolumna(table))
                         buscandoColumna=buscandoColumna+1
                         buscandodtos = self.buscandoelemento(table)
                         nod = Nodo(database, table, buscandoColumna,buscandodtos)
                         self.modificar(table, nod)
                         for j in range(len(self.listaRegistros)):
                             Verificartabla = self.listaRegistros[j][0]
                             print(Verificartabla)
                             if Verificartabla==table:

                                 self.listaRegistros[j].append(default)
                                 verificar=1
                                  
                                        #return 
                         if verificar ==1:
                            print(self.listaRegistros)
                            return 0;   
                            
                    else:
                        return 3 # tabla no existe
                else:
                    return 2
            else:
                return 2 #base no existente
        except :
             return 1 #Error en la operacion
    
    def dropTable(self, database, table): 
        try:
            buscandobase = self.buscarBase(database) #buscando base
            if buscandobase != None: 
                buscandoTabla = self.buscar(table)
                if buscandoTabla is not None:
                   if (self.eliminar(table)):
                       return 0 # operacion exitosa
                else:
                    return 3 #tabla no existente
            else:
                return 2 #basa de datos no existente
        
        except:
            return 1 #Error en la operacion
    #Funciones TUPLAS
    def insert(self,database, table, register):
        try:
            #guardandoRegistros=[]
            self.ListaRegistroTabla = []
            if database in self.listabase:
                buscandobase = self.buscarBase(database) #buscando base
                if buscandobase != None: 
                    
                    buscandoTabla = self.buscar(table)
                    if buscandoTabla != None:
                        
                        self.ListaRegistroTabla.insert(0, table)
                        m = 0
                        for x in register.split(','):
                            self.ListaRegistroTabla.append(x)
                            m=m+1
                            buscandoColumna = int(self.buscarcolumna(table))
                        if buscandoColumna == m:
                                if self.listaRegistros:
                                    for i in range(len(self.listaRegistros)):
                                        for j in range(len(self.listaRegistros)):
                                            llaveprimaria = self.ListaRegistroTabla[1]
                                            VerificarLlavePrimaria = self.listaRegistros[j][1]
                                            verificandotabla = self.listaRegistros[j][0]
                                            if llaveprimaria == VerificarLlavePrimaria:
                                                if  verificandotabla==table:
                                                    verificando = 0
                                                    self.ListaRegistroTabla= []
                                                    return 4 #llave primaria duplicada
                                            else:
                                                verificando = 1
                                        if verificando == 1:
                                            self.listaRegistros.append(self.ListaRegistroTabla)
                                            return 0           
                                else:
                                    self.listaRegistros.append(self.ListaRegistroTabla)
                                    return 0 #operacion exitosa       
                        elif m > buscandoColumna:
                                self.ListaRegistroTabla= []
                                return 5 #columnas fuera limite   
                    else:
                        self.ListaRegistroTabla= []
                        return 3 #tabla no existente
                else:
                    self.ListaRegistroTabla= []
                    return 3
            else:
                self.ListaRegistroTabla= []
                return 2 #basa de datos no existente
        
        except:
            self.ListaRegistroTabla= []
            return 1 #Error en la operacion
    def truncate(self, database, table):
        try:
            verificar =0
            if database in self.listabase:
                buscandobase = self.buscarBase(database) #buscando base
                if buscandobase != None:
                    buscandotabla = self.buscar(table)
                    if buscandotabla != None:
                        for i in range(len(self.listaRegistros)):
                        
                            for j in range(len(self.listaRegistros[i])):
                                Verificartabla = self.listaRegistros[i][0]
                                if Verificartabla==table:
                                    self.listaRegistros.pop(i)
                                    print("elimine")
                                
                                    verificar=1
                                
                        if verificar==1:
                             return 0
                        
                    else:
                        return 3 # tabla no existe
                else:
                    return 2
            else:
                return 2 #base no existente
        except :
             return 1 #Error en la operacion    

