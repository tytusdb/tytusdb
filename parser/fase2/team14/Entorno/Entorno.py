from graphviz import Digraph


class Entorno:
    def __init__(self, anterior=None):
        self.anterior = anterior
        self.database = ""
        self.tablaSimbolo = {}
        self.consola = []
        self.temp = 0
        self.label = 0
        self.codigo = ''

    def nuevoSimbolo(self, symbol):
        x = self.tablaSimbolo.get(symbol.nombre)

        if x == None:
            self.tablaSimbolo[symbol.nombre] = symbol
            return "ok"

        return str("El simbolo " + symbol.nombre + " no se puede agregar porque ya existe")

    def editarSimbolo(self, identificador, nuevo):
        x = self.tablaSimbolo.get(identificador)

        if x != None:
            self.tablaSimbolo[identificador] = nuevo
            return "ok"

        return str("El simbolo " + identificador + " no se puede modificar porque no existe")

    def eliminarSimbolo(self, identificador):
        x = self.tablaSimbolo.get(identificador)

        if x != None:
            del self.tablaSimbolo[identificador]
            return "ok"

        return str("el simbolo " + identificador + " no se puede eliminar porque no existe")

    def buscarSimbolo(self, identificador):
        ent = self

        while ent != None:
            x = ent.tablaSimbolo.get(identificador)
            if x != None:
                return x
            ent = ent.anterior

        return None

    def mostrarSimbolos(self):
        ent = self

        # nombre,tipoSym,baseDatos,tabla,valor
        salida = ""
        while ent != None:
            for x in ent.tablaSimbolo.values():
                if x != None:
                    salida += x.toString()

            ent = ent.anterior

        return salida
    
    def mostrarProc(self):
        ent = self

        # nombre,tipoSym,baseDatos,tabla,valor
        salida = ""
        while ent != None:
            for x in ent.tablaSimbolo.values():
                if x != None:
                    salida += x.proc()

            ent = ent.anterior

        return salida

    def getDataBase(self):
        ent = self

        while ent != None:
            x = ent.database
            if x != "":
                return x
            ent = ent.anterior

        return None

    def eliminarDataBase(self, basedatos):
        ent = self

        while ent != None:
            x = 0
            for x in ent.tablaSimbolo.copy():
                db: str = ent.tablaSimbolo[x].baseDatos
                if db == basedatos:
                    ent.tablaSimbolo.pop(x)

            ent = ent.anterior

        return None

    def eliminarIndex(self, nombreIndex):
        eliminado: bool = False
        ent = self

        while ent != None:
            x = 0
            for x in ent.tablaSimbolo.copy():
                ix: str = ent.tablaSimbolo[x].indexId
                if ix == nombreIndex:
                    ent.tablaSimbolo.pop(x)
                    eliminado = True

            ent = ent.anterior

        return eliminado

    def buscarIndex(self, nombreIndex):
        ent = self

        while ent != None:
            x = 0
            for x in ent.tablaSimbolo.copy():
                ix: str = ent.tablaSimbolo[x].indexId
                if ix == nombreIndex:
                    return ent.tablaSimbolo[x]

            ent = ent.anterior

        return None

    def renombrarDatabase(self, viejaDB, nuevaDB):
        ent = self

        while ent != None:
            x = 0
            for x in ent.tablaSimbolo.copy():
                db: str = ent.tablaSimbolo[x].baseDatos
                if db == viejaDB:
                    ent.tablaSimbolo[x].baseDatos = nuevaDB

            ent = ent.anterior

    def eliminarSymTabla(self, tabla):
        ent = self

        while ent != None:
            for x in ent.tablaSimbolo.copy():
                table: str = ent.tablaSimbolo[x].tabla
                if table == tabla:
                    ent.tablaSimbolo.pop(x)

            ent = ent.anterior

    def eliminarTodo(self):
        ent = self
        while ent != None:
            ent.tablaSimbolo = {}

            ent = ent.anterior

    def newtemp(self):
        self.temp += 1
        return 't' + str(self.temp)

    def newlabel(self, nombre=''):
        if nombre == '':
            self.label += 1
            return '.L' + str(self.label)
        else:
            return '.L' + str(nombre)