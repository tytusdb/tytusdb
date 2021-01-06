import Error as Error

class Simbolo:
    '''Clase Símbolo Para un Leguaje de Programación Convencional '''

    def __init__(self, nombre, tipo, valor, fila, columna, ambito):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.ambito = ambito


class SimboloBase:
    ''' Clase Para Almacenar La Información De Una Base de Datos '''

    def __init__(self, nombre, owner, mode):
        self.nombre = nombre
        self.owner = owner
        self.mode = mode
        self.tablas = {}
        self.funciones={}

    def crearTabla(self, id, tabla):
        if id not in self.tablas:
            self.tablas[id] = tabla
            return True
        return None

    def crearF(self,id,funcion):
        if id not in self.funciones:
            self.funciones[id]=funcion
            return True
        return None 

    def getFuncion(self,id):
        if id in self.funciones:
            return self.funciones[id]
        return None

    def deleteFuncion(self,id):
        if id in self.funciones:
            del self.funciones[id]
            return True
        return None

    def getTabla(self, id):

        if id in self.tablas:
            return self.tablas[id]

        return None

    def deleteTable(self, id):
        if id in self.tablas:
            del self.tablas[id]
            return True
        return None

    def renameTable(self, idactual, idnuevo):
        if idactual in self.tablas:
            if idnuevo not in self.tablas:
                self.tablas[idnuevo] = self.tablas.pop(idactual)
                self.tablas[idnuevo].nombre = idnuevo
                return 0
            return 1
        return 2


class SimboloTabla:
    '''Clase Símbolo Para Almacenar Información de Las Tablas '''

    def __init__(self, nombre, padre):
        self.nombre = nombre
        self.columnas = {}
        self.padre = padre
        self.indices = []


    def __str__(self):
        return "{ 'SimboloTabla' | 'nombre': %s, 'padre': %s, 'columnas': %s, indices: '%s' }" % (
            str(self.nombre), str(self.padre), str(self.columnas), str(self.indices)
        )

    def modificarColumnaIndice(self,nombre,viejo,nuevo):
        
        for i in range(len(self.indices)):

            if nombre == self.indices[i].nombre:

                for j in range(len(self.indices[i].columnas)):

                    if viejo == self.indices[i].columnas[j]:
                        self.indices[i].columnas[j] = nuevo
                        return True

        return False




    def alterarIndice(self,nombre,nuevo):
        
        modificado = False

        for i in range(len(self.indices)):

            if nombre == self.indices[i].nombre:
                self.indices[i].nombre = nuevo
                modificado = True
                break
        
        return modificado

    
    def eliminarIndice(self,nombre):

        eliminado = False
        
        for i in range(len(self.indices)):

            if nombre == self.indices[i].nombre:
                self.indices.pop(i)
                eliminado = True
                break
        
        return eliminado



    def crearIndice(self, nombre,tipo,columnnas,orden,null_first,null_last,lower,condicion,unique):

        listaErrores = []


        if len(listaErrores) > 0:

            return listaErrores

        else:

            self.indices.append(SimboloIndice(nombre, tipo, columnnas,orden,null_first,null_last,lower,condicion,unique))
              
            return True



            





    def comprobarNulas(self, listaColumnas):
        #VERIFICAMOS SI EXISTE EN LA TABLA
        nombres = []
        for col in listaColumnas:
            nombres.append(col.valor)
            if col.valor not in self.columnas:
                return {"cod": 1, "col": col.valor}
        
        

        #VERIFICAMOS SI EN LA LISTA DE COLUMNAS VIENEN COLUMNAS NO NULAS
        for col in self.columnas:
            if self.columnas[col].nombre not in nombres:
                if self.columnas[col].null != True and self.columnas[col].default == None and self.columnas[col].primary_key==True:
                    return {"cod": 2, "col": self.columnas[col].nombre}
        return {"cod": 0}

    # MÉTODO PARA OBTENER LOS ÍNDICES DE LAS LLAVES PRIMARIAS
    def get_pk_index(self):

        i = 0
        lista = []
        for k in self.columnas:
            if self.columnas[k].primary_key:
                lista.append(i)
            i += 1
        return lista

    def comprobarNulas2(self, listaColumnas):
        #VERIFICAMOS SI EXISTE EN LA TABLA
        nombres = []
        for col in listaColumnas:
            nombres.append(col)
            if col not in self.columnas:
                return {"cod": 1, "col": col}
        # VERIFICAMOS SI EN LA LISTA DE COLUMNAS VIENEN COLUMNAS NO NULAS
        for col in self.columnas:
            if self.columnas[col].nombre not in nombres:
                if self.columnas[col].null != True and self.columnas[col].default == None and self.columnas[col].primary_key == True:
                    return {"cod": 2, "col": self.columnas[col].nombre}
        return {"cod": 0}

    def deleteColumn(self, id):
        val = 0
        if id in self.columnas:
            val = self.columnas[id].index
            del self.columnas[id]
            return True
        for id2 in self.columnas:
            if self.columnas[id2].index > val:
                self.columnas[id2].index = self.columnas[id2].index - 1
        return None

    def crearColumna(self, id, columna):
        if id not in self.columnas:
            self.columnas[id] = columna
            return True
        return None

    def getIndex(self, idcol):
        if idcol in self.columnas:
            return self.columnas[idcol].index
        return None

    def renameColumna(self, idactual, idnuevo):
        if idactual in self.columnas:
            if idnuevo not in self.columnas:
                self.columnas[idnuevo] = self.columnas.pop(idactual)
                self.columnas[idnuevo].nombre = idnuevo
                return 0
            return 1
        return 2

    def modificarUnique(self, idcol, unique, idconstraint):
        if idcol in self.columnas:
            self.columnas[idcol].unique = {"id": idconstraint, "unique": unique}
            return True
        return None

    def deleteUnique(self, idcol):
        if idcol in self.columnas:
            self.columnas[idcol].unique = False
            return True
        return None

    def modificarCheck(self, idcolumna, condicion, idconstraint):
        if idcolumna in self.columnas:
            self.columnas[idcolumna].check = {"id": idconstraint, "condicion": condicion}
            return True
        return None

    def deleteCheck(self, idcol):
        if idcol in self.columnas:
            self.columnas[idcol].check = None
            return True
        return None

    def modificarFk(self, idlocal, idTablaFk, idcolFk):
        if idlocal in self.columnas:
            self.columnas[idlocal].foreign_key = {"tabla": idTablaFk, "columna": idcolFk}
            return True
        return None

    def deleteFk(self, idcol):
        if idcol in self.columnas:
            self.columnas[idcol].foreign_key = None
            return True
        return None

    def modificarPk(self, id):
        if id in self.columnas:
            self.columnas[id].primary_key = True
            return True
        return None

    def modificarNull(self, idcol):
        if idcol in self.columnas:
            self.columnas[idcol].null = False
            return True
        return None

    def modificarTipo(self, idcol, tipo, ntama):
        if idcol in self.columnas:
            if self.columnas[idcol].tipo.tipo == tipo:
                if self.columnas[idcol].tipo.cantidad < ntama:
                    self.columnas[idcol].tipo.cantidad = ntama
                    return 0
                return 1
            return 2
        return 3

    def getColumna(self, idcolumna):
        if idcolumna in self.columnas:
            return self.columnas[idcolumna]
        else:
            return None

    def get_name_list(self):
        names = []

        for name in self.columnas:
            names.append(name)

        return names


class colsConsulta:
    def __init__(self, nombre, alias, tipo, param, tabla, cindice,vtipo,nodo):
        self.nombre = nombre
        self.alias = alias
        self.tipo = tipo
        self.param = param
        self.tabla = tabla
        self.cindice = cindice
        self.vtipo=vtipo
        self.nodo=nodo


class Grupo:
    def __init__(self, indice, indiceCol, tabla, valor):
        self.indice = indice
        self.indiceCol = indiceCol
        self.tabla = tabla
        self.valor = valor


class colsTabla:
    def __init__(self, nombre, alias):
        self.nombre = nombre
        self.alias = alias


class SimboloColumna:
    ''' Clase Para Almacenar Información Sobre Las Columnas de Una Tabla '''

    def __init__(self, nombre, tipo, primary_key, foreign_key, unique, default, null, check, index):
        self.nombre = nombre
        self.tipo = tipo
        self.primary_key = primary_key
        self.foreign_key = foreign_key
        self.unique = unique
        self.default = default
        self.null = null
        self.check = check
        self.index = index

    def __str__(self):
        return "{ 'SimboloColumna' | 'nombre': %s, 'tipo': %s, 'primary_key': %s,'foreign_key': %s, 'unique': %s, 'default': %s,'null': %s, 'check': %s, 'index': %s }" % (
            str(self.nombre), str(self.tipo), str(self.primary_key), str(self.foreign_key), str(self.unique), str(self.default), str(self.null), str(self.check), str(self.index))


class SimboloIndice:
    
    def __init__(self, nombre, tipo, columnas,orden,null_first,null_last,lower,condicion,unique):
        self.nombre = nombre
        self.tipo = tipo
        self.columnas = columnas
        self.orden = orden
        self.null_first = null_first
        self.null_last = null_last
        self.lower = lower
        self.condicion = condicion
        self.unique = unique




    def __str__(self):
        return "{ SimboloIndice | nombre: '%s', tipo: '%s', columnas: '%s', orden: '%s', null_first: '%s', null_last: '%s', lower: '%s', condicion: '%s', unique: '%s' }" % ( 
            str(self.nombre), str(self.tipo), str(self.columnas), str(self.orden), str(self.null_first), str(self.null_last), str(self.lower), str(self.condicion), str(self.unique) 
            )


class UbicacionIndice:

    def __init__(self,base,tabla,nombre) -> None:
        self.base = base
        self.tabla = tabla
        self.nombre = nombre


    def __str__(self):
        return "{ UbicacionIndice | base: '%s', tabla: '%s', nombre: '%s' }" %(
            str(self.base), str(self.tabla), str(self.nombre)
        )

class llaveForanea:
    def __init__(self, idbase, idtlocal, idtfk, idclocal, idcfk):
        self.idbase = idbase
        self.idtlocal = idtlocal
        self.idtfk = idtfk
        self.idclocal = idclocal
        self.idcfk = idcfk


class Constraints:
    def __init__(self, idbase, idtabla, idconstraint, idcol, tipo):
        self.idbase = idbase
        self.idtabla = idtabla
        self.idconstraint = idconstraint
        self.idcol = idcol
        self.tipo = tipo

class SimboloVariable:
    def __init__(self, nombre, tipo, valor, ambito):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
        self.ambito = ambito

class SimboloFuncion:
    def __init__(self, nombre,parametros, tipo, retorno, ambito):
        self.nombre = nombre
        self.tipo = tipo
        self.retorno = retorno
        self.ambito = ambito
        self.variables={}

    def crearVariable(self,id,variable):
        if id not in self.variables:
            self.variables[id]=variable
            return True
        return None 

    def getVariable(self,id):
        if id in self.variables:
            return self.variables[id]
        return None

    def deleteVariable(self,id):
        if id in self.variables:
            del self.variables[id]
            return True
        return None


class SimboloProcedure:
    def __init__(self, nombre,parametros, tipo, retorno, ambito):
        self.nombre = nombre
        self.tipo = tipo
        self.retorno = retorno
        self.ambito = ambito

class Entorno:

    # CONSTRUCTOR PARA LA TABLA DE SÍMBOLOS
    def __init__(self, ent):
        self.tabla = {}
        self.padre = ent

    # COLOCAR UN SÍMBOLO
    def put(self, s, simbolo):
        self.tabla[s] = simbolo

    # OBTENER EL VALOR DE UN SÍMBOLO
    def get_value(self, id):

        myEnt = self

        while myEnt != None:

            if id in myEnt.tabla:
                return myEnt.tabla[id]

            myEnt = myEnt.padre

        return None

    # GET BASE
    def get(self, id):
        for key in self.tabla.keys():
            if self.tabla[key].nombre == id:
                return self.tabla[key]
        return None

    # eliminar base
    def eliminar(self, id):
        for key in self.tabla.keys():
            if self.tabla[key].nombre == id:
                del self.tabla[key]
                return True
        return None

    # renombrar base
    def renameBase(self, idactual, idnuevo):
        actual = self.get(idactual)
        if actual != None:
            self.tabla[idnuevo] = self.tabla.pop(idactual)
            self.tabla[idnuevo].nombre = idnuevo
            return True
        return None

    # MOSTRAR Base
    def mostrar(self):
        for key in self.tabla.keys():
            print("Nombre Base")
            print(self.tabla[key].nombre)
            print("Owner")
            print(self.tabla[key].owner)
            print("Mode")
            print(self.tabla[key].mode)
            print("-------------------")
            base = self.tabla[key]
            for tab in base.tablas:
                print("Columnas")
                tabla = base.tablas[tab]
                print(tabla.columnas)
                for col in tabla.columnas:
                    print(tabla.columnas[col].nombre)
                    print(tabla.columnas[col].tipo)
                    print(tabla.columnas[col].primary_key)
                    print(tabla.columnas[col].foreign_key)
                    print(tabla.columnas[col].default)
                    print(tabla.columnas[col].check)
                    print(tabla.columnas[col].unique)

    # Get columna
    def getColumna(self, idbase, idtabla, idcol):
        base = self.get(idbase)
        if base != None:
            tabla = base.getTabla(idtabla)
            return tabla.getColumna(idcol)
        return None

    def mostrar_tabla(self):

        salida = ""

        for k in self.tabla:
            salida += "\n"
            salida += "===========================================================" + "\n"
            salida += "BASE DE DATOS    : " + str(self.tabla[k].nombre) + "\n"
            salida += "OWNER            : " + str(self.tabla[k].owner) + "\n"
            salida += "DUEÑO            : " + str(self.tabla[k].mode) + "\n"
            salida += "-----------------------------------------------------------" + "\n"

            for j in self.tabla[k].tablas:

                my_tabla = self.tabla[k].tablas[j]
                salida += "\tNOMBRE TABLA   : " + str(my_tabla.nombre) + "\n"
                salida += "\tPADRE          : " + str(my_tabla.padre) + "\n"
                salida += "-----------------------------------------------------------" + "\n"

                for l in my_tabla.columnas:

                    my_column = my_tabla.columnas[l]

                    salida += "\t\tNOMBRE COLUMNA   : " + str(my_column.nombre) + "\n"
                    salida += "\t\tTIPO COLUMNA     : " + str(my_column.tipo) + "\n"
                    salida += "\t\tLLAVES PRIMARIAS : " + str(my_column.primary_key) + "\n"
                    salida += "\t\tLLAVES FORÁNEAS  : " + str(my_column.foreign_key) + "\n"
                    salida += "\t\tCLÁUSULA UNIQUE  : " + str(my_column.unique) + "\n"
                    salida += "\t\tCLÁUSULA DEFAULT : " + str(my_column.default) + "\n"
                    salida += "\t\tCLÁUSULA NULL    : " + str(my_column.null) + "\n"
                    salida += "\t\tCLÁUSULA CHECK   : " + str(my_column.check) + "\n"
                    salida += "\t\tCLÁUSULA INDEX   : " + str(my_column.index) + "\n"
                    salida += "\n"

        return salida



        

        