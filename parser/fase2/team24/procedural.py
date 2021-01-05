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
            col = self.collate

        if self.tipo == 'SMALLINT':

            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.SMALLINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'INTEGER':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'BIGINT':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.BIGINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DECIMAL':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'NUMERIC': 
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.NUMERIC,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'REAL':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.REAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DOUBLE_PRECISION':   
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.DOUBLE_PRECISION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DOUBLE':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.DOUBLE,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'CHARACTER':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.CHARACTER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'CHARACTER_VARYING':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.CHARACTER_VARYING,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'TEXT': 
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.TEXT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'TIMESTAMP':
            c3d += '\tambitoFuncion =  buscarIDF(cont)\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,'+str(self.id)+',TIPO.TIMESTAMP,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        return c3d


    def traducir(self):
        c3d = ''
       
        if self.tipo == 'SMALLINT': 
            
            if  self.exp == None:
                c3d += str(self.id)+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
            
        elif self.tipo == 'INTEGER':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
            
        elif self.tipo == 'BIGINT':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
            
        elif self.tipo == 'DECIMAL':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
            
        elif self.tipo == 'NUMERIC': 
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
            
        elif self.tipo == 'REAL':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
        elif self.tipo == 'DOUBLE':   
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
        elif self.tipo == 'PRECISION':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
        elif self.tipo == 'CHARACTER':
            if  self.exp == None:
                c3d += self.id+' = \'\' '
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
        elif self.tipo == 'CHARACTER_VARYING':
            if  self.exp == None:
                c3d += self.id+' = \'\' '
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
        elif self.tipo == 'TEXT': 
            if  self.exp == None:
                c3d += self.id+' = \'\' '
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico
        elif self.tipo == 'TIMESTAMP':
            if  self.exp == None:
                c3d += self.id+' = \'\' '
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traducir()[1]) #variable final o valor en especifico

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
        c3d += '\tNuevoSimbolo = Simbolo(cont,'+self.id+',TIPO.FUNCTION,id_db)\n'
        c3d += '\tcont+=1\n'
        
        funcion = ''
        funcion += 'def '+self.id+'():\n' 
        #variables a usar, guardando en ts y declarando
        for decla in block.declare:

            c3d += decla.c3d()+'\n' 
            funcion += '\t'+decla.traducir()+'\n' 

        pcont = 0
        for param in lparams:
            #variables de parametros
            if param.alias == None:
                #Mira como jalas de las declaraciones
                for declara in block.declare:
                    if pcont == declara.tipo:
                        funcion += '\t'+declara.id+' = pila['+str(pcont)+']\n'         

            else:
                #Solo es para.alias = pilas en el numero 
                funcion += '\t'+param.alias+' = pila['+str(pcont)+']\n'

            pcont += 1


        for inst in block.instrucciones:
            funcion += '\t'+inst.traducir()+'\n'
            c3d += inst.c3d()
        



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

    def traducir(self):
        c3d = str(self.alias)
        return c3d

class block(pl):
    def __init__(self,declare,instrucciones) -> None:
        self.instrucciones = instrucciones
        self.declare = declare
    
    def traducir(self):
        return '\n'

    def c3d(self):
        return '\n'

class instruccion():
    'clase abstracta'

class raisenotice(instruccion):
    def __init__(self,texto,variable) -> None:
        self.texto = texto
        self.variable = variable
    
    def traducir(self):
        c3d = ''
        if self.variable == None:
            c3d += 'print(\''+texto+'\')'
        else:
            c3d += 'print(\''+str(self.texto).replace('%',self.variable.traducir())+'\')'

    def c3d(self):
        return '\n'


class asignacion(instruccion):
    def __init__(self,id,exp) -> None:
        self.id = id
        self.exp = exp
    
    def ejecutar(self):
        ts.modificar_valor(self.id,self.exp)

    def c3d():
        c3d = ''
        c3d += '\ttabla.modificar_valor('+ str(self.id) + ', ' + str(self.exp.traducir()[1]) +')\n'
        return c3d   

    def traducir():
        c3d = ''
        c3d += self.exp.traducir()[0]
        c3d += self.id + ' += ' + str(self.exp.traducir()[1]) + '\n'
        return c3d

class rtrn(instruccion):
    def __init__(self,exp) -> None:
        self.exp = exp

class searched_case(instruccion):
    def __init__(self,condition,instrucciones,elsif,els) -> None:
        self.codition = condition
        self.instrucciones = instrucciones
        self.elsif = elsif
        self.els= els
    
    def traducir(self):
        c3d = ''
        c3d += self.condition.traducir()[0]
        #variables temporales a utilizar en else if
        
        #tengo que ejecutar y añadir los elif
        for eli in self.elsif :
            c3d += str(eli.condition.traducir()[0])
            
            

        c3d += 'if '+ self.condition.traducir()[1] +':\n'
        for inst in self.instrucciones:
            c3d += '\t'+inst.traducir()+'\n'
        
        for eli in self.elsif :
            #tengo que ejecutar y añadir los elif
            c3d += 'elif '+ eli.condition.traducir()[1] +' :'
            for inst in eli.instrucciones:
                c3d += '\t'+inst.traducir()+'\n'
            

        if els != None:
            c3d += 'else:'
            for inst in els.instrucciones:
                c3d += '\t'+inst.traducir()+'\n'

        return c3d

    def c3d(self):
        c3d = ''
        for inst in instrucciones:
            c3d += inst.c3d()

        for eli in self.elsif:
            c3d += eli.c3d()
        
        c3d += els.c3d()

        
        return c3d


class iff(instruccion):
    def __init__(self,condition,instrucciones,elsif,els) -> None:
        self.codition = condition
        self.instrucciones = instrucciones
        self.elsif = elsif
        self.els= els
    
    def traducir(self):
        c3d = ''
        c3d += self.condition.traducir()[0]
        #variables temporales a utilizar en else if
        
        #tengo que ejecutar y añadir los elif
        for eli in self.elsif :
            c3d += str(eli.condition.traducir()[0])
            
            

        c3d += 'if '+ self.condition.traducir()[1] +':\n'
        for inst in self.instrucciones:
            c3d += '\t'+inst.traducir()+'\n'
        
        for eli in self.elsif :
            #tengo que ejecutar y añadir los elif
            c3d += 'elif '+ eli.condition.traducir()[1] +' :'
            for inst in eli.instrucciones:
                c3d += '\t'+inst.traducir()+'\n'
            

        if els != None:
            c3d += 'else:'
            for inst in els.instrucciones:
                c3d += '\t'+inst.traducir()+'\n'

        return c3d

    def c3d(self):
        c3d = ''
        for inst in instrucciones:
            c3d += inst.c3d()

        for eli in self.elsif:
            c3d += eli.c3d()
        
        c3d += els.c3d()

        
        return c3d

class els(instruccion):
    def __init__(self,instrucciones) -> None:
        self.instrucciones = instrucciones

    def traducir(self):
        c3d = ''
        return c3d

    def c3d(self):
        c3d = ''
        for inst in instrucciones:
            c3d += inst.c3d()
        return c3d

class elsif(instruccion):
    def __init__(self,condition,instrucciones) -> None:
        self.condition = condition
        self.instrucciones = instrucciones
    
    def traducir(self):
        c3d = ''
        return c3d

    def c3d(self):
        c3d = ''
        for inst in instrucciones:
            c3d += inst.c3d()
        return c3d


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

class exp_mayorp(expresion):
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
        tmpf  = f'{tmp} = {tmp1} > {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_menorp(expresion):
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
        tmpf  = f'{tmp} = {tmp1} < {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_igualp(expresion):
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
        tmpf  = f'{tmp} = {tmp1} == {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_mayor_igualp(expresion):
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
        tmpf  = f'{tmp} = {tmp1} >= {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_menor_igualp(expresion):
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
        tmpf  = f'{tmp} = {tmp1} <= {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor

class exp_diferentep(expresion):
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
        tmpf  = f'{tmp} = {tmp1} != {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        #print(codigo,valor)
        return codigo,valor