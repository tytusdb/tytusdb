from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.instruccion import *
from Compi2RepoAux.team21.Analisis_Ascendente.storageManager.jsonMode import *
import Compi2RepoAux.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Select as Select
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Time import  Time
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.expresion import  *
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import  Trigonometrica
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import  IdAsId
from Compi2RepoAux.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import  Math_
from prettytable import PrettyTable

class Selectp3(Instruccion):

    def ejecutar(Select,ts,Consola,exceptions):

        #type(self).__name__
        print('what -- '+type(Select.columnas).__name__)
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
            elif isinstance(columna,Id): # no porque no tiene from
                Consola.append('what -- ' + type(columna).__name__ + '\n')
                exceptions.append('Error semantico - numero error - Falta nombre de Tabla, error en '+columna.id.id+' - fila - columna')
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
                en.append(str(columna.nombre))
                val=Math_.Resolver(columna,Consola)
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
        Consola.append(x.get_string()+'\n')
