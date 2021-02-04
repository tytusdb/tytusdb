from sql.storageManager.jsonMode import *
class Arbol():
    'Esta clase almacenará todas las instrucciones, errores y mensajes.'
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.excepciones = []
        self.consola = []
        self.bdUsar = None
        self.listaBd = []
        self.where = False
        self.update = False
        self.relaciones = False
        self.nombreTabla = None
        self.tablaActual = []
        self.columnasActual = []
        self.lEnum = []
        self.lRepDin = []
        self.comprobacionCreate = False
        self.columnaCheck = None
        self.order = None

    def setEnum(self, nuevo):
        self.lEnum.append(nuevo)

    #devuelve un objeto enum
    def getEnum(self, nombre):
        for x in range(0, len(self.lEnum)):
            if nombre == self.lEnum[x].id:
                return self.lEnum[x]
        
        return None

    def setListaBd(self, nueva):
        self.listaBd.append(nueva)

    #esto es para la base de datos actual
    def setBaseDatos(self,datos):
        self.bdUsar = datos
        print("la tabla a usar es "+self.bdUsar)

    #retornar la base de datos
    def getBaseDatos(self):
        return self.bdUsar

    def devolverBaseDeDatos(self):
        nombre = self.getBaseDatos()
        for x in range(0,len(self.listaBd)):
            if(self.listaBd[x].nombreTabla == nombre):
                #print(self.listaBd[x])
                return self.listaBd[x]

    def existeBd(self,nombre):
        for x in range(0,len(self.listaBd)):
            if(self.listaBd[x].nombreTabla == nombre):
                return 1
        return 0

    def eliminarBD(self,nombre):
        for x in range(0,len(self.listaBd)):
            if(self.listaBd[x].nombreTabla == nombre):
                self.listaBd.pop(x)
                return 1
        return 0

    def renombrarBd(self, nombre1, nombre2):
        for x in range(0,len(self.listaBd)):
            if(self.listaBd[x].nombreTabla == nombre2):
                print(self.listaBd[x])
                return self.listaBd[x]

    def eliminarTabla(self, nombreT):
        res = self.devolverBaseDeDatos()
        res.eliminarTabla(nombreT)

    def agregarTablaABd(self, nueva):
        #devolver tabla
        res = self.devolverBaseDeDatos()
        res.agregarTabla(nueva)

    def llenarTablas(self,nombre):
        #agregar las tablas
        tablas = showTables(nombre)
        self.devolverBaseDeDatos()
        self.agregarTablaABd(tablas)

    def devolviendoTablaDeBase(self, nombreTabla):
        nombreBd = self.getBaseDatos()
        if(self.existeBd(nombreBd) == 1):
            base = self.devolverBaseDeDatos()
            tabla = base.devolverTabla(nombreTabla)
            if( tabla == 0):
                print("No se encontro la tabla")
                return 0
            else:
                return tabla

    def devolverColumnasTabla(self,nombreTabla):
        print(nombreTabla)
        tabla = self.devolviendoTablaDeBase(nombreTabla)
        if(tabla == 0):    
            print("No se encontro la tabla")
            return 0
        else:
            return tabla.devolverTodasLasColumnas()


    def devolverOrdenDeColumna(self, nombreTabla, nombreColumna):
        nombreBd = self.getBaseDatos()
        if(self.existeBd(nombreBd) == 1):
            base = self.devolverBaseDeDatos()
            tabla = base.devolverTabla(nombreTabla)
            if( tabla == 0):
                print("No se encontro la tabla")
            else:
                res = tabla.devolverColumna(nombreColumna)
                if(res==-1):
                    print("No se encontro el ide")
                    return -1
                return res
        else:
            print("No existe bd en uso")
            return -1

    def devolverTipoColumna(self, nombreTabla, nombreColumna):
        nombreBd = self.getBaseDatos()
        if(self.existeBd(nombreBd) == 1):
            base = self.devolverBaseDeDatos()
            tabla = base.devolverTabla(nombreTabla)
            if( tabla == 0):
                print("No se encontro la tabla")
            else:
                res = tabla.devolverTipo(nombreColumna)
                if(res==-1):
                    print("No se encontro el ide")
                    return -1
                return res
        else:
            print("No existe bd en uso")
            return -1

    def getMensajeTabla(self, columnas, tuplas):
        lf = []
        for i in range(0,len(columnas)):
            temporal = []
            temporal.append(len(columnas[i]))
            for l in tuplas:
                temporal.append(len(str(l[i])))
            lf.append(max(temporal))

        # Encabezado
        cad = ''
        for s in range(0,len(lf)):
            cad += '+---'+'-'*lf[s]
        cad += '+\n'    
        for s in range(0,len(lf)):
            cad += '| ' +str(columnas[s]) + ' ' *((lf[s]+4)-(2+len(str(columnas[s]))))
        cad += '|\n'
        cad += '|'
        for s in range(0,len(lf)):
            cad += '---'+'-'*lf[s]+ '+'
        size = len(cad)
        cad = cad[:size - 1] + "|\n"

        # Valores
        for i in tuplas:
            for j in range(0,len(lf)):
                cad += '| ' + str(i[j]) + ' ' *((lf[j]+4)-(2+len(str(i[j]))))
            cad += "|\n"
        # Línea final
        for s in range(0,len(columnas)):
            cad += '+---'+'-'*lf[s]
        cad += '+\n'
        self.consola.append(cad)

    def setColumnasActual(self, valor):
        self.columnasActual = valor

    def getColumnasActual(self):
        return self.columnasActual
    
    def setWhere(self, valor):
        self.where = valor

    def getWhere(self):
        return self.where
    
    def setTablaActual(self, valor):
        self.tablaActual = valor 
    
    def getTablaActual(self):
        return self.tablaActual

    def setRelaciones(self, valor):
        self.relaciones = valor

    def getRelaciones(self):
        return self.relaciones

    def setUpdate(self):
        self.update = not self.update

    def getUpdate(self):
        return self.update

    def getNombreTabla(self):
        return self.nombreTabla

    def setNombreTabla(self, valor):
        self.nombreTabla = valor

    def devolverTamanio(self, nombreTabla):
        tabla = self.devolviendoTablaDeBase(nombreTabla)
        can = tabla.devolverTodasLasColumnas()
        return len(can)

    def setOrder(self, order):
        self.order = order
    
    def getOrder(self):
        return self.order
    