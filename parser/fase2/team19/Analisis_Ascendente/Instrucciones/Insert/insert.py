from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import Expresion
from Analisis_Ascendente.Instrucciones.PLPGSQL import EjecutarFuncion
from Analisis_Ascendente.Instrucciones.expresion import Primitivo
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.storageManager.jsonMode import *
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
from datetime import date,datetime

from C3D import GeneradorTemporales
from Analisis_Ascendente.Instrucciones.expresion import Funcion
from Analisis_Ascendente.Instrucciones.Expresiones.Math import Math_
from Analisis_Ascendente.Instrucciones.Time import Time
from Analisis_Ascendente.Instrucciones.Expresiones.Expresion import *

todoBien = True
#INSERT INTO
class InsertInto(Instruccion):
    def __init__(self,caso, id, listaId, values,fila,columna):
        self.caso=caso
        self.id = id
        self.listaId = listaId
        self.values = values
        self.fila = fila
        self.columna = columna
        
    def get_quemado(self):
        quemado = 'insert into ' + self.id
        if self.listaId is not None:
                ides = ''
                quemado += '('
                for ide in self.listaId:
                    ides += ide.id + ','
                ids = list(ides)
                size = len(ids) - 1
                del (ids[size])
                s = "".join(ids)
                quemado += s + ') values('
        else:
                quemado += ' values ('
        values = ''
        for val in self.values:
            if isinstance(val,Math_):
                if val.E1 == None and val.E2 == None:
                    quemado += '%s ,' %val.nombre + ','
                else:
                    if val.E2 == None:
                        if isinstance(val.E1.valor, str):
                            quemado += "'%s'" % str(val.E1.valor)
                        else:
                            val1 = str(val.E1.valor)
                            quemado  += '%s ( %s ),' % (val.nombre, val1)
                    else:
                        val1 = ''
                        if isinstance(val.E1.valor, str):
                            quemado += "'%s'" % str(val.E1.valor)
                        else:
                            quemado += str(val.E1.valor)
                        val2 = ''
                        if isinstance(val.E2.valor, str):
                            quemado += "'%s'" % str(val.E2.valor)
                        else:
                            quemado += str(val.E2.valor)
                        #quemado += '%s ( %s , %s ),' % (val.nombre, val1, val2)
            elif isinstance(val, Time):
                quemado += '%s,' % val.get_quemado()
            elif isinstance(val, Id):
               quemado += val.id + ','
            elif isinstance(val, Primitivo):
                if isinstance(val.valor, str):
                    quemado += '\''+ str(val.valor) + '\','
                else:
                    quemado += str(val.valor) + ','

        quemado = quemado[:-1]
        quemado += ')'
        return quemado


    def getC3D(self, lista_Optim):
        etiqueta = GeneradorTemporales.nuevo_temporal()
        code = '\n     # ---------INSERT INTO----------- \n'
        code += '    top_stack = top_stack + 1 \n'
        code += '    %s = ' % etiqueta
        code += '\"insert into ' + self.id
        ides = ''
        if self.listaId is not None:
            code += '('
            for ide in self.listaId:
                ides += ide.id + ','
            ids = list(ides)
            size = len(ids) - 1
            del (ids[size])
            s = "".join(ids)
            code += s + ') values('
        else:
            code += ' values ('
        values = ''
        for val in self.values:
            if isinstance(val, Math_):
                if val.E1 == None and val.E2 == None:
                    values += '%s,' % val.nombre
                else:
                    if val.E2 == None:
                        val1 = ''
                        if isinstance(val.E1.valor, str):
                            val1 = "'%s'" % str(val.E1.valor)
                        else:
                            val1 = str(val.E1.valor)
                        values += '%s ( %s ),' % (val.nombre, val1)
                    else:
                        val1 = ''
                        if isinstance(val.E1.valor, str):
                            val1 = "'%s'" % str(val.E1.valor)
                        else:
                            val1 = str(val.E1.valor)
                        val2 = ''
                        if isinstance(val.E2.valor, str):
                            val2 = "'%s'" % str(val.E2.valor)
                        else:
                            val2 = str(val.E2.valor)
                        values += '%s ( %s , %s ),' % (val.nombre, val1, val2)
            elif isinstance(val, Time):
                values += '%s,' % val.getC3D()
            elif isinstance(val, Id):
                values += val.id
            elif isinstance(val, Funcion):
                lista_expresiones = ''
                if val.listaexpresiones is not None:
                    for expresion in val.listaexpresiones:
                        if isinstance(expresion, Primitivo):
                            if isinstance(expresion.valor, str):
                                temporal = "'%s'" % expresion.valor
                            else:
                                temporal = str(expresion.valor)
                            if lista_expresiones == '':
                                lista_expresiones = temporal
                            else:
                                lista_expresiones += ', %s' % temporal
                values += '%s(%s),' % (val.id, lista_expresiones)
            elif isinstance(val, Primitivo):
                if isinstance(val.valor, str):
                    values += '\''+ str(val.valor) + '\','
                else:
                    values += str(val.valor) + ','
        vals = list(values)
        size = len(vals) - 1
        del (vals[size])
        v = "".join(vals)
        code += v
        code += ')'
        code += ';\" \n'
        code += '    stack[top_stack] = %s \n' % etiqueta
        return code


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


                    #print("caso1")
                    for data in insertinto.listaId:
                        contador = 1
                        for columna in entornoTabla.simbolos:
                            if data.id == columna:
                                indices_a_buscar.append(contador)

                                break
                            contador=contador+1

                    #print(indices_a_buscar)

                    lista = entornoTabla.simbolos
                    contador = 1
                    for columna in lista:

                        if not contador in indices_a_buscar:
                            #print("((((((((((((((((((((((((((((((((((((((")
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
                        pass#print("val :",data.valor)

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
                                consola.append("No se insertaron los datos, columnas inconsistentes")
                                todobien = False
                                break
                            contadoraux =contadoraux+1


                        if todobien:

                            insert(BD.id, simbolo_tabla.id, dataainsertar)

                            #consola.append(f"insert en la tabla {insertinto.id}, exitoso\n")
                        else:
                            consola.append(f"Campos insconsistentes")

                        consola.append(f"insert en la tabla {insertinto.id}, exitoso\n")
                    else:
                        consola.append(f"datos dectectados como no nulos")

                    todoBien=True
                else:
                    #print("caso 2")

                    if len(insertinto.values) == len(entornoTabla.simbolos):
                        i =0
                        todobien = True


                        for data in entornoTabla.simbolos:

                            todobien = comprobar_tipos(dataainsertar,i,insertinto.values,data,entornoTabla.simbolos,entornoTabla,consola,exceptions,BD,simbolo_tabla,ts)



                            if not todobien:
                                consola.append("No se insertaron los datos, columnas inconsistentes")
                                todobien= False
                                break

                            i=i+1

                        if todobien:

                            insert(BD.id,simbolo_tabla.id,dataainsertar)

                            consola.append(f"insert en la tabla {insertinto.id}, exitoso\n")
                        else:
                            consola.append(f"Campos insconsistentes")
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

def comprobar_tipos(datainsertar,index,lista_valores,campo,lista_tabla,ts,Consola,exception,bd,tabla,globall):
    #print("estoy aqui !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    todobien = False
#    #print(lista_valores[index].valor)
#    #print(date.fromisoformat(lista_valores[index].valor))
#    #print(isinstance(date.fromisoformat(lista_valores[index].valor),date))
#    #print('DATE' in str(lista_tabla.get(campo).tipo).upper())
    datafinal = None
    if isinstance(lista_valores[index],Instruccion):
        datafinal = Expresion.Resolver(lista_valores[index],ts,Consola,exception)
        datainsertar.append(datafinal)
    elif isinstance(lista_valores[index],Funcion):
        datafinal = EjecutarFuncion.ResolverFuncion(lista_valores[index],globall,Consola,exception)
        datainsertar.append(datafinal)
        EjecutarFuncion.limpiarFuncion(lista_valores[index],globall)
    else:
        datafinal = lista_valores[index].valor
        datainsertar.append(datafinal)
    #print(datafinal)


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
                todobien = comprobar_caracteristicas(lista_tabla.get(campo).valor, datafinal, Consola, exception, bd,
                                                     tabla, index)

        except:
            #print("error de tipo")
            todobien = False
    else:
        try:
            #print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5")
            #print(lista_tabla.get(campo).tipo)
            for data in globall.simbolos:
                pass#print(":: ",data)
            if globall.validar_sim(str(lista_tabla.get(campo).tipo).lower()) == 1:
                #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
                for data in ts.simbolos:
                    pass#print(";;; ",data)
                simbolo_enumo = globall.buscar_sim(str(lista_tabla.get(campo).tipo).lower())

                if datafinal in simbolo_enumo.valor:
                    todobien = True
                    Consola.append("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11")
            else:
                pass#print("no encotrado")
        except:
            todobien= False
    return todobien


def comprobarcheck(expresion,data,valor,nombre_columna,ts,Consola,exception):
    valor_retorno=True
    #print("que pedo",data)
    #if data == 1:
    #print("-> ",expresion)
    if expresion != None:

        for datos in expresion:
            dataiz = datos.iz
            datade = datos.dr
            operador= datos.operador
            if nombre_columna != dataiz.id:
                valor_retorno=False
                break
            valor_retorno = Expresion.Resolver(Expresion(Primitivo(valor,1,1),datade,operador,1,1),ts,Consola,exception)



    return valor_retorno



def comprobar_caracteristicas(tipo_caracteristica,data,Consola,Exception,nombre_bd,nombre_tabla,posicion):
    devolver=True
    #print("->>>>>",tipo_caracteristica)
    if tipo_caracteristica != None:
        #print("aqui estamos")

        for caracteristica in tipo_caracteristica:
            #print(caracteristica)
            if "NOTNULL" in str(caracteristica):

                if data == None:
                    Consola.append("Dato encontrado con not null, debe llevar un valor")
                    devolver=False
                    break
            elif "UNIQUE" in str(caracteristica) or "PRIMARYKEY" in str(caracteristica):
                #print(nombre_bd.id,nombre_tabla.id)
                datas = extractTable(nombre_bd.id,nombre_tabla.id)
                #print("unique or primary ->  ",posicion)
                for fila in datas:
                    if str(fila[posicion])== str(data):
                        devolver= False
                        Consola.append("Constraint unique active")
                    #print(fila[posicion])


                #print(data)

    return  devolver
