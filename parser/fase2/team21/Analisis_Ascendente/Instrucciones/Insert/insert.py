from  tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from  tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.expresion import Primitivo
from  tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from  tytus.parser.fase2.team21.Analisis_Ascendente.storageManager.jsonMode import *
import  tytus.parser.fase2.team21.Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
from datetime import date,datetime
todoBien = True
#INSERT INTO
class InsertInto(Instruccion):
    def __init__(self,caso, id, listaId, values,concatena, con_expresiones,fila,columna):
        self.caso=caso
        self.id = id
        self.listaId = listaId
        self.values = values
        self.concatena = concatena
        self.con_expresiones = con_expresiones
        self.fila = fila
        self.columna = columna





    def ejecutar(insertinto,ts,consola,exceptions):


        if ts.validar_sim("usedatabase1234") == 1:

            # nombre de la bd
            bdactual = ts.buscar_sim("usedatabase1234")
            # se busca el simbolo y por lo tanto se pide el entorno de la bd
            BD = ts.buscar_sim(bdactual.valor)
            entornoBD = BD.Entorno

            dataainsertar =[]
            if entornoBD.validar_sim(insertinto.id) == 1:

                simbolo_tabla = entornoBD.buscar_sim(insertinto.id)

                entornoTabla = simbolo_tabla.Entorno
                indices_a_buscar=[]

                if insertinto.caso==1:


                    print("caso1")
                    for data in insertinto.listaId:
                        contador = 1
                        for columna in entornoTabla.simbolos:
                            if data.id == columna:
                                indices_a_buscar.append(contador)

                                break
                            contador=contador+1

                    print(indices_a_buscar)

                    lista = entornoTabla.simbolos
                    contador = 1
                    for columna in lista:

                        if not contador in indices_a_buscar:
                            print("((((((((((((((((((((((((((((((((((((((")
                            if "NOTNULL" in lista.get(columna).valor:
                                global todoBien
                                todoBien = False
                                consola.append(f"Error esta columna no puede ser nula {columna}")
                                break
                            else:
                                todoBien = True
                        contador=contador+1

                    for data in insertinto.listaId:

                        if entornoTabla.validar_sim(data.id)==-1:
                            consola.append(f"Error no hay coincidencia de ids en {data.id}")
                            todoBien = False


                    for data in insertinto.values:
                        print("val :",data.valor)

                    if todoBien:
                        contadoraux= 1
                        i = 0
                        todobien = True

                        for data in entornoTabla.simbolos:

                            if contadoraux in indices_a_buscar:
                                todobien = comprobar_tipos(dataainsertar, i, insertinto.values, data, entornoTabla.simbolos,
                                                           entornoTabla, consola, exceptions, BD, simbolo_tabla,ts)
                                i = i + 1
                            else:
                                dataainsertar.append(str(None))

                            if not todobien:
                                consola.append(f"No se insertaron los datos, columnas inconsistentes en {simbolo_tabla.id}")
                                todobien = False
                                break
                            contadoraux =contadoraux+1


                        if todobien:

                            insert(BD.id, simbolo_tabla.id, dataainsertar)

                            consola.append(f"insert en la tabla {insertinto.id}, exitoso\n")
                        else:
                            consola.append(f"Error \n")

                        #consola.append(f"insert en la tabla {insertinto.id}, exitoso\n")
                    else:
                        consola.append(f"datos dectectados como no nulos")

                    todoBien=True
                else:
                    print("caso 2")

                    if len(insertinto.values) == len(entornoTabla.simbolos):
                        i =0
                        todobien = True


                        for data in entornoTabla.simbolos:

                            todobien = comprobar_tipos(dataainsertar,i,insertinto.values,data,entornoTabla.simbolos,entornoTabla,consola,exceptions,BD,simbolo_tabla,ts)



                            if not todobien:
                                consola.append(f"No se insertaron los datos, columnas inconsistentes en {simbolo_tabla.id}")
                                todobien= False
                                break

                            i=i+1

                        if todobien:

                            insert(BD.id,simbolo_tabla.id,dataainsertar)

                            consola.append(f"insert en la tabla {insertinto.id}, exitoso\n")
                        else:
                            consola.append(f"Error\n")
                    else:
                        consola.append(f"La cantidad de columnas esperadas es de {len(entornoTabla.simbolos)} para insersar en tabla {insertinto.id}")
                        exceptions.append(f"Error semantico-22023-invalid_parameter_value -{insertinto.fila}-{insertinto.columna}")
            else:
                consola.append(f"42P01	undefined_table, no existe la tabla {insertinto.id}")
                exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la tabla {insertinto.id}-fila-columna")

        else:
            consola.append("42P12	invalid_database_definition, Error al insertar\n")
            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")
            exceptions.append("Error semantico-22005	error_in_assignment-No se ha seleccionado DB-fila-columna")

    def traducir(insertinto,consola,tv):

        #iniciar traduccion
        info = "" #info contiene toda el string a mandar como parametros
        print("concatena \n")
        print(insertinto.concatena)

        guardartemporales = []

        for data in insertinto.concatena:
            if isinstance(data,list):
                guardar_parametros_funciones = []
                for datasub in data:
                    if "%" in datasub:
                        temporalaux = tv.Temp()
                        guardar_parametros_funciones.append(temporalaux)
                        try:
                            data1  = str(datasub).replace("\\\"","")
                            consola.append(
                                "\t" + str(str(data1).replace("!", str(temporalaux))).replace("%", "") + "\n")

                            print("ññññññ ",data)
                        except:
                            print("ññññññ ",datasub)
                            consola.append("\t"+str(str(datasub).replace("!", str(temporalaux))).replace("%","") + "\n")
                    elif "?" in datasub:
                        concatena_parametros = ""
                        j = 1
                        for parametro in guardar_parametros_funciones:

                            if 0 == len(guardartemporales):
                                concatena_parametros += parametro
                            elif j == len(guardartemporales):
                                concatena_parametros += parametro
                            else:
                                concatena_parametros += parametro + ","
                            j = j + 1
                        temporal = tv.Temp()
                        guardartemporales.append(temporal)

                        consola.append("\t"+str(datasub).replace("?",str(temporal))+"("+concatena_parametros+")"+"\n")
                    elif "$" in datasub:
                        temporal = tv.Temp()
                        guardartemporales.append(temporal)
                        consola.append("\t"+str(datasub).replace("$",str(temporal))+"\n")
                    elif "!" in datasub:
                        temporal = tv.Temp()
                        guardartemporales.append(temporal)
                        #guardarConvert.append("\t"+str(datasub).replace("!",str(temporal))+"\n")
                        consola.append("\t" + str(datasub).replace("!", str(temporal)) + "\n")
            else:
                info += " " +str(data)


        obtenerTemporal = tv.Temp()
        concatena_temporales  = ""
        contador = 1

        for temporal in guardartemporales:
            if contador == len(guardartemporales):
                concatena_temporales += "{" + temporal + "}"
            else:
                concatena_temporales +=  "{" + temporal + "}" ","
            contador = contador + 1

        consola.append(f"\n\t{obtenerTemporal} = f\"{info} ({concatena_temporales});\"")

        contador2 = tv.Temp()
        consola.append(f"\n\t{contador2} = T({obtenerTemporal})")
        consola.append(f"\n\tT1 = T3({contador2})")
        consola.append(f"\n\tstack.append(T1)\n")



def comprobar_tipos(datainsertar,index,lista_valores,campo,lista_tabla,ts,Consola,exception,bd,tabla,globall):
    print("estoy aqui !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    todobien = False
#    print(lista_valores[index].valor)
#    print(date.fromisoformat(lista_valores[index].valor))
#    print(isinstance(date.fromisoformat(lista_valores[index].valor),date))
#    print('DATE' in str(lista_tabla.get(campo).tipo).upper())
    datafinal = None
    if isinstance(lista_valores[index],Instruccion):
        datafinal = Expresion.Resolver(lista_valores[index],ts,Consola,exception)
        datainsertar.append(datafinal)
    else:
        print("quepaso",lista_valores[index])
        if isinstance(lista_valores[index],Primitivo):
            print("si es primtivo")
            datafinal = lista_valores[index].valor
            datainsertar.append(datafinal)
        else:
            return

    print(datafinal, "que estoy haciendo mal",tabla.id)


    if isinstance(datafinal,int) and 'INTEGER' in str(lista_tabla.get(campo).tipo).upper():
        todobien = True
        todobien = comprobarcheck(lista_tabla.get(campo).Entorno,1,datafinal,lista_tabla.get(campo).id,ts,Consola,exception)
        todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor,datafinal,Consola,exception,bd,tabla,index)
    elif isinstance(datafinal,float) and 'DOUBLE' in str(lista_tabla.get(campo).tipo).upper() or 'DECIMAL' in str(lista_tabla.get(campo).tipo).upper():
        todobien = True
        todobien = comprobarcheck(lista_tabla.get(campo).Entorno,1,datafinal,lista_tabla.get(campo).id,ts,Consola,exception)
        todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor, datafinal, Consola, exception, bd, tabla, index)

    elif str(datafinal).upper() == 'TRUE' or str(datafinal).upper() == 'FALSE' and 'BOOLEAN' in str(lista_tabla.get(campo).tipo).upper():
        todobien = True
        todobien = comprobarcheck(lista_tabla.get(campo).Entorno,1,datafinal,lista_tabla.get(campo).id,ts,Consola,exception)
        todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor, datafinal, Consola, exception, bd, tabla,
                                             index)

    elif isinstance(datafinal,str) and 'TEXT' in str(lista_tabla.get(campo).tipo).upper():
        todobien = True
        todobien = comprobarcheck(lista_tabla.get(campo).Entorno,1,datafinal,lista_tabla.get(campo).id,ts,Consola,exception)
        todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor, datafinal, Consola, exception, bd, tabla,
                                             index)

    elif isinstance(str(datafinal),str) and 'VARCHAR' in str(lista_tabla.get(campo).tipo).upper() or 'CHARACTERVARYING' in str(lista_tabla.get(campo).tipo).upper() or 'CHARACTER' in str(lista_tabla.get(campo).tipo).upper() or 'CHAR' in str(lista_tabla.get(campo).tipo).upper():
        todobien = True
        cantidad = str(lista_tabla.get(campo).tipo).split("-")[1]
        if len(str(datafinal)) <= int(cantidad):
            todobien = True
            todobien = comprobarcheck(lista_tabla.get(campo).Entorno,1,str(datafinal),lista_tabla.get(campo).id,ts,Consola,exception)
            todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor, datafinal, Consola, exception, bd, tabla,
                                                 index)

        else:
            todobien = False


    elif isinstance(datafinal,float) and 'MONEY' in str(lista_tabla.get(campo).tipo).upper():
        todobien = True
        todobien = comprobarcheck(lista_tabla.get(campo).Entorno,1,datafinal,lista_tabla.get(campo).id,ts,Consola,exception)
        todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor, datafinal, Consola, exception, bd, tabla,
                                             index)

    elif isinstance(datafinal,int) and 'MONEY' in str(lista_tabla.get(campo).tipo).upper():
        todobien = True
        try:
            todobien = comprobarcheck(lista_tabla.get(campo).Entorno,1,datafinal,lista_tabla.get(campo).id,ts,Consola,exception)
            todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor, datafinal, Consola, exception, bd, tabla,
                                                 index)

        except:
            todobien = False
    elif 'DATE' in str(lista_tabla.get(campo).tipo).upper():
        try:

                #todobien= isinstance(date.fromisoformat(str(datafinal)), date)

                todobien = comprobarcheck(lista_tabla.get(campo).Entorno, 1, datafinal, lista_tabla.get(campo).id, ts,Consola, exception)
                todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor, datafinal, Consola, exception, bd, tabla, index)

        except:
            print("error de tipo")
            todobien = False
    else:
        try:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
            print(lista_tabla.get(campo).tipo)
            for data in globall.simbolos:
                print(":: ",data)
            if globall.validar_sim(str(lista_tabla.get(campo).tipo).lower()) == 1:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
                for data in ts.simbolos:
                    print(";;; ",data)
                simbolo_enumo = globall.buscar_sim(str(lista_tabla.get(campo).tipo).lower())

                if datafinal in simbolo_enumo.valor:
                    todobien = True
                    #Consola.append("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11")
            else:
                print("no encotrado")
        except:
            todobien= False
    return todobien


def comprobarcheck(expresion,data,valor,nombre_columna,ts,Consola,exception):
    valor_retorno=True
    print("que pedo",data)
    #if data == 1:
    print("-> ",expresion)
    if expresion != None:

        for datos in expresion:
            dataiz = datos.iz
            datade = datos.dr
            operador= datos.operador
            if nombre_columna != dataiz.id:
                valor_retorno=False
                break
            valor_retorno = Expresion.Resolver(Expresion(Primitivo(valor,1,1,False),datade,operador,1,1),ts,Consola,exception)



    return valor_retorno



def comprobar_caracteristicas(tipo_caracteristica,data,Consola,Exception,nombre_bd,nombre_tabla,posicion):
    devolver=True
    print("->>>>>",tipo_caracteristica)
    if tipo_caracteristica != None:
        print("aqui estamos")

        for caracteristica in tipo_caracteristica:
            print(caracteristica)
            if "NOTNULL" in str(caracteristica):

                if data == None:
                    Consola.append("Dato encontrado con not null, debe llevar un valor")
                    devolver=False
                    break
            elif "UNIQUE" in str(caracteristica) or "PRIMARYKEY" in str(caracteristica):
                print(nombre_bd.id,nombre_tabla.id)
                datas = extractTable(nombre_bd.id,nombre_tabla.id)
                print("unique or primary ->  ",posicion)
                for fila in datas:
                    if str(fila[posicion])== str(data):
                        devolver= False
                        Consola.append("Constraint unique active")
                    print(fila[posicion])


                print(data)

    return  devolver


