#from Instrucciones.instruccion import Instruccion
from Analisis_Ascendente.Instrucciones.expresion import Id, Primitivo
from Analisis_Ascendente.Instrucciones.instruccion import Instruccion
#from storageManager.jsonMode import *
from Analisis_Ascendente.storageManager.jsonMode import *
#import Tabla_simbolos.TablaSimbolos as ts
import Analisis_Ascendente.Tabla_simbolos.TablaSimbolos as TS
import C3D.GeneradorTemporales as GeneradorTemporales
from Analisis_Ascendente.Instrucciones.instruccion import Tipo


class Alter(Instruccion):
    def __init__(self,caso, accion, ccc, id, tipo, check, id2, typeSet, id3,fila,columna):
        self.caso = caso
        self.accion = accion
        self.ccc = ccc
        self.id = id
        self.tipo = tipo
        self.check = check
        self.id2 = id2
        self.typeSet = typeSet
        self.id3 = id3
        self.fila = fila
        self.columna = columna

    def getC3D(self, lista_optimizaciones_C3D):
        if self.caso == 1: #ADD COLUMN listaID tipo
            lista_id = None
            for id_en_lista in self.id:
                if lista_id is None:
                    lista_id = id_en_lista.id
                else:
                    lista_id += ', %s' % id_en_lista.id
            tipo = ''
            lista_tipo = self.tipo.tipo.split('-')
            if len(lista_tipo) == 1:
                tipo = self.tipo.tipo
            elif len(lista_tipo) == 2:
                if lista_tipo[0] == 'CHARACTERVARYING':
                    tipo = 'CHARACTER VARYING ( %s )' % lista_tipo[1]
                else:
                    tipo = '%s ( %s )' % (lista_tipo[0], lista_tipo[1])
            else:
                tipo = '%s ( %s, %s )' % (lista_tipo[0], lista_tipo[1], lista_tipo[2])
            return 'add column %s %s' % (lista_id, tipo)
        elif self.caso == 2: #DROP COLUMN listaID
            lista_id = None
            for id_en_lista in self.id:
                if lista_id is None:
                    lista_id = id_en_lista.id
                else:
                    lista_id += ', %s' % id_en_lista.id
            return 'drop column %s' % lista_id
        elif self.caso == 3: #ADD CHECK PARIZQ checkprima PARDR
            izquierda = self.check.iz
            derecha = self.check.dr
            if isinstance(izquierda, Primitivo):
                if isinstance(izquierda.valor, str):
                    izquierda = "'%s'" % izquierda.valor
                else:
                    izquierda = izquierda.valor
            elif isinstance(izquierda, Id):
                izquierda = izquierda.id
            if isinstance(derecha, Primitivo):
                if isinstance(derecha.valor, str):
                    derecha = "'%s'" % derecha.valor
                else:
                    derecha = derecha.valor
            elif isinstance(derecha, Id):
                derecha = derecha.id
            return 'add check ( %s %s %s )' % (izquierda, self.valorDefault.operador, derecha)
        elif self.caso == 4: #DROP CONSTRAINT ID
            return 'drop constraint %s' % self.id
        elif self.caso == 5: #ADD FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR
            lista_id = None
            for id_en_lista in self.id:
                if lista_id is None:
                    lista_id = id_en_lista.id
                else:
                    lista_id += ', %s' % id_en_lista.id
            lista_id_ref = None
            for id_en_lista in self.id3:
                if lista_id_ref is None:
                    lista_id_ref = id_en_lista.id
                else:
                    lista_id_ref += ', %s' % id_en_lista.id
            return 'add foreign key ( %s ) references %s ( %s )' % (lista_id, self.id2, lista_id_ref)
        elif self.caso == 6: #ALTER COLUMN ID TYPE tipo
            tipo = ''
            lista_tipo = self.tipo.tipo.split('-')
            if len(lista_tipo) == 1:
                tipo = self.tipo.tipo
            elif len(lista_tipo) == 2:
                if lista_tipo[0] == 'CHARACTERVARYING':
                    tipo = 'CHARACTER VARYING ( %s )' % lista_tipo[1]
                else:
                    tipo = '%s ( %s )' % (lista_tipo[0], lista_tipo[1])
            else:
                tipo = '%s ( %s, %s )' % (lista_tipo[0], lista_tipo[1], lista_tipo[2])
            return 'alter column %s type %s' % (self.id, tipo)
        elif self.caso == 7: #ALTER COLUMN ID SET NOT NULL
            return 'alter column %s set not null' % self.id
        elif self.caso == 8: #ADD PRIMARY KEY PARIZQ listaID PARDR
            lista_id = None
            for id_en_lista in self.id:
                if lista_id is None:
                    lista_id = id_en_lista.id
                else:
                    lista_id += ', %s' % id_en_lista.id
            return 'add primary key ( %s )' % lista_id
        elif self.caso == 9: #ADD CONSTRAINT ID PRIMARY KEY PARIZQ listaID PARDR
            id = self.ccc[11:len(self.ccc)]
            lista_id = None
            for id_en_lista in self.id:
                if lista_id is None:
                    lista_id = id_en_lista.id
                else:
                    lista_id += ', %s' % id_en_lista.id
            return 'add constraint %s primary key ( %s )' % (id, lista_id)
        elif self.caso == 10: #ADD CONSTRAINT ID FOREIGN KEY PARIZQ listaID PARDR REFERENCES ID PARIZQ listaID PARDR
            id_constraint = self.ccc[11:len(self.ccc)]
            lista_id = None
            for id_en_lista in self.id:
                if lista_id is None:
                    lista_id = id_en_lista.id
                else:
                    lista_id += ', %s' % id_en_lista.id
            lista_id_ref = None
            for id_en_lista in self.id3:
                if lista_id_ref is None:
                    lista_id_ref = id_en_lista.id
                else:
                    lista_id_ref += ', %s' % id_en_lista.id
            return 'add constraint %s foreign key ( %s ) references %s ( %s )' % (id_constraint, lista_id, self.id2, lista_id_ref)
        elif self.caso == 11: #ADD CONSTRAINT ID UNIQUE PARIZQ listaID PARDR
            id_constraint = self.ccc[11:len(self.ccc)]
            lista_id = None
            for id_en_lista in self.id:
                if lista_id is None:
                    lista_id = id_en_lista.id
                else:
                    lista_id += ', %s' % id_en_lista.id
            return 'add constraint %s unique ( %s )' % (id_constraint, lista_id)




class AlterTable(Instruccion):
    def __init__(self, id, alter,fila,columna):
        self.id = id
        self.alter = alter
        self.fila = fila
        self.columna = columna


    def ejecutar(alterTable, ts, consola,exceptions):

        if ts.validar_sim("usedatabase1234") == 1:

            # nombre de la bd
            bdactual = ts.buscar_sim("usedatabase1234")
            # se busca el simbolo y por lo tanto se pide el entorno de la bd
            BD = ts.buscar_sim(bdactual.valor)
            entornoBD = BD.Entorno

            if entornoBD.validar_sim(alterTable.id) == 1:

                simbolo_tabla = entornoBD.buscar_sim(alterTable.id)
                entornoTabla = simbolo_tabla.Entorno

                banderaTodoBien = True

                for altirto in alterTable.alter:

                    if altirto.caso == 1:
                        #print("caso 1")
                        #alter table add column ( listaids)
                        for idcito in altirto.id:
                            if entornoTabla.validar_sim(idcito.id) == -1:
                                #print(idcito.id, "<-----------------------------------")
                                valores = []
                                columna_nueva = TS.Simbolo(TS.TIPO_DATO.CAMPO,idcito.id,altirto.tipo.tipo,valores,None)
                                simbolo_tabla.valor = simbolo_tabla.valor + 1
                                entornoTabla.agregar_sim(columna_nueva)
                                alterAddColumn(BD.id,simbolo_tabla.id,1)
                                consola.append(f"Alter ejecutado correctamente en tabla , {alterTable.id}, add column {idcito.id}")

                            else:
                                consola.append(f"42701 Duplicate column, No se puede agregar la columna {idcito}")
                                exceptions.append(f"Error semantico-42701 - Duplicate column, No se puede agregar la columna {idcito} -fila-columna")





                    elif altirto.caso == 2:
                        #print("caso 2")
                        #alter table drop column ( listaids)
                        for idcito in altirto.id:
                            if entornoTabla.validar_sim(idcito.id) == 1:
                                #print(idcito.id, "<-----------------------------------")
                                valores = []
                                #columna_nueva = TS.Simbolo(TS.TIPO_DATO.CAMPO,idcito.id,altirto.tipo.tipo,valores,None)
                                entornoTabla.eliminar_sim(idcito.id)
                                simbolo_tabla.valor = simbolo_tabla.valor-1;


                                alterDropColumn(BD.id,simbolo_tabla.id,len(entornoTabla.simbolos)-1)
                                consola.append(f"Alter ejecutado correctamente en tabla , {alterTable.id}, drop column {idcito.id}")

                            else:
                                consola.append(f"42703 Undefined column, No se puede eliminar la columna {idcito.id}")
                                exceptions.append(f"Error semantico-42701 - Duplicate column, No se puede agregar la columna  {idcito.id} - fila - columna")




                    elif altirto.caso == 3:
                        #print("caso 3")
                        #print(altirto.check)
                        datos = altirto.check



                        campo = datos.iz
                        #print(campo.id)
                        data2 = datos.dr
                        #print(data2)
                        ##print(data2.valor)
                        operador= datos.operador
                        #print(operador)

                        if entornoTabla.validar_sim(campo.id) == 1:

                            #
                            if isinstance(data2,Id):

                                if entornoTabla.validar_sim(data2.id) == 1:
                                    simbolo = entornoTabla.buscar_sim(campo.id)
                                    simbolo.valor.append(f"CHECK:{campo.id}:{operador}:{data2.id}")
                                    simbolo.Entorno = altirto.check
                                    nueva_Data = TS.Simbolo(simbolo.categoria, simbolo.id, simbolo.tipo, simbolo.valor,
                                                            simbolo.Entorno)
                                    entornoTabla.actualizar_sim(nueva_Data)
                                    # en los checks va el entorno de expresion
                                    consola.append(
                                        f"Add check hacia la tabla {alterTable.id}, en la columna {campo.id}\n")

                                else:
                                    consola.append(
                                        f"42703 Undefined column, No se puede agregar check a la columna {campo.id}")
                                    exceptions.append(
                                        f"Error semantico-42703 - Undefined, No se puede agregar la columna  {campo.id} - fila - columna")



                            else:
                                simbolo = entornoTabla.buscar_sim(campo.id)
                                simbolo.valor.append(f"CHECK:{campo.id}:{operador}:{data2.valor}")
                                simbolo.Entorno = altirto.check
                                nueva_Data = TS.Simbolo(simbolo.categoria,simbolo.id,simbolo.tipo,simbolo.valor,simbolo.Entorno)
                                entornoTabla.actualizar_sim(nueva_Data)
                                #en los checks va el entorno de expresion
                                consola.append(f"Add check hacia la tabla {alterTable.id}, en la columna {campo.id}\n")

                        else:
                            consola.append(f"42703 Undefined column, No se puede agregar check a la columna {campo.id}")
                            exceptions.append(
                                f"Error semantico-42703 - Undefined, No se puede agregar la columna  {campo.id} - fila - columna")




                    elif altirto.caso == 4:
                        #print("caso 4")

                        data_borrar = altirto.id

                        lista = entornoTabla.simbolos
                        for columna  in lista:
                            #print(columna)
                            indice = 0
                            banderaBorrar = False
                            for valor in lista.get(columna).valor:
                                #print(" ->",valor)
                                if "CONSTRAINT" in valor:
                                    nombre=str(valor).split(":")[1]
                                    #print("-- ",nombre, data_borrar)
                                    if nombre == data_borrar:
                                        banderaBorrar = True
                                        break
                                indice = indice + 1
                            if banderaBorrar:
                                break


                        #print(banderaBorrar, indice)
                        if banderaBorrar:
                            lista.get(columna).valor.pop(indice)
                            consola.append(f"Drop constraint eliminada de la tabla {alterTable.id}")
                        else:
                            consola.append(f"23000 integrity_constraint_violation, no se encontro el constraint{data_borrar} de la tabla {alterTable.id}")
                            exceptions.append(f"Error semantico- 23000-integrity_constraint_violation- fila - columna ")

                    elif altirto.caso == 5:
                        #print("caso 5")
                        # constraint
                        #print("")
                        banderaTodoBien = True
                        if entornoBD.validar_sim(altirto.id2) == 1:
                            # referencia la tabla a cual se desea hacer la llave foranea
                            obtener_simbolo = entornoBD.buscar_sim(altirto.id2)

                            entornoTablarefrencia = obtener_simbolo.Entorno

                            for campito in altirto.id3:
                                if entornoTablarefrencia.validar_sim(campito.id) == 1:
                                    pass#print("todo bien")
                                else:
                                    banderaTodoBien = False
                                    break;

                        if banderaTodoBien:

                            for idcito in altirto.id:

                                #print(idcito.id)
                                if entornoTabla.validar_sim(idcito.id) == 1:
                                    obtenerCampo = entornoTabla.buscar_sim(idcito.id)
                                    #print("ejecutando campos------------------------------------------!!!!!!1")
                                    tablita = []
                                    for dataReferencia in altirto.id3:
                                        tablita.append(dataReferencia.id)

                                    obtenerCampo.valor.append(f"FOREIGNKEY:{altirto.id2}:{tablita}")
                                    # para llegar antes debe validarse que existe la tabla y los campos a los cuales
                                    # se referencia
                                    consola.append(f"Add foreing key exitoso en la tabla {alterTable.id}\n")


                                else:
                                    consola.append(f"42P10	invalid_column_reference, Campo {idcito.id} no encontrado")
                                    exceptions.append("Error Semantico - 42P10- invalid_column_reference-fila-columna")
                                    valor = False
                            #print("")

                        else:
                            consola.append(
                                f"22005	error_in_assignment,No se creo el constraint {alterTable.id} campos incosistente \n")
                            exceptions.append(
                                "Error semantico-22005	error_in_assignment-Columnas check-fila-columna")



                    elif altirto.caso == 6:
                        #print("caso 6")

                        if entornoTabla.validar_sim(altirto.id) == 1:
                            data = entornoTabla.buscar_sim(altirto.id)
                            nueva_Data = TS.Simbolo(data.categoria, altirto.id, altirto.tipo.tipo, data.valor, data.Entorno)

                            entornoTabla.actualizar_sim(nueva_Data)
                            #print(altirto.tipo.tipo)
                            consola.append(f"Alter column realizado con exito en {altirto.id}\n")
                        else:
                            consola.append(f"No existe el campo {altirto.id}, Error alter columna")
                            exceptions.append(
                                f"Error semantico-22005	error_in_assignment-No se ha encontrado la columna {altirto.id}-fila-columna")


                    elif altirto.caso == 7:
                        #print("caso 6")

                        if entornoTabla.validar_sim(altirto.id) == 1:
                            data = entornoTabla.buscar_sim(altirto.id)
                            data.valor.append("NOTNULL")
                            nueva_Data = TS.Simbolo(data.categoria, altirto.id, data.tipo, data.valor,
                                                    data.Entorno)

                            entornoTabla.actualizar_sim(nueva_Data)

                            consola.append(f"Alter column realizado con exito en {altirto.id}\n")
                        else:
                            consola.append(f"No existe el campo {altirto.id}, Error alter columna")
                            exceptions.append(
                                f"Error semantico-22005	error_in_assignment-No se ha encontrado la columna {altirto.id}-fila-columna")

                    elif altirto.caso == 8:
                        #print("caso 8")
                        # constraint
                        #print("")
                        banderaTodoBien = True
                        valor=True
                        if banderaTodoBien:
                            pks = []
                            for idcito in altirto.id:

                                #print(idcito.id)

                                if entornoTabla.validar_sim(idcito.id) == 1:
                                    obtenerCampo = entornoTabla.buscar_sim(idcito.id)
                                    #print("ejecutando campos------------------------------------------!!!!!!1")



                                    obtenerCampo.valor.append(f"PRIMARYKEY")
                                    # para llegar antes debe validarse que existe la tabla y los campos a los cuales
                                    # se referencia
                                    consola.append(f"Add Constraint PRIMARY key exitoso en la tabla {alterTable.id}\n")
                                    i = 0
                                    for columna in entornoTabla.simbolos:
                                        if entornoTabla.simbolos.get(columna).id == idcito.id:
                                            pks.append(i)
                                        i = i+1

                                else:

                                    consola.append(
                                        f"42P10	invalid_column_reference, Campo {idcito.id} no encontrado")
                                    exceptions.append("Error Semantico - 42P10- invalid_column_reference-fila-columna")
                                    valor = False

                            if valor:
                                pass#print(pks)
                                #print(BD.id, simbolo_tabla.id, pks)
                                #print(alterAddPK(BD.id, simbolo_tabla.id, pks))
                                #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")




                    elif altirto.caso == 9:
                        #print("caso 9")
                        # constraint
                        #print("")
                        valor=True
                        if banderaTodoBien:
                            pks = []
                            for idcito in altirto.id:

                                #print(idcito.id)
                                if entornoTabla.validar_sim(idcito.id) == 1:
                                    obtenerCampo = entornoTabla.buscar_sim(idcito.id)
                                    #print("ejecutando campos------------------------------------------!!!!!!1")
                                    tablita = []
                                    for dataReferencia in altirto.id:
                                        tablita.append(dataReferencia.id)
                                        if str(altirto.ccc+":PRIMARYKEY") not in obtenerCampo.valor:
                                            obtenerCampo.valor.append(f"{altirto.ccc}:PRIMARYKEY")
                                    # para llegar antes debe validarse que existe la tabla y los campos a los cuales
                                    # se referencia
                                    consola.append(f"Add Constraint PRIMARY key exitoso en la tabla {alterTable.id}\n")
                                    i = 0
                                    for columna in entornoTabla.simbolos:
                                        if entornoTabla.simbolos.get(columna).id == idcito.id:
                                            pks.append(i)
                                        i = i+1


                                else:
                                    consola.append(
                                        f"42P10	invalid_column_reference, Campo {idcito.id} no encontrado")
                                    exceptions.append("Error Semantico - 42P10- invalid_column_reference-fila-columna")
                                    valor = False
                            if valor:
                                pass#print(pks)
                                #print(BD.id, simbolo_tabla.id, pks)
                                #print(alterAddPK(BD.id, simbolo_tabla.id, pks))
                                #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



                    elif altirto.caso == 10:
                        #print("caso 10")
                        # constraint
                        #print("")
                        banderaTodoBien = True
                        if entornoBD.validar_sim(altirto.id2) == 1:
                            # referencia la tabla a cual se desea hacer la llave foranea
                            obtener_simbolo = entornoBD.buscar_sim(altirto.id2)

                            entornoTablarefrencia = obtener_simbolo.Entorno

                            for campito in altirto.id3:
                                if entornoTablarefrencia.validar_sim(campito.id) == 1:
                                    pass#print("todo bien")
                                else:
                                    banderaTodoBien = False
                                    break;

                        if banderaTodoBien:

                            for idcito in altirto.id:

                                #print(idcito.id)
                                if entornoTabla.validar_sim(idcito.id) == 1:
                                    obtenerCampo = entornoTabla.buscar_sim(idcito.id)
                                    #print("ejecutando campos------------------------------------------!!!!!!1")
                                    tablita = []
                                    for dataReferencia in altirto.id3:
                                        tablita.append(dataReferencia.id)

                                    obtenerCampo.valor.append(f"{altirto.ccc}:FOREIGNKEY:{altirto.id2}:{tablita}")
                                    # para llegar antes debe validarse que existe la tabla y los campos a los cuales
                                    # se referencia
                                    consola.append(f"Add Constraint foreing key exitoso en la tabla {alterTable.id}\n")


                                else:
                                    consola.append(f"42P10	invalid_column_reference, Campo {idcito.id} no encontrado")
                                    exceptions.append("Error Semantico - 42P10- invalid_column_reference-fila-columna")
                                    valor = False
                            #print("")

                        else:
                            consola.append(
                                f"22005	error_in_assignment,No se creo el constraint {alterTable.id} campos incosistente \n")
                            exceptions.append(
                                "Error semantico-22005	error_in_assignment-Columnas check-fila-columna")



                    elif altirto.caso == 11:
                        #print("caso 8")
                        # constraint
                        #print("")
                        banderaTodoBien = True
                        if banderaTodoBien:

                            for idcito in altirto.id:

                                #print(idcito.id)
                                if entornoTabla.validar_sim(idcito.id) == 1:
                                    obtenerCampo = entornoTabla.buscar_sim(idcito.id)
                                    #print("ejecutando campos------------------------------------------!!!!!!1")
                                    tablita = []
                                    for dataReferencia in altirto.id:
                                        tablita.append(dataReferencia.id)
                                        obtenerCampo.valor.append(f"{altirto.ccc}:UNIQUE")
                                    # para llegar antes debe validarse que existe la tabla y los campos a los cuales
                                    # se referencia
                                    consola.append(f"Add UNIQUE constraint exitoso en la tabla {alterTable.id}\n")


                                else:
                                    consola.append(
                                        f"42P10	invalid_column_reference, Campo {idcito.id} no encontrado")
                                    exceptions.append("Error Semantico - 42P10- invalid_column_reference-fila-columna")
                                    valor = False

                if banderaTodoBien:
                    pass#print("todo correcto")
                else:
                    pass#print("todo mal")
            else:
                consola.append(f"42P01	undefined_table, no existe la tabla {alterTable.id}")
                exceptions.append(f"Error semantico-42P01- 42P01	undefined_table, no existe la tabla {alterTable.id}-fila-columna")




        else:
            consola.append("22005	error_in_assignment, No se ha seleccionado una BD\n")
            exceptions.append("Error semantico-22005	error_in_assignment-No se ha seleccionado DB-fila-columna")

    def getC3D(self, lista_optimizaciones_C3D):
        temporal1 = GeneradorTemporales.nuevo_temporal()
        codigo_quemado1 = 'alter table %s ' % self.id
        c3d = '''
    # ------------ALTER TABLE------------
    top_stack = top_stack + 1
    %s = "%s \\n"
''' % (temporal1, codigo_quemado1)
        temporal2 = GeneradorTemporales.nuevo_temporal()
        temporal2_anterior = temporal1
        for i, elemento_lista in enumerate(self.alter):
            c3d += '    %s = "%s \\n"\n' % (temporal2, elemento_lista.getC3D(lista_optimizaciones_C3D))
            c3d += '    %s = %s + %s\n' % (temporal2, temporal2_anterior, temporal2)
            if (i+1) != len(self.alter):
                temporal2_anterior = temporal2
                temporal2 = GeneradorTemporales.nuevo_temporal()
        temporal3 = GeneradorTemporales.nuevo_temporal()
        c3d += '''    %s = ";"
    %s = %s + %s 
    stack[top_stack] = %s 
''' % (temporal3, temporal3, temporal2, temporal3, temporal3)
        return c3d






