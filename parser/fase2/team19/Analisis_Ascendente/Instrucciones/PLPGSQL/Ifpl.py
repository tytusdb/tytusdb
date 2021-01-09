import Analisis_Ascendente.Instrucciones.PLPGSQL.EjecutarFuncion as EjecutarFuncion
from Analisis_Ascendente.Instrucciones.PLPGSQL.plasignacion import Plasignacion
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.Create.createTable import CreateTable
from Analisis_Ascendente.Instrucciones.Create.createDatabase import CreateReplace
from Analisis_Ascendente.Instrucciones.Select.select import Select
from Analisis_Ascendente.Instrucciones.Use_Data_Base.useDB import Use
from Analisis_Ascendente.Instrucciones.Select.select1 import selectTime
import Analisis_Ascendente.Instrucciones.Insert.insert as insert_import
from Analisis_Ascendente.Instrucciones.Select.Select2 import Selectp3
from Analisis_Ascendente.Instrucciones.Select import selectInst
from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from Analisis_Ascendente.Instrucciones.Drop.drop import Drop
from Analisis_Ascendente.Instrucciones.Alter.alterDatabase import AlterDatabase
from Analisis_Ascendente.Instrucciones.Alter.alterTable import AlterTable
from Analisis_Ascendente.Instrucciones.Update.Update import Update
from Analisis_Ascendente.Instrucciones.Delete.delete import Delete
from Analisis_Ascendente.Instrucciones.Select import SelectDist
from Analisis_Ascendente.Instrucciones.Type.type import CreateType

#----------------------------------Imports FASE2--------------------------
from Analisis_Ascendente.Instrucciones.Index.Index import Index
from Analisis_Ascendente.Instrucciones.PLPGSQL.createFunction import CreateFunction
from Analisis_Ascendente.Instrucciones.Index.DropIndex import DropIndex
from Analisis_Ascendente.Instrucciones.Index.AlterIndex import AlterIndex
from Analisis_Ascendente.Instrucciones.PLPGSQL.DropProcedure import DropProcedure
from Analisis_Ascendente.Instrucciones.PLPGSQL.CreateProcedure import CreateProcedure
from Analisis_Ascendente.Instrucciones.PLPGSQL.CasePL import CasePL
from Analisis_Ascendente.Instrucciones.PLPGSQL.plCall import plCall
from Analisis_Ascendente.Instrucciones.PLPGSQL.dropFunction import DropFunction

import C3D.GeneradorEtiquetas as GeneradorEtiquetas
import C3D.GeneradorTemporales as GeneradorTemporales
import Analisis_Ascendente.reportes.Reportes as Reportes

class Ifpl(Instruccion):
    ''' #1 If
        #2 If elif else
        #3 If else '''

    def __init__(self, caso,e_if,s_if,elif_s,s_else, fila, columna):
        self.caso = caso
        self.e_if = e_if
        self.s_if = s_if
        self.elif_s = elif_s
        self.s_else = s_else
        self.fila = fila
        self.columna = columna

    def ejecutar(self,tsglobal,ts, consola, exceptions):
        try:
            if self.caso == 1:
                resultado = Expresion.Resolver(self.e_if, ts, consola, exceptions)
                if resultado == True:
                    for x in range(0, len(self.s_if)):
                        self.procesar_instrucciones(self.s_if[x],ts,consola,exceptions,tsglobal)
                else:
                    pass
            elif self.caso == 2:
                print('hola')
            else:
                resultado = Expresion.Resolver(self.e_if, ts, consola, exceptions)
                if resultado == True:
                    for x in range(0, len(self.s_if)):
                        self.procesar_instrucciones(self.s_if[x], ts, consola, exceptions,tsglobal)
                else:
                    for x in range(0, len(self.s_else)):
                        self.procesar_instrucciones(self.s_else[x],ts,consola,exceptions,tsglobal)

        except:
            consola.append("XX000 : internal_error")


    def procesar_instrucciones(self,instr,ts,consola,exceptions,tsglobal):
        if isinstance(instr, CreateReplace):
            CreateReplace.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, Select):
            if instr.caso == 1:
                consola.append('caso 1')
                selectTime.ejecutar(instr, ts, consola, exceptions, True)
            elif instr.caso == 2:
                consola.append('caso 2')
                variable = SelectDist.Select_Dist()
                SelectDist.Select_Dist.ejecutar(variable, instr, ts, consola, exceptions)
            elif instr.caso == 3:
                consola.append('caso 3')
                variable = selectInst.Select_inst()
                selectInst.Select_inst.ejecutar(variable, instr, ts, consola, exceptions)
            elif instr.caso == 4:
                consola.append('caso 4')
                Selectp3.ejecutar(instr, ts, consola, exceptions, True)
            elif instr.caso == 6:
                consola.append('caso 6')
        elif isinstance(instr, CreateTable):
            CreateTable.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, Use):
            Use.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, insert_import.InsertInto):
            insert_import.InsertInto.ejecutar(instr, ts, consola, exceptions)
            # print("Ejecute un insert")
        elif isinstance(instr, Drop):
            Drop.ejecutar(instr, ts, consola, exceptions)
            # print("Ejecute drop")
        elif isinstance(instr, AlterDatabase):
            AlterDatabase.ejecutar(instr, ts, consola, exceptions)
            # print("Ejecute alter database")
        elif isinstance(instr, AlterTable):
            AlterTable.ejecutar(instr, ts, consola, exceptions)
            # print("Ejecute alter table")
        elif isinstance(instr, Delete):
            Delete.ejecutar(instr, ts, consola, exceptions)
            # print("Ejecute delete")
        elif isinstance(instr, Update):
            Update.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, CreateType):
            CreateType.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, Index):
            Index.ejecutar(instr, ts, consola, exceptions)
            # print("Ejecute Index")
        elif isinstance(instr, CreateFunction):
            CreateFunction.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, DropFunction):
            DropFunction.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, DropIndex):
            DropIndex.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, AlterIndex):
            AlterIndex.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, DropProcedure):
            DropProcedure.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, CreateProcedure):
            CreateProcedure.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, CasePL):
            CasePL.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, plCall):
            plCall.ejecutar(instr, ts, consola, exceptions)
        elif isinstance(instr, Plasignacion):
            EjecutarFuncion.ejecutarPlasignacionIf(instr,ts,consola,exceptions,tsglobal)
        elif isinstance(instr, Ifpl):
            instr.ejecutar(tsglobal,ts,consola,exceptions)
        else:
            return

    def getC3D(self, lista_optimizaciones_C3D):
        etiqueta_if = GeneradorEtiquetas.nueva_etiqueta()
        etiqueta_else = GeneradorEtiquetas.nueva_etiqueta()
        etiqueta_salida = GeneradorEtiquetas.nueva_etiqueta()
        e_if = self.e_if.getC3D(lista_optimizaciones_C3D)
        noOptimizado = '''if %s: goto .%s <br>
goto .%s<br>
label .%s<br>
&lt;instrucciones&gt;<br>
label .%s''' % (e_if['tmp'], etiqueta_if, etiqueta_else, etiqueta_if, etiqueta_else)
        optimizado = '''if not %s: goto .%s <br>
&lt;instrucciones&gt;<br>
label .%s''' % (e_if['tmp'], etiqueta_else, etiqueta_else)
        optimizacion1 = Reportes.ListaOptimizacion(noOptimizado, optimizado, Reportes.TipoOptimizacion.REGLA3)
        lista_optimizaciones_C3D.append(optimizacion1)

        sentencias_if = ''
        for sentencias in self.s_if:
            sentencias_if += sentencias.getC3D(lista_optimizaciones_C3D)
        c3d = '''
%s
    if not %s: goto .%s
%s
    goto .%s
''' % (e_if['code'], e_if['tmp'], etiqueta_else, sentencias_if, etiqueta_salida)

        if self.s_else is not None:
            sentencias_else = ''
            for sentencias in self.s_else:
                sentencias_else += sentencias.getC3D(lista_optimizaciones_C3D)
            c3d += '''    label .%s
%s
    label .%s''' % (etiqueta_else, sentencias_else, etiqueta_salida)
        else:
            c3d += '''    label .%s
    label .%s
''' % (etiqueta_else, etiqueta_salida)
        return c3d

    def get_quemado(self):
        sententias_if = ''
        for sentencia in self.s_if:
            sententias_if += sentencia.get_quemado() + ';\n'
        quemado = '''   if %s then
%s
''' % (self.e_if.get_quemado(), sententias_if)
        if self.s_else is not None:
            sentencias_else = ''
            for sentencia in self.s_else:
                sentencias_else += sentencia.get_quemado() + ';\n'
            quemado += '''ELSE
%s
''' % sentencias_else
        quemado += '    end if'
        return quemado
