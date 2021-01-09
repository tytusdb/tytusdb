import hashlib
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont as ncont

import tablaDGA as TAS

import mathtrig as mt
import reportError as errores
#from Interfaz import lista
funciones = []
objopt = []
cont = ncont
class pl():
    'Clase abstacta'

def deleteF(name):

    name = name +'():'
    for i in range(len(funciones)):
        x = funciones[i].split(" ")
        print( 'tengo que eliminar la posicion '+ str(i) +' ya que elimine '+ str(x[1]))
        funciones.pop(i)
        break
        


class declaration(pl):
    def __init__(self,id,constant,tipo,collate,notnull,exp):
        self.id = id
        self.constant = constant
        self.tipo = tipo
        self.collate = collate
        self.notnull = notnull
        self.exp = exp
        self.traduccion = None

    def c3d(self):
        if self.traduccion == None:
            if  self.exp == None:
                self.traduccion  = 'a'
            else:
                
                self.traduccion =self.exp.traducir()

        c3d = ''

        if  self.traduccion == 'a':
            valor = 'None'
        else:
            if isinstance(self.traduccion[2],str):
                valor = '\''+str(self.traduccion[2])+'\''
            else:
                valor = str(self.traduccion[2])

        if  self.collate == None:
            col = 'None'
        else:
            col = self.collate

        if self.tipo == 'SMALLINT':
                
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.SMALLINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'

        elif self.tipo == 'INTEGER':
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'BIGINT':
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.BIGINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DECIMAL':
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'NUMERIC': 
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.NUMERIC,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\ttabla.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'REAL':
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.REAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DOUBLE_PRECISION':   
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.DOUBLE_PRECISION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'DOUBLE':
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.DOUBLE,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'CHARACTER':
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.CHARACTER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'CHARACTER_VARYING':
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.CHARACTER_VARYING,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'TEXT': 
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.TEXT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        elif self.tipo == 'TIMESTAMP':
            c3d += '\tambitoFuncion =  ts.buscarIDF()\n'
            c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.TIMESTAMP,ambitoFuncion,None, None, None, None, None, None, None ,None,None,'+valor+', '+col+','+str(self.notnull)+','+str(self.constant)+')\n'
            c3d += '\tts.agregar(NuevoSimbolo)\n'
            c3d += '\tcont+=1\n'
        objopt.append(c3d)
        return c3d


    def traducir(self):
        c3d = ''
        if self.traduccion == None:
            self.traduccion =self.exp.traducir()
       
        if self.tipo == 'SMALLINT': 
            
            if  self.exp == None:
                c3d += str(self.id)+' = 0'
            else:
                c3d += self.exp.codigo #codigo que va detras
                c3d += str(self.id)+' = '+str(self.traduccion[1]) #variable final o valor en especifico
            
        elif self.tipo == 'INTEGER':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.traduccion[1]) #variable final o valor en especifico
            
        elif self.tipo == 'BIGINT':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traduccion[1]) #variable final o valor en especifico
            
        elif self.tipo == 'DECIMAL':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traduccion[1]) #variable final o valor en especifico
            
        elif self.tipo == 'NUMERIC': 
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traduccion[1]) #variable final o valor en especifico
            
        elif self.tipo == 'REAL':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traduccion[1]) #variable final o valor en especifico
        elif self.tipo == 'DOUBLE':   
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traduccion[1]) #variable final o valor en especifico
        elif self.tipo == 'PRECISION':
            if  self.exp == None:
                c3d += self.id+' = 0'
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traduccion[1]) #variable final o valor en especifico
        elif self.tipo == 'CHARACTER':
            if  self.exp == None:
                c3d += self.id+' = \'\' '
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.exp.traduccion[1]) #variable final o valor en especifico
        elif self.tipo == 'CHARACTER_VARYING':
            if  self.exp == None:
                c3d += self.id+' = \'\' '
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.traduccion[1]) #variable final o valor en especifico
        elif self.tipo == 'TEXT': 
            if  self.exp == None:
                c3d += self.id+' = \'\' '
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.traduccion[1]) #variable final o valor en especifico
        elif self.tipo == 'TIMESTAMP':
            if  self.exp == None:
                c3d += self.id+' = \'\' '
            else:
                c3d += self.exp.traducir[0] #codigo que va detras
                c3d += str(self.id)+' = '+str(self.traduccion[1]) #variable final o valor en especifico

        return c3d
        

    def ejecutar(self):
        global cont
        ambitoFuncion = ts.buscarIDF()
        #ambitoFuncion =  ts.buscarIDF()
        
        if self.traduccion == None:
            if  self.exp == None:
                self.traduccion  = 'a'
            else:
                
                self.traduccion =self.exp.traducir()

        if  self.traduccion == 'a':
            valor = 'None'
        else:
            valor = str(self.traduccion[2])

        

        if self.tipo.upper() == 'SMALLINT':
            if valor == 'None':
                valor = 0

            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.SMALLINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'INTEGER':
            if valor == 'None':
                valor = 0
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'BIGINT':
            if valor == 'None':
                valor = 0
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.BIGINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'DECIMAL':
            if valor == 'None':
                valor = 0.0
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'NUMERIC': 
            if valor == 'None':
                valor = 0.0
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.NUMERIC,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'REAL':
            if valor == 'None':
                valor = 0.0
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.REAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'DOUBLE':  
            if valor == 'None':
                valor = 0.0 
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.DOUBLE,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'PRECISION':
            if valor == 'None':
                valor = 0.0
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.PRECISION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'CHARACTER':
            if valor == 'None':
                valor = ''
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.CHARACTER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'CHARACTER_VARYING':
            if valor == 'None':
                valor = ''
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.CHARACTER_VARING,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'TEXT':
            if valor == 'None':
                valor = ''
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.TEXT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'TIMESTAMP':
            if valor == 'None':
                valor = ''
            NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.TIMESTAMP,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor, self.collate,self.notnull) 
            ts.agregar(NuevoSimbolo)
            cont += 1

class expre(pl):
    def __init__(self,tipo, exp):
        self.tipo = tipo 
        self.exp = exp
    
    def traducir(self):
        return self.exp.traducir()

    def ejecutar(self):
        pass

class llamadaP(pl):
    def __init__(self,id,lparams) -> None:
        self.id = id
        self.lparams = lparams

    def traducir(self):
        if  not ts.existeF(str(self.id)):
            print('Funcion '+str(self.id) +' no existe')
            e = errores.CError(0,0,"Error en llamada de proceso, no existe",'Semantico') 
            errores.insert_error(e)
            return '\tprint( \'Funcion '+ str(self.id) + ' no existe\')\n'
        c3d = ''
        contadorP = 0
        for expresion in self.lparams:
            
            trad = expresion.traducir()
            c3d += trad[0] +'\n'
            c3d += 'pila['+str(contadorP)+'] = '+str(trad[1])
            objopt.append('pila['+str(contadorP)+'] = '+str(trad[1]))
            contadorP +=1



        c3d += ''+str(self.id)+'()\n'
        objopt.append('\t'+str(self.id)+'()\n')
        return c3d
    
    def c3d(self):
        return '\n'

    def ejecutar(self):
        pass

class llamadaF(pl):
    def __init__(self,id,lparams) -> None:
        self.id = id
        self.lparams = lparams

    def traducir(self):
        if  not ts.existeF(str(self.id)):
            e = errores.CError(0,0,"Error en llamada de funcion, no existe",'Semantico') 
            errores.insert_error(e)
            print('Funcion '+str(self.id) +' no existe')
            return '\tprint( \'Funcion '+ str(self.id) + 'no existe\')\n'
        c3d = ''
        contadorP = 0
        for expresion in self.lparams:
            
            trad = expresion.traducir()
            
            c3d += trad[0] +'\n'
            
            c3d += 'pila['+str(contadorP)+'] = ' + str(trad[1]) + '\n'
            objopt.append('pila['+str(contadorP)+'] = ' + str(trad[1]) + '\n')
            contadorP +=1


        tmp = getTemp()
        c3d += str(self.id)+'()'
        objopt.append(str(self.id)+'()')
        c3d += '\n'
        c3d += tmp +' = pila[10]\n'
        objopt.append(tmp +' = pila[10]\n')
        return c3d,tmp,0
    
    def c3d():
        return '\n'

    def ejecutar(self):
        pass

class dropfunc(pl):
    def __init__(self,ids) -> None:
        self.ids = ids

    def traducir(self):
        
        c3d = ''
        self.ejecutar()
        for identificador in self.ids:
            
            c3d += '\tts.deleteFP(str(\''+str(identificador)+'\'))\n'
            objopt.append('\tts.deleteFP(str(\''+str(identificador)+'\'))\n')
            if  not ts.existeF(str(identificador)):    
                e = errores.CError(0,0,"Error drop funcion, "+str(identificador)+" no existe como funcion",'Semantico') 
                errores.insert_error(e)
        return c3d
    
    

    def ejecutar(self):
        
        for identificador in self.ids:
            if  ts.existeF(str(identificador)):
                 
                deleteF(str(identificador))
                ts.deleteFP(str(identificador))

class createfunc(pl):
    def __init__(self,id,lparams,returntype,block):
        self.id = id
        self.lparams = lparams
        self.returntype = returntype
        self.block = block
    
    def ejecutar(self):
        return 'Se creo la funcion o procedimiento'

    def traducir(self):
        
        global cont
        if  ts.existeF(str(self.id)):
            print('Funcion '+str(self.id) +' ya existe')

            e = errores.CError(0,0,"Error en llamada creacion de funcion/proceso, ya existe",'Semantico') 
            errores.insert_error(e)
            objopt.append('\tprint( \'Funcion '+ str(self.id) + ' ya existe\')\n')
            return '\tprint( \'Funcion '+ str(self.id) + ' ya existe\')\n'
        c3d = ''
        c3d += '\tn_db = ts.buscarIDTB(NombreDB)\n'
        c3d += '\tNuevoSimbolo = TAS.Simbolo(cont,\''+self.id+'\',TAS.TIPO.FUNCTION,n_db)\n'
        c3d += '\tts.agregar(NuevoSimbolo)\n'
        c3d += '\tcont+=1\n'
        objopt.append(c3d)
        ambito = ts.buscarIDTB(NombreDB)
        NuevoSimbolo = TAS.Simbolo(cont,self.id,TAS.TIPO.FUNCTION,ambito,None, None, None, None, None, None, None ,None,None,None, None,None) 
        ts.agregar(NuevoSimbolo)
        cont += 1
        #creo la funcion en ts
        funcion = ''
        funcion += 'def '+self.id+'():\n' 
        #variables a usar, guardando en ts y declarando
        if self.block.declare != None:
            for decla in self.block.declare:
                decla.ejecutar()
                c3d += str(decla.c3d())+'\n' 
                funcion += '\t'+str(decla.traducir())+'\n' 

        pcont = 0

        for param in self.lparams:
            #variables de parametros
            if param.alias == None:
                #Mira como jalas de las declaraciones
                for declara in self.block.declare:
                    if pcont == declara.tipo:
                        funcion += '\t'+str(declara.id)+' = pila['+str(pcont)+']\n'    
                        objopt.append('\t'+str(declara.id)+' = pila['+str(pcont)+']\n')     

            else:
                #Solo es para.alias = pilas en el numero 
                funcion += '\t'+str(param.alias)+' = pila['+str(pcont)+']\n'
                objopt.append('\t'+str(param.alias)+' = pila['+str(pcont)+']\n')

                param.ejecutar()


            pcont += 1

        
        
        for inst in self.block.instrucciones:
            
            funcion += '\t'+str(inst.traducir()).replace('\n','\n\t')+'\n'
            c3d += inst.c3d()
            inst.ejecutar()
        



        funciones.append(funcion)

        return c3d
    
    def ejecutar1(self):
        c3d = ''
        c3d += '\tbuscarIDF = buscarIDTB(NombreDB)\n'
        c3d += '\tNuevoSimbolo = Simbolo(cont,\''+str(self.id)+'\',TAS.TIPO.FUNCTION,buscarIDF)\n'
        c3d += '\tcont+=1\n'
        objopt.append(c3d)
        
        funcion = ''
        funcion += 'def '+str(self.id)+'():\n' 
        objopt.append(funcion)
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

    def ejecutar(self):
        global cont
        #ambitoDB = ts.buscarIDDB(NombreDB)
        ambitoFuncion =  ts.buscarIDF()
        
        valor = 'None'
    

        if self.tipo.upper() == 'SMALLINT':
            if valor == 'None':
                valor = 0

            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.SMALLINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'INTEGER':
            if valor == 'None':
                valor = 0
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.INTEGER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'BIGINT':
            if valor == 'None':
                valor = 0
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.BIGINT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'DECIMAL':
            if valor == 'None':
                valor = 0.0
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.DECIMAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'NUMERIC': 
            if valor == 'None':
                valor = 0.0
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.NUMERIC,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'REAL':
            if valor == 'None':
                valor = 0.0
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.REAL,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'DOUBLE':  
            if valor == 'None':
                valor = 0.0 
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.DOUBLE,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'PRECISION':
            if valor == 'None':
                valor = 0.0
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.PRECISION,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'CHARACTER':
            if valor == 'None':
                valor = ''
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.CHARACTER,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'CHARACTER_VARYING':
            if valor == 'None':
                valor = ''
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.CHARACTER_VARYING,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'TEXT':
            if valor == 'None':
                valor = ''
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.TEXT,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1
        elif self.tipo.upper() == 'TIMESTAMP':
            if valor == 'None':
                valor = ''
            NuevoSimbolo = TAS.Simbolo(cont,self.alias,TAS.TIPO.TIMESTAMP,ambitoFuncion,None, None, None, None, None, None, None ,None,None,valor) 
            ts.agregar(NuevoSimbolo)
            cont += 1


class block(pl):
    def __init__(self,declare,instrucciones) -> None:
        self.instrucciones = instrucciones
        self.declare = declare
    
    def traducir(self):
        funcion = ''
        for inst in self.instrucciones:
            
            funcion += '\t'+str(inst.traducir()).replace('\n','\n\t')+'\n'

        return funcion
            

    def c3d(self):
        c3d = ''
        for inst in self.instrucciones:
            
            
            c3d += '\t'+inst.c3d()
        return c3d
        
    
    def ejecutar(self):
        for inst in self.instrucciones:
            
            inst.ejecutar()

class instruccion():
    'clase abstracta'

class raisenotice(instruccion):
    def __init__(self,texto,variable) -> None:
        self.texto = texto
        self.variable = variable
    
    def traducir(self):
        c3d = ''
        if self.variable == None:
            c3d += 'print(\''+self.texto+'\')'
            objopt.append(c3d)
        else:
            c3d += str(self.variable.exp.traducir()[0])
            c3d += 'print(f\''+str(self.texto).replace('%','{'+self.variable.exp.traducir()[1]+'}')+'\')'
            objopt.append(c3d)

    def c3d(self):
        return '\n'

    def ejecutar(self):
        pass

class asignacion(instruccion):
    def __init__(self,id,exp) -> None:
        self.id = id
        self.exp = exp
        self.traduccion = None
    
    def ejecutar(self):
        if self.traduccion == None:
            self.traduccion =self.exp.traducir()
        #print(self.id,self.traduccion[2])
        ts.modificar_valor(self.id,self.traduccion[2])

    def c3d(self):
        if self.traduccion == None:
            self.traduccion =self.exp.traducir()
        c3d = ''
        #c3d += str(self.exp.traducir()[0])
        if isinstance(self.traduccion[2],str):
            valor = '\''+str(self.traduccion[2])+'\''
        else:
            valor = str(self.traduccion[2])
        c3d += '\tts.modificar_valor(\''+ str(self.id) + '\', ' + valor +')\n'
        objopt.append('\tts.modificar_valor(\''+ str(self.id) + '\', ' + valor +')\n')
        return c3d   

    def traducir(self):
        if self.traduccion == None:
            self.traduccion =self.exp.traducir()
        var = self.traduccion
        c3d = ''
        c3d += var[0]+ '\n'
        c3d += self.id + ' = ' + str(var[1]) + '\n'
        return c3d

class rtrn(instruccion):
    def __init__(self,exp) -> None:
        self.exp = exp

    def traducir(self):
        c3d = ''
        var = self.exp.traducir()
        c3d += var[0]
        c3d += '\n'
        c3d += 'pila[10] = ' + var[1] + '\n'
        return c3d

    def c3d(self):
        return '\n'

    def ejecutar(self):
        pass

class searched_case(instruccion):
    def __init__(self,condition,instrucciones,elsif,els) -> None:
        self.codition = condition
        self.instrucciones = instrucciones
        self.elsif = elsif
        self.els= els
    
    def traducir(self):
        c3d = ''
        c3d += self.condition.exp.traducir()[0]
        #variables temporales a utilizar en else if
        
        #tengo que ejecutar y añadir los elif
        for eli in self.elsif :
            c3d += str(eli.condition.exp.traducir()[0])
            
            

        c3d += 'if '+ self.condition.exp.traducir()[1] +':\n'
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

    def ejecutar(self):
        pass

class iff(instruccion):
    def __init__(self,condition,instrucciones,elsif,els) -> None:
    
        self.condition = condition
        self.instrucciones = instrucciones
        self.elsif = elsif
        self.els= els
    
    def traducir(self):
        c3d = ''
        varcon = self.condition.traducir()
        c3d += varcon[0]+'\n'
        #variables temporales a utilizar en else if
        
        #tengo que ejecutar y añadir los elif
        aveli = []
        for eli in self.elsif :
            veli = eli.condition.traducir()
            aveli.append(veli)
            c3d += veli[0]+'\n'
            
            

        c3d += 'if '+ varcon[1] +':\n'
        for inst in self.instrucciones:
            c3d += '\t'+inst.traducir().replace('\n','\n\t')+'\n'
        
        contadori = 0
        for eli in self.elsif :
            #tengo que ejecutar y añadir los elif
            c3d += 'elif '+ aveli[contadori][1] +' :\n'
            for inst in eli.instrucciones:
                c3d += '\t'+inst.traducir().replace('\n','\n\t')+'\n'
            contadori += 1
            

        if self.els != None:
            c3d += 'else:\n'
            for inst in self.els.instrucciones:
                c3d += '\t'+inst.traducir().replace('\n','\n\t')+'\n'

        return c3d

    def c3d(self):
        c3d = ''
        for inst in self.instrucciones:
            c3d += inst.c3d()

        for eli in self.elsif:
            c3d += eli.c3d()
        
        if self.els != None:
            c3d += self.els.c3d()

        
        return c3d

    def ejecutar(self):
        pass

class els(instruccion):
    def __init__(self,instrucciones) -> None:
        self.instrucciones = instrucciones

    def traducir(self):
        c3d = ''
        return c3d

    def c3d(self):
        c3d = ''
        for inst in self.instrucciones:
            c3d += inst.c3d()
        return c3d

    def ejecutar(self):
        pass

class elsif(instruccion):
    def __init__(self,condition,instrucciones) -> None:
        self.condition = condition
        self.instrucciones = instrucciones
    
    def traducir(self):
        c3d = ''
        return c3d

    def c3d(self):
        c3d = ''
        for inst in self.instrucciones:
            c3d += inst.c3d()
        return c3d

    def ejecutar(self):
        pass

class expresion():
    'Clase abstracta'

tempcont = 0

def getTemp():
    global tempcont
    tempcont += 1
    return 't'+str(tempcont-1)

import OptimizarObjetos as oo

class exp_boolp(expresion):
    'Esta expresion devuelve un'
    'boolean'

    def __init__(self, val):
        self.val = val

    def traducir(self):
        tmp = getTemp()
        codigo = tmp + f' = {self.val}'
        valor = tmp
        res = self.val
        obj = oo.Temporal(tmp,self.val)
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

    def ejecutar(self):
        pass

class exp_textp(expresion):
    'Devuelve el texto'

    def __init__(self, val):
        self.val = val

    def ejecutar(self):
        pass

    def traducir(self):
        tmp = getTemp()
        codigo = tmp + f' = \'{self.val}\''
        valor = tmp
        res = self.val
        obj = oo.Temporal(tmp,self.val,True)
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

class exp_nump(expresion):
    'Devuelve un número'

    def __init__(self, val):
        self.val = val
        
    def ejecutar(self):
        pass

    def traducir(self):
        tmp = getTemp()
        codigo = tmp + f' = {self.val}'
        valor = tmp
        res = float(self.val)
        obj = oo.Temporal(tmp,self.val)
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

class expresionC:
    'clase abstracta para las operaciones'

class exp_sumap(expresionC):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def ejecutar(self):
        pass

    def traducir(self):
        

        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        res1 = tr1[2]
        res2 = tr2[2]
        
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} + {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        res =  res1 + res2
        obj = oo.Asignacion(tmp,tmp1,tmp2,'+')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

class exp_restap(expresion):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2    
    def ejecutar(self):
        pass
    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} - {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        res = res1 - res2
        obj = oo.Asignacion(tmp,tmp1,tmp2,'-')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res    

class exp_multiplicacionp(expresion):
    'Multiplica las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def ejecutar(self):
        pass
    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} * {tmp2}'
        c3df += f'\n{tmpf}'
        codigo = c3df 
        valor = tmp
        res = res1 * res2
        obj = oo.Asignacion(tmp,tmp1,tmp2,'*')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res
        
class exp_divisionp(expresion):
    'Suma las dos expresiones'

    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def ejecutar(self):
        pass
    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} / {tmp2}'
        c3df += f'\n{tmpf}\n'
        codigo = c3df 
        valor = tmp
        res = res1 / res2
        obj = oo.Asignacion(tmp,tmp1,tmp2,'/')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

class exp_idp(expresion):
    def __init__(self,val):
        self.val = val
    def ejecutar(self):
        pass

    def traducir(self):
        tmp = getTemp()
        codigo = tmp + f' = {self.val}\n'
        valor = tmp
        print(ts.getVariable(self.val))
        res = ts.getVariable(self.val)
        obj = oo.Asignacion(tmp,self.val,None,None)
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

class exp_mayorp(expresion):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def ejecutar(self):
        pass
    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        c3d1 = tr1[0]
        c3d2 = tr2[0]
        tmp1 = tr1[1]
        tmp2 = tr2[1]
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} > {tmp2}'
        c3df += f'\n{tmpf}\n'
        codigo = c3df 
        valor = tmp
        #res = res1 > res2
        res = True
        obj = oo.Asignacion(tmp,tmp1,tmp2,'>')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

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
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} < {tmp2}'
        c3df += f'\n{tmpf}\n'
        codigo = c3df 
        valor = tmp
        #res = res1 < res2
        res = True
        obj = oo.Asignacion(tmp,tmp1,tmp2,'<')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

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
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} == {tmp2}'
        c3df += f'\n{tmpf}\n'
        codigo = c3df 
        valor = tmp
        #res = res1 == res2
        res = True
        obj = oo.Asignacion(tmp,tmp1,tmp2,'==')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

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
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} >= {tmp2}'
        c3df += f'\n{tmpf}\n'
        codigo = c3df 
        valor = tmp
        #res = res1 >= res2
        res = True
        obj = oo.Asignacion(tmp,tmp1,tmp2,'>=')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

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
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} <= {tmp2}'
        c3df += f'\n{tmpf}\n'
        codigo = c3df 
        valor = tmp
        #res = res1 <= res2
        #True
        obj = oo.Asignacion(tmp,tmp1,tmp2,'<=')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

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
        res1 = tr1[2]
        res2 = tr2[2]
        c3df = c3d1 + '\n' + c3d2 
        tmp = getTemp()
        tmpf  = f'{tmp} = {tmp1} != {tmp2}'
        c3df += f'\n{tmpf} \n'
        codigo = c3df 
        valor = tmp
        #res = res1 != res2
        res = True
        obj = oo.Asignacion(tmp,tmp1,tmp2,'!=')
        objopt.append(obj)
        #print(codigo,valor)
        return codigo,valor,res

class inst_procedural(expresion):
    def __init__(self,val):
        self.val = val
        self.lista = []
    
    def c3d(self):
        return ''

        

    def traducir(self):
        return f'\tsql.execute(\'\'\'{self.val}\'\'\')\n'
    def ejecutar(self):
        pass
    

class pl_mathtrig(pl):
    'Abstract Class'

class math_absp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
        
    
    def traducir(self):
        tr1 = self.exp.traducir()
        try:
            resultado = abs(tr1[2])
        except:
            resultado = 0

        codigo = tr1[0]+'\n'
        tmp = getTemp()
        codigo += tmp +'=abs('+tr1[1]+')\n'

        return codigo,tmp,resultado
   
class math_cbrtp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        resultado = mt.cbrt(tr1[2])
        codigo = tr1[0] +'\n'
        tmp = getTemp()
        codigo += tmp +'=mt.cbrt('+tr1[1]+')\n'

        return codigo,tmp,resultado

class math_ceilp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        resultado = round(float(tr1[2]))
        codigo = tr1[0]+'\n'
        tmp = getTemp()
        codigo += tmp +'=round(float('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_degreesp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        resultado = mt.degrees(float(tr1[2]))
        codigo = tr1[0]
        tmp = getTemp()
        codigo += tmp +'=mt.degrees(float('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_divp(pl_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        resultado = mt.div(float(tr1[2]),float(tr2[2]))
        codigo = tr1[0] + '\n'
        codigo += tr2[0] + '\n'
        tmp = getTemp()
        codigo += tmp +'=mt.div(float('+tr1[1]+'),float('+tr2[1]+'))\n'

        return codigo,tmp,resultado

class math_expp(pl_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        resultado = mt.exp(int(tr1[2]))
        codigo = tr1[0]+'\n'
        tmp = getTemp()
        codigo += tmp +'=mt.exp(int('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_factorialp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        resultado = mt.factorial(int(tr1[2]))
        codigo = tr1[0]+'\n'
        tmp = getTemp()
        codigo += tmp +'=mt.factorial(int('+tr1[1]+'))\n'

        return codigo,tmp,resultado
    
class math_floorp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        resultado = mt.floor(float(tr1[2]))
        codigo = tr1[0] +'\n'
        tmp = getTemp()
        codigo += tmp +'=mt.floor(float('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_gcdp(pl_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        resultado = mt.gcd(int(tr1[2]),int(tr2[2]))
        codigo = tr1[0] + '\n'
        codigo += tr2[0]
        tmp = getTemp()
        codigo += tmp +'=mt.gcd(int('+tr1[1]+'),int('+tr2[1]+'))\n'

        return codigo,tmp,resultado

class math_lcmp(pl_mathtrig):
    def __init__(self,exp1,exp2,alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias 

    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        resultado = mt.lcm(int(tr1[2]),int(tr2[2]))
        codigo = tr1[0] + '\n'
        codigo += tr2[0]
        tmp = getTemp()
        codigo += tmp +'=mt.lcm(int('+tr1[1]+'),int('+tr2[1]+'))\n'

        return codigo,tmp,resultado

class math_lnp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp1.traducir()
        
        resultado = mt.ln(float(tr1[2]))
        codigo = tr1[0] + '\n'
        
        tmp = getTemp()
        codigo += tmp +'=mt.ln(float('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_logp(pl_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        resultado = mt.log(int(tr1[2]),int(tr2[2]))
        codigo = tr1[0] + '\n'
        codigo += tr2[0]
        tmp = getTemp()
        codigo += tmp +'=mt.log(int('+tr1[1]+'),int('+tr2[1]+'))\n'

        return codigo,tmp,resultado

class math_log10p(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        
        resultado = mt.log10(float(tr1[2]))
        codigo = tr1[0] + '\n'
        
        tmp = getTemp()
        codigo += tmp +'=mt.log10(float('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_min_scalep(pl_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        
        resultado = mt.min_scale(int(tr1[2]))
        codigo = tr1[0] + '\n'
        
        tmp = getTemp()
        codigo += tmp +'=mt.min_scale(int('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_scalep(pl_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        
        
        codigo = tr1[0] + '\n'
        resultado = mt.scale(str(tr1[2]))
        tmp = getTemp()
        codigo += tmp +'=mt.scale(str('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_modp(pl_mathtrig):
    def __init__(self, exp1,exp2, alias):
        self.exp1 = exp1
        self.exp2  = exp2
        self.alias = alias

    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        codigo = tr1[0] + '\n'
        codigo += t21[0] + '\n'
        resultado = mt.mod(float(tr1[2]),float(tr2[2]))
        tmp = getTemp()
        codigo += tmp +'=mt.mod(float('+tr1[1]+'),float('+tr2[1]+'))\n'

        return codigo,tmp,resultado

class math_pip(pl_mathtrig):
    def __init__(self, alias):
        self.val = mt.pi()
        self.alias = alias

    def traducir(self):
        codigo ='\n'
        tmp = getTemp()
        codigo += tmp +'= mt.pi()\n'
        resultado = mt.pi()
        return codigo,tmp,resultado

class math_powerp(pl_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        codigo = tr1[0] + '\n'
        codigo += t21[0] + '\n'
        
        tmp = getTemp()
        codigo += tmp +'=mt.power(int('+tr1[1]+'),int('+tr2[1]+'))\n'
        resultado = mt.power(int(tr1[2]),int(tr2[2]))
        return codigo,tmp,resultado

class math_radiansp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.radians(float(tr1[2]))
        tmp = getTemp()
        codigo += tmp +'=mt.radians(float('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class math_roundp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        
        tmp = getTemp()
        codigo += tmp +'=round(float('+tr1[1]+'))\n'
        resultado = round(float(tr1[2]))
        return codigo,tmp,resultado

class math_signp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        
        tmp = getTemp()
        codigo += tmp +'=mt.sign(float('+tr1[1]+'))\n'
        resultado = mt.sign(float(tr1[2]))
        return codigo,tmp, resultado

class math_sqrtp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        tmp = getTemp()
        codigo += tmp +'=mt.sqrt(float('+tr1[1]+'))\n'
        resultado = mt.sqrt(float(tr1[2]))
        return codigo,tmp,resultado

class math_trim_scalep(pl_mathtrig):
    def __init__(self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        tmp = getTemp()
        codigo += tmp +'=mt.trim_scale(int('+tr1[1]+'))\n'
        resultado = mt.trim_scale(int(tr1[2]))
        return codigo,tmp,resultado

class math_widthBucketp(pl_mathtrig):
    def __init__(self, exp1, exp2, exp3, exp4, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.exp3 = exp3
        self.exp4 = exp4
        self.alias = alias

    def traducir(self):
        tr1 = self.exp1.traducir()
        tr2 = self.exp2.traducir()
        tr3 = self.exp3.traducir()
        codigo = tr1[0] + '\n'
        codigo += tr2[0] + '\n'
        codigo += tr3[0] + '\n'
        tmp = getTemp()
        codigo += tmp +'=mt.width_bucket(9,8,7,6)\n'
        resultado = mt.width_bucket(9,8,7,6)
        return codigo,tmp,resultado

class math_truncp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.trunc(float(tr1[2]))
        tmp = getTemp()
        codigo += tmp +'=mt.trunc(float('+tr1[1]+'))\n'
        resultado = mt.trunc(float(tr1[2]))
        return codigo,tmp,resultado

class math_randomp(pl_mathtrig):
    def __init__(self, alias):
        self.alias = alias

    def traducir(self):
        
        codigo = '\n'
        
        tmp = getTemp()
        codigo += tmp +'= mt.random()\n'
        resultado = mt.random()
        return codigo,tmp,resultado

class math_setseedp(pl_mathtrig):
    def __init__(self,exp, alias):
        self.exp = exp
        self.alias = alias 
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.setseed(tr1[2])
        tmp = getTemp()
        codigo += tmp +'= mt.setseed('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_acosp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.acos(tr1[2])
        tmp = getTemp()
        codigo += tmp +'= mt.acos('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_acosdp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.acosd(tr1[2])
        tmp = getTemp()
        codigo += tmp +'= mt.acosd('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_asinp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.asin(tr1[2])
        tmp = getTemp()
        codigo += tmp +'= mt.asin('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_asindp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.asind(tr1[2])
        tmp = getTemp()
        codigo += tmp +'= mt.asind('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_atanp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.atan(tr1[2])
        tmp = getTemp()
        codigo += tmp +'= mt.atan('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_atandp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.atand(tr1[2])
        tmp = getTemp()
        codigo += tmp +'= mt.atand('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_atan2p(pl_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.atan2(tr1[2])
        tmp = getTemp()
        codigo += tmp +'= mt.atan2('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_atan2dp(pl_mathtrig):
    def __init__(self, exp1, exp2, alias):
        self.exp1 = exp1
        self.exp2 = exp2
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.atan2d(tr1[2])
        tmp = getTemp()
        codigo += tmp + '= mt.atan2d('+tr1[1]+')\n'

        return codigo,tmp,resultado    

class trig_cosp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.cos(tr1[2])
        tmp = getTemp()
        codigo += tmp +' = mt.cos('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_cosdp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.cosd(tr1[2])
        codigo += tmp +' = mt.cosd('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_cotp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        tmp = getTemp()
        resultado = mt.cot(tr1[2])
        codigo += tmp+ ' = mt.cot('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_cotdp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.cotd(tr1[2])
        tmp = getTemp()
        codigo +=tmp + ' = mt.cotd('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_sinp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.sin(tr1[2])
        tmp = getTemp()
        codigo += tmp+ ' = mt.sin('+tr1[1]+')'

        return codigo,tmp,resultado

class trig_sindp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.sind(tr1[2])
        tmp = getTemp()
        codigo +=tmp +' = mt.sind('+tr1[1]+')\n'

        return codigo,tmp,resultado
 
class trig_tanp(pl_mathtrig):
    def __init__(self, exp, alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.tan(tr1[2])
        tmp = getTemp()
        codigo +=tmp +' = mt.tan('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_tandp(pl_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.tand(tr1[2])
        tmp = getTemp()
        codigo +=  tmp +' = mt.tand('+tr1[1]+')\n'

        return codigo,tmp,resultado
    
class trig_sinhp(pl_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.sinh(tr1[2])
        tmp = getTemp()
        codigo += tmp +' = mt.sinh('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_coshp(pl_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.cosh(tr1[2])
        tmp = getTemp()
        codigo += tmp +' = mt.cosh('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_tanhp(pl_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.tanh(tr1[2])
        tmp = getTemp()
        codigo +=tmp+ ' = mt.tanh('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_asinhp(pl_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.asinh(tr1[2])
        tmp = getTemp()
        codigo += tmp + ' = mt.asinh('+tr1[1]+')\n'

        return codigo,tmp,resultado

class trig_acoshp(pl_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.acosh(tr1[2])
        tmp = getTemp()
        codigo += tmp +' = mt.acosh('+tr1[1]+')'

        return codigo,tmp,resultado

class trig_atanhp(pl_mathtrig):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = mt.atanh(tr1[2])
        tmp = getTemp()
        codigo +=tmp +' = mt.atanh('+tr1[1]+')\n'

        return codigo,tmp,resultado

class pl_function():
    ''' clase abstracta '''

class fun_lengthp(pl_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = len(str(tr1[2]))
        tmp = getTemp()
        codigo += tmp +' = len(str('+tr1[1]+'))\n'

        return codigo,tmp,resultado

class fun_trimp(pl_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias    

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = str(tr1[2]).strip()
        tmp = getTemp()
        codigo += tmp +' = str('+tr1[1]+').strip()\n'

        return codigo,tmp,resultado

class fun_md5p(pl_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias

    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        
        crypt = hashlib.md5()
        crypt.update(tr1[2].encode('utf-8'))
        resultado = crypt.hexdigest()
        
        codigo += 'crypt = hashlib.md5()\n'
        codigo += 'crypt.update('+tr1[1]+'.encode(\'utf-8\'))\n'
        
        tmp = getTemp()
        codigo +=tmp +' = crypt.hexdigest()\n'

        return codigo,tmp,resultado    

class fun_sha256p(pl_function):
    def __init__ (self,exp,alias):
        self.exp = exp
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        
        crypt = hashlib.sha256()
        crypt.update(tr1[2].encode('utf-8'))
        resultado = crypt.hexdigest()
        
        codigo += 'crypt = hashlib.sha256()\n'
        codigo += 'crypt.update('+tr1[1]+'.encode(\'utf-8\'))\n'
        
        tmp = getTemp()
        codigo += tmp +' = crypt.hexdigest()\n'

        return codigo,tmp,resultado  

class fun_convertp(pl_function):
    def __init__ (self,exp,tipo,alias):
        self.exp = exp
        self.type = tipo
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'
        resultado = tr1[2] + '\n'
        valor = tr1[1] + '\n'

        return codigo,valor,resultado

    def ejecutar(self,tables):
        return self.exp

class fun_substrp(pl_function):
    def __init__ (self,exp,min,max,alias):
        self.exp = exp
        self.min = min
        self.max = max
        self.alias = alias
    
    def traducir(self):
        tr1 = self.exp.traducir()
        codigo = tr1[0] + '\n'

        resultado = str(tr1[2])[self.min:self.max]
        tmp = getTemp()
        codigo += tmp +' = '+tr1[1]+'['+str(self.min)+':'+str(self.max)+']\n'

        return codigo,tmp,resultado

class fun_nowp(pl_function):
    def __init__ (self,alias):
        self.alias = alias
    
    def traducir(self):
        
        codigo ='\n'
        today = date.today()
        resultado = today.strftime("%Y-%m-%d %H:%M:%S")
        codigo += 'today = date.today()'
        valor  = 'today.strftime("%Y-%m-%d %H:%M:%S")\n'

        

        return codigo,valor,resultado

class queryf(instruccion):
    def __init__(self,callfunc):
        self.callfunc = callfunc

    def traducir(self):
        t = self.callfunc.traducir()
        t0 = t[0].replace('\n','\n\t')
        return f'\t{t0}print({t[1]})\n'
        
    def ejecutar(self):
        return 'Se creo el select'