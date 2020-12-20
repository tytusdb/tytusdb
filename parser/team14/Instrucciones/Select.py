from Instrucciones.Instruccion import Instruccion
from Entorno.Entorno import Entorno
from storageManager import jsonMode as DBMS
from Expresion.Terminal import Terminal
from Expresion.Unaria import Unaria
from Expresion.Relacional import  Relacional
from Expresion.Logica import Logica
from Expresion.Expresion import Expresion
from Expresion.variablesestaticas import variables
from tkinter import *
import copy

class Select(Instruccion):
    'This is an abstract class'
    encabezado = []
    nombreres=''
    def __init__(self,distinct=None,exps=None,froms=None,where=None,group=None,having=None,combinging=None,order=None,limit=None):
        self.distinct=distinct
        self.exps=exps
        self.froms=froms
        self.where=where
        self.group=group
        self.having=having
        self.order=order
        self.limit=limit
        self.combinig=combinging


    def ejecutar(self,ent:Entorno):
            tablas = [] 
            result = []
            self.encabezado = []

            'Metodo Abstracto para ejecutar la instruccion'
            if self.distinct is None and self.froms is None and self.where is None and self.group is None and self.having is None and self.order is None and self.combinig is None:
                resultados = [];
                for exp in self.exps:
                    if exp != None:
                        resultados.append(exp.getval(ent))
                return resultados
            elif self.froms != None and self.exps!= None:

                for exp in self.froms:
                    if exp != None:
                        tipo =exp.tipo;
                        if tipo.tipo=='identificador':
                            nombre=exp.getval(ent)
                            tabla=ent.buscarSimbolo(nombre+"_"+ent.getDataBase())
                            if tabla!=None:
                                tablas.append(tabla)

                if len(tablas)>1:
                    'producto cartesiano'
                else:
                    'llenar resultado desde backend'
                    real=tablas[0].nombre.replace('_'+ent.getDataBase(),'')
                    result=DBMS.extractTable(ent.getDataBase(),real)




                #filtros
                if self.where != None:
                    result=self.execwhere(ent,tablas)



                #acceder a columnas
                if len(self.exps) == 1:
                    if self.exps[0].getval(ent) == '*':
                        self.mostarresult(result, 'prueba xd')
                    elif self.exps[0].tipo.tipo=='identificador':
                        'obtengo  solo columnas pedidas'
                    else:
                        'pendientes subconsultas y funciones'



    def mostarresult(self,result,nomresult):
            if not len(result)>0:
                return
            data = result[0]
            cols = len(data)



            variables.consola.insert(INSERT, "Ejecutando select: " + self.nombreres)
            variables.consola.insert(INSERT, "\n")
            variables.x.title = self.nombreres
            variables.x.field_names = self.encabezado
            variables.x.add_rows(result)
            variables.consola.insert(INSERT, variables.x)
            variables.x.clear()
            variables.consola.insert(INSERT, "\n")



    def producto(self, entorno):
        'realizacion producto cartesiano de tablas'
    def getcolumna(self,entorno,tablas):
        '''   datos = DBMS.extractTable(entorno.getDataBase(), nomtabla)
        if datos != None:
            for fila in datos:
                colres.append(fila[nocol])
        tam = len(colres) '''


    def where2id(self,entorno,tablas):
        filtrado=[]
        exp1:Expresion
        exp2:Expresion
        colres=[]
        tipo1=''
        tipo2= ''
        encontrado1=0
        encontrado2= 0
        nocol1 = -1
        nocol2 = -1
        nomtabla1 = ''
        nomtabla2 = ''

        'realizar operacion'
        exp1=self.where.exp1
        exp2=self.where.exp2
        val1=exp1.getval(entorno)
        val2=exp2.getval(entorno)
        op=self.where.operador

        for tabla in tablas:
            columnas=tabla.valor
            i=0
            for columna in columnas:
                nombre = columna.nombre
                self.encabezado.append(nombre)
                if val1 == nombre:
                    encontrado1+=1
                    tipo1=columna.tipo
                    nocol1=i
                    nomtabla1=tabla.nombre
                    nomtabla1=nomtabla1.replace('_'+entorno.getDataBase(),'')
                    i=i+1
                    continue
                if val2 == nombre:
                    encontrado2+=1
                    tipo2=columna.tipo
                    nocol2 = i
                    nomtabla2=tabla.nombre
                    nomtabla2=nomtabla2.replace('_'+entorno.getDataBase(),'')
                    i=i+1
                    continue
                i=i+1

        if encontrado1 == 1 and encontrado2 == 1:
            datos1 = DBMS.extractTable(entorno.getDataBase(),nomtabla1)
            datos2 = DBMS.extractTable(entorno.getDataBase(), nomtabla2)

            if datos1 == datos2:
                self.nombreres=nomtabla1
                for i in range(0,len(datos1)):
                    dato1=datos1[i][nocol1]
                    dato2=datos1[i][nocol2]
                    expi = Terminal(tipo1, dato1)
                    expd = Terminal(tipo2, dato2)

                    if op in ('>','<','>=','<=','='):
                        nuevaop = Relacional(expi,expd,op);
                        if nuevaop.getval(entorno):
                            'Agrego la fila al resultado'
                            filtrado.append(datos1[i])
                    elif op in ('or','and','not'):
                        nuevaop = Logica(expi,expd,op);
                        if nuevaop.getval(entorno):
                            'Agrego la fila al resultado'
                            filtrado.append(datos1[i])

                    else:
                        variables.consola.insert('Error el resultado del where no es booleano \n')
                return filtrado

        else:
            variables.consola.insert('Error el nombre de las columnas es ambiguo \n')



    def execwhere(self,entorno,tablas):
        filtrado=[]
        exp1:Expresion
        exp2:Expresion
        colres=[]
        tipo=''
        isid=False
        posid=-1
        if isinstance(self.where, Relacional) or isinstance(self.where,Logica):
            encontrado=0
            nocol=-1
            nomtabla=''
            'realizar operacion'
            exp1=self.where.exp1
            exp2=self.where.exp2
            op=self.where.operador
            val=''
            if(exp1.tipo.tipo=='identificador') and exp2.tipo.tipo=='identificador':
                return self.where2id(entorno,tablas)

            elif (exp1.tipo.tipo=='identificador'):
                val = exp1.getval(entorno)
                posid = 1
            else:
                val = exp2.getval(entorno)
                posid=2

            for tabla in tablas:
                columnas=tabla.valor
                i=0
                for columna in columnas:
                    nombre = columna.nombre
                    self.encabezado.append(nombre)
                    if val == nombre:
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
                        expi = None
                        expd = None
                        if posid == 1:
                            expi = Terminal(tipo, dato)
                            expd = exp2
                        else:
                            expi = exp1
                            expd = Terminal(tipo, dato)

                        if op in ('>','<','>=','<=','='):
                            nuevaop = Relacional(expi,expd,op);
                            if nuevaop.getval(entorno):
                                'Agrego la fila al resultado'
                                filtrado.append(datos[i])
                        elif op in ('or','and','not'):
                            nuevaop = Logica(expi,expd,op);
                            if nuevaop.getval(entorno):
                                'Agrego la fila al resultado'
                                filtrado.append(datos[i])

                        else:
                            variables.consola.insert('Error el resultado del where no es booleano \n')
                    return filtrado

            else:
                variables.consola.insert('Error el nombre de las columnas es ambiguo \n')
        elif isinstance(self.where,Unaria):
            'busco columna y resulvo unaria'

        else:
            'ya veremos dijo el ciego'


    '''def group(self):
        'Ejecucucion del group'

    def having(self):
        'Ejecucucion del having'

    def order(self):
        'Ejecucucion del order'

    def limit(self):
        'Ejecucucion del limit'

    def combining(self):
        'Ejecucucion de combining'
    '''
