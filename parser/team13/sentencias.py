from enum import Enum

cont=0
txt=""
def incrementarContador():
     global cont
     cont= cont+1
     return "%d" %cont 

class Node():
      pass


class Aritmetica(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5
    POTENCIA = 6


class Relacionales(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    DIFERENTE = 4
    MAYORIGUAL_QUE = 5
    MENORIGUAL_QUE = 6


class Logicas(Enum):
    AND = 1
    OR = 2
    NOT = 3


class Expresion(Enum):
    ID = 1
    BOOLEAN = 2
    DECIMAL = 3
    ENTERO = 4
    CADENA = 5
    TABATT = 6
    NEGATIVO = 7


class TipoDato(Enum):
    NUMERICO = 1
    CHAR = 2
    FECHA = 3
    FIELDS = 4
    BOOLEAN=5


class TipoAlterColumn(Enum):
    NOTNULL = 1
    CAMBIOTIPO = 2


class TipoAlterDrop(Enum):
    CONSTRAINT = 1
    COLUMN = 2


class TipoOpcionales(Enum):
    PRIMARYKEY = 1
    DEFAULT = 2
    NOTNULL = 3
    NULL = 4
    UNIQUE = 5
    CHECK = 6


class Sentencia:
    '''clase abstracta'''

class S(Sentencia):
      
      def __init__(self, Etiqueta,hijo1):
           self.Etiqueta=Etiqueta
           self.hijo1=hijo1    
      def traducir(self):
           global txt
           id = incrementarContador()
           if type(self.hijo1.son1)== type(tuple()):
               hijo1 = self.hijo1.son1[0].traducir() 
           else:             
               hijo1 = self.hijo1.son1py.traducir() 
           txt+= id+"[label="+self.Etiqueta+"]"+"\n\t"
           txt+= id+"->"+hijo1+"\n\t"
           return "digraph G {\n\t"+txt+"}"

 
class statementList2(Sentencia):
     
     def __init__(self,son1,son2,name):
         self.son1=son1
         self.son2=son2
         self.name=name
     
     def traducir(self):
         global txt
         id = incremetarContador()
         son1 = self.son1.traducir()
         son2 = self.son2.traducir()
         txt += id + "[label= "+self.name+"]"+"\n\t"     
         txt += id + " -> " + son1 + "\n\t"
         txt += id + " -> " + son2 + "\n\t"
         return id 

class statementList1(Sentencia):
        def __init__(self,son1,name):
            self.name = name
            self.son1 = son1

        def traducir(self):
            global txt
            id = incremetarContador()
            son1 = self.son1.traducir()
            txt += id + "[label= "+self.name+"]"+"\n\t"
            txt += id + " -> " + son1 + "\n\t"
            return id

class SCrearBase(Sentencia):
    def __init__(self, owner, mode, replace, exists, id):
        self.id = id
        self.owner = owner
        self.mode = mode
        self.replace = replace
        self.exists = exists
    
    
    def traducir(self):
           global txt
           txt=""
           id = incrementarContador()
           
           hijo1 = self.owner 
           hijo2 = self.mode 
           hijo3 = self.replace 
           hijo4 = self.exists 
           
           txt+= id+"[label="+"CrearBases"+"]"+"\n\t"
           txt+= id+"->"+str("create")+"\n\t"
           txt+= id+"->"+str("database")+"\n\t"
           txt+= id+"->"+str(self.id)+"\n\t"
           return txt 
           
           



class SShowBase(Sentencia):
    def __init__(self, like, cadena):
        self.like = like
        self.cadena = cadena


class SAlterBase(Sentencia):
    def __init__(self, id, rename, owner, idnuevo):
        self.id = id
        self.rename = rename
        self.owner = owner
        self.idnuevo = idnuevo


class SDropBase(Sentencia):
    def __init__(self, exists, id):
        self.exists = exists
        self.id = id


class STypeEnum(Sentencia):
    def __init__(self, id, lista=[]):
        self.id = id
        self.lista = lista


class SExpresion(Sentencia):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo


class SOperacion(Sentencia):
    def __init__(self, opIzq, opDer, operador):
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador


class SUpdateBase(Sentencia):
    def __init__(self, id, listaSet=[], listaWhere=[]):
        self.id = id
        self.listaSet = listaSet
        self.listaWhere = listaWhere


class SValSet(Sentencia):
    def __init__(self, columna, valor):
        self.columna = columna
        self.valor = valor


class SValWhere(Sentencia):
    def __init__(self, columna, valor):
        self.columna = columna
        self.columna = valor


class SDeleteBase(Sentencia):
    def __init__(self, id, listaWhere=[]):
        self.id = id
        self.listaWhere = listaWhere


class STruncateBase(Sentencia):
    def __init__(self, listaIds=[]):
        self.listaIds = listaIds


class SInsertBase(Sentencia):
    def __init__(self, id, listValores=[]):
        self.id = id
        self.listValores = listValores


class SCrearTabla(Sentencia):
    def __init__(self, id, herencia, nodopadre, columnas=[]):
        self.id = id
        self.columnas = columnas
        self.herencia = herencia
        self.nodopadre = nodopadre


class STipoDato(Sentencia):
    def __init__(self, dato, tipo, cantidad):
        self.dato = dato
        self.tipo = tipo
        self.cantidad = cantidad


class SShowTable(Sentencia):
    ''' Show table'''


class SDropTable(Sentencia):
    def __init__(self, id):
        self.id = id


class SAlterTableRename(Sentencia):
    def __init__(self, idtabla, idcolumna, idnuevo):
        self.idtabla = idtabla
        self.idcolumna = idcolumna
        self.idnuevo = idnuevo


class SAlterTableCheck(Sentencia):
    def __init__(self, idtabla, expresion):
        self.idtabla = idtabla
        self.expresion = expresion


class SAlterTable_AlterColumn(Sentencia):
    def __init__(self, idtabla, columnas=[]):
        self.idtabla = idtabla
        self.columnas = columnas


class SAlterColumn(Sentencia):
    def __init__(self, idcolumna, tipo, valcambio):
        self.idcolumna = idcolumna
        self.tipo = tipo
        self.valcambio = valcambio


class SAlterTableAddColumn(Sentencia):
    def __init__(self, idtabla, idcolumna, tipo):
        self.idtabla = idtabla
        self.idcolumna = idcolumna
        self.tipo = tipo


class SAlterTableAddUnique(Sentencia):
    def __init__(self, idtabla, idconstraint, idcolumna):
        self.idtabla = idtabla
        self.idconstraint = idconstraint
        self.idcolumna = idcolumna


class SAlterTableAddFK(Sentencia):
    def __init__(self, idtabla, idcolumna, idtpadre):
        self.idtabla = idtabla
        self.idcolumna = idcolumna
        self.idtpadre = idtpadre


class SAlterTableDrop(Sentencia):
    def __init__(self, idtabla, idco, tipo):
        self.idtabla = idtabla
        self.idco = idco
        self.tipo = tipo


class SColumna(Sentencia):
    def __init__(self, id, tipo, opcionales=[]):
        self.id = id
        self.tipo = tipo
        self.opcionales = opcionales


class SColumnaCheck(Sentencia):
    def __init__(self, id=[]):
        self.id = id


class SColumnaUnique(Sentencia):
    def __init__(self, id=[]):
        self.id = id


class SColumnaPk(Sentencia):
    def __init__(self, id=[]):
        self.id = id


class SColumnaFk(Sentencia):
    def __init__(self, id, idlocal=[], idfk=[]):
        self.id = id
        self.idlocal = idlocal
        self.idfk = idfk


class SOpcionales(Sentencia):
    def __init__(self, tipo, valor, id):
        self.tipo = tipo
        self.valor = valor
        self.id = id
