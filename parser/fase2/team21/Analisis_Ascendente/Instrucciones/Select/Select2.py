from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Binario import Binario
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion as Expresion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Function.Llamada import Llamada
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import *
from tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
import tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Select as Select
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Time import  Time
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import  *
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Trigonometrica import  Trigonometrica
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.IdAsId import  IdAsId
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Math import  Math_
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
                '''           
                elif isinstance(columna,Llamada):
                    #rowpp.append(Llamada.obtenerCadena(columna,1)
                    Llamada.obtenerCadena(columna)'''


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
            elif isinstance(columna,Expresion.Expresion):  #hay que resolver
                en.append(str("col"+str(aux)))
                REST=Expresion.Expresion.Resolver(columna,ts,Consola,exceptions)
                rowpp.append(str(REST))
                aux = aux+1
                #Consola.append('what -- ' + str(REST) + '\n')
            elif isinstance(columna,Binario):  #hay que resolver
                en.append(str("col"+str(aux)))
                REST=Binario.Resolver(columna,ts,Consola,exceptions)
                rowpp.append(str(REST))
                aux = aux+1
                #Consola.append('what -- ' + str(REST) + '\n')
            elif isinstance(columna,Primitivo):
                print("aqui")
                print(columna)
                print(columna.valor)
                en.append(str("col" + str(aux)))

                #REST=Binario.Resolver(columna,ts,Consola,exceptions)
                rowpp.append(str(columna.valor))
                aux = aux+1
                #en.append(columna.valor)
            i= i + 1


        x.add_row(rowpp)
        x.field_names = en

        if Mostrar:
            Consola.append(x.get_string()+'\n')
        return [en,rowpp]

    def traducir(select, consola, tv):

        #iniciar traduccion
        info = "" #info contiene toda el string a mandar como parametros
        print("concatena \n")
        print(select.concatena)

        guardartemporales = []
        guardarAS = []
        guardarConvert = []

        for data in select.concatena:
            if isinstance(data,list):
                guardar_parametros_funciones = []
                for datasub in data:
                    if "%" in datasub:
                        temporalaux = tv.Temp()
                        guardar_parametros_funciones.append(temporalaux)
                        consola.append("\t"+str(str(datasub).replace("!", str(temporalaux))).replace("%","") + "\n")
                    elif "?" in datasub:
                        concatena_parametros = ""
                        j =1
                        for parametro in guardar_parametros_funciones:

                            if j == len(guardartemporales):
                                concatena_parametros += parametro
                            else:
                                concatena_parametros += parametro + ","

                            j = j + 1
                        temporal = tv.Temp()
                        guardarConvert.append(temporal)
                        guardartemporales.append(temporal)
                        consola.append("\t"+str(datasub).replace("?",str(temporal))+"("+concatena_parametros+")"+"\n")
                    elif "$" in datasub:
                        temporal = tv.Temp()
                        guardartemporales.append("$"+temporal)
                        consola.append("\t"+str(datasub).replace("$",str(temporal))+"\n")
                    elif "!" in datasub:
                        temporal = tv.Temp()
                        guardartemporales.append(temporal)
                        guardarConvert.append("\t"+str(datasub).replace("!",str(temporal))+"\n")
                        consola.append("\t" + str(datasub).replace("!", str(temporal)) + "\n")
                    else:
                        guardarAS.append(datasub)


            else:
                info += " " +str(data)


        obtenerTemporal = tv.Temp()
        concatena_temporales  = ""
        contador = 1

        for temporal in guardartemporales:
            if contador == 1:
                if "$" in str(temporal):

                    concatena_temporales += "{" + str(temporal).replace("$", "") + "}"
                else:
                    concatena_temporales += "{" + temporal + "}"
            else:
                if "$" in str(temporal):

                    concatena_temporales += "{" + str(temporal).replace("$","") + "}"
                else:
                    concatena_temporales +=  ", {" + temporal + "}"
            contador = contador + 1

        if len(guardarAS) >= 1:
            consola.append(f"\n\t{obtenerTemporal} = f\"{info} ({concatena_temporales}) {guardarAS[0]};\"")
        elif len(guardarConvert) >= 1:
            consola.append(f"\n\t{obtenerTemporal} = f\"{info} {concatena_temporales};\"")

        else:
            consola.append(f"\n\t{obtenerTemporal} = f\"{info} ({concatena_temporales});\"")

        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({obtenerTemporal})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")
