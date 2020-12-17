from storageManager.jsonMode import *
class Arbol():
    'Esta clase almacenará todas las instrucciones, errores y mensajes.'
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.excepciones = []
        self.consola = []
        self.bdUsar = None
        self.listaBd = []

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

    def devolverTabla(self, nombre):
        for x in range(0,len(self.listaBd)):
            if(self.listaBd[x].nombreTabla == nombre):
                return self.listaBd[x]
        return 0

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
