from Analisis_Ascendente.Instrucciones.PLPGSQL import EjecutarFuncion
from Analisis_Ascendente.Instrucciones.instruccion import *
from Analisis_Ascendente.storageManager.jsonMode import *
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import Analisis_Ascendente.Instrucciones.Select as Select
from Analisis_Ascendente.Instrucciones.Time import Time
from Analisis_Ascendente.Instrucciones.expresion import *
from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import *
from Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import Trigonometrica
from Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import IdAsId
from Analisis_Ascendente.Instrucciones.Expresiones.Math import Math_
from prettytable import PrettyTable

class Selectp3(Instruccion):
    def get3D(self, ts, listaopt):
        dict = {}
        etiq = GeneradorTemporales.nuevo_temporal()
        code = '   \n# ---------SELECT----------- \n'
        code += '    top_stack = top_stack + 1 \n'
        code += '    %s = "select ' % etiq
        if self.columnas is not None:
            for col in self.columnas:
                if isinstance(col, Instruccion):
                    code += col.getC3D() + ','
                if isinstance(col, Expresion):
                    dict = col.getC3D(listaopt)
                if isinstance(col, Funcion):
                    code += col.getC3D()
        code += '\"'
        if bool(dict):
            code += '\n'+dict["code"] + '\n'
            code += '    %s = %s + %s' % (etiq, etiq, dict["tmp"])
        tmp = GeneradorTemporales.nuevo_temporal()
        code += '\n    %s = ";" \n' % tmp
        code += '    %s = %s + %s \n' % (etiq, etiq, tmp)
        code += '    stack[top_stack] = %s \n' % etiq
        return code

    def ejecutar(Select,ts,Consola,exceptions,Mostrar):
        #type(self).__name__
        ##print('what -- '+type(Select.columnas).__name__)
        x = PrettyTable()
        rowpp=[]
        en=[]

        for columna in Select.columnas:
            i=0

            if isinstance(columna , Select.__class__):
                Consola.append('what -- ' + type(columna).__name__ + '\n')
            elif isinstance(columna,Time):
                en.append('time')

                time = Time.resolverTime(columna)
                rowpp.append(time)
                #Consola.append('what -- ' + time + '\n')
            elif isinstance(columna,IdId):# no porque no tiene from
                Consola.append('what -- ' + type(columna).__name__ + '\n')
                exceptions.append(
                    'Error semantico - 42P01 - falta una entrada para la tabla en la cláusula FROM, error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')
            elif isinstance(columna,IdId):# no porque no tiene from
                Consola.append('42P01 - falta una entrada para la tabla en la cláusula FROM')
                exceptions.append(
                    'Error semantico - 42P01 - falta una entrada para la tabla en la cláusula FROM, error en ' + ' - ' + str(Select.fila) + ' - ' + str(Select.columna) + '')
            elif isinstance(columna, Funcion):
                bdactual = ts.buscar_sim("usedatabase1234")
                if bdactual is not None:
                    BD = ts.buscar_sim(bdactual.valor)
                    entornoBD = BD.Entorno
                    funcion = entornoBD.buscar_sim(columna.id)
                    if funcion.categoria == TS.TIPO_DATO.FUNCTION:
                        datafinal = EjecutarFuncion.ResolverFuncion(columna, ts, Consola, exceptions)
                        EjecutarFuncion.limpiarFuncion(columna, ts)
                    en.append(columna.id)
                    rowpp.append(datafinal)
                    EjecutarFuncion.limpiarFuncion(columna, ts)
                else:
                    Consola.append('42883	undefined_function')
                    exceptions.append(
                        'Error semantico - 42883 - undefined_functions' + ' - ' + str(
                            Select.fila) + ' - ' + str(Select.columna) + '')
            elif isinstance(columna, IdAsId):
                # no porque no tiene from
                if(isinstance(columna.id2,Primitivo)):
                    en.append(columna.id2.valor)
                else:
                    en.append(columna.id2.id)


                val = IdAsId.Resolver(columna, ts, Consola, exceptions)
                rowpp.append(str(val))
                #Consola.append('what -- ' + str(val)+ '\n')
            elif isinstance(columna,Math_): #hay que resolver
                en.append(str(columna.nombre))
                val=Math_.Resolver(columna,Consola,Consola,exceptions)
                rowpp.append(str(val))
                #Consola.append('what -- ' + type(columna).__name__ + '\n')
            elif isinstance(columna,Trigonometrica):  #hay que resolver
                en.append(str(columna.trig))
                REST=Trigonometrica.Resolver(columna,ts,Consola,exceptions)
                rowpp.append(str(REST))
                #Consola.append('what -- ' + str(REST) + '\n')
            i= i + 1


        x.add_row(rowpp)
        x.field_names = en

        if Mostrar:
            Consola.append('\n'+x.get_string()+'\n')
        return [en, rowpp]
