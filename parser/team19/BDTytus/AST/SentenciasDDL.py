from AST.Nodo import Nodo

class CreateDatabase(Nodo):
    def __init__(self, Exp1, Exp2, op, fila, col):
        super().__init__(fila, col)
        self.Exp1 = Exp1
        self.Exp2 = Exp2
        self.op = op

class ShowDatabases(Nodo):
    def __init__(self, fila, columna):
        super().__init__(fila=fila, columna=columna)

    def ejecutar(self,TS,Errores):
        return ['Aqui mando a llamar el metodo de los de estructuras show databases']

    def getC3D(self,TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)

class CreateType(Nodo):
    def __init__(self, nombre_type, lista_enum, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.nombre_type = nombre_type
        self.lista_enum = lista_enum

    def ejecutar(self, TS, Errores):
        return ['Aqui se deben crear y guardar los tipos']

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_type%s" % self.mi_id, 'nombre: %s' % self.nombre_type)
        grafica.edge(self.mi_id,"nombre_type"+self.mi_id)

        id_lista = "lista_type%s" % self.mi_id
        grafica.node(id_lista, 'lista_enum')
        grafica.edge(self.mi_id, id_lista)
        for i,enum in enumerate(self.lista_enum):
            enum_id = "%senum%s" % (str(i), self.mi_id)
            grafica.node(enum_id, enum)
            grafica.edge(id_lista, enum_id)


