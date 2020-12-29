class pl():
    'Clase abstacta'

class declaration(pl):
    def __init__(self,id,tipo,collate,notnull,exp):
        self.id = id
        self.tipo = tipo
        self.collate = collate
        self.notnull = notnull
        self.exp = exp
    
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

class rtrn(instruccion):
    def __init__(self,exp) -> None:
        self.exp = exp