#from main import ts
import tablaDGA as TAS
import InstruccionesDGA as dga

class pl():
    'Clase abstacta'

class declaration(pl):
    def __init__(self,id,constant,tipo,collate,notnull,exp):
        self.id = id
        self.constant = constant
        self.tipo = tipo
        self.collate = collate
        self.notnull = notnull
        self.exp = exp
    
    def ejecutar(self):
        #ambitoDB = ts.buscarIDDB(dga.NombreDB)
        ambitoFuncion =  ts.buscarIDF(dga.cont)

        if tipo == 'SMALLINT':
            

            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.SMALLINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'INTEGER':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'BIGINT':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.BIGINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'DECIMAL':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'NUMERIC': 
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.NUMERIC,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'REAL':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.REAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'DOUBLE':   
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.DOUBLE,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'PRECISION':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.PRECISION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'CHARACTER':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.CHARACTER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'CHARACTER_VARYING':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.CHARACTER_VARING,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'TEXT': 
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.TEXT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif tipo == 'TIMESTAMP':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.TIMESTAMP,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        
        print(NuevoSimbolo)
        
     

     


class expre(pl):
    def __init__(self,tipo, exp):
        self.tipo = tipo 
        self.exp = exp

class createfunc(pl):
    def __init__(self,id,lparams,returntype,block) -> None:
        self.id = id
        self.lparams = lparams
        self.returntype = returntype
        self.block = block


class param(pl):
    def __init__(self,alias,tipo) -> None:
        self.alias = alias
        self.tipo = tipo

class block(pl):
    def __init__(self,declare,instrucciones,) -> None:
        self.instrucciones = instrucciones
        self.declare = declare

class instruccion():
    'clase abstracta'

class raisenotice(instruccion):
    def __init__(self,texto,variable) -> None:
        self.texto = texto
        self.variable = variable

class asignacion(instruccion):
    def __init__(self,id,exp) -> None:
        self.id = id
        self.exp = exp
    
    def ejecutar(self):
        ts.modificar_valor(self.id,self.exp)

class rtrn(instruccion):
    def __init__(self,exp) -> None:
        self.exp = exp

class expresion():
    'Clase abstracta'

class exp_boolp(expresion):
    'Esta expresion devuelve un'
    'boolean'

    def _init_(self, val):
        self.val = val

class exp_textp(expresion):
    'Devuelve el texto'

    def _init_(self, val):
        self.val = val

class exp_nump(expresion):
    'Devuelve un número'

    def _init_(self, val):
        self.val = val

class exp_sumap(expresion):
    'Suma las dos expresiones'

    def _init_(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        

class exp_multiplicacionp(expresion):
    'Multiplica las dos expresiones'

    def _init_(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
        
class exp_divisionp(expresion):
    'Suma las dos expresiones'

    def _init_(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

class exp_idp(expresion):
    def _init_( val):
        self.val = val