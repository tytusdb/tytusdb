from typing import Type
from AST.Nodo import Nodo
import data.jsonMode as JM
import Errores.Nodo_Error as err
from prettytable import PrettyTable
import TypeCheck.Type_Checker as TypeChecker


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
            if self.nombre_DB in TypeChecker.showDataBases():
                Errores.insertar(err.Nodo_Error('42P04', 'duplicated database', self.fila, self.columna))
                return '42P04: duplicated database\n'

        if self.or_replace:
            respuesta = TypeChecker.dropDataBase(self.nombre_DB)
            if respuesta == 1:
                Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                return 'XX000: internal_error\n'

        if self.mode > 5 or self.mode < 1:
            Errores.insertar(err.Nodo_Error('Semantico', 'El modo debe estar entre 1 y 5', self.fila, self.columna))
            return 'Error semantico: El modo debe estar entre 1 y 5\n'
        
        respuesta = TypeChecker.createDataBase(self.nombre_DB, self.mode, self.owner)
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
    def __init__(self, fila, columna, like_str = None):
        super().__init__(fila=fila, columna=columna)
        if like_str is not None:
            like_str = like_str.lower()
        self.like_str = like_str

    def ejecutar(self,TS,Errores):
        databases = TypeChecker.showDataBases()
        if self.like_str is not None:
            databases_con_filtro = []
            for nombre_db in databases:
                if self.like_str in nombre_db:
                    databases_con_filtro.append(nombre_db)
            databases = databases_con_filtro
        respuesta = PrettyTable()
        respuesta.field_names = ["DBName"]
        for nombre_db in databases:
            respuesta.add_row([nombre_db])
        return respuesta.get_string() + '\n'

    def getC3D(self,TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        if self.like_str is not None:
            grafica.node("like_str%s" % self.mi_id, 'Like: %s' % self.like_str)
            grafica.edge(self.mi_id, "like_str%s" % self.mi_id)

class AlterDatabase(Nodo):
    def __init__(self, fila, columna, nombre_DB, nuevo_nombre_DB = None, owner = None):
        super().__init__(fila=fila, columna=columna)
        self.nombre_DB = nombre_DB.lower()
        if nuevo_nombre_DB is not None:
            nuevo_nombre_DB = nuevo_nombre_DB.lower()
        elif owner is not None:
            owner = owner.lower()
        self.nuevo_nombre_DB = nuevo_nombre_DB
        self.owner = owner
        self.current_user = (owner == 'current_user')
        self.session_user = (owner == 'session_user')

    def ejecutar(self, TS, Errores):
        if self.nuevo_nombre_DB is not None:
            respuesta = TypeChecker.alterDataBase(self.nombre_DB, self.nuevo_nombre_DB)
            if respuesta == 1:
                Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                return 'XX000: internal_error\n'
            elif respuesta == 2:
                Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % self.nombre_DB, self.fila, self.columna))
                return '3D000: No existe base de datos <<%s>>' % self.nombre_DB
            elif respuesta == 3:
                Errores.insertar(err.Nodo_Error('42P04', 'duplicated database', self.fila, self.columna))
                return '42P04: duplicated database\n'
            return 'Base de datos %s, renombrada a: %s' % (self.nombre_DB, self.nuevo_nombre_DB)
        else:
            if self.current_user:
                return 'No hay implementacion para esto porque no se maneja usuario\n'
            elif self.session_user:
                return 'No hay implementacion para esto porque no se maneja usuario\n'
            else:
                respuesta = TypeChecker.alterDataBaseOwner(self.nombre_DB, self.owner)
                if respuesta == 1:
                    Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                    return 'XX000: internal_error\n'
                elif respuesta == 2:
                    Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % self.nombre_DB, self.fila, self.columna))
                    return '3D000: No existe base de datos <<%s>>' % self.nombre_DB
                return 'Owner de base de datos <<%s>>, cambiado a <<%s>>' % (self.nombre_DB, self.owner)

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node('nombre_DB%s' % self.mi_id, self.nombre_DB)
        grafica.edge(self.mi_id, 'nombre_DB%s' % self.mi_id)
        if self.nuevo_nombre_DB is not None:
            grafica.node('nuevo_nombre_DB%s' % self.mi_id, 'Nuevo: %s' % self.nuevo_nombre_DB)
            grafica.edge(self.mi_id, 'nuevo_nombre_DB%s' % self.mi_id)
        else:
            grafica.node('owner_user_DB%s' % self.mi_id, 'Owner: %s' % self.owner)
            grafica.edge(self.mi_id, 'owner_user_DB%s' % self.mi_id)    
            
class DropDatabase(Nodo):
    def __init__(self, fila, columna, nombre_DB, if_exists = False):
        super().__init__(fila, columna)
        self.nombre_DB = nombre_DB.lower()
        self.if_exists = if_exists

    def ejecutar(self, TS, Errores):
        respuesta = TypeChecker.dropDataBase(self.nombre_DB)
        if respuesta == 2:#Base de datos no existente
            if self.if_exists:
                return 'NOTICIA: BASE DE DATOS %s, NO EXISTENTE\n' % self.nombre_DB
            Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % self.nombre_DB, self.fila, self.columna))
            return '3D000: No existe base de datos <<%s>>\n' % self.nombre_DB
        if respuesta == 1: #Error interno
            Errores.insertar(err.Nodo_Error('P0000', 'plpgsql_error', self.fila, self.columna))
            return 'P0000: plpgsql_error\n'
        return 'BASE DE DATOS %s ELIMINADA\n' % self.nombre_DB

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        if self.if_exists:
            grafica.node('if_exists%s' % self.mi_id, 'If Exists')
            grafica.edge(self.mi_id, 'if_exists%s' % self.mi_id)

class CreateType(Nodo):
    def __init__(self, fila, columna, nombre_type, lista_enum):
        super().__init__(fila=fila, columna=columna)
        self.nombre_type = nombre_type
        self.lista_enum = lista_enum

    def ejecutar(self, TS, Errores):
        respuesta = TypeChecker.registarEnum(self.nombre_type, self.lista_enum)
        if respuesta != 0:
            Errores.insertar(err.Nodo_Error('42710', 'duplicate_object, ya existe un tipo <<%s>>' % self.nombre_type, self.fila, self.columna))
            return '42710: duplicate_object, ya existe un tipo <<%s>>' % self.nombre_type
        return 'Type <<%s>> creado satisfactoriamente' % self.nombre_type

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

class CreateTable(Nodo):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)

    def ejecutar(self, TS, Errores):
        pass
    
    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
