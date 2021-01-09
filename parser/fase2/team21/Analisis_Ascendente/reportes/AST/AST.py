from subprocess import check_call
#from Instrucciones.expresion import *
#from Instrucciones.instruccion import *
#from Instrucciones.Create.createTable import CreateTable
#from Instrucciones.Create.createDatabase import CreateReplace,ComplementoCR
#from Instrucciones.Select.select import Select, Limit, Having, GroupBy
#from Instrucciones.Select.union import Union
#from Instrucciones.Use_Data_Base.useDB import Use
#from Instrucciones.Time import  Time

direccion = "from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones"

from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Create.createTable import CreateTable,Acompaniamiento,Campo
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Create.createDatabase import CreateReplace,ComplementoCR
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.select import Select, Limit, Having,GroupBy
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select.union import Union
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Use_Data_Base.useDB import Use
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Time import  Time
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Insert.insert import InsertInto
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import IdAsId
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import  Math_
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario import  Binario
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Drop.drop import Drop
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Alter.alterDatabase import AlterDatabase
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Alter.alterTable import AlterTable
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Alter.alterTable import Alter
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Update.Update import Update
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Delete.delete import Delete
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Where import  Where
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Type.type import CreateType


#------------------------------------------------------------------------------------------------------
#--------------------------------------------FASE 2----------------------------------------------------
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Index.Index import Index
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Index.AsignacionF2 import AsignacionF2, Return
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Declaracion.Declaracion import Declaracion, AsignacionVariable
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.Function import Function
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Execute.Execute import Execute
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Procedure.Procedure import Procedure
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Procedure.Call import Call
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.Llamada import Llamada
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.Do import Do
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.Loop import Loop
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.For import For
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.While import While
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.If import SElseIf, SIF
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Sentencias_De_Control.Case import When, CaseF2

class AST:
    def __init__(self, sentencias):
        self.contador = 0
        self.c = ""
        self.sentencias = sentencias
        self.pe = 0

    def ReportarAST(self):
        print('Graficando AST....')
        #print(self.sentencias)
        f = open('AST.dot', 'w')
        self.c = 'digraph G{\n' 
        self.c += 'edge [color=blue]; rankdir = TB;\n'
        self.c += 'Nodo'+ str(self.contador)+ '[label="S"]\n'
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instrucciones"]\n' 
        self.c += 'Nodo' + '0' +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.TiposInstruccion(self.sentencias, str(self.contador))
        self.c += "}\n"
        #print(arbol)
        f.write(self.c)
        f.close()
        check_call(['dot', '-Tsvg', 'AST.dot', '-o', 'AST.svg'])

    def TiposInstruccion(self, inst, padre):
        if inst != None:
            for i in inst:
                if isinstance(i, CreateTable):
                    self.CreateTable(i, padre)
                elif isinstance(i, InsertInto):
                    self.InsertInto(i, padre)
                elif isinstance(i, CreateReplace):
                    self.CreateReplace(i, padre)
                elif isinstance(i, Show):
                    self.Show(padre)
                elif isinstance(i, AlterDatabase):
                    self.AlterDatabase(i, padre)
                elif isinstance(i, AlterTable):
                    self.AlterTable(i, padre)
                elif isinstance(i, Update):
                    self.Update(i, padre)
                elif isinstance(i, Delete):
                    self.Delete(i, padre)
                elif isinstance(i, Select):
                    self.Select(i, padre)
                elif isinstance(i, Union):
                    self.Union(i, padre)
                elif isinstance(i, Use):
                    self.Use(i, padre)
                elif isinstance(i, Drop):
                    self.Drop(i, padre)
                elif isinstance(i, CreateType):
                    self.CreateType(i, padre)
                #--------FASE 2--------------
                elif isinstance(i, Loop):
                    self.Loop(i, padre)
                elif isinstance(i, Do):
                    self.Do(i, padre)
                elif isinstance(i, Llamada):
                    self.Llamada(i, padre)
                elif isinstance(i, Call):
                    self.Call(i, padre)
                elif isinstance(i, Execute):
                    self.Execute(i, padre)
                elif isinstance(i, Procedure):
                    self.Procedure(i, padre)
                elif isinstance(i, Function):
                    self.Function(i, padre)
                elif isinstance(i, Declaracion):
                    self.Declaracion(i, padre)
                elif isinstance(i, AsignacionF2):
                    self.AsignacionF2(i, padre)
                elif isinstance(i, Return):
                    self.Return(i, padre)
                elif isinstance(i, Index):
                    self.Index(i, padre)
                elif isinstance(i, While):
                    self.While(i, padre)
                elif isinstance(i, For):
                    self.For(i, padre)
                elif isinstance(i, SIF):
                    self.SIF(i, padre)
                elif isinstance(i, CaseF2):
                    self.CaseF2(i, padre)

    
    def CreateTable(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: CREATE TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Id: ' + inst.id + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        #recorrer campos
        for campo in inst.campos:
            if isinstance(campo, Campo): 
                self.contador = self.contador + 1
                self.c += 'Nodo'+ str(self.contador)+ '[label="Campo"]\n' 
                self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                ncp = str(self.contador) 
                if campo.caso == 1:
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador)+ '[label="Id: ' + campo.id + '"]\n' 
                    self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    self.contador = self.contador + 1
                    if campo.tipo.longitud != None:
                        try:
                            self.c += 'Nodo'+ str(self.contador)+ '[label="Tipo: ' + campo.tipo.tipo + '(' + str(campo.tipo.longitud.valor) + ')' + '"]\n'
                        except:
                            self.c += 'Nodo' + str(self.contador) + '[label="Tipo: ' + campo.tipo.tipo + '(' + str(campo.tipo.longitud) + ')' + '"]\n'

                    else:
                        self.c += 'Nodo'+ str(self.contador)+ '[label="Tipo: ' + campo.tipo.tipo + '"]\n' 
                    self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    if campo.acompaniamiento != None:
                        for acom in campo.acompaniamiento:
                            self.contador = self.contador + 1
                            a = str(self.contador)
                            if acom.tipo == 'DEFAULT':
                                self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + ': '+ str(acom.valorDefault.valor) + '"]\n' 
                            elif acom.tipo == 'UNIQUE':
                                if acom.valorDefault != None:
                                    if isinstance(acom.valorDefault, Id):
                                        self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + ': ' + acom.valorDefault.id +'"]\n' 
                                    else:    
                                        self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + '"]\n'
                                        #listaId padre self.contador 
                                        self.listaID(acom.valorDefault, str(self.contador))
                                else:    
                                    self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + '"]\n' 
                            elif acom.tipo == 'CHECK':
                                self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + '"]\n'
                                if isinstance(acom.valorDefault, Expresion):
                                    self.E(acom.valorDefault, ncp)
                                else:
                                    self.listaID(acom.valorDefault, ncp)
                            else:
                                self.c += 'Nodo'+ str(self.contador)+ '[label="' + acom.tipo + '"]\n' 
                            self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ a + ';\n'
                if campo.caso == 2 or campo.caso == 3:
                    if campo.caso == 2:
                        self.contador = self.contador + 1
                        self.c += 'Nodo'+ str(self.contador)+ '[label="CONSTRAINT: ' + campo.id + '"]\n' 
                        self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    self.contador = self.contador + 1
                    a = str(self.contador)
                    if len(campo.idFk) == 1:
                        self.c += 'Nodo'+ str(self.contador)+ '[label="FOREIGN KEY: ' + campo.idFk[0].id + '"]\n' 
                    else:
                        self.c += 'Nodo'+ str(self.contador)+ '[label="FOREIGN KEY"]\n' 
                        self.listaID(campo.idFk, str(self.contador))
                    self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ a + ';\n'
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador)+ '[label="REFERENCES: ' + campo.tablaR + '"]\n' 
                    self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    self.contador = self.contador + 1
                    a = str(self.contador)
                    if len(campo.idR) == 1:
                        self.c += 'Nodo'+ str(self.contador)+ '[label="Columna: ' + campo.idR[0].id + '"]\n' 
                    else:
                        self.c += 'Nodo'+ str(self.contador)+ '[label="Columnas"]\n' 
                        self.listaID(campo.idR, str(self.contador))    
                    self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ a + ';\n'                     
                if campo.caso == 4:
                    self.contador = self.contador + 1
                    a = str(self.contador)
                    #if len(campo.id) == 1:
                     #   self.c += 'Nodo'+ str(self.contador)+ '[label="PRIMARY KEY: '+ campo.id +'"]\n' 
                    #else:
                    self.c += 'Nodo'+ str(self.contador)+ '[label="PRIMARY KEY"]\n' #
                    self.listaID(campo.id, str(self.contador))#
                    self.c += 'Nodo' + ncp +' -> ' + 'Nodo'+ a + ';\n'
        if inst.idInherits != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="INHERITS: '+ inst.idInherits +'"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def InsertInto(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: INSERT INTO"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Table: ' + inst.id + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        if inst.listaId != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="Columnas"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.listaID(inst.listaId, str(self.contador))  
           # self.contador = self.contador + 1
            #self.c += 'Nodo'+ str(self.contador)+ '[label="Values"]\n' 
            #self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            
        #if len(inst.values) == 1:
         #   self.listaID(inst.values[0], str(self.contador))
        #else:
            #for val in inst.values:
        if inst.values != None:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="Value"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            self.listaID(inst.values, str(self.contador))          

    def CreateReplace(self, inst, padre):
        label = ""
        if inst.caso == 1: 
            label = 'CREATE'
        elif inst.caso == 2:
            label = 'CREATE OR REPLACE'
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: '+label+'"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        if inst.exists:
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="IF NOT EXISTS"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.id + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        if inst.complemento != None:
            if isinstance(inst.complemento, ComplementoCR):
                self.contador = self.contador + 1
                self.c += 'Nodo'+ str(self.contador)+ '[label="OWNER: ' + inst.complemento.idOwner + '"]\n' 
                self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                if inst.complemento.mode != None:
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador)+ '[label="MODE: ' + str(inst.complemento.mode) + '"]\n' 
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def Show(self, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: SHOW DATABASES"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        
    def AlterDatabase(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER DATABASE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.name + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        label = ""
        if inst.caso == 1: 
            label = 'RENAME'
        elif inst.caso == 2:
            label = 'OWNER'
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + label + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador = self.contador + 1
        if isinstance(inst.newName, Primitivo):
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.newName.valor + '"]\n' 
        elif isinstance(inst.newName, Id):
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.newName.id + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

    def AlterTable(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: ALTER TABLE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Tabla: ' + inst.id + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        for alt in inst.alter:
            if isinstance(alt, Alter):
                print('es alter')
                self.Alter(alt, np)

    def Alter(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="ALTER"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.accion + inst.ccc + '"]\n' 
        self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        if inst.accion == 'ADD':
            if inst.ccc == ' COLUMN':
                self.listaID(inst.id, str(self.contador))    
                self.contador = self.contador + 1
                label = inst.tipo.tipo
                if inst.tipo.longitud != None:
                    label += '(' + str(inst.tipo.longitud.valor) + ')'
                self.c += 'Nodo'+ str(self.contador)+ '[label="Tipo: ' + label + '"]\n' 
                self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            elif inst.ccc == ' CONSTRAINT':
                self.Id(inst.id, np) 
            elif inst.ccc == ' CHECK':
                if isinstance(inst.check, Expresion):
                    self.E(inst.check, str(self.contador))
                else: #lista de valores
                    self.listaID(inst.check, str(self.contador))
            elif inst.ccc == ' FOREIGN KEY':
                    self.listaID(inst.id, str(self.contador))
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador)+ '[label="REFERENCES: ' + inst.id2 + '"]\n' 
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador)+ '[label="Columnas"]\n' 
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    self.listaID(inst.id3, str(self.contador)) 
        elif inst.accion == 'DROP':
            self.listaID(inst.id, str(self.contador))
        elif inst.accion == 'ALTER':
            self.Id(inst.id, np)
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.typeSet + '"]\n' 
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            if inst.tipo != None:
                self.contador = self.contador + 1
                self.c += 'Nodo'+ str(self.contador)+ '[label="Tipo: ' + str(inst.tipo) + '"]\n'
                self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        elif inst.accion == 'UNIQUE':
            self.Id(inst.id, np)
        elif inst.accion == 'PRIMARY':
            self.listaID(inst.id, str(self.contador))


    def Update(self, inst, padre):
        self.contador = self.contador + 1
        self.c += 'Nodo'+ str(self.contador)+ '[label="Instruccion: UPDATE"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        self.CrearNodo('Table: ' + inst.id, np)
        self.CrearNodo('SET', np)
        for asign in inst.asignaciones:
            if isinstance(asign, Expresion):
                if asign.operador == '=':
                    self.Asignacion(asign, np)
        if inst.where != None:
            self.CrearNodo('WHERE', np)
            #where
            #puede ser expresion, primitivo o where
            if isinstance(inst.where, Expresion):#asignacion, andOr
                self.E(inst.where, np)
            elif isinstance(inst.where, Primitivo):
                self.Primitivo(inst.where, np)
            elif isinstance(inst.where, Where):
                self.Where(inst.where, np)

    def Delete(self, inst, padre):
        self.CrearNodo('Instruccion: Delete', padre)
        np = str(self.contador)
        self.CrearNodo('Table: ' + inst.id, np)
        if inst.where != None:
            self.CrearNodo('WHERE', np)
            #where
            #puede ser expresion, primitivo o where
            if isinstance(inst.where, Expresion):#asignacion, andOr
                self.E(inst.where, np)
            elif isinstance(inst.where, Primitivo):
                self.Primitivo(inst.where, np)
            elif isinstance(inst.where, Where):
                self.Where(inst.where, np)


    def Select(self, inst, padre):
        self.CrearNodo('Instruccion: Select', padre)
        np = str(self.contador)
        if inst.distinct:
            self.CrearNodo('DISTINCT', np)
        if inst.time != None:
            #select time ;
            self.Time(inst.time, np)
        if inst.columnas != None:
            if inst.columnas == '*':
                self.CrearNodo('*', np)
            else:
                self.Columnas(inst.columnas, np)
        if inst.subquery != None:
            self.CrearNodo('FROM', np)
            self.Select(inst.subquery, np)
        if inst.inner != None:
            if inst.subquery == None:
                self.CrearNodo('FROM', np)
            #puede ser un GroupBy o una lista de columnas, por esta fase
            if isinstance(inst.inner, GroupBy):
                print('group by')
                if inst.inner.listaC != None:
                    self.Columnas(inst.inner.listaC, np)
                self.CrearNodo('GROUP BY', np)
                #es Having si andOr != None
                #inst.inner.compGroup
                if isinstance(inst.inner.compGroup, Having):
                    self.Columnas(inst.inner.compGroup.lista, np)
                    if inst.inner.compGroup.ordenar != None:
                        self.CrearNodo(inst.inner.compGroup.ordenar, np)
                    if inst.inner.compGroup.andOr != None:
                        self.CrearNodo('HAVING', np)
                        #where | andOr
                        #puede ser expresion, primitivo o where
                        if isinstance(inst.inner.compGroup.andOr, Expresion):#asignacion, andOr
                            self.E(inst.inner.compGroup.andOr, np)
                        elif isinstance(inst.inner.compGroup.andOr, Primitivo):
                            self.Primitivo(inst.inner.compGroup.andOr, np)
                        elif isinstance(inst.inner.compGroup.andOr, Where):
                            self.Where(inst.inner.compGroup.andOr, np)
            else:
                self.Columnas(inst.inner, np)
        #where
        #es expresion andOr
        #primitivo
        #where
        #GroupBy
        if inst.complementS != None:
            self.CrearNodo('WHERE', np)
            if isinstance(inst.complementS, Expresion):#asignacion, andOr
                self.E(inst.complementS, np)
            elif isinstance(inst.complementS, Primitivo):
                self.Primitivo(inst.complementS, np)
            elif isinstance(inst.complementS, Where):
                self.Where(inst.complementS, np)
            elif isinstance(inst.complementS, GroupBy):
                #where
                if isinstance(inst.complementS.listaC, Expresion):#asignacion, andOr
                    self.E(inst.complementS.listaC, np)
                elif isinstance(inst.complementS.listaC, Primitivo):
                    self.Primitivo(inst.complementS.listaC, np)
                elif isinstance(inst.complementS.listaC, Where):
                    self.Where(inst.complementS.listaC, np)

                self.CrearNodo('GROUP BY', np)
                if isinstance(inst.complementS.compGroup, Having):
                    self.Columnas(inst.complementS.compGroup.lista, np)
                    if inst.complementS.compGroup.ordenar != None:
                        self.CrearNodo(inst.complementS.compGroup.ordenar, np)
                    if inst.complementS.compGroup.andOr != None:
                        self.CrearNodo('HAVING', np)
                        #where | andOr
                        #puede ser expresion, primitivo o where
                        if isinstance(inst.complementS.compGroup.andOr, Expresion):#asignacion, andOr
                            self.E(inst.complementS.compGroup.andOr, np)
                        elif isinstance(inst.complementS.compGroup.andOr, Primitivo):
                            self.Primitivo(inst.complementS.compGroup.andOr, np)
                        elif isinstance(inst.complementS.compGroup.andOr, Where):
                            self.Where(inst.complementS.compGroup.andOr, np)
                if inst.complementS.ordenar != None:
                    self.CrearNodo(inst.complementS.ordenar, np)
        if inst.orderby != None:
            self.CrearNodo('ORDER BY', np)
            self.listaID(inst.orderby, np)
        if inst.limit != None:
            self.CrearNodo('LIMIT', np) 
            self.Limit(inst.limit, np)

    def Limit(self, inst, padre):
        if inst.all:
            self.CrearNodo('ALL', padre)
        if inst.e1 != None:
            self.CrearNodo(inst.e1, padre)
        if inst.e2 != None:
            self.CrearNodo('OFFSET', padre)
            self.CrearNode(inst.e2, padre)

    def Union(self, inst, padre):
        self.CrearNodo('Instruccion: Combinar Queries', padre)
        np = str(self.contador)
        self.Select(inst.q1, np)
        self.CrearNodo(inst.tipo, np)
        if inst.all:
            self.CrearNodo('ALL', np)
        self.Select(inst.q2, np)

    def Use(self, inst, padre):
        self.CrearNodo('Instruccion: USE DATABASE', padre)
        self.CrearNodo(inst.id, str(self.contador))

    def Drop(self, inst, padre):
        self.CrearNodo('Instruccion: Drop', padre)
        np = str(self.contador)
        if inst.caso == 1:
            self.CrearNodo('DATABASE', np)
        else:
            self.CrearNodo('TABLE', np)
        if inst.exists:
            self.CrearNodo('IF EXISTS', np)
        self.CrearNodo(inst.id, np)

#---------------------WHERE----------------------------------------
    def Where(self, inst, padre):
        #caso, boolean, columna, listaValores, valor1, valor2, comparison
        print('-----------------------WHERE')
        self.CrearNodo('WHERE', padre)
        np = str(self.contador)
        if inst.caso == 1:
            self.CrearNodo('NOT', np)
            if isinstance(inst.boolean, Primitivo):
                self.CrearNodo(inst.boolean.valor, np)
            elif isinstance(inst.boolean, Expresion):
                self.E(inst.boolean, np)
        elif inst.caso == 2:
            self.Columna(inst.columna, np)
            self.CrearNodo('IN', np)
            if isinstance(inst.listaValores, Select):
                self.Select(inst.listaValores, np)
            else:
                self.listaID(inst.listaValores, np)
        elif inst.caso == 3:
            self.Columna(inst.columna, np)
            self.CrearNodo('BETWEEN', np)
            self.Valor(inst.valor1, np)
            self.CrearNodo('AND', np)
            self.Valor(inst.valor2, np)
        elif inst.caso == 4:
            self.Columna(inst.columna, np)
            self.CrearNodo('ILIKE', np)
            self.Valor(inst.valor1, np)
        elif inst.caso == 5:
            self.Columna(inst.columna, np)
            self.CrearNodo('LIKE', np)
            self.Valor(inst.valor1, np)
        elif inst.caso == 6:
            if isinstance(inst.valor1, Expresion):
                self.E(inst.valor1, np)
            elif isinstance(inst.valor1, Primitivo):
                self.CrearNodo(inst.valor1.valor, np)
            else:
                self.Columna(inst.valor1, np)
            self.Comparison(inst.comparison, np)
        elif inst.caso == 7:
            self.Columna(inst.columna, np)
            self.CrearNodo('IS NOT DISTINCT FROM', np)
            self.Valor(inst.valor1, np)
        elif inst.caso == 8:
            self.Columna(inst.columna, np)
            self.CrearNodo('IS DISTINCT FROM', np)
            self.Valor(inst.valor1, np)
        elif inst.caso == 9:
            self.Columna(inst.columna, np)
            self.CrearNodo('NOT IN', np)
            if isinstance(inst.listaValores, Select):
                self.Select(inst.listaValores, np)
            else:
                self.listaID(inst.listaValores, np)
        elif inst.caso == 10:
            self.CrearNodo('NOT EXISTS', np)
            if isinstance(inst.listaValores, Select):
                self.Select(inst.listaValores, np)
            else:
                self.listaID(inst.listaValores, np)
        elif inst.caso == 11:
            self.CrearNodo('EXISTS', np)
            if isinstance(inst.listaValores, Select):
                self.Select(inst.listaValores, np)
            else:
                self.listaID(inst.listaValores, np)


#---------------------COMPARISON
    def Comparison(self, num, padre):
        if num == 1:
            self.CrearNodo('IS TRUE', padre)
        elif num == 2:
            self.CrearNodo('IS FALSE', padre)
        elif num == 3:
            self.CrearNodo('IS UNKNOWN', padre)
        elif num == 4:
            self.CrearNodo('IS NOT TRUE', padre)
        elif num == 5:
            self.CrearNodo('IS NOT FALSE', padre)
        elif num == 6:
            self.CrearNodo('IS NOT UNKNOWN', padre)
        elif num == 7:
            self.CrearNodo('IS NULL', padre)
        elif num == 8:
            self.CrearNodo('IS NOT NULL', padre)
        elif num == 9:
            self.CrearNodo('NOTNULL', padre)
        elif num == 10:
            self.CrearNodo('ISNULL', padre)


#---------------------LISTAS----------------------------------------
#es una lista de entero, decimal, cadena, id, time, expresion
    def listaID(self, inst, padre):
        for var in inst:
            #modificacion, pasa esto a metodo Valor
            self.Valor(var, padre)

    def Valor(self, var, padre):
        if isinstance(var, Id):
            self.contador += self.contador
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + var.id + '"]\n' 
            self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        elif isinstance(var, IdId):
            self.CrearNodo(var.id1.id + '.' + var.id2.id, padre)
        elif isinstance(var, Primitivo):
            self.contador += self.contador
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + str(var.valor) + '"]\n' 
            self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        elif isinstance(var, Time):
            self.Time(var, padre)
        elif isinstance(var, Math_):
            self.Math_(var, padre)
        elif isinstance(var, Trigonometrica):
            self.Trig(var, padre)
        elif isinstance(var, Binario):
            self.Binario(var, padre)
        #para que tambien sea lista de expresiones
        elif isinstance(var, Expresion):
            self.E(var, padre)
        elif isinstance(var, Llamada):
            self.Llamada(var, padre)


    def Columnas(self, inst, padre):
        self.CrearNodo('Columnas', padre)
        np = str(self.contador)
        for col in inst:
            #modificacion, pasa esto a metodo Columna
            self.Columna(col, np)

    def Columna(self, col, padre):
        self.CrearNodo('Columna', padre)
        np = str(self.contador)
        if isinstance(col, Select):
            self.Select(col, np)
        elif isinstance(col, Time):
            self.Time(col, np)
        elif isinstance(col, IdId):
            self.CrearNodo(col.id1.id + '.' + col.id2.id, np)
        elif isinstance(col, Id):
            self.CrearNodo(col.id, np)
        elif isinstance(col, IdAsId):
            self.IdAsId(col, np)
        elif isinstance(col, Math_):
            self.Math_(col, np)
        elif isinstance(col, Trigonometrica):
            self.Trig(col, np)
        elif isinstance(col, Binario):
            self.Binario(col, np)
        elif isinstance(col, ColCase):
            self.ColCase(col, np)

    def IdAsId(self, inst, padre):
        self.CrearNodo('Alias', padre)
        np = str(self.contador)
        #id1
        if isinstance(inst.id1, Time):
            self.Time(inst.id1, np)
        elif isinstance(inst.id1, Select):
            self.Select(inst.id1, np)
        elif isinstance(inst.id1, Id):
            self.CrearNodo(inst.id1.id, np)
        elif isinstance(inst.id1, IdId):
            self.CrearNodo(inst.id1.id1.id + '.' + inst.id1.id2.id, np)
        elif isinstance(inst.id1, Math_):
            self.Math_(inst.id1, np)
        elif isinstance(inst.id1, Trigonometrica):
            self.Trig(inst.id1, np)
        #elif isinstance(inst.id1, Binario):
         #   self.Binario(col, np)
        #id2
        if isinstance(inst.id2, Id):
            self.CrearNodo(inst.id2.id, np)
        elif isinstance(inst.id2, Primitivo):
            self.Primitivo(inst.id2, np)

    def ColCase(self, inst, padre):
        self.CrearNodo('CASE', padre)
        for case in inst.cases:
            if isinstance(case, Case):
                self.CrearNodo('case', padre)
                np = str(self.contador)
                self.CrearNodo('WHEN', np)
                self.E(case.asignacion, np)
                self.CrearNodo('THEN', np)
                self.Valor(case.valor, np)
        self.CrearNodo('END', padre)
        self.Valor(inst.id, padre)

    def Math_(self, inst, padre):
        self.CrearNodo('Math', padre)
        np = str(self.contador)
        self.CrearNodo(inst.nombre, np)
        if inst.E1 != None:
            print(inst.E1)
            if isinstance(inst.E1, Id):
                self.Id(inst.E1.id, np)
                print('es id')
            elif isinstance(inst.E1, Primitivo):
                self.Primitivo(inst.E1, np)
            elif isinstance(inst.E1, IdId):
                self.CrearNodo(inst.E1.id1 + '.' + inst.E1.id2, np)
            elif isinstance(inst.E1,list):
                self.listaID(inst.E1,np)

            #elif isinstance(inst.E1, Expresion):
            else:
                self.E(inst.E1, np)
        if inst.E2 != None:
            print(inst.E2)
            if isinstance(inst.E2, Id):
                self.Id(inst.E2.id, np)
                print('es id')
            elif isinstance(inst.E2, Primitivo):
                self.Primitivo(inst.E2, np)
            elif isinstance(inst.E2, IdId):
                self.CrearNodo(inst.E2.id1 + '.' + inst.E2.id2, np)
            #elif isinstance(inst.E2, Expresion):
            else:
                self.E(inst.E2, np)

    def Trig(self, inst, padre):
        self.CrearNodo('Trigonometrica', padre)
        np = str(self.contador)
        self.CrearNodo(inst.trig, np)
        if inst.E != None:
            self.E(inst.E, np)

    def Binario(self, inst, padre):
        self.CrearNodo('Binario', padre)
        np = str(self.contador)
        if inst.caso == 1:
            self.CrearNodo('LENGTH', np)
        elif inst.caso == 2:
            self.CrearNodo('SHA256', np)
        elif inst.caso == 3:
            self.CrearNodo('ENCODE', np)
        elif inst.caso == 4:
            self.CrearNodo('DECODE', np)
        if inst.caso == 1 | inst.caso == 2 | inst.caso == 3 | inst.caso == 4:
            self.E(inst.valor1, np)
        if inst.caso == 5:
            self.CrearNodo('SUBSTRING', np)
            self.Valor(inst.valor1, np)
            self.CrearNodo(',', np)
            self.Valor(inst.valor2, np)
            self.CrearNodo(',', np)
            self.Valor(inst.valor3, np)
        elif inst.caso == 6:
            self.CrearNodo('TRIM', np)
            self.Valor(inst.valor1, np)
            self.CrearNodo('FROM', np)
            self.Columna(inst.valor2, np)
        elif inst.caso == 7:
            self.CrearNodo('GET_BYTE', np)
            self.Valor(inst.valor1, np)
            self.CrearNodo(',', np)
            self.Valor(inst.valor2, np)
        elif inst.caso == 8:
            self.CrearNodo('SET_BYTE', np)
            self.Valor(inst.valor1, np)
            self.CrearNodo(',', np)
            self.Valor(inst.valor2, np)
            self.CrearNodo(',', np)
            self.Valor(inst.valor3, np)
        elif inst.caso == 9:
            self.CrearNodo('CONVERT', np)
            self.Valor(inst.valor1, np)
            self.CrearNodo('AS', np)
            if inst.valor2.longitud != None:
                self.CrearNodo('Tipo: ' + inst.valor2.tipo + '(' + str(inst.valor2.longitud.valor) + ')', np)
            else:
                self.Columna('Tipo: ' + inst.valor2.tipo, np)
        elif inst.caso == 10:
            self.CrearNodo('GREATEST', np)
            self.listaID(inst.valor1, np)
        elif inst.caso == 11:
            self.CrearNodo('LEAST', )
            self.listaID(inst.valor1, np)

#EXPRESION
    def E(self, inst, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="E"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        np = str(self.contador)
        eiz = False
        edr = False
        prim = False
        prim2 = False
        print('expresion')
        if isinstance(inst, Unario):
            print('unario')
            print(inst)
            print(inst.op)
            print(inst.operador)
            self.contador = self.contador + 1
            self.c += 'Nodo'+ str(self.contador) + '[label="Operador\nUnario: '+str(inst.operador)+' "]\n'
            self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            npu = str(self.contador)
            if isinstance(inst.op, Primitivo):
                self.Primitivo(inst.op, npu)
            if isinstance(inst.op, Id):
                self.Id(inst.op.id, npu)
            if isinstance(inst.op, IdId):
                self.CrearNodo(inst.op.id1.id + '.' + inst.op.id2.id, npu)
            if isinstance(inst.op, Expresion):
                self.E(inst.op, npu)
                ##########
            if isinstance(inst.op, Unario):
                print('UNARIO-----')
                self.E(inst.op, npu)
        elif isinstance(inst, Primitivo):
            self.Primitivo(inst, np)
        elif isinstance(inst, IdId):
            self.CrearNodo(inst.id1.id + '.' + inst.id2.id, np)
        elif isinstance(inst, Id):
            self.Id(inst.id, np)
        elif isinstance(inst, Time):
            self.Time(inst, np)
        elif isinstance(inst, Math_):
            self.Math_(inst, np)
        elif isinstance(inst, Trigonometrica):
            self.Trig(inst, np)
        elif isinstance(inst, Binario):
            self.Binario(inst, np)
        elif isinstance(inst, Where):
            self.Where(inst, np)
        #------------FASE 2
        elif isinstance(inst, Llamada):
            self.Llamada(inst, np)
        else : #expresion iz operador dr
            print('no unario')
            try:
                if isinstance(inst.iz, Unario):
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador) + '[label="Operador\nUnario: '+inst.iz.operador+' "]\n'
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    npu = str(self.contador)
                    if isinstance(inst.iz.op, Primitivo):
                        self.Primitivo(inst.iz.op, npu)
                    if isinstance(inst.iz.op, Id):
                        self.Id(inst.iz.op.id, npu)
                    if isinstance(inst.iz.op, IdId):
                        self.CrearNodo(inst.iz.op.id1.id + '.' + inst.iz.op.id2.id, npu)
                    if isinstance(inst.iz.op, Expresion):
                        self.E(inst.iz.op, npu)
                    if isinstance(inst.iz.op, Unario):
                        self.E(inst.iz.op, npu)
                    self.contador += self.contador
                    self.c += 'Nodo'+ str(self.contador) + '[label="Operador: ' + inst.operador+'"]\n'
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                if isinstance(inst.dr, Unario):
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador) + '[label="Operador\nUnario: '+inst.dr.operador+' "]\n'
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    npu = str(self.contador)
                    if isinstance(inst.dr.op, Primitivo):
                        self.Primitivo(inst.dr.op, npu)
                    if isinstance(inst.dr.op, Id):
                        self.Id(inst.dr.op.id, npu)
                    if isinstance(inst.dr.op, IdId):
                        self.CrearNodo(inst.dr.op.id1.id + '.' + inst.dr.op.id2.id, npu)
                    if isinstance(inst.dr.op, Expresion):
                        self.E(inst.dr.op, npu)
                    if isinstance(inst.dr.op, Unario):
                        self.E(inst.dr.op, npu)
                if isinstance(inst.iz, Primitivo):
                    self.contador += self.contador
                    self.c += 'Nodo'+ str(self.contador) + '[label="Primitivo: ' + str(inst.iz.valor) + '"]\n'
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador) + '[label="Operador: ' + inst.operador+'"]\n'
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    prim = True
                if isinstance(inst.dr, Primitivo):
                    self.contador += self.contador
                    self.c += 'Nodo'+ str(self.contador) + '[label="Primitivo: ' + str(inst.dr.valor) + '"]\n'
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    prim2 = True
                if isinstance(inst.iz, Id):
                    self.Id(inst.iz.id, np)
                    self.contador = self.contador + 1
                    self.c += 'Nodo'+ str(self.contador) + '[label=" Operador: ' + inst.operador+'"]\n'
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    prim = True
                if isinstance(inst.dr, Id):
                    self.Id(inst.dr.id, np)
                    prim2 = True
                if isinstance(inst.iz, IdId):
                    self.CrearNodo(inst.iz.id1.id + '.' + inst.iz.id2.id, np)
                    self.CrearNodo('Operador: ' + inst.operador, np)
                if isinstance(inst.dr, IdId):
                    self.CrearNodo(inst.dr.id1.id + '.' + inst.dr.id2.id, np)
                if isinstance(inst.iz, Expresion):
                    print('expresion iz')
                    self.E(inst.iz, np)
                    self.contador += self.contador
                    self.c += 'Nodo'+ str(self.contador) + '[label="Operador: ' + inst.operador+'"]\n'
                    self.c += 'Nodo' + np +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
                    eiz = True
                if isinstance(inst.dr, Expresion):
                    self.E(inst.dr, np)
                    diz = True
                if isinstance(inst.iz, Where):
                    self.Where(inst.iz, np)
                    self.CrearNodo(inst.operador, np)
                if isinstance(inst.dr, Where):
                    self.Where(inst.dr, np)
                if isinstance(inst.iz, Math_):
                    self.Math_(inst.iz, np)
                    self.CrearNodo('Operador: ' + inst.operador, np)
                if isinstance(inst.dr, Math_):
                    self.Math_(inst.dr, np)
                if isinstance(inst.iz, Trigonometrica):
                    self.Trig(inst.iz, np)
                    self.CrearNodo('Operador: ' + inst.operador, np)
                if isinstance(inst.dr, Trigonometrica):
                    self.Trig(inst.dr, np)
                if isinstance(inst.iz, Time):
                    self.Time(inst.iz, np)
                    self.CrearNodo('Operador: ' + inst.operador, np)
                if isinstance(inst.dr, Time):
                    self.Time(inst.dr, np)
                if isinstance(inst.iz, Binario):
                    self.Binario(inst.iz, np)
                    self.CrearNodo('Operador: ' + inst.operador, np)
                if isinstance(inst.dr, Binario):
                    self.Binario(inst.dr, np)
            except:
                print("")
    def Id(self, id, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="Id: ' + id + '"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            
    def Primitivo(self, prim, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + str(prim.valor) + '"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
            
    def Unario(self, unario, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + unario.operador + '"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        a = str(self.contador)
        #self.contador += self.contador#
        print('UNARIO')
        #if isinstance(unario.op, Id):
         #   print(unario.op)
          #  self.c += 'Nodo'+ str(self.contador)+ '[label="' + unario.op.id + '"]\n' 
        #elif isinstance(unario.op, Primitivo):
         #   print(unario.op)
          #  self.c += 'Nodo'+ str(self.contador)+ '[label="' + str(unario.op.val) + '"]\n' 
        #elif isinstance(unario.op, IdId):
         #   pass
        # self.c += 'Nodo' + a +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        
        #es una expresion
        self.E(unario.op, a)    
        
#ASIGNACION
    def Asignacion(self, inst, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="Asignacion"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        padre = str(self.contador)
        self.contador += self.contador
        if isinstance(inst.iz, Id):
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + inst.iz.id + '"]\n' 
        if isinstance(inst.iz, IdId):
            self.c += 'Nodo'+ str(self.contador)+ '[label="' + str(inst.iz.id1.id) + '.' + str(inst.iz.id2.id) + '"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="="]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        #self.contador += self.contador
        #self.c += 'Nodo'+ str(self.contador)+ '[label="E"]\n' 
        #self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'
        self.E(inst.dr, padre)

    def CrearNodo(self, label, padre):
        self.contador += self.contador
        self.c += 'Nodo'+ str(self.contador)+ '[label="' + label + '"]\n' 
        self.c += 'Nodo' + padre +' -> ' + 'Nodo'+ str(self.contador) + ';\n'

        
    def Time(self, inst, padre):
        self.CrearNodo('Time', padre)
        np = str(self.contador)
        if inst.caso == 1:
            self.CrearNodo('EXTRACT', np)
            self.CrearNodo(inst.momento, np)
            self.CrearNodo('FROM TIMESTAMP', np)
            self.CrearNodo(inst.cadena, np)
        elif inst.caso == 2:
            self.CrearNodo('NOW', np)
        elif inst.caso == 3:
            self.CrearNodo('date_part', np)
            self.CrearNodo(inst.cadena, np)
            self.CrearNodo('INTERVAL', np)
            self.CrearNodo(inst.cadena2, np)
        elif inst.caso == 4:
            self.CrearNodo('CURRENT_DATE', np)
        elif inst.caso == 5:
            self.CrearNodo('CURRENT_TIME', np)
        elif inst.caso == 6:
            self.CrearNodo('TIMESTAMP', np)
            self.CrearNodo(inst.cadena, np)


    def CreateType(self, inst, padre):
        self.CrearNodo('Instruccion: CREATE TYPE', padre)
        np = str(self.contador)
        self.CrearNodo('CREATE TYPE', np)
        self.CrearNodo(inst.id, np)
        self.CrearNodo('AS ENUM', np)
        self.listaID(inst.lista, np)

# ------------------------------------------------------------------------------------------------------
# --------------------------------------------FASE 2----------------------------------------------------

    def Loop(self, inst, padre):
        self.CrearNodo('Instruccion: LOOP', padre)
        np = str(self.contador)
        self.CrearNodo('LOOP', np)
        self.CrearNodo('Instrucciones', np)
        np2 = str(self.contador)
        self.TiposInstruccion(inst.instrucciones, np2)
        self.CrearNodo('END LOOP', np)

    def Do(self, inst, padre):
        self.CrearNodo('Instruccion: DO', padre)
        np = str(self.contador)
        self.CrearNodo('DO', np)
        self.E(inst.E, np)
        if inst.declareInst != None:
            self.CrearNodo('DECLARE', np)
            self.TiposInstruccion(inst.declareInst, np)
        self.CrearNodo('BEGIN', np)
        self.TiposInstruccion(inst.beginInst, np)
        self.CrearNodo('END', np)

    def Llamada(self, inst, padre):
        self.CrearNodo('Instruccion: LLAMADA A FUNCION', padre)
        np = str(self.contador)
        if inst.caso == 2:
            self.CrearNodo(inst.id + '()', np)
        elif inst.caso == 1:
            self.CrearNodo(inst.id, np)
            self.CrearNodo('PARAMETROS', np)
            np = str(self.contador)
            self.listaID(inst.listaE, np)

    def Call(self, inst, padre):
        self.CrearNodo('INSTRUCCION: CALL', padre)
        np = str(self.contador)
        if inst.caso == 2:
            self.CrearNodo(inst.id + '()', np)
        elif inst.caso == 1:
            self.CrearNodo(inst.id, np)
            self.CrearNodo('PARAMETROS', np)
            np = str(self.contador)
            self.listaID(inst.listaE, np)

    def Execute(self, inst, padre):
        self.CrearNodo('INSTRUCCION: EXECUTE', padre)
        np = str(self.contador)
        if inst.caso == 2:
            self.CrearNodo(inst.id + '()', np)
        elif inst.caso == 1:
            self.CrearNodo(inst.id, np)
            self.CrearNodo('PARAMETROS', np)
            np = str(self.contador)
            self.listaID(inst.listaE, np)

    def Procedure(self, inst, padre):
        self.CrearNodo('Instruccion: PROCEDURE', padre)
        np = str(self.contador)
        if inst.replace:
            self.CrearNodo('CREATE OR REPLACE PROCEDURE', np)
        else:
            self.CrearNodo('CREATE PROCEDURE', np)
        self.CrearNodo(inst.id, np)
        if inst.parametros != None and len(inst.parametros) != 0:
            if len(inst.parametros) == 1:
                if inst.parametros[0] != None:
                    print(inst.parametros)
                    self.CrearNodo('PARAMETROS', np)
                    np2 = str(self.contador)
                    self.Parametros(inst.parametros, np2)
            else:
                print(inst.parametros)
                self.CrearNodo('PARAMETROS', np)
                np2 = str(self.contador)
                self.Parametros(inst.parametros, np2)
        self.CrearNodo('LANGUAGE', np)
        self.E(inst.languageE, np)
        self.CrearNodo('AS', np)
        self.E(inst.asE, np)
        if inst.caso == 1:
            self.CrearNodo('Instrucciones', np)
            np2 = str(self.contador)
            self.TiposInstruccion(inst.inst, np2)
            self.CrearNodo(inst.id2, np)
        elif inst.caso == 2:
            self.CrearNodo('DECLARE', np)
            self.CrearNodo('Instrucciones', np)
            np2 = str(self.contador)
            self.TiposInstruccion(inst.declareInst, np2)
            self.CrearNodo('BEGIN', np)
            self.CrearNodo('Instrucciones', np)
            np2 = str(self.contador)
            self.TiposInstruccion(inst.beginInst, np2)
            self.CrearNodo('END', np)
        elif inst.caso == 3:
            self.CrearNodo('BEGIN', np)
            self.CrearNodo('Instrucciones', np)
            np2 = str(self.contador)
            self.TiposInstruccion(inst.beginInst, np2)
            self.CrearNodo('END', np)

#--------------------------Parametros--------------------------------------
    def Parametros(self, listap, padre):
        if len(listap) != 0 and listap != None:
            for param in listap:
                if isinstance(param, Parametro):
                    self.CrearNodo('PARAMETRO', padre)
                    np = str(self.contador)
                    self.Parametro(param, np)

    def Parametro(self, param, padre):
        self.CrearNodo(param.id, padre)
        if isinstance(param.tipo, Tipo):
            self.CrearNodo(param.tipo.tipo, padre)
            if param.tipo.longitud != None:
                self.CrearNodo(str(param.tipo.longitud.valor), padre)
#--------------------------------------------------------------------------

    def Function(self, inst, padre):
        self.CrearNodo('Instruccion: FUNCTION', padre)
        np = str(self.contador)
        if inst.replace:
            self.CrearNodo('CREATE OR REPLACE FUNCTION', np)
        else:
            self.CrearNodo('CREATE FUNCTION', np)
        self.CrearNodo(inst.id, np)
        if inst.parametros != None and len(inst.parametros) != 0:
            if len(inst.parametros) == 1:
                if inst.parametros[0] != None:
                    print(inst.parametros)
                    self.CrearNodo('PARAMETROS', np)
                    np2 = str(self.contador)
                    self.Parametros(inst.parametros, np2)
            else:
                print(inst.parametros)
                self.CrearNodo('PARAMETROS', np)
                np2 = str(self.contador)
                self.Parametros(inst.parametros, np2)
        self.CrearNodo('RETURNS', np)
        if isinstance(inst.tipo, Tipo):
            self.CrearNodo(inst.tipo.tipo, np)
        self.CrearNodo('AS', np)
        self.E(inst.E, np)
        if inst.declareInst != None:
            self.CrearNodo('DECLARE', np)
            self.CrearNodo('Instrucciones', np)
            np2 = str(self.contador)
            self.TiposInstruccion(inst.declareInst, np2)
        self.CrearNodo('BEGIN', np)
        self.CrearNodo('Instrucciones', np)
        np2 = str(self.contador)
        self.TiposInstruccion(inst.beginInst, np2)
        self.CrearNodo('END', np)

    def Declaracion(self, inst, padre):
        self.CrearNodo('Instruccion: DECLARACION', padre)
        np = str(self.contador)
        self.CrearNodo(inst.id, np)
        if inst.constant:
            self.CrearNodo('CONSTANT', np)
        if isinstance(inst.tipo, Tipo):
            self.CrearNodo(inst.tipo.tipo, np)
        if inst.colate != None:
            self.CrearNodo(inst.colate, np)
        if inst.notnull:
            self.CrearNodo('NOTNULL', np)
        if isinstance(inst.asignacionv, AsignacionVariable):
            self.AsginacionVar(inst.asignacionv, np)

#-------------ASIGNACION VARIABLE----------------------
    def AsginacionVar(self, inst, padre):
        if inst.caso == 1:
            self.CrearNodo('DEFAULT', padre)
        elif inst.caso == 2:
            self.CrearNodo('=', padre)
        elif inst.caso == 3:
            self.CrearNodo(':=', padre)
        self.E(inst.E, padre)

    def AsignacionF2(self, inst, padre):
        self.CrearNodo('Instruccion: ASIGNACION', padre)
        np = str(self.contador)
        self.CrearNodo(inst.id, np)
        if inst.caso == 1:
            self.CrearNodo(':=', np)
        elif inst.caso == 2:
            self.CrearNodo('=', np)
        self.E(inst.E, np)

    def Return(self, inst, padre):
        self.CrearNodo('Instruccion: RETURN', padre)
        np = str(self.contador)
        self.E(inst.E, np)

    def Index(self, inst, padre):
        self.CrearNodo('Instruccion: INDEX', padre)
        np = str(self.contador)
        if inst.caso == 3:
            self.CrearNodo('CREATE UNIQUE INDEX', np)
        else:
            self.CrearNodo('CREATE INDEX', np)
        self.CrearNodo(inst.id1 + ' ON ' + inst.id2, np)
        if inst.caso == 2:
            self.CrearNodo('USING HASH', np)
        self.CrearNodo('IDS', np)
        np = str(self.contador)
        self.listaID(inst.listaId, np)

    def While(self, inst, padre):
        self.CrearNodo('Instruccion: WHILE', padre)
        np = str(self.contador)
        self.CrearNodo('WHILE', np)
        if inst.opNot:
            self.CrearNodo('NOT', np)
        self.E(inst.E, np)
        self.CrearNodo('LOOP', np)
        self.CrearNodo('Instrucciones', np)
        np2 = str(self.contador)
        self.TiposInstruccion(inst.instrucciones, np2)
        self.CrearNodo('END LOOP', np)

    def For(self, inst, padre):
        self.CrearNodo('Instruccion: FOR', padre)
        np = str(self.contador)


    def SIF(self, inst, padre):
        self.CrearNodo('Instruccion: IF', padre)
        np = str(self.contador)
        self.CrearNodo('IF', np)
        self.E(inst.E, np)
        self.CrearNodo('THEN', np)
        self.CrearNodo('INSTRUCCIONES', np)
        np2 = str(self.contador)
        self.TiposInstruccion(inst.instrucciones, np2)
        if inst.elsesif != None:
            if len(inst.elsesif) == 1:
                if inst.elsesif[0] != None:
                    for ei in inst.elsesif:
                        if isinstance(ei, SElseIf):
                            self.CrearNodo('ELSIF', np)
                            self.E(ei.E, np)
                            self.CrearNodo('THEN', np)
                            self.CrearNodo('INSTRUCCIONES', np)
                            np2 = str(self.contador)
                            self.TiposInstruccion(ei.instrucciones, np2)
            else:
                for ei in inst.elsesif:
                    if isinstance(ei, SElseIf):
                        self.CrearNodo('ELSIF', np)
                        self.E(ei.E, np)
                        self.CrearNodo('THEN', np)
                        self.CrearNodo('INSTRUCCIONES', np)
                        np2 = str(self.contador)
                        self.TiposInstruccion(ei.instrucciones, np2)
        if inst.Belse:
            self.CrearNodo('ELSE', np)
            self.CrearNodo('INSTRUCCIONES', np)
            np2 = str(self.contador)
            self.TiposInstruccion(inst.instruccionesElse, np2)
        self.CrearNodo('END IF', np)

    def CaseF2(self, inst, padre):
        self.CrearNodo('Instruccion: CASE', padre)
        np = str(self.contador)
        self.CrearNodo('CASE', np)
        self.E(inst.E, np)
        for w in inst.listaWhen:
            if isinstance(w, When):
                self.CrearNodo('WHEN', np)
                #self.CrearNodo('EXPRE', np)
                #np2 = str(self.contador)
#                self.listaID(w.listaE, np2)
                self.E(w.E, np)
                self.CrearNodo('THEN', np)
                self.CrearNodo('INSTRUCCIONES', np)
                np2 = str(self.contador)
                self.TiposInstruccion(w.instrucciones, np2)
        if inst.elseCase != None:
            self.CrearNodo('ELSE', np)
            self.CrearNodo('INSTRUCCIONES', np)
            np2 = str(self.contador)
            self.TiposInstruccion(inst.elseCase, np2)
        self.CrearNodo('END CASE', np)
