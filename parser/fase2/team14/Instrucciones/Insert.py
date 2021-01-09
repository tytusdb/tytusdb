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
from Expresion.Id import  Identificador

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
                            #print("UNIQUE",colunique,"colactual",nombre,"valor",self.valores[i].getval(ent).valor,"---")
                            exp=self.valores[i].getval(ent)
                            exp=exp.valor
                            v=self.validarunique(ent,tabla,colunique,exp)
                            #print("-----",v)
                            if v:
                                #print('Error Violacion de Constraint Unique en:',colunique,' : ',self.valores[i].getval(ent).valor)
                                variables.consola.insert(INSERT,'Error Violacion de Constraint Unique en columna:'+colunique +' : '+str(self.valores[i].getval(ent).valor)+'\n')
                                reporteerrores.append(Lerrores("Error Semantico", 'Error Violacion de Constraint Unique en columna:'+colunique +' : '+str(self.valores[i].getval(ent).valor),'',''))
                                return

                    if(verificarcheck!=None):
                        check=ent.buscarSimbolo(verificarcheck)
                        #print("Condicion:",check.valor.exp1.getval(ent).valor,check.valor.simbolo,check.valor.exp2.getval(ent).valor)

                        if isinstance(check.valor.exp1, Identificador):
                            condicion1 = check.valor.exp1.getval(ent)
                            if condicion1 == None:
                                condicion1 = Terminal(columna.tipo, check.valor.exp1.nombre)
                        else:
                            condicion1 = Terminal(columna.tipo, check.valor.exp1.getval(ent).valor)

                        if isinstance(check.valor.exp2, Identificador):
                            condicion2 = check.valor.exp2.getval(ent)
                            if condicion2 == None:
                                condicion2 = Terminal(columna.tipo, check.valor.exp2.nombre)
                        else:
                            condicion2 = Terminal(columna.tipo, check.valor.exp2.getval(ent).valor)
                        operador=check.valor.simbolo
                        l=0
                        for columna in columnas:
                            #tipo=columna.tipo
                            if isinstance(check.valor.exp1, Identificador):
                                check.valor.exp1 = Terminal(check.valor.exp1.tipo, check.valor.exp1.nombre)

                            if(check.valor.exp1.getval(ent).valor==columna.nombre):
                                condicion1=Terminal(columna.tipo,self.valores[l].getval(ent).valor)
                            l=l+1

                        n=0
                        for columna in columnas:
                            if isinstance(check.valor.exp2, Identificador):
                                check.valor.exp2 = Terminal(check.valor.exp2.tipo, check.valor.exp2.nombre)

                            if(check.valor.exp2.getval(ent).valor==columna.nombre):

                                condicion2=Terminal(columna.tipo,self.valores[n].getval(ent).valor)
                            n=n+1

                        correcto=False
                        if operador in ('>','<','>=','<=','='):
                            #print(condicion1.getval(ent).valor,operador,condicion2.getval(ent).valor)
                            nuevaop = Relacional(condicion1,condicion2,operador)
                            if nuevaop.getval(ent).valor:
                                correcto=True
                            else:
                                variables.consola.insert(INSERT,'Error Registro no cumple con condicion check\n')
                                reporteerrores.append(Lerrores("Error Semantico", 'Registro no cumple con condicion check','',''))
                                return

                        elif operador in ('or','and','not'):
                            nuevaop = Logica(condicion1,condicion2,operador);
                            if nuevaop.getval(ent).valor:
                                correcto=True
                            else:
                                variables.consola.insert(INSERT,'Error Registro no cumple con condicion check\n')
                                reporteerrores.append(Lerrores("Error Semantico", 'Error Registro no cumple con condicion check','',''))
                                return

                    buscado=str('ENUM_'+ent.getDataBase()+'_'+tipo.tipo)
                    types:Simbolo= ent.buscarSimbolo(buscado)

                    tipocorrecto = False

                    if types!=None:
                        tiposenum=types.valor
                        print("Comparando Enum")
                        for valenum in tiposenum:
                             if str(valenum.getval(ent).valor).lower() == str(self.valores[i].getval(ent).valor).lower():
                                  tipocorrecto=True
                        if not tipocorrecto:
                            variables.consola.insert(INSERT,str('Error Tipo enum no correcto en valor: '+self.valores[i].getval(ent).valor)+'\n')
                            reporteerrores.append(Lerrores("Error Semantico",str('Error Tipo enum no correcto en valor: '+self.valores[i].getval(ent).valor),'',''))
                            return


                    if not tipocorrecto:


                        util=Tipo(None,None,-1,-1)
                        #tabla:Simbolo = ent.buscarSimbolo(completo)


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
                    terminales.append(val.valor)

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

    def traducir(self, ent: Entorno):
        self.codigo3d = 'ci.ejecutarsql(\" insert into ' + self.nombre + ' values('

        for i in range(0, len(self.valores), 1):
            if (i == 0):
                if isinstance(self.valores[i],Identificador):
                    self.codigo3d += '\"+str('+self.valores[i].traducir(ent).stringsql+')+\"'
                else:
                    self.codigo3d += self.valores[i].traducir(ent).stringsql
            else:
                if isinstance(self.valores[i],Identificador):
                    self.codigo3d += ',\"+str('+self.valores[i].traducir(ent).stringsql+')+\"'
                else:
                    self.codigo3d += ', ' +self.valores[i].traducir(ent).stringsql


        self.codigo3d += ')'

        self.codigo3d += ";\")\n"
        return self

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
                    #print("Condicion:",check.valor.exp1.getval(ent).valor,check.valor.simbolo,check.valor.exp2.getval(ent).valor)

                    if isinstance(check.valor.exp1,Identificador):
                        condicion1=check.valor.exp1.getval(ent)
                        if condicion1==None:

                            condicion1=Terminal(columna.tipo, check.valor.exp1.nombre)
                    else:
                        condicion1 = Terminal(columna.tipo, check.valor.exp1.getval(ent).valor)

                    if isinstance(check.valor.exp2, Identificador):
                        condicion2 = check.valor.exp2.getval(ent)
                        if condicion2 == None:
                            condicion2 = Terminal(columna.tipo, check.valor.exp2.nombre)
                    else:
                        condicion2 = Terminal(columna.tipo, check.valor.exp2.getval(ent).valor)


                    operador=check.valor.simbolo
                    l=0
                    for columna in columnas:
                        #tipo=columna.tipo
                        if(check.valor.exp1.getval(ent)==columna.nombre):
                            k=0
                            for actual in self.namecolums:
                                if(check.valor.exp1.getval(ent)==actual.getval(ent).valor):
                                    condicion1=Terminal(columna.tipo,self.valores[k].getval(ent).valor)
                                k=k+1
                        l=l+1

                    n=0
                    for columna in columnas:
                        if(check.valor.exp2.getval(ent)==columna.nombre):
                            k=0
                            for actual in self.namecolums:
                                if(check.valor.exp2.getval(ent)==actual.getval(ent).valor):
                                    condicion2=Terminal(columna.tipo,self.valores[k].getval(ent).valor)
                                k=k+1
                        n=n+1

                    correcto=False
                    if operador in ('>','<','>=','<=','='):
                        #print(condicion1.getval(ent).valor,operador,condicion2.getval(ent).valor)
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
                    if j < len(self.namecolums):
                        nombre=columna.nombre
                        tipo=columna.tipo
                        util=Tipo(None,None,-1,-1)
                        if isinstance(self.namecolums[j],Identificador):
                            v=self.namecolums[j].getval(ent)
                            if v==None:
                                self.namecolums[j] = Terminal(self.namecolums[j].tipo, self.namecolums[j].nombre)
                            else:
                                self.namecolums[j]=v

                        if(nombre==self.namecolums[j].valor):
                            #print("iguales",nombre,":",self.namecolums[j].getval(ent).valor,"J",j,"t",t)

                            for colunique in columnaunique:
                                if nombre==colunique:
                                    #print("UNIQUE",colunique,"colactual",nombre,"valor",self.valores[j].getval(ent).valor,"---")
                                    v=self.validarunique(ent,tabla,colunique,self.valores[j].getval(ent).valor)
                                    #print("-----",v)
                                    if v:
                                        variables.consola.insert(INSERT,'Error Violacion de Constraint Unique en columna:'+colunique +' : '+str(self.valores[j].getval(ent).valor)+'\n')
                                        reporteerrores.append(Lerrores("Error Semantico", 'Error Violacion de Constraint Unique en columna:'+colunique +' : '+str(self.valores[j].getval(ent).valor),'',''))
                                        return


                            buscado=str('ENUM_'+ent.getDataBase()+'_'+tipo.tipo)
                            types:Simbolo= ent.buscarSimbolo(buscado)

                            tipocorrecto = False

                            if types!=None:
                                tiposenum=types.valor
                                print("Comparando Enum")
                                for valenum in tiposenum:
                                    if str(valenum.getval(ent).valor).lower() == str(self.valores[j].getval(ent).valor).lower():
                                        tipocorrecto=True
                                if not tipocorrecto:
                                    variables.consola.insert(INSERT,str('Error Tipo enum no correcto en valor: '+self.valores[j].getval(ent).valor)+'\n')
                                    reporteerrores.append(Lerrores("Error Semantico",str('Tipo enum no correcto en valor: '+self.valores[j].getval(ent).valor),'',''))
                                    return



                            if not tipocorrecto:
                                if util.comparetipo(tipo,self.valores[j].getval(ent).tipo):
                                    'todo correcto'
                                else:
                                    correcto=False
                                    variables.consola.insert(INSERT,'Error los tipos no coinciden con la definicion de la tabla\n')
                                    reporteerrores.append(Lerrores("Error Semantico",'Tipo de datos en columanas no son iguales','',''))
                                    return


                            terminales.append(self.valores[j].valor)
                            j=j+1
                        else:
                            #print("diferentes",nombre,":",self.namecolums[j].getval(ent).valor,"J",j,"t",t)
                            terminales.append('')
                    else:
                        terminales.append('')
                r=DBMS.insert(ent.getDataBase(),self.nombre,terminales)
                if(r==4):
                    variables.consola.insert(INSERT,'Error violacion de Constraint Primary key\n')
                    reporteerrores.append(Lerrores("Error Semantico",'Violacion de Constraint primary Key','',''))
                    return
                elif r==0:
                    variables.consola.insert(INSERT, 'Registros Ingresados EXITOSAMENTE\n')





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

    def traducir(self, ent: Entorno):
        self.codigo3d = 'ci.ejecutarsql(\" insert into ' + self.nombre + ' ('
        i = 0
        for i in range(0, len(self.namecolums), 1):
            if (i == 0):
                self.codigo3d += self.namecolums[i].valor
            else:
                self.codigo3d += ', ' + self.namecolums[i].valor

        self.codigo3d += ') values ('

        i = 0
        for i in range(0, len(self.valores), 1):
            if (i == 0):
                self.codigo3d += self.valores[i].traducir(ent).stringsql
            else:
                self.codigo3d += ', ' + self.valores[i].traducir(ent).stringsql

        self.codigo3d += ");\")\n"
        return self