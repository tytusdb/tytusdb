#from Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion,ColCase,Case
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import  IdAsId,Id,IdId
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import  Math_
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import  Trigonometrica
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario as Binario
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Where as Where
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Time as Time

class Select(Instruccion):
    '''#1 time
       #2 p_instselect
       #3 p_instselect2
       #4 p_instselect3
       #5 p_instselect4
       #6 p_instselect7'''

    def __init__(self, caso, distinct, time, columnas, subquery, inner, orderby, limit, complementS,concatena,fila,columna):
        self.caso = caso
        self.distinct = distinct
        self.time = time
        self.columnas = columnas #puede venir *
        self.subquery = subquery
        self.inner = inner #por el momento solo viene lista de columnas o group by #vienen los nombres
        self.orderby = orderby #es listaID o None
        self.limit = limit
        self.complementS = complementS
        self.fila = fila
        self.columna = columna
        self.concatena = concatena

    def obtenerCadenalistColumna(lista):
        select_list=''
        cont=0
        for columna in lista:
            if isinstance(columna, Id):
                print(columna.id)
                select_list+=' '+str(columna.id)+' '
            elif isinstance(columna,IdId):
                select_list+= IdId.ObtenerCadenaEntrada(columna)+' '
            elif isinstance(columna, IdAsId):
                select_list+= ' '+IdAsId.ObtenerCadenaEntrada(columna,True)+' '
            elif isinstance(columna, Math_):
                select_list+=' '+ Math_.obtenerCadenaEntrada(columna,True)+' '
            elif isinstance(columna, Trigonometrica):
                select_list+=' '+Trigonometrica.obtenerCadenaEntrada(columna,True)+' '
            elif isinstance(columna, Expresion.Expresion):
                select_list+= ' '+ Expresion.Expresion.ObtenerCadenaEntrada(columna,True)+' '
            elif isinstance(columna, Binario.Binario):
                select_list+= ' '+Binario.Binario.ObtenerCadenaEntrada(columna,True)+' '
            elif isinstance(columna, Time.Time ):
                select_list+= ' '+Time.Time.ObtenerCadenaEntrada(columna)+' '
            elif isinstance(columna,ColCase):
                select_list+= ' '+ Select.ObtenerCadenaEntradaColCase(columna.cases)+' '+str(columna.id)+' '
            cont += 1
            if cont < len(lista):
                select_list+=', '
            else:
                select_list+=' '
        return select_list

    def obtenerCadenaInner(inner):
        print(type(inner).__name__)
        if isinstance(inner,list):
            valrs= Select.obtenerCadenalistColumna(inner)
            return valrs
        elif isinstance(inner,GroupBy):
            valrs = GroupBy.ObtenerCadenaGroupBy(inner)
            return valrs

    def obtenerCadenaWhere(complementS):
        if isinstance(complementS,Expresion.Expresion):
            condicion = Expresion.Expresion.ObtenerCadenaEntrada(complementS,False);
        elif isinstance(complementS,GroupBy):
            condicion = GroupBy.ObtenerCadenaGroupBy(complementS)
        elif isinstance(complementS, Where.Where ):
            print(type(complementS).__name__) #esto es un caso where
            condicion = Where.Where.ObtenerCadenaEntrada(complementS)

        return condicion

    def ObtenerCadenaEntradaCase(case):

        if isinstance(case, Case):
            asign = str(Select.ObtenerCadenaEntradaCase(case.asignacion))
            val = str(Select.ObtenerCadenaEntradaCase(case.valor))
            cadena = ''
            cadena += ' WHEN ' + asign + ' THEN ' + val
            return cadena
        else:
            return str(Expresion.Expresion.ObtenerCadenaEntrada(case, False))

    def ObtenerCadenaEntradaColCase(Cases):  # CASE cases END ID

        if isinstance(Cases, list):
            listaCases = ' CASE '
            for casee in Cases:
                c = str(Select.ObtenerCadenaEntradaCase(casee))
                listaCases += c + ' '

            listaCases += ' END '
            return listaCases

        elif isinstance(Cases, Case):
            return str(Select.ObtenerCadenaEntradaCase(Cases))

class Limit(Instruccion):
    def __init__(self, all, e1, e2,fila,columna):
        self.all = all
        self.e1 = e1
        self.e2 = e2
        self.fila = fila
        self.columna = columna

    def ObtenerCadenaEntrada(limit):
        pass



class Having(Instruccion):
    def __init__(self, lista, ordenar, andOr,fila,columna):
        self.lista = lista
        self.ordenar = ordenar #ASC DESC None
        self.andOr = andOr #si es None, no es having
        self.fila = fila
        self.columna = columna

    def ObtenerCadenaHaving(hav):
        if isinstance(hav.lista,list):
            camposagrupar = Select.obtenerCadenalistColumna(hav.lista)

        if hav.andOr == None:
            #solo es un group by sencillo
            havCad=''
            if( hav.ordenar!=None):
                havCad= camposagrupar+' '+str(hav.ordenar)
            else:
                havCad= camposagrupar

            return  havCad
        else: #tiene having
            andor=''
            if isinstance(hav.andOr,Expresion.Expresion):
                andor= Expresion.Expresion.ObtenerCadenaEntrada(hav.andOr,False)

            havCad=''
            if hav.ordenar != None:
                havCad= camposagrupar + ' '+str(hav.ordenar)+' HAVING '+ andor
            else:
                havCad = camposagrupar + ' ' + ' HAVING ' + andor
            return havCad


class GroupBy(Instruccion):
    def __init__(self, listaC, compGroup, ordenar,fila,columna):
        self.listaC = listaC
        self.compGroup = compGroup #es otra lista o having
        self.ordenar = ordenar #ASC DESC None
        self.fila = fila
        self.columna = columna

    def ObtenerCadenaGroupBy(group):
        tablas=''
        camposagrupar=''
        if isinstance(group.listaC,list) and group.listaC!=None: #verificamos las tablas antes del group by
            tablas = Select.obtenerCadenalistColumna(group.listaC)
        elif isinstance(group.listaC,Expresion.Expresion) and group.listaC!=None:
            tablas = Expresion.Expresion.ObtenerCadenaEntrada(group.listaC, False)

        if isinstance(group.compGroup,Having):
            camposagrupar= ' GROUP BY  '+Having.ObtenerCadenaHaving(group.compGroup)

        cadenaFinal= tablas+camposagrupar
        return cadenaFinal





