from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario import Binario
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.instruccion import *
from tytus.parser.team21.Analisis_Ascendente.storageManager.jsonMode import *
import tytus.parser.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import tytus.parser.team21.Analisis_Ascendente.Instrucciones.Select as Select
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Time import  Time
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.expresion import  *
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import  Trigonometrica
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import  IdAsId
from tytus.parser.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import  Math_
from prettytable import PrettyTable

class Selectp3(Instruccion):

    def ejecutar(Select,ts,Consola,exceptions,Mostrar):

        #type(self).__name__
        print('what -- '+type(Select.columnas).__name__)
        x = PrettyTable()
        rowpp=[]
        en=[]
        aux =0

        print(Select.columnas)

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
            elif isinstance(columna,Id): # no porque no tiene from
                Consola.append('what -- ' + type(columna).__name__ + '\n')
                exceptions.append('Error semantico - 42703 - no existe la columna, error en '+' - '+str(Select.fila)+' - '+str(Select.columna)+'')
            elif isinstance(columna, IdAsId):
                # no porque no tiene from
                if(isinstance(columna.id2,Primitivo)):
                    en.append(columna.id2.valor)
                else:
                    en.append(columna.id2.id)
                val = IdAsId.Resolver(columna,Consola)
                rowpp.append(str(val))
                #Consola.append('what -- ' + str(val)+ '\n')
            elif isinstance(columna,Math_): #hay que resolver
                en.append(str(columna.nombre+str(aux)))
                val=Math_.Resolver(columna,Consola,Consola,exceptions)
                rowpp.append(str(val))
                aux = aux + 1
                #Consola.append('what -- ' + type(columna).__name__ + '\n')
            elif isinstance(columna,Trigonometrica):  #hay que resolver
                en.append(str(columna.trig+str(aux)))
                REST=Trigonometrica.Resolver(columna,ts,Consola,exceptions)
                rowpp.append(str(REST))
                aux = aux + 1
                #Consola.append('what -- ' + str(REST) + '\n')
            elif isinstance(columna,Expresion):  #hay que resolver
                en.append(str("col"+str(aux)))
                REST=Expresion.Resolver(columna,ts,Consola,exceptions)
                rowpp.append(str(REST))
                aux = aux+1
                #Consola.append('what -- ' + str(REST) + '\n')
            elif isinstance(columna,Binario):  #hay que resolver
                en.append(str("col"+str(aux)))
                REST=Binario.Resolver(columna,ts,Consola,exceptions)
                rowpp.append(str(REST))
                aux = aux+1
                #Consola.append('what -- ' + str(REST) + '\n')
            i= i + 1


        x.add_row(rowpp)
        x.field_names = en

        if Mostrar:
            Consola.append(x.get_string()+'\n')
        return [en,rowpp]
