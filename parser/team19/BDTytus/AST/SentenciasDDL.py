from AST.Nodo import Nodo
import data.jsonMode as JM
import Errores.Nodo_Error as err
from prettytable import PrettyTable

class CreateDatabase(Nodo):
    def __init__(self, fila, columna, nombre_BD, or_replace = False, if_not_exist =False, owner = None, mode = 1):
        super().__init__(fila, columna)
        self.nombre_DB = nombre_BD.lower()
        self.or_replace = or_replace
        self.if_not_exist = if_not_exist
        self.owner = owner
        self.mode = mode

    def ejecutar(self,TS,Errores):#No se toca el owner para esta fase
        if self.if_not_exist:
            if self.nombre_DB in JM.showDatabases():
                Errores.insertar(err.Nodo_Error('42P04', 'duplicated database', self.fila, self.columna))
                return '42P04: duplicated database\n'

        if self.or_replace:
            respuesta = JM.dropDatabase(self.nombre_DB)
            if respuesta == 1:
                Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                return 'XX000: internal_error\n'

        if self.mode > 5 or self.mode < 1:
            Errores.insertar(err.Nodo_Error('Semantico', 'El modo debe estar entre 1 y 5', self.fila, self.columna))
            return 'Error semantico: El modo debe estar entre 1 y 5\n'
        
        respuesta = JM.createDatabase(self.nombre_DB)
        if respuesta == 2:
            Errores.insertar(err.Nodo_Error('42P04', 'duplicated database', self.fila, self.columna))
            return '42P04: duplicated database\n'
        if respuesta == 1:
            Errores.insertar(err.Nodo_Error('P0000', 'plpgsql_error', self.fila, self.columna))
            return 'P0000: plpgsql_error\n'
        return 'BASE DE DATOS %s CREADA\n' % self.nombre_DB
            

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        if self.or_replace:
            grafica.node("orReplaceCreateDB%s" % self.mi_id, 'Or Replace')
            grafica.edge(self.mi_id, "orReplaceCreateDB%s" % self.mi_id)
        if self.if_not_exist:
            grafica.node("ifNotExistCreateDB%s" % self.mi_id, 'If Not Exist')
            grafica.edge(self.mi_id, "ifNotExistCreateDB%s" % self.mi_id)
        grafica.node("nombreCreateDB%s" % self.mi_id, 'nombre BD: %s' % self.nombre_DB)
        grafica.edge(self.mi_id, "nombreCreateDB%s" % self.mi_id)
        if self.owner is not None:
            grafica.node("ownerCreateDB%s" % self.mi_id, 'Owner: %s' % self.owner)
            grafica.edge(self.mi_id, "ownerCreateDB%s" % self.mi_id)
        grafica.node("modeCreateDB%s" % self.mi_id, 'Mode: %s' % self.mode)
        grafica.edge(self.mi_id, "modeCreateDB%s" % self.mi_id)

class ShowDatabases(Nodo):
    def __init__(self, fila, columna):
        super().__init__(fila=fila, columna=columna)

    def ejecutar(self,TS,Errores):
        databases = JM.showDatabases()
        respuesta = PrettyTable()
        respuesta.field_names = ["DBName"]
        for nombre_db in databases:
            respuesta.add_row([nombre_db])
        return respuesta.get_string() + '\n'

    def getC3D(self,TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)

class CreateType(Nodo):
    def __init__(self, nombre_type, lista_enum, fila, columna):
        super().__init__(fila=fila, columna=columna)
        self.nombre_type = nombre_type
        self.lista_enum = lista_enum

    def ejecutar(self, TS, Errores):
        return ['Aqui se deben crear y guardar los tipos']

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node("nombre_type%s" % self.mi_id, 'nombre: %s' % self.nombre_type)
        grafica.edge(self.mi_id,"nombre_type"+self.mi_id)

        id_lista = "lista_type%s" % self.mi_id
        grafica.node(id_lista, 'lista_enum')
        grafica.edge(self.mi_id, id_lista)
        for i,enum in enumerate(self.lista_enum):
            enum_id = "%senum%s" % (str(i), self.mi_id)
            grafica.node(enum_id, enum)
            grafica.edge(id_lista, enum_id)


