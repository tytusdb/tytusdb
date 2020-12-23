from Tipo import Tipo
from Instrucciones.Instruccion import Instruccion
from storageManager import jsonMode as DBMS
from Entorno.Entorno import Entorno
from Entorno.Simbolo import Simbolo
from Entorno.TipoSimbolo import TipoSimbolo
from Expresion.Logica import *
from Expresion.Relacional import *
from Expresion.Expresion import *
from Expresion.Terminal import *
from Expresion.FuncionesNativas import *
from Expresion.variablesestaticas import variables
from tkinter import *
from reportes import *
class Insert(Instruccion):
    def __init__(self, nombre,valores=[]):
        self.nombre=nombre
        self.valores=valores

    def ejecutar(self, ent:Entorno):
        completo=str(self.nombre+'_'+ent.getDataBase())
        tabla:Simbolo = ent.buscarSimbolo(completo)
        if tabla != None:
            columnas=tabla.valor
            columnaunique=[]
            columnacheck=[]

            if len(self.valores)== len(columnas):
                i=0
                correcto=True
                for columna in columnas:
                    verificarunique=tabla.valor[i].atributos.get('unique')
                    verificarcheck=tabla.valor[i].atributos.get('check')
                    nombre=columna.nombre
                    tipo=columna.tipo

                    condicion1:Expresion
                    condicion2:Expresion
                    if verificarunique!=None:
                        #print("unique",verificarunique,"m--",nombre)
                        columnaunique.append(columna.nombre)

                    for colunique in columnaunique:
                        if nombre==colunique:
                            #print("UNIQUE",colunique,"colactual",nombre,"valor",self.valores[i].getval(ent),"---")
                            v=self.validarunique(ent,tabla,colunique,self.valores[i].getval(ent))
                            #print("-----",v)
                            if v:
                                #print('Error Violacion de Constraint Unique en:',colunique,' : ',self.valores[i].getval(ent))
                                variables.consola.insert(INSERT,'Error Violacion de Constraint Unique en columna:'+colunique +' : '+str(self.valores[i].getval(ent))+'\n')
                                reporteerrores.append(Lerrores("Error Semantico", 'Error Violacion de Constraint Unique en columna:'+colunique +' : '+str(self.valores[i].getval(ent)),'',''))
                                return
                                
                    if(verificarcheck!=None):
                        check=ent.buscarSimbolo(verificarcheck)
                        #print("Condicion:",check.valor.exp1.getval(ent),check.valor.simbolo,check.valor.exp2.getval(ent))
                        condicion1=Terminal(columna.tipo,check.valor.exp1.getval(ent))
                        condicion2=Terminal(columna.tipo,check.valor.exp2.getval(ent))
                        operador=check.valor.simbolo
                        l=0
                        for columna in columnas:
                            #tipo=columna.tipo
                            if(check.valor.exp1.getval(ent)==columna.nombre):
                                condicion1=Terminal(columna.tipo,self.valores[l].getval(ent))     
                            l=l+1
                        
                        n=0
                        for columna in columnas:
                            if(check.valor.exp2.getval(ent)==columna.nombre):
                                
                                condicion2=Terminal(columna.tipo,self.valores[n].getval(ent))
                            n=n+1
                        
                        correcto=False
                        if operador in ('>','<','>=','<=','='):
                            #print(condicion1.getval(ent),operador,condicion2.getval(ent))
                            nuevaop = Relacional(condicion1,condicion2,operador);
                            if nuevaop.getval(ent):
                                correcto=True
                            else:
                                variables.consola.insert(INSERT,'Error Registro no cumple con condicion check\n')
                                reporteerrores.append(Lerrores("Error Semantico", 'Registro no cumple con condicion check','',''))
                                return

                        elif operador in ('or','and','not'):
                            nuevaop = Logica(condicion1,condicion2,operador);
                            if nuevaop.getval(ent):
                                correcto=True
                            else:
                                variables.consola.insert(INSERT,'Error Registro no cumple con condicion check\n')
                                reporteerrores.append(Lerrores("Error Semantico", 'Error Registro no cumple con condicion check','',''))
                                return
                    
                    buscado=str('ENUM_'+ent.getDataBase()+'_'+tipo.getTipo())
                    types:Simbolo= ent.buscarSimbolo(buscado)
                    
                    tipocorrecto = False 
                    
                    if types!=None:
                        tiposenum=types.valor
                        print("Comparando Enum")
                        for valenum in tiposenum:
                             if str(valenum.getval(ent)).lower() == str(self.valores[i].getval(ent)).lower():
                                  tipocorrecto=True
                        if not tipocorrecto:
                            variables.consola.insert(INSERT,str('Error Tipo enum no correcto en valor: '+self.valores[i].getval(ent))+'\n')
                            reporteerrores.append(Lerrores("Error Semantico",str('Error Tipo enum no correcto en valor: '+self.valores[i].getval(ent)),'',''))
                            return

                            
                    if not tipocorrecto:
                        print("comparando tipos")
                       
                        util=Tipo(None,None,-1,-1)
                        #tabla:Simbolo = ent.buscarSimbolo(completo)
        
                        if isinstance (self.valores[i],FuncionesNativas):
                            self.valores[i]=self.valores[i].getval(ent)

                        if util.comparetipo(tipo,self.valores[i].tipo):
                            'todo correcto'
                            
                        else:
                            correcto=False
                            variables.consola.insert(INSERT,'Error los tipos no coinciden con la definicion de la tabla\n')
                            reporteerrores.append(Lerrores("Error Semantico",'Tipo de datos en columanas no son iguales','',''))
                            return
                           
                    i=i+1
                terminales = []
                for val in self.valores:
                    terminales.append(val.getval(ent))

                r=DBMS.insert(ent.getDataBase(),self.nombre,terminales)
                if(r==4):
                    variables.consola.insert(INSERT,'Error violacion de Constraint Primary key\n')
                    reporteerrores.append(Lerrores("Error Semantico",'Violacion de Constraint primary Key','',''))
                    return
                variables.consola.insert(INSERT,'Registros Ingresados EXITOSAMENTE\n')
                           
                return    
             
    def validarunique(self,entorno,tabla,namecolums,unique):
        encontrado=0
        nocol=-1
        
        if tabla != None:
      
            columnas=tabla.valor
            i=0
            param=[]
            for columna in columnas:
                nombre = columna.nombre
            
                if namecolums == nombre:
                    encontrado+=1
                    tipo=columna.tipo
                    nocol=i
                    nomtabla=tabla.nombre
                    nomtabla=nomtabla.replace('_'+entorno.getDataBase(),'')
                    continue
                i=i+1
            
            if encontrado==1 and nocol>-1:
                datos=DBMS.extractTable(entorno.getDataBase(),nomtabla)
                if datos!= None:
                    self.nombreres = nomtabla
                    for i in range(0,len(datos)):

                        dato=datos[i][nocol]  
                        param.append(dato)       
                        for val in param:
                            #print("LIsta-->",val,'------',unique,"-----------")
                            if(val==unique and val!='' ):  
                                return True

            return False


class InsertWhitColum(Instruccion):
    def __init__(self, nombre,namecolums=[],valores=[]):
        self.nombre=nombre
        self.valores=valores
        self.namecolums=namecolums

    def ejecutar(self, ent:Entorno):
        completo=str(self.nombre+'_'+ ent.getDataBase())
        tabla:Simbolo = ent.buscarSimbolo(completo)
        if tabla != None:
            columnas=tabla.valor
            i=0
            contador=0
            columnaunique=[]
            for columna in columnas:
              
                verificarnull=tabla.valor[i].atributos.get('not null')
                verificarprimary=tabla.valor[i].atributos.get('primary')
                verificarunique=tabla.valor[i].atributos.get('unique')
                verificarcheck=tabla.valor[i].atributos.get('check')
                
                condicion1:Expresion
                condicion2:Expresion
                if verificarunique!=None:
                    columnaunique.append(columna.nombre)
                


                if(verificarcheck!=None):
                    check=ent.buscarSimbolo(verificarcheck)
                    #print("Condicion:",check.valor.exp1.getval(ent),check.valor.simbolo,check.valor.exp2.getval(ent))
                    condicion1=Terminal(columna.tipo,check.valor.exp1.getval(ent))
                    condicion2=Terminal(columna.tipo,check.valor.exp2.getval(ent))
                    operador=check.valor.simbolo
                    l=0
                    for columna in columnas:
                        #tipo=columna.tipo
                        if(check.valor.exp1.getval(ent)==columna.nombre):
                            k=0
                            for actual in self.namecolums:
                                if(check.valor.exp1.getval(ent)==actual.getval(ent)):
                                    condicion1=Terminal(columna.tipo,self.valores[k].getval(ent))
                                k=k+1
                        l=l+1
                    
                    n=0
                    for columna in columnas:
                        if(check.valor.exp2.getval(ent)==columna.nombre):
                            k=0
                            for actual in self.namecolums:
                                if(check.valor.exp2.getval(ent)==actual.getval(ent)):
                                    condicion2=Terminal(columna.tipo,self.valores[k].getval(ent))
                                k=k+1
                        n=n+1
                    
                    correcto=False
                    if operador in ('>','<','>=','<=','='):
                        #print(condicion1.getval(ent),operador,condicion2.getval(ent))
                        nuevaop = Relacional(condicion1,condicion2,operador);
                        if nuevaop.getval(ent):
                            correcto=True
                        else:
                            variables.consola.insert(INSERT,'Error Registro no cumple con condicion check\n')
                            reporteerrores.append(Lerrores("Error Semantico", 'Registro no cumple con condicion check','',''))
                            return

                    elif operador in ('or','and','not'):
                        nuevaop = Logica(condicion1,condicion2,operador);
                        if nuevaop.getval(ent):
                            correcto=True
                        else:
                            variables.consola.insert(INSERT,'Error Registro no cumple con condicion check\n')
                            reporteerrores.append(Lerrores("Error Semantico", 'Registro no cumple con condicion check','',''))
                            return 
                  



                if(verificarnull !=None or verificarprimary!=None or verificarunique!=None):
                    contador=contador+1
                i=i+1
                
                #print("contador",contador)
            if( (len(self.valores) >= contador) and (len(self.valores) == len(self.namecolums)) and (len(self.namecolums)<=len(columnas))):
                j=0
                t=0
                correcto=True
                terminales = []
                for columna in columnas:
                    nombre=columna.nombre
                    tipo=columna.tipo
                    util=Tipo(None,None,-1,-1)
                    if(nombre==self.namecolums[j].getval(ent)):
                        #print("iguales",nombre,":",self.namecolums[j].getval(ent),"J",j,"t",t)
                        
                        for colunique in columnaunique:
                            if nombre==colunique:
                                #print("UNIQUE",colunique,"colactual",nombre,"valor",self.valores[j].getval(ent),"---")
                                v=self.validarunique(ent,tabla,colunique,self.valores[j].getval(ent))
                                #print("-----",v)
                                if v:
                                    variables.consola.insert(INSERT,'Error Violacion de Constraint Unique en columna:'+colunique +' : '+str(self.valores[j].getval(ent))+'\n')
                                    reporteerrores.append(Lerrores("Error Semantico", 'Error Violacion de Constraint Unique en columna:'+colunique +' : '+str(self.valores[j].getval(ent)),'',''))
                                    return
                                    
                        if isinstance (self.valores[j],FuncionesNativas):
                            self.valores[j]=self.valores[j].getval(ent)
                        
                        buscado=str('ENUM_'+ent.getDataBase()+'_'+tipo.getTipo())
                        types:Simbolo= ent.buscarSimbolo(buscado)
                    
                        tipocorrecto = False 
                    
                        if types!=None:
                            tiposenum=types.valor
                            print("Comparando Enum")
                            for valenum in tiposenum:
                                if str(valenum.getval(ent)).lower() == str(self.valores[j].getval(ent)).lower():
                                    tipocorrecto=True
                            if not tipocorrecto:
                                variables.consola.insert(INSERT,str('Error Tipo enum no correcto en valor: '+self.valores[j].getval(ent))+'\n')
                                reporteerrores.append(Lerrores("Error Semantico",str('Tipo enum no correcto en valor: '+self.valores[j].getval(ent)),'',''))
                                return



                        if not tipocorrecto:
                            if util.comparetipo(tipo,self.valores[j].tipo):
                                'todo correcto'
                            else:
                                correcto=False
                                variables.consola.insert(INSERT,'Error los tipos no coinciden con la definicion de la tabla\n')
                                reporteerrores.append(Lerrores("Error Semantico",'Tipo de datos en columanas no son iguales','',''))
                                return
                        
                        
                        terminales.append(self.valores[j].getval(ent))
                        j=j+1
                    else: 
                        #print("diferentes",nombre,":",self.namecolums[j].getval(ent),"J",j,"t",t)
                        terminales.append('')
                r=DBMS.insert(ent.getDataBase(),self.nombre,terminales)
                if(r==4):
                    variables.consola.insert(INSERT,'Error violacion de Constraint Primary key\n')
                    reporteerrores.append(Lerrores("Error Semantico",'Violacion de Constraint primary Key','',''))
                    return

                variables.consola.insert(INSERT,'Registros Ingresados EXITOSAMENTE\n')
                return 
                
                
            else:
                variables.consola.insert(INSERT,'Error Numero Parametros en tabla '+self.nombre+' Incorrectos\n')
                reporteerrores.append(Lerrores('Erro semantico','Numero Parametros en tabla '+self.nombre+' Incorrectos','',''))
                return
                
        else:
            variables.consola.insert(INSERT,'Error Tabla '+self.nombre+' No Existe en la BD actual\n')
            reporteerrores.append(Lerrores('Error Semantico','Numero Parametros en tabla '+self.nombre+' Incorrectos','',''))
            return
           

    def validarunique(self,entorno,tabla,namecolums,unique):
        encontrado=0
        nocol=-1
        
        if tabla != None:
      
            columnas=tabla.valor
            i=0
            param=[]
            for columna in columnas:
                nombre = columna.nombre
            
                if namecolums == nombre:
                    encontrado+=1
                    tipo=columna.tipo
                    nocol=i
                    nomtabla=tabla.nombre
                    nomtabla=nomtabla.replace('_'+entorno.getDataBase(),'')
                    continue
                i=i+1
            
            if encontrado==1 and nocol>-1:
                datos=DBMS.extractTable(entorno.getDataBase(),nomtabla)
                if datos!= None:
                    self.nombreres = nomtabla
                    for i in range(0,len(datos)):

                        dato=datos[i][nocol]  
                        param.append(dato)       
                        for val in param:
                            #print("LIsta-->",val,'------',unique,"-----------")
                            if(val==unique and val!='' ):  
                                return True

                        
                        #if dato==unique:
                            #print("iguales",dato,unique)
                        #else:
                            #print("diferete",dato,unique)
            return False