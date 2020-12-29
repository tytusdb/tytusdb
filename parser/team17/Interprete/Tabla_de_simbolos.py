from Interprete.simbolo import Simbolo
from Interprete.Valor.Valor import Valor

class Tabla_de_simbolos(Simbolo) :

    def __init__(self) :
        super().__init__("","","")
        self.Pila_de_tablas  = [[]]
        self.Tabla_deSimbolos = []
        self.BD = ""
        self.actual_table = []

    def NuevoAmbito(self):
        nuevoAmito = [Simbolo("VACIO", 2, Valor(2, "VACIO"))]
        self.Pila_de_tablas.append(nuevoAmito)

    def BorrarAmbito(self):
        self.Pila_de_tablas.pop()

    def insertar_variable(self, simbol:Simbolo):
        for item in self.Pila_de_tablas[len(self.Pila_de_tablas) - 1]:
            simbol_: Simbolo = item
            if simbol_.id == simbol.id:
                item = simbol
                print("TS -> se inserto la var: " + simbol.id)
                return
        self.Pila_de_tablas[len(self.Pila_de_tablas) - 1].append(simbol)
        print("TS -> se inserto la var: " + simbol.id )

    def obtener_varibale(self, identificador):
        '''entorno: [] = self.Pila_de_tablas[len(self.Pila_de_tablas) - 1]
        for item_1 in range(len(entorno)):
            simbol:Simbolo = entorno[item_1]
            if simbol.id == identificador:
                return simbol.valor'''
        for item in self.Pila_de_tablas[len(self.Pila_de_tablas) - 1]:
            simbol: Simbolo = item
            if simbol.id == identificador:
                return simbol.valor

    def varibaleExiste(self, identificador):
        for item in self.Pila_de_tablas[len(self.Pila_de_tablas) - 1]:
            simbol: Simbolo = item
            if simbol.id == identificador:
                return True
        return False
    '''
        Manejo de BD
    '''
    def setBD(self, id):
        self.BD = str(id)

    def BDisNull(self):
        if self.BD == "":
            return True
        else:
            return False

    def getBD(self):
        return str(self.BD)

    def settable(self, table):
        self.actual_table = table

    def gettable(self):
        return self.actual_table
