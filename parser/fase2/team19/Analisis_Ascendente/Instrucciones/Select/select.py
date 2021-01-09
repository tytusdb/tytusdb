#from Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion

class Select(Instruccion):
    '''#1 time
       #2 p_instselect
       #3 p_instselect2
       #4 p_instselect3
       #5 p_instselect4
       #6 p_instselect7'''

    def __init__(self, caso, distinct, time, columnas, subquery, inner, orderby, mode, limit, complementS,fila,columna):
        self.caso = caso
        self.distinct = distinct
        self.time = time
        self.columnas = columnas #puede venir *
        self.subquery = subquery
        self.inner = inner #por el momento solo viene lista de columnas o group by #vienen los nombres
        if orderby is not None:
            self.orderby = orderby["lista"]
            self.orderbymod = orderby["mode"]
        else:
            self.orderby = orderby
            self.orderbymod = orderby
        self.limit = limit
        self.complementS = complementS
        self.fila = fila
        self.columna = columna

    def get_quemado(self):
        return ''


class Limit(Instruccion):
    def __init__(self, all, e1, e2,fila,columna):
        self.all = all
        self.e1 = e1
        self.e2 = e2
        self.fila = fila
        self.columna = columna



class Having(Instruccion):
    def __init__(self, lista, ordenar, andOr,fila,columna):
        self.lista = lista
        self.ordenar = ordenar #ASC DESC None
        self.andOr = andOr #si es None, no es having
        self.fila = fila
        self.columna = columna


class GroupBy(Instruccion):
    def __init__(self, listaC, compGroup, ordenar,fila,columna):
        self.listaC = listaC
        self.compGroup = compGroup #es otra lista o having
        self.ordenar = ordenar #ASC DESC None
        self.fila = fila
        self.columna = columna
