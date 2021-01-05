class Sentencia():
    'Abstracta'

    def Ejecutar(self):
        pass


class CaseSimple(Sentencia):

    def __init__(self, busqueda, listawhen, caseelse):
        self.busqueda = busqueda
        self.listawhen = listawhen
        self.caseelse = caseelse


class CSWhen(Sentencia):

    def __init__(self, expresiones, sentencias):
        self.expresiones = expresiones
        self.sentencias = sentencias

class CElse(Sentencia):

    def __init__(self, sentencias):
        self.sentencias = sentencias


class CaseBuscado(Sentencia):

    def __init__(self, listawhen, caseelse):
        self.listawhen = listawhen
        self.caseelse = caseelse

class CBWhen(Sentencia):

    def __init__(self, expresion, sentencias):
        self.expresion = expresion
        self.sentencias = sentencias


class LoopSimple(Sentencia):

    def __init__(self, label, sentencias, labelfinal):
        self.label = label
        self.sentencias = sentencias
        self.labelfinal = labelfinal

class Exit(Sentencia):

    def __init__(self, label, when):
        self.label = label
        self.when = when

class Continue(Sentencia):

    def __init__(self, label, when):
        self.label = label
        self.when = when


class WhenAuxilar(Sentencia):

    def __init__(self, expresion):
        self.expresion = expresion


class Declaracion(Sentencia):

    def __init__(self, id, constante, tipo, notnull, simbolodeclaracion, expresion):
        self.id = id
        self.constante = constante #puede venir o no la palabra constante
        self.tipo = tipo
        self.notnull = notnull #puede venir o no la palabra not null
        self.simbolodeclaracion = simbolodeclaracion
        self.expresion = expresion


class Asignacion(Sentencia):

    def __init__(self, id, expresion):
        self.id = id
        self.expresion = expresion



#=======================================================================  INSTRUCCIONES PL SQL


#----------------------------   FUNCIONES
class Funciones_(Sentencia):
    def __init__(self,Reservada, Nombre,Retorno,Alias, Parametros=[], Instrucciones=[], Declaraciones=[], Codigo=[]):
        self.Reservada     = Reservada #create or replace
        self.Nombre        = Nombre #
        self.Retorno       = Retorno #que retorna, expresion
        self.Parametros    = Parametros #lista de ID's ( nombre tipo )
        self.Alias         = Alias
        self.Instrucciones = Instrucciones # sql
        self.Declaraciones = Declaraciones #
        self.Codigo        = Codigo # sentencias



#----------------------------   PROCEDURES
class Procedimientos_(Sentencia):
    def __init__(self,Reservada, Nombre,Comand,Alias, Parametros=[], Instrucciones=[], Declaraciones=[], Codigo=[]):
        self.Reservada     = Reservada  #create or replace
        self.Nombre        = Nombre
        self.Comand        = Comand
        self.Alias         = Alias
        self.Parametros    = Parametros
        self.Instrucciones = Instrucciones
        self.Declaraciones = Declaraciones
        self.Codigo        = Codigo




#---------------------------------------  codigo funciones
class Code_Funciones(Sentencia):
    def __init__(self,Argumento,Codigo=[]):
        self.Argumento     = Argumento
        self.Codigo        = Codigo


class Name_Expresion(Sentencia):
    def __init__(self,Reservada,Expresion):
        self.Reservada     = Reservada
        self.Expresion        = Expresion


#-------------------------------------- Objeto Variables
class Variables_Name(Sentencia):
    def __init__(self,Identificador,Valor):
        self.Identificador = Identificador
        self.Valor         = Valor


#-------------------------------------- Valor de retorno
class RetornoFuncion(Sentencia):
    def __init__(self,Expresion):
        self.Expresion = Expresion


#-------------------------------------- Objeto Parametros
class Parametros_(Sentencia):
    def __init__(self,Tipo,Nombre,Valor):
        self.Tipo   = Tipo
        self.Nombre = Nombre
        self.Valor  = Valor






#=======================================================================  INSTRUCCION FOR  y FOREACH
class ForInstruccion(Sentencia):
    def __init__(self, Nombre, Tipo, By_Expre,Argumento,Lista_Expresiones=[],Lista_Codigo=[]):
        self.Nombre            = Nombre
        self.Tipo              = Tipo
        self.By_Expre          = By_Expre
        self.Argumento         = Argumento
        self.Lista_Expresiones = Lista_Expresiones
        self.Lista_Codigo      = Lista_Codigo




class ForeachInstruccion(Sentencia):
    def __init__(self, Nombre, Slice, Expre,Argumento,Lista_Codigo=[]):
        self.Nombre       = Nombre
        self.Slice        = Slice
        self.Expre        = Expre
        self.Argumento    = Argumento
        self.Lista_Codigo = Lista_Codigo



#-------------------------  Ejecucion de una Funcion
class EjecucionFuncion(Sentencia):
    def __init__(self, Id, Parametros):
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   FFFFFFFFFFFFFFFFFFFFFFFFFFf")
        self.Id         = Id
        self.Parametros = Parametros


class Eje():
    def __init__(self,id,param):
        self.id = id
        self.param = param

#------------------------  Sentencias SQL
class SentenciasSQL(Sentencia):
    def __init__(self,CadenaSQL):
        self.CadenaSQL = CadenaSQL

