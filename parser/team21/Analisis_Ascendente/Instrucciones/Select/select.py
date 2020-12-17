from Instrucciones.instruccion import Instruccion
#from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Select(Instruccion):
    def __init__(self, distinct, time, columnas, subquery, inner, orderby, limit, complemetS):
        self.distinct = distinct
        self.time = time
        self.columnas = columnas #puede venir *
        self.subquery = subquery
        self.inner = inner #por el momento solo viene lista de columnas o group by
        self.orderby = orderby #es listaID o None
        self.limit = limit
        self.complemetS = complemetS



class Limit(Instruccion):
    def __init__(self, all, e1, e2):
        self.all = all
        self.e1 = e1
        self.e2 = e2


class Having(Instruccion):
    def __init__(self, lista, ordenar, andOr):
        self.lista = lista
        self.ordenar = ordenar #ASC DESC None
        self.andOr = andOr #si es None, no es having


class GroupBy(Instruccion):
    def __init__(self, listaC, compGroup, ordenar):
        self.listaC = listaC
        self.compGroup = compGroup #es otra lista
        self.ordenar = ordenar #ASC DESC None