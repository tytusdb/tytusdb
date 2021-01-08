import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *

class Instruccion:
    'clase abstracta'



#TIPOS DE DATO
class Tipo(Instruccion):
    def __init__(self, tipo, longitud,fila,columna):
        self.tipo = tipo
        self.longitud = longitud
        self.fila = fila
        self.columna = columna

class IdId(Instruccion):
    '''ID.ID'''
    def __init__(self, id1, id2,fila,columna):
        self.id1 = id1
        self.id2 = id2
        self.fila = fila
        self.columna = columna

    def ObtenerCadenaEntrada(IdId):
        id1=''
        id2=''

        if isinstance(IdId.id1,Id):
            id1 = str(IdId.id1.id)
        if isinstance(IdId.id2,Id):
            id2 = str(IdId.id2.id)
        else:
            id2 = str(IdId.id2)

        return id1+'.'+id2



        

#WHERE


#asignacion x = e
#puede venir id o id.id
class Asignacion(Instruccion):
    def __init__(self, id, expresion, fila,columna):
        self.id = id
        self.expresion = expresion
        self.fila = fila
        self.columna = columna




#SHOW DATABASE
class Show(Instruccion):
    def __init__(self, fv,concatena,fila,columna):
        self.fv = fv
        self.concatena = concatena
        self.fila = fila
        self.columna = columna

    def ejecutar(shown, ts,consola,exceptions):

        consola.append("----------------SHOW DATABASE----------------")
        i = 1
        for data in ts.simbolos:
            if ts.simbolos.get(data).categoria == TS.TIPO_DATO.BASEDEDATOS:
                consola.append(f"{i}. {data}")
                i = i +1
        consola.append("--------------END SHOW DATABASE--------------")

    def traducir(show, ts, consola, tv):

        #iniciar traduccion
        info = "" #info contiene toda el string a mandar como parametros
        print("concatena \n")
        print(show.concatena)
        for data in show.concatena:
            info += " " +data

        contador = tv.Temp()
        consola.append(f"\n\t{contador} = \"{info}\";")
        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({contador})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")

#UPDATE


#SELECT
#-----------------------
#TIME




#COMBINACION QUERIES
class Combinacion(Instruccion):
    '''#1 union
       #2 intersect
       #3 except'''
    def __init__(self, caso, all, querie1, querie2,fila,columna):
        self.caso = caso
        self.all = all
        self.querie1 = querie1
        self.querie2 = querie2
        self.fila = fila
        self.columna = columna


 #MATH

#Trigonometrica


#Binaria

#CASE
class Case(Instruccion): #WHEN asignacion THEN valores
    def __init__(self, asignacion, valor,fila,columna):
        self.asignacion = asignacion
        self.valor = valor
        self.fila = fila
        self.columna = columna




class ColCase(Instruccion):
    def __init__(self, cases, id,fila,columna):
        self.cases = cases #lista de cases
        self.id = id # id
        self.fila = fila
        self.columna = columna







class Parametro(Instruccion):
    def __init__(self, id, tipo, fila, columna):
        self.id = id
        self.tipo = tipo
        self.fila = fila
        self.columna = columna