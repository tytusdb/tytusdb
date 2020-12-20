import AST.Nodo as Node
from TablaSimbolos.Tipos import *
from prettytable import PrettyTable
from Errores.Nodo_Error import *
import data.jsonMode as jm
import os
import json


class Select(Node.Nodo):
    def __init__(self, *args):
        if args[0] == '*':
            self.arguments = None
            self.tables = [args[1]]
            self.line = args[3]
            self.column = args[4]
            self.conditions = args[2]
            self.result_query = PrettyTable()
        else:
            self.arguments = args[0]
            self.tables = args[1]
            self.line = args[3]
            self.column = args[4]
            self.conditions = args[2]
            self.result_query = PrettyTable()

    def ejecutar(self, TS, Errores):
        columnas = []
        result = 'Query from tables: '
        for columna in self.arguments:
            columna.ejecutar(TS, Errores)
            columnas.append(columna.val)
        self.result_query.field_names = columnas
        for obj in self.tables:
            result += str(obj)
        db = os.environ['DB']
        #jm.extractRow(db, self.tables, self.arguments)
        result += '\n' + self.result_query.get_string()
        return result

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        return 1

class Insert(Node.Nodo):
    def __init__(self, table_id,col, values, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.table_id = table_id
        self.col = col
        self.values = values

    def ejecutar(self, TS, Errores): #falta la funcion de insertar solo ciertas columnas 
        bd = os.environ['DB']
        tipos = [] #verifica que los tipos coincidan
        val =[]
        for columna in self.values:
            columna.ejecutar(TS, Errores)
            val.append(columna.val)
            tipos.append(columna.type)
        respuesta = jm.insert(bd,self.table_id,val)
        if respuesta == 2:  # noexisteDB
            Errores.insertar(Nodo_Error('08003', 'connection_does_not_exist', self.fila, self.columna))
            return '08003: ' + str(bd) + ' connection_does_not_exist\n'
        elif respuesta == 3:  # noexisteTB
            Errores.insertar(Nodo_Error('42P01', 'undefined_table', self.fila, self.columna))
            return '42P01: ' + str(self.table_id)  +' undefined_table \n'
        elif respuesta == 5: #noColDiferente
            Errores.insertar(Nodo_Error('HV008', 'fdw_invalid_column_number', self.fila, self.columna))
            return 'HV008: fdw_invalid_column_number \n'
        elif respuesta == 4: #Pk_duplicada
            Errores.insertar(Nodo_Error('42710', 'duplicate_object', self.fila, self.columna))
            return '42710: duplicate_object  \n'
        elif respuesta == 1:  # error
            Errores.insertar(Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
            return 'XX000: internal_error \n'
        else:
            return 'Se ingresaron los registros exitosamente \n'

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_TB%s" % self.mi_id, 'id: %s' % self.table_id)
        grafica.edge(self.mi_id, "nombre_TB" + self.mi_id) 

        if self.col != None:
            lista_col = "columnas%s" % self.mi_id
            grafica.node(lista_col, 'columnas')
            grafica.edge(self.mi_id, lista_col)
            for i, elem in enumerate(self.col):
                col_id = "%selem%s" % (str(i), self.mi_id)
                grafica.node(col_id, elem)
                grafica.edge(lista_col, col_id)

class Update(Node.Nodo):
    def __init__(self, table_id, list_id, list_values, file, col):
        self.table_id = table_id
        self.list_id = list_id
        self.values = list_values
        self.fila = file
        self.columna = col

    def ejecutar(self, TS, Errores):
        return 1

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_TB%s" % self.mi_id, 'id: %s' % self.table_id)
        grafica.edge(self.mi_id, "nombre_TB" + self.mi_id)



class Delete(Node.Nodo): 
    def __init__(self, id, condicion, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.id = id
        self.condicion = condicion

    def ejecutar(self, TS, Errores):
        bd = os.environ['DB']

        if self.condicion != '':
            self.condicion.ejecutar(TS, Errores)
            valor = self.condicion.exp2.val
            col = self.condicion.exp1.val      #se tiene que verificar el index de la columna 
            res= jm.extractTable(bd,self.id)
            c = 0
            valores = []
            for n in res:
                for k in n: 
                    if k == valor:
                        valores.append(c)
                c += 1
            respuesta = jm.delete(bd,self.id,valores)
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
            grafica.node("Condicion%s" % self.mi_id, 'where: %s%s' %
                         (self.condicion.op,str(self.condicion.exp2.val)))
            grafica.edge(self.mi_id, "Condicion"+self.mi_id)

class UseDB(Node.Nodo):
    def __init__(self, id, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.id = id

    def ejecutar(self, TS, Errores):
        if not self.id in jm.showDatabases():
            Errores.insertar(Nodo_Error("TytusDB: 08003", "\'" + str(self.id) + "\' connection_does_not_exist", self.fila, self.columna))
            return 'TytusDB: 08003, '+ str(self.id) + ' connection_does_not_exist'
        else: 
            os.environ['DB'] = str(self.id)
            return 'Base de Datos ' + str(self.id) + ' seleccionada.'

    def getC3D(self, TS):
        return ""

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_DB%s" % self.mi_id, 'id: %s' % self.id)
        grafica.edge(self.mi_id, "nombre_DB" + self.mi_id)




