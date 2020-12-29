import AST.Nodo as Node
from prettytable import PrettyTable
from Errores.Nodo_Error import *
import data.jsonMode as jm
import os
from operator import itemgetter
import AST.Where as wh
import TypeCheck.Type_Checker as tp


class Select(Node.Nodo):
    def __init__(self, *args):
        if args[0] == '*':
            self.arguments = None
            self.tables = args[1]
            self.line = args[5]
            self.column = args[6]
            self.conditions = args[2]
            self.grp = args[3]
            self.ord = args[4]
            self.result_query = PrettyTable()
        else:
            self.arguments = args[0]
            self.tables = args[1]
            self.line = args[5]
            self.column = args[6]
            self.conditions = args[2]
            self.grp = args[3]
            self.ord = args[4]
            self.result_query = PrettyTable()

    def ejecutar(self, TS, Errores):
        columnas = []
        col_dict = {}
        tuplas = []
        tuplas_aux = []
        ordencol = []
        db = os.environ['DB']
        result = 'Query from tables: '
        contador = 0
        tablasError = []
        tableState = True
        #---------------------FROM
        if len(self.tables) != 0:
            for tabla in self.tables:
                while jm.extractTable(db, tabla) is not None:
                    tuplas += jm.extractTable(db, tabla)
                    col_dict += tp.showColumns(db, tabla)
                tablasError.append(tabla)
                tableState = False
        if tableState:
            #--------------------WHERE
            if isinstance(self.conditions, Where):
                self.conditions.ejecutar(TS, Errores)
            # ---------------------ORDER BY
            if self.ord is not None:
                for ord in self.ord:
                    ord.ejecutar(TS, Errores)
                    ord_dict = {
                        'columna': ord.columna,
                        'orden': ord.orden,
                        'nulls': ord.nulls
                    }
                    ordencol.append(ord_dict)
            if self.arguments is not None:
                for columna in self.arguments:
                    columna.ejecutar(TS, Errores)
                    if columna.op_type == 'as':
                        if columna.val.op_type == 'valor' or \
                                columna.val.op_type == 'Aritmetica' or \
                                columna.val.op_type == 'Relacional' or \
                                columna.val.op_type == 'Logica' or \
                                columna.val.op_type == 'unario':
                            tuplas_aux.append(columna.val.val)
                        columnas.append(columna.asid)
                    elif columna.op_type == 'valor':
                        columnas.append('Columna ' + str(contador))
                        tuplas_aux.append(columna.val)
                        contador = contador + 1
                    elif columna.op_type == 'iden':
                        columnas.append(columna.id)
                    else:
                        tuplas.append(columna.val)
                        columnas.append('Columna ' + str(contador))
                        contador = contador + 1
            else:
                columnas = list(col_dict.keys())

            if len(columnas) != 0:
                self.result_query.field_names = columnas

            cont = 0;
            if len(tuplas_aux) > 0:
                tuplas += [tuplas_aux]
            if len(tuplas) != 0:
                if ordencol is not None:
                    for dic in ordencol:
                        while dic['columna'] != columnas[cont]:
                            cont = cont + 1
                    for item in ordencol:
                        if item['orden'] == 'asc':
                            tuplas = sorted(tuplas, key=itemgetter(cont))
                        else:
                            tuplas = sorted(tuplas, key=itemgetter(cont), reverse=True)
                if isinstance(self.conditions, Where):
                    new_tuplas = []
                    for tupla in tuplas:
                        if self.conditions.dictionary['val'] in tupla:
                            new_tuplas.append(tupla)
                    tuplas = new_tuplas
                if len(tuplas[0]) == len(columnas):
                    for tupla in tuplas:
                        self.result_query.add_row(tupla)
                else:
                    new_tuplas2 = []
                    indices = []
                    index = 0
                    for col in col_dict.keys():
                        if col == columnas[index]:
                            indices.append(index)
                            index = index + 1
                    for ind in indices:
                        new_tuplas2 = list(map(itemgetter(ind), tuplas))
                    print(new_tuplas2)
        else:
            tabless = ''
            for tabla in tablasError:
                Errores.insertar(Nodo_Error('42P01', 'undefined_table', self.line, self.column))
                tabless += str(tabla) + ' '
            result = '42P01: <<' + str(tabless) + '>> UNDEFINED TABLE(S)'
            return result
        if self.tables is not []:
            for obj in self.tables:
                result += str(obj) + ' '
        result += '\n' + self.result_query.get_string()
        return result

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        pass

class Insert(Node.Nodo):
    def __init__(self, table_id, col, values, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.table_id = table_id
        self.col = col
        self.values = values

    def ejecutar(self, TS, Errores):
        bd = os.environ['DB']
        infoTB = tp.showColumns(bd, self.table_id)  # datos de tabla
        noCol = len(infoTB)
        nombreCol = list(infoTB.keys())
        TiposCol = list(infoTB.values())
        tipos = []
        val = []  # valores
        noValores = len(self.values)  # noValues
        for columna in self.values:
            columna.ejecutar(TS, Errores)
            val.append(columna.val)
            tipos.append(columna.type)

        if self.col != None:
            noc = len(self.col)
            if noc == noCol:
                for nn, ss in enumerate(self.col):
                    if ss == nombreCol[nn]:
                        pass
                    else:
                        Errores.insertar(Nodo_Error(
                            '42P10', 'invalid_column_reference', self.fila, self.columna))
                        return '42P10 : invalid_column_reference'
                for n, s in enumerate(TiposCol):
                    k = list(s.values())
                    if(k[0] == 'integer' or k[0] == 'smallint' or k[0] == 'bigint' or k[0] == 'decimal' or k[0] == 'numeric' or k[0]=='double' or k[0] == 'money'):
                        if (tipos[n] == 'INT' or tipos[n] == 'DOUBLE' or tipos[n] == 'FLOAT'):
                            if len(str(val[n])) <= k[1]:
                                pass
                            else: 
                                Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                                return '22023 : invalid_parameter_value'
                        else:
                             Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                             return '22023 : invalid_parameter_value'        
                    elif(k[0]== 'character varying' or k[0] == 'character' or k[0] == 'varchar' or k[0] == 'char' or k[0] == 'text'):
                        if (tipos[n] == 'CHAR' or tipos[n] == 'STR'):
                            if len(str(val[n])) <= k[1]:
                                pass
                            else: 
                                Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                                return '22023 : invalid_parameter_value'
                        else:
                             Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                             return '22023 : invalid_parameter_value'  
                    elif(k[0]== 'boolean'):
                        if (tipos[n] == 'BOOLEAN'):
                             pass
                        else:
                            Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                            return '22023 : invalid_parameter_value'
                    elif( k[0]== 'date'):
                        if (tipos[n] == 'DATE'):
                            if len(str(val[n])) <= k[1]:
                                pass
                            else: 
                                Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                                return '22023 : invalid_parameter_value'
                        else:
                            Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                            return '22023 : invalid_parameter_value'
                    else: 
                        res1 = tp.obtenerTiposEnum(k[0])
                        if val[n] in res1:
                            pass
                        else: 
                            Errores.insertar(Nodo_Error(
                                     '22023', 'invalid_parameter_value', self.fila, self.columna))
                            return '22023 : invalid_parameter_value'
                respuesta = jm.insert(bd,self.table_id,val)
                if respuesta == 2:  # noexisteDB
                        Errores.insertar(Nodo_Error(
                            '08003', 'connection_does_not_exist', self.fila, self.columna))
                        return '08003: ' + str(bd) + ' connection_does_not_exist\n'
                elif respuesta == 3:  # noexisteTB
                        Errores.insertar(Nodo_Error(
                            '42P01', 'undefined_table', self.fila, self.columna))
                        return '42P01: ' + str(self.table_id) + ' undefined_table \n'
                elif respuesta == 5:  # noColDiferente
                        Errores.insertar(Nodo_Error(
                            'HV008', 'fdw_invalid_column_number', self.fila, self.columna))
                        return 'HV008: fdw_invalid_column_number \n'
                elif respuesta == 4:  # Pk_duplicada
                        Errores.insertar(Nodo_Error(
                            '42710', 'duplicate_object', self.fila, self.columna))
                        return '42710: duplicate_object  \n'
                elif respuesta == 1:  # error
                        Errores.insertar(Nodo_Error(
                            'XX000', 'internal_error', self.fila, self.columna))
                        return 'XX000: internal_error \n'
                else:
            
                        for n, s in enumerate(TiposCol):
                            k = list(s.values())
                            r = nombreCol[n] #nombrecol
                            a = k[0]        #tipo dato
                            b = k[1]        #size
                            #tts.TabladeSimbolos.insertar(r,a,b,self.table_id,self.fila,self.columna,'Insert')
                        return 'Se ingresaron los registros exitosamente \n'
            else:
                Errores.insertar(Nodo_Error(
                    'HV008', 'fdw_invalid_column_number', self.fila, self.columna))
                return 'HV008: fdw_invalid_column_number \n'    
        else:
            if noValores == noCol:
                for n, s in enumerate(TiposCol):
                    k = list(s.values())
                    if(k[0] == 'integer' or k[0] == 'smallint' or k[0] == 'bigint' or k[0] == 'decimal' or k[0] == 'numeric' or k[0]=='double' or k[0] == 'money'):
                        if (tipos[n] == 'INT' or tipos[n] == 'DOUBLE' or tipos[n] == 'FLOAT'):
                            if len(str(val[n])) <= k[1]:
                                pass
                            else: 
                                Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                                return '22023 : invalid_parameter_value'
                        else:
                             Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                             return '22023 : invalid_parameter_value'        
                    elif(k[0]== 'character varying' or k[0] == 'character' or k[0] == 'varchar' or k[0] == 'char' or k[0] == 'text'):
                        if (tipos[n] == 'CHAR' or tipos[n] == 'STR'):
                            if len(str(val[n])) <= k[1]:
                                pass
                            else: 
                                Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                                return '22023 : invalid_parameter_value'
                        else:
                             Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                             return '22023 : invalid_parameter_value'  
                    elif(k[0]== 'boolean'):
                        if (tipos[n] == 'BOOLEAN'):
                             pass
                        else:
                            Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                            return '22023 : invalid_parameter_value'
                    elif( k[0]== 'date'):
                        if (tipos[n] == 'DATE'):
                            if len(str(val[n])) <= k[1]:
                                pass
                            else: 
                                Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                                return '22023 : invalid_parameter_value'
                        else:
                            Errores.insertar(Nodo_Error(
                                 '22023', 'invalid_parameter_value', self.fila, self.columna))
                            return '22023 : invalid_parameter_value'
                    else: 
                        res1 = tp.obtenerTiposEnum(k[0])
                        if val[n] in res1:
                            pass
                        else: 
                            Errores.insertar(Nodo_Error(
                                     '22023', 'invalid_parameter_value', self.fila, self.columna))
                            return '22023 : invalid_parameter_value'

                respuesta = jm.insert(bd,self.table_id,val)
                if respuesta == 2:  # noexisteDB
                        Errores.insertar(Nodo_Error(
                            '08003', 'connection_does_not_exist', self.fila, self.columna))
                        return '08003: ' + str(bd) + ' connection_does_not_exist\n'
                elif respuesta == 3:  # noexisteTB
                        Errores.insertar(Nodo_Error(
                            '42P01', 'undefined_table', self.fila, self.columna))
                        return '42P01: ' + str(self.table_id) + ' undefined_table \n'
                elif respuesta == 5:  # noColDiferente
                        Errores.insertar(Nodo_Error(
                            'HV008', 'fdw_invalid_column_number', self.fila, self.columna))
                        return 'HV008: fdw_invalid_column_number \n'
                elif respuesta == 4:  # Pk_duplicada
                        Errores.insertar(Nodo_Error(
                            '42710', 'duplicate_object', self.fila, self.columna))
                        return '42710: duplicate_object  \n'
                elif respuesta == 1:  # error
                        Errores.insertar(Nodo_Error(
                            'XX000', 'internal_error', self.fila, self.columna))
                        return 'XX000: internal_error \n'
                else:
                        for n, s in enumerate(TiposCol):
                            k = list(s.values())
                            r = nombreCol[n] #nombrecol
                            a = k[0]        #tipo dato
                            b = k[1]        #size
                            #tts.TabladeSimbolos.insertar(r,a,b,self.table_id,self.fila,self.columna,'Insert')
                        return 'Se ingresaron los registros exitosamente \n'
            else:
                Errores.insertar(Nodo_Error(
                    'HV008', 'fdw_invalid_column_number', self.fila, self.columna))
                return 'HV008: fdw_invalid_column_number \n'    
      
    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_TB%s" % self.mi_id, 'TB: %s' % self.table_id)
        grafica.edge(self.mi_id, "nombre_TB" + self.mi_id)

        if self.col != None:
            lista_col = "columnas%s" % self.mi_id
            grafica.node(lista_col, 'columnas')
            grafica.edge(self.mi_id, lista_col)
            for i, elem in enumerate(self.col):
                col_id = "%selem%s" % (str(i), self.mi_id)
                grafica.node(col_id, elem)
                grafica.edge(lista_col, col_id)

        lista_valores = "valores%s" % self.mi_id
        grafica.node(lista_valores, 'valores')
        grafica.edge(self.mi_id, lista_valores)
        c = 0
        for n in self.values:
            grafica.node("%sValores%s" % (str(c), self.mi_id), str(n.val))
            grafica.edge(lista_valores, "%sValores%s" % (str(c), self.mi_id))
            c += 1

class Update(Node.Nodo):
    def __init__(self, table_id, list_exp, clausula, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.table_id = table_id
        self.list_exp = list_exp
        self.clausula = clausula

    def ejecutar(self, TS, Errores):
        bd = os.environ['DB']
    
        registros = {} #se crea el diccionario de registros 
        for i in self.list_exp:
            i.ejecutar(TS,Errores)
            registros[i.exp1.val] = i.exp2.val        
            print(registros)

        if self.clausula != None:
            try:
                respuesta = jm.update(bd,table_id,registros)
                if respuesta == 2 :#noDB
                    Errores.insertar(Nodo_Error('08003', 'connection_does_not_exist', self.fila, self.columna))
                    return '08003: connection_does_not_exist\n'
                elif respuesta == 3 : #noTB
                    Errores.insertar(Nodo_Error('HV00R', 'fdw_table_not_found', self.fila, self.columna))
                    return 'HV00R: fdw_table_not_found \n'
                elif respuesta == 4 :#noPK
                    Errores.insertar(Nodo_Error('P0002', 'no_data_found ', self.fila, self.columna))
                    return 'P0002: no_data_found \n'
                elif respuesta == 1 : #error
                    Errores.insertar(Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                    return 'XX000: internal_error \n'
                elif respuesta == 0 :
                    return 'Se actualizaron los registros de la tabla \n'
            except:
                Errores.insertar(Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                return 'XX000: internal_error \n'
        else:
            try:
                respuesta = jm.update(bd,self.table_id,registros)
                if respuesta == 2 :#noDB
                    Errores.insertar(Nodo_Error('08003', 'connection_does_not_exist', self.fila, self.columna))
                    return '08003: connection_does_not_exist\n'
                elif respuesta == 3 : #noTB
                    Errores.insertar(Nodo_Error('HV00R', 'fdw_table_not_found', self.fila, self.columna))
                    return 'HV00R: fdw_table_not_found \n'
                elif respuesta == 4 :#noPK
                    Errores.insertar(Nodo_Error('P0002', 'no_data_found ', self.fila, self.columna))
                    return 'P0002: no_data_found \n'
                elif respuesta == 1 : #error
                    Errores.insertar(Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                    return 'XX000: internal_error \n'
                elif respuesta == 0 :
                    return 'Se actualizaron los registros de la tabla \n'
            except:
                Errores.insertar(Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                return 'XX000: internal_error \n'

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_TB%s" % self.mi_id, 'TB: %s' % self.table_id)
        grafica.edge(self.mi_id, "nombre_TB" + self.mi_id)

        lista_valores = "columnas%s" % self.mi_id
        grafica.node(lista_valores,'columnas')
        grafica.edge(self.mi_id,lista_valores)
        c = 0
        for n in self.list_exp:
            grafica.node("%scolumnas%s" % (str(c),self.mi_id),' %s%s%s' % (str(n.exp1.val),n.op,str(n.exp2.val)))
            grafica.edge(lista_valores,"%scolumnas%s" % (str(c),self.mi_id))
            c += 1

        if self.clausula != '':
            print(self.clausula)
            grafica.node("Condicion%s" % self.mi_id, 'where: %s%s%s' % (str(self.clausula.exp1.val),self.clausula.op,str(self.clausula.exp2.val)))
            grafica.edge(self.mi_id, "Condicion"+self.mi_id)

class Delete(Node.Nodo): 
    def __init__(self, id, condicion, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.id = id
        self.condicion = condicion

    def ejecutar(self, TS, Errores):
            bd = os.environ['DB']
            infoTB = tp.showColumns(bd,self.id) #datos de tabla
            nombreCol = list(infoTB.keys())
            TiposCol = list(infoTB.values())

            if self.condicion != '':
                col = self.condicion.exp1.id
                op = self.condicion.op
                valor = self.condicion.exp2.val

                if col in nombreCol : 
                    noColumna = nombreCol.index(col) #indice col 
                    npPK = tp.showPrimaryKeys(bd,self.id) #retorna nombre
                    indicePK = nombreCol.index(npPK[0]) #indice pk
                    try:
                        res = wh.evaluar(bd,self.id,col,op,valor,noColumna,indicePK,'delete')
                        respuesta = jm.delete(bd,self.id,res)
                        if respuesta == 2:  # noexisteDB
                            Errores.insertar(Nodo_Error('08003', 'connection_does_not_exist', self.fila, self.columna))
                            return '08003: connection_does_not_exist\n'
                        elif respuesta == 3:  # noexisteTB
                            Errores.insertar(Nodo_Error('HV00R', 'fdw_table_not_found', self.fila, self.columna))
                            return 'HV00R: fdw_table_not_found \n'
                        elif respuesta == 4:  # noexistePk
                            Errores.insertar(Nodo_Error('P0002', 'no_data_found ', self.fila, self.columna))
                            return 'P0002: no_data_found \n'
                        elif respuesta == 1:  # error
                            Errores.insertar(Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                            return 'XX000: internal_error \n'
                        else:
                            return 'Se eliminaron los registros de la tabla \n'
                    except:
                        Errores.insertar(Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                        return 'XX000: internal_error \n'
                else: 
                    Errores.insertar(Nodo_Error('42P10', 'invalid_column_reference ', self.fila, self.columna))
                    return '42P10 : invalid_column_reference \n'
            else: #elimina todos los registros 
                respuesta = jm.truncate(bd, self.id)
                if respuesta == 2:  # noexisteDB
                    Errores.insertar(Nodo_Error('08003', 'connection_does_not_exist', self.fila, self.columna))
                    return '08003: ' + str(bd)  +' connection_does_not_exist\n'
                elif respuesta == 3:  # noexisteTB
                    Errores.insertar(Nodo_Error('42P01', 'undefined_table', self.fila, self.columna))
                    return '42P01: ' + str(self.id)  +'undefined_table \n'
                elif respuesta == 1:  # error
                    Errores.insertar(Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                    return 'XX000: internal_error \n'
                else:
                    return 'Se eliminaron los registros de la tabla ' + str(self.id) 

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_TB%s" % self.mi_id, 'id: %s' % self.id)
        grafica.edge(self.mi_id, "nombre_TB" + self.mi_id)

        if self.condicion != '': 
            grafica.node("Condicion%s" % self.mi_id, 'where: %s%s%s' % (str(self.condicion.exp1.id),self.condicion.op,str(self.condicion.exp2.val)))
            grafica.edge(self.mi_id, "Condicion"+self.mi_id)



class UseDB(Node.Nodo):
    def __init__(self, id, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.id = id

    def ejecutar(self, TS, Errores):
        if not self.id in jm.showDatabases():
            Errores.insertar(Nodo_Error("TytusDB: 08003", "\'" + str(self.id) +
                                        "\' connection_does_not_exist", self.fila, self.columna))
            return 'TytusDB: 08003, ' + str(self.id) + ' connection_does_not_exist'
        else:
            os.environ['DB'] = str(self.id)
            return 'Base de Datos ' + str(self.id) + ' seleccionada.'

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_DB%s" % self.mi_id, 'TB: %s' % self.id)
        grafica.edge(self.mi_id, "nombre_DB" + self.mi_id)



class Order(Node.Nodo):
    def __init__(self, *args):
        if len(args) == 5:
            self.columna = args[0]
            self.orden = args[1]
            self.nulls = args[2]
            self.line = args[3]
            self.column = args[4]
        elif len(args) == 4:
            self.columna = args[0]
            self.orden = args[1]
            self.nulls = None
            self.line = args[2]
            self.column = args[3]
        else:
            self.columna = args[0]
            self.orden = 'asc'
            self.nulls = None
            self.line = args[1]
            self.column = args[2]

    def ejecutar(self, TS, Errores):
        self.columna.ejecutar(TS, Errores)
        self.columna = self.columna.id
        if self.orden is not None:
            print(self.orden)
        if self.nulls is not None:
            print(self.nulls)
        return self

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        return 1


class Where(Node.Nodo):
    def __init__(self, *args):
        self.exp = args[0]
        self.dictionary = {}
        self.line = args[1]
        self.column = args[2]

    def ejecutar(self, TS, Errores):
        self.exp.ejecutar(TS, Errores)
        if self.exp.op_type == 'Relacional':
            self.dictionary = {
                'columna': self.exp.exp1.id,
                'val': self.exp.exp2.val
            }
        return self

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        return 1
