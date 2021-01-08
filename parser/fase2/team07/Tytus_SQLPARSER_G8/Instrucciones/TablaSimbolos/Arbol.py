from storageManager.jsonMode import *
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
        self.numeroTemporal = 0
        self.numeroEtiqueta = 0
        self.valoresActuales = []

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
        self.valoresActuales = tuplas

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

    def generaEtiqueta(self):
        self.numeroEtiqueta = self.numeroEtiqueta + 1
        etiqueta = "L" + str(self.numeroEtiqueta)
        return etiqueta
    
    def generaTemporal(self):
        self.numeroTemporal = self.numeroTemporal + 1
        temporal = "t" + str(self.numeroTemporal)
        return temporal

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def esFuncionNativa(self,funcion):
        #Funciones de agregacion
        if "AVG(" in funcion:
            return True
        elif "COUNT(" in funcion:
            return True
        elif "GREATEST(" in funcion:
            return True
        elif "LEAST(" in funcion:
            return True
        elif "MAX(" in funcion:
            return True
        elif "MIN(" in funcion:
            return True
        elif "SUM(" in funcion:
            return True
        elif "TOP(" in funcion:
            return True
        
        #Funciones Matematicas
        elif "ABS(" in funcion:
            return True
        elif "CBRT(" in funcion:
            return True
        elif "CEIL(" in funcion:
            return True
        elif "CEILING(" in funcion:
            return True
        elif "DEGREES(" in funcion:
            return True
        elif "DIV(" in funcion:
            return True
        elif "EXP(" in funcion:
            return True
        elif "FACTORIAL(" in funcion:
            return True
        elif "FLOOR(" in funcion:
            return True
        elif "GCD(" in funcion:
            return True
        elif "LCM(" in funcion:
            return True
        elif "LN(" in funcion:
            return True
        elif "LOG(" in funcion:
            return True
        elif "LOG10(" in funcion:
            return True
        elif "MIN_SCALE(" in funcion:
            return True
        elif "MOD(" in funcion:
            return True
        elif "PI(" in funcion:
            return True
        elif "POWER(" in funcion:
            return True
        elif "RADIANS(" in funcion:
            return True
        elif "RANDOM(" in funcion:
            return True
        elif "ROUND(" in funcion:
            return True
        elif "SCALE(" in funcion:
            return True
        elif "SETSEED(" in funcion:
            return True
        elif "SIGN(" in funcion:
            return True
        elif "SQRT(" in funcion:
            return True
        elif "TRIM_SCALE(" in funcion:
            return True
        elif "TRUNC(" in funcion:
            return True
        elif "WIDTH_BUCKET(" in funcion:
            return True
        
        #Funciones de string
        elif "CONVERT(" in funcion:
            return True
        elif "DECODE(" in funcion:
            return True
        elif "ENCODE(" in funcion:
            return True
        elif "GET_BYTE(" in funcion:
            return True
        elif "LENGTH(" in funcion:
            return True
        elif "MD5(" in funcion:
            return True
        elif "SET_BYTE(" in funcion:
            return True
        elif "SHA256(" in funcion:
            return True
        elif "SUBSTR(" in funcion:
            return True
        elif "SUBSTRING(" in funcion:
            return True
        elif "TRIM(" in funcion:
            return True

        #Funciones trigonometricas
        elif "ACOS(" in funcion:
            return True
        elif "ACOSD(" in funcion:
            return True
        elif "ACOSH(" in funcion:
            return True
        elif "ASIN(" in funcion:
            return True
        elif "ASIND(" in funcion:
            return True
        elif "ASINH(" in funcion:
            return True
        elif "ATAN(" in funcion:
            return True
        elif "ATAN2(" in funcion:
            return True
        elif "ATAN2D(" in funcion:
            return True
        elif "ATAND(" in funcion:
            return True
        elif "ATANH(" in funcion:
            return True
        elif "COS(" in funcion:
            return True
        elif "COSD(" in funcion:
            return True
        elif "COSH(" in funcion:
            return True
        elif "COT(" in funcion:
            return True
        elif "COTD(" in funcion:
            return True
        elif "SIN(" in funcion:
            return True
        elif "SIND(" in funcion:
            return True
        elif "SINH(" in funcion:
            return True
        elif "TAN(" in funcion:
            return True
        elif "TAND(" in funcion:
            return True
        elif "TANH(" in funcion:
            return True
        
        #Funciones TIME
        elif "NOW(" in funcion:
            return True
        elif "EXTRACT(" in funcion:
            return True
        elif "DATE_PART(" in funcion:
            return True
        
        else:
            return False