from InstruccionesDGA import tabla as ts
import tablaDGA as TAS
import InstruccionesDGA as dga

funciones = []

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

    def c3d(self):
        c3d = ''
        if  self.exp == None:
            valor = 'None'
        else:
            valor = str(self.exp.exp.traducir())


        if  self.collate == None:
            col = 'None'
        else:
            col = self.collate.val

        if self.tipo == 'SMALLINT':

            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.SMALLINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'INTEGER':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'BIGINT':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.BIGINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DECIMAL':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'NUMERIC': 
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.NUMERIC,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'REAL':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.REAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DOUBLE_PRECISION':   
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.DOUBLE_PRECISION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DOUBLE':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.DOUBLE,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'CHARACTER':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.CHARACTER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'CHARACTER_VARYING':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.CHARACTER_VARYING,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'TEXT': 
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.TEXT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'TIMESTAMP':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id.val)+',TIPO.TIMESTAMP,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        return c3d


    def traducir(self):
        c3d = ''
       
        if self.tipo == 'SMALLINT': 
            
            if  self.exp == None:
                c3d += '\self.id.val = 0'
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
            
        elif self.tipo == 'INTEGER':
            if  self.exp == None:
                c3d += '\self.id.val = 0'
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
            
        elif self.tipo == 'BIGINT':
            if  self.exp == None:
                c3d += '\self.id.val = 0'
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
            
        elif self.tipo == 'DECIMAL':
            if  self.exp == None:
                c3d += '\self.id.val = 0'
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
            
        elif self.tipo == 'NUMERIC': 
            if  self.exp == None:
                c3d += '\self.id.val = 0'
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
            
        elif self.tipo == 'REAL':
            if  self.exp == None:
                c3d += '\self.id.val = 0'
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
        elif self.tipo == 'DOUBLE':   
            if  self.exp == None:
                c3d += '\self.id.val = 0'
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
        elif self.tipo == 'PRECISION':
            if  self.exp == None:
                c3d += '\self.id.val = 0'
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
        elif self.tipo == 'CHARACTER':
            if  self.exp == None:
                c3d += '\self.id.val = \'\' '
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
        elif self.tipo == 'CHARACTER_VARYING':
            if  self.exp == None:
                c3d += '\self.id.val = \'\' '
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
        elif self.tipo == 'TEXT': 
            if  self.exp == None:
                c3d += '\self.id.val = \'\' '
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())
        elif self.tipo == 'TIMESTAMP':
            if  self.exp == None:
                c3d += '\self.id.val = \'\' '
            else:
                c3d += '\self.id.val = '+str(self.exp.traducir())

        return c3d
        

    def ejecutar(self):
        #ambitoDB = ts.buscarIDDB(dga.NombreDB)
        ambitoFuncion =  ts.buscarIDF(dga.cont)

        if self.tipo == 'SMALLINT':
            

            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.SMALLINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'INTEGER':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'BIGINT':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.BIGINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'DECIMAL':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'NUMERIC': 
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.NUMERIC,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'REAL':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.REAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'DOUBLE':   
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.DOUBLE,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'PRECISION':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.PRECISION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'CHARACTER':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.CHARACTER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'CHARACTER_VARYING':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.CHARACTER_VARING,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'TEXT': 
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.TEXT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        elif self.tipo == 'TIMESTAMP':
            NuevoSimbolo = TAS.Simbolo(dga.cont,self.id,TAS.TIPO.TIMESTAMP,ambitoFuncion,None, None, None, None, None, None, None ,None,None,self.exp, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
        
    


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
    
    def traducir(self):
        
        c3d = ''
        c3d += '\tid_db = id_db(NombreDB)\n'
        c3d += '\tNuevoSimbolo = TS.Simbolo(cont,'+self.id.val+',TIPO.FUNCTION,id_db)\n'
        c3d += '\tcont+=1\n'
        
        funcion = ''
        funcion += 'def '+self.id.val+'():\n' 
        #variables a usar, guardando en ts y declarando
        for decla in block.declare:

            c3d += decla.c3d()+'\n' 
            funcion += '\t'+decla.traducir()+'\n' 
        for inst in block.instrucciones:
            funcion += '\t'+inst.traducir()+'\n'

        funciones.append(funcion)
        return c3d
    
    def ejecutar(self):
        c3d = ''
        c3d += '\tid_db = id_db(NombreDB)\n'
        c3d += '\tNuevoSimbolo = TS.Simbolo(cont,'+self.id+',TIPO.FUNCTION,id_db)\n'
        c3d += '\tcont+=1\n'
        
        funcion = ''
        funcion += 'def '+self.id+'():\n' 
        #variables a usar, guardando en ts y declarando
        for decla in self.block.declare:

            c3d += decla.c3d()+'\n' 
            funcion += '\t'+decla.traducir()+'\n' 
        for inst in self.block.instrucciones:
            funcion += '\t'+inst.traducir()+'\n'

        funciones.append(funcion)
        return c3d




class param(pl):
    def __init__(self,alias,tipo) -> None:
        self.alias = alias
        self.tipo = tipo

class block(pl):
    def __init__(self,declare,instrucciones) -> None:
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

    def traducir(self):
        tupla = self.exp.traducir()
        codigo = tupla[0]
        valor = tupla[1]
        return codigo + '\n' + valor

class rtrn(instruccion):
    def __init__(self,exp) -> None:
        self.exp = exp

class expresion():
    'Clase abstracta'

tempcont = 0

def getTemp():
    global tempcont
    tempcont += 1
    return 't'+str(tempcont-1)


class exp_boolp(expresion):
    'Esta expresion devuelve un'
    'boolean'

    def __init__(self, val):
        self.val = val

    def traducir(self):
        tmp = getTemp()
        codigo = tmp + f' = {self.val}'
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_textp(expresion):
    'Devuelve el texto'

    def __init__(self, val):
        self.val = val

    def traducir(self):
        tmp = getTemp()
        codigo = tmp + f' = {self.val}'
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_nump(expresion):
    'Devuelve un número'

    def __init__(self, val):
        self.val = val
        
    def traducir(self):
        tmp = getTemp()
        codigo = tmp + f' = {self.val}'
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class expresionC:
    'clase abstracta para las operaciones'

class exp_sumap(expresionC):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} + {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_restap(expresion):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2    
    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} - {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor    

class exp_multiplicacionp(expresion):
    'Multiplica las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} * {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor
        
class exp_divisionp(expresion):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} / {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_idp(expresion):
    def __init__(self,val):
        self.val = val

    def traducir(self):
        tmp = getTemp()
        codigo = tmp + f' = {self.val}'
        valor = tmp
        #print(codigo,valor)
        return codigo,valor