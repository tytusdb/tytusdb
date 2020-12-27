from typing import Type
from AST.Nodo import Nodo
import data.jsonMode as JM
import Errores.Nodo_Error as err
from prettytable import PrettyTable
import TypeCheck.Type_Checker as TypeChecker
import os


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
            return '42710: duplicate_object, ya existe un tipo <<%s>>\n' % self.nombre_type
        return 'Type <<%s>> creado satisfactoriamente\n' % self.nombre_type

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
    def __init__(self, fila, columna, nombre_tabla, columnas, inherits):
        super().__init__(fila, columna)
        self.nombre_tabla = nombre_tabla
        for col in columnas:
            col.agregar_nombre_tabla(nombre_tabla)
        self.columnas = columnas
        self.inherits = inherits
    
    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        if nombre_DB == 'None':
            Errores.insertar(err.Nodo_Error('P0002', 'no data found, no hay una base de datos seleccionada', self.fila, self.columna))
            return 'P0002: no data found, no hay una base de datos seleccionada\n'
        if self.nombre_tabla == self.inherits:
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.inherits, self.fila, self.columna))
            return '42P01: No existe la tabla <<%s>>\n' % self.nombre_tabla
        respuesta = TypeChecker.createTable(nombre_DB, self.nombre_tabla, self.get_cantidad_columnas())
        if respuesta == 0:
            for col in self.columnas:
                if col.ejecutar(TS, Errores) != 0:
                    respuesta = TypeChecker.dropTable(nombre_DB, self.nombre_tabla)
                    if respuesta == 0:
                        return '%s: %s\n' % (Errores.fin.tipo, Errores.fin.descripcion)
                    else:
                        return 'XX000: La tabla <<%s>> tuvo errores al crearse y ni siquiera se quiso eliminar error: <<%s>>\n' % (self.nombre_tabla, str(respuesta))
            
            respuesta = TypeChecker.addInheritsToTable(nombre_DB, self.nombre_tabla, self.inherits)
            if respuesta == 0:
                return 'La tabla <<%s>> se crea exitosamente\n' % self.nombre_tabla
            else:
                TypeChecker.dropTable(nombre_DB, self.nombre_tabla)
            
        if respuesta == 1:
            Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
            return 'XX000: internal_error\n'
        elif respuesta == 2:
            Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % nombre_DB, self.fila, self.columna))
            return '3D000: No existe base de datos <<%s>>\n' % nombre_DB
        elif respuesta == 3: #Tabla creada
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.nombre_tabla, self.fila, self.columna))
            return '42P01: No existe la tabla <<%s>>\n' % self.nombre_tabla
        else: #Tabla de inherits
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.inherits, self.fila, self.columna))
            return '42P01: No existe la tabla <<%s>>\n' % self.inherits
            


    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node('create_tb_nombre%s' % self.mi_id, 'Nombre Tabla: %s' % self.nombre_tabla)
        grafica.edge(self.mi_id, 'create_tb_nombre%s' % self.mi_id)
        for col in self.columnas:
            col.graficarasc(self.mi_id, grafica)
        grafica.node('create_tb_inherits%s' % self.mi_id, 'Inherits: %s' % self.inherits)
        grafica.edge(self.mi_id, 'create_tb_inherits%s' % self.mi_id)

    def get_cantidad_columnas(self):
        contador = 0
        for col in self.columnas:
            if col.__class__.__name__ == 'CreateTableColumn':
                contador += 1
        return contador

class CreateTableColumn(Nodo):
    def __init__(self, fila, columna, nombre_columna, tipo_columna, lista_constraints):
        super().__init__(fila=fila, columna=columna)
        self.nombre_tabla = None
        self.nombre_columna = nombre_columna
        self.tipo_columna = tipo_columna
        self.lista_constraints = lista_constraints

    def agregar_nombre_tabla(self, nombre_tabla):
        self.nombre_tabla = nombre_tabla
        for constraint in self.lista_constraints:
            constraint.agregar_nombre_tabla(nombre_tabla, self.nombre_columna)

    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        if nombre_DB == 'None':
            Errores.insertar(err.Nodo_Error('P0002', 'no data found, no hay una base de datos seleccionada', self.fila, self.columna))
            return 1
        respuesta = TypeChecker.getIfTipoColumnaIsReserverd(self.tipo_columna['tipo'])
        if respuesta == 14:#Si el tipo no es uno determinado
            respuesta = TypeChecker.obtenerTiposEnum(self.tipo_columna['tipo'])
            if respuesta is None:
                Errores.insertar(err.Nodo_Error('42704', 'undefined_object, no existe el tipo <<%s>>' % self.tipo_columna['tipo'], self.fila, self.columna))
                return 1
        elif respuesta == 4:#Si el tipo es Numeric
            if self.tipo_columna['size'] > 1000 or self.tipo_columna['size'] < 1:
                Errores.insertar(err.Nodo_Error('22023', 'la precisión %s de NUMERIC debe estar entre 1 y 1000' % str(self.tipo_columna['size']), self.fila, self.columna))
                return 1
        elif respuesta >= 8 and respuesta <= 11:#Si el tipo es char, varchar, character, character varying
            if self.tipo_columna['size'] < 1:
                Errores.insertar(err.Nodo_Error('22023', 'el largo para el tipo %s debe ser al menos 1' % self.tipo_columna['tipo'], self.fila, self.columna))
                return 1
        respuesta = TypeChecker.createColumn(nombre_DB, self.nombre_tabla, self.nombre_columna, self.tipo_columna)
        if respuesta == 0:
            for constraint in self.lista_constraints:
                if constraint.ejecutar(TS, Errores) != 0:
                    return 1
            return 0
        elif respuesta == 1:
            Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
        elif respuesta == 2:
            Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % nombre_DB, self.fila, self.columna))
        elif respuesta == 3:
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.nombre_tabla, self.fila, self.columna))
        else:
            Errores.insertar(err.Nodo_Error('42701', 'duplicate_column <<%s>>' % self.nombre_columna, self.fila, self.columna))
        return 1

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node('createtablecolumnname%s' % self.mi_id, 'Nombre Columna: %s' % self.nombre_columna)
        grafica.edge(self.mi_id, 'createtablecolumnname%s' % self.mi_id)
        grafica.node('createtablecolumntipo%s' % self.mi_id, 'Tipo Columna: %s' % self.tipo_columna['tipo'])
        grafica.edge(self.mi_id, 'createtablecolumntipo%s' % self.mi_id)
        for constraint in self.lista_constraints:
            constraint.graficarasc(self.mi_id, grafica)

class CreateTableConstraint(Nodo):
    def __init__(self, fila, columna, nombre_constraint, numero_propiedad, extra):
        super().__init__(fila=fila, columna=columna)
        self.nombre_tabla = None
        self.nombre_columna = None
        self.nombre_constraint = nombre_constraint
        self.numero_propiedad = numero_propiedad
        self.extra = extra

    def agregar_nombre_tabla(self, nombre_tabla, nombre_columna = None):
        self.nombre_tabla = nombre_tabla
        self.nombre_columna = nombre_columna
        if self.numero_propiedad == 6 and self.extra is None:
            self.extra = [self.nombre_columna]
        elif self.numero_propiedad == 5 and self.extra['lista_columnas_ref'] is None and self.extra['lista_columnas'] is None:
            self.extra['lista_columnas_ref'] = []
            base_actual = TypeChecker.obtenerBase(os.environ['DB'])
            if base_actual is not None:
                tablaActual = base_actual.listaTablas.obtenerTabla(nombre_tabla)
                if tablaActual is not None:
                    self.extra['lista_columnas_ref'] = tablaActual.primary.columnas
            self.extra['lista_columnas'] = [self.nombre_columna]

    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        if nombre_DB == 'None':
            Errores.insertar(err.Nodo_Error('P0002', 'no data found, no hay una base de datos seleccionada', self.fila, self.columna))
            return 1
            
        respuesta = 0
        _constraint = TypeChecker.create_new_constraint(self.nombre_constraint, self.numero_propiedad, self.extra)
        if self.numero_propiedad == 3: #Unique
            if self.extra is None:
                respuesta = TypeChecker.addConstraint(nombre_DB, self.nombre_tabla, self.nombre_columna, _constraint)
            else:
                for iteracion in self.extra:
                    _constraint = TypeChecker.create_new_constraint(self.nombre_constraint, self.numero_propiedad, None)
                    respuesta = TypeChecker.addConstraint(nombre_DB, self.nombre_columna, iteracion, _constraint)
                    if respuesta != 0:
                        break
        elif self.numero_propiedad == 4: #CHECK
            if self.nombre_columna is not None:
                respuesta = TypeChecker.addConstraint(nombre_DB, self.nombre_tabla, self.nombre_columna, _constraint)
            else:
                respuesta = TypeChecker.add_constraint_general_check(nombre_DB, self.nombre_tabla, _constraint)
        elif self.numero_propiedad == 1 or self.numero_propiedad == 2: # 1. DEFAULT, 2. ISNULL
            respuesta = TypeChecker.addConstraint(nombre_DB, self.nombre_tabla, self.nombre_columna, _constraint)
        elif self.numero_propiedad == 6: #PRIMARY KEY
            respuesta = TypeChecker.alterAddPK(nombre_DB, self.nombre_tabla, self.nombre_constraint, self.extra)
        else: #FOREIGN KEY
            '''Validar que ambas listas sean del mismo tamaño'''
            if len(self.extra['lista_columnas_ref']) == len(self.extra['lista_columnas']):
                '''validar foraneas sean del mismo tipo'''
                for i, columna in enumerate(self.extra['lista_columnas']):
                    tipo_lista_columna = TypeChecker.obtenerTipoColumna(nombre_DB, self.nombre_tabla, columna)
                    tipo_lista_columna_ref = TypeChecker.obtenerTipoColumna(nombre_DB, self.extra['nombre_ref'], self.extra['lista_columnas_ref'][i])
                    if tipo_lista_columna_ref is None or tipo_lista_columna is None:
                        _id_columna = self.extra['lista_columnas_ref'][i] if tipo_lista_columna_ref is None else columna
                        Errores.insertar(err.Nodo_Error('42703', 'No existe la columna <<%s>> referida en la llave foránea' % _id_columna, self.fila, self.columna))
                        return 1
                    if tipo_lista_columna['tipo'] != tipo_lista_columna_ref['tipo']:
                        Errores.insertar(err.Nodo_Error('42804', 
                        'datatype_mismatch, Las columnas llave «%s» y «%s» son de tipos incompatibles: %s y %s' % (columna, self.extra['lista_columnas_ref'][i], tipo_lista_columna['tipo'], tipo_lista_columna_ref['tipo'])))
                        return 1
                respuesta = TypeChecker.alterAddFK(nombre_DB, self.nombre_tabla, self.nombre_constraint, self.extra['lista_columnas'], self.extra['nombre_ref'], self.extra['lista_columnas_ref'])
            else:
                Errores.insertar(err.Nodo_Error('42830', 'el número de columnas referidas en la llave foránea no coincide con el número de columnas de referencia', self.fila, self.columna))
                return 1


        if respuesta == 0:
            return 0
        elif respuesta == 1:
            Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
        elif respuesta == 2:
            Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % nombre_DB, self.fila, self.columna))
        elif respuesta == 3:
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.nombre_tabla, self.fila, self.columna))
        elif respuesta == 4:
            if self.numero_propiedad == 6:
                Errores.insertar(err.Nodo_Error('42P16', 'No se permiten múltiples llaves primarias para la tabla «tabla10» <<%s>>' % self.nombre_tabla, self.fila, self.columna))
            elif self.numero_propiedad == 5:
                Errores.insertar(err.Nodo_Error('42710', 'duplicate_object <<%s>>' % self.nombre_constraint, self.fila, self.columna))
            else:
                Errores.insertar(err.Nodo_Error('42703', 'undefined_column <<%s>>' % self.nombre_columna, self.fila, self.columna))
        elif respuesta == 5:
            if self.numero_propiedad == 6:
                Errores.insertar(err.Nodo_Error('42710', 'duplicate_object, primary key ya existente <<%s>>' % self.nombre_constraint, self.fila, self.columna))
            else:   
                Errores.insertar(err.Nodo_Error('42710', 'duplicate_object, propiedad ya existente <<%s>>' % self.nombre_constraint, self.fila, self.columna))
        return 1



    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        if self.nombre_constraint is not None:
            grafica.node("createtableconstraintnombre%s" % self.mi_id, 'Nombre: %s' % str(self.nombre_constraint))
            grafica.edge(self.mi_id, "createtableconstraintnombre%s" % self.mi_id)
        if self.numero_propiedad == 1: #DEFAULT
            grafica.node("createtableconstraintdefault%s" % self.mi_id, 'Default: %s' % str(self.extra))
            grafica.edge(self.mi_id, "createtableconstraintdefault%s" % self.mi_id)
        elif self.numero_propiedad == 2: #ISNULL
            grafica.node("createtableconstraintisnull%s" % self.mi_id, 'Not Null' if self.extra else 'Null')
            grafica.edge(self.mi_id, "createtableconstraintisnull%s" % self.mi_id)
        elif self.numero_propiedad == 3: #ISUNIQUE
            grafica.node("createtableconstraintisunique%s" % self.mi_id, 'Unique')
            grafica.edge(self.mi_id, "createtableconstraintisunique%s" % self.mi_id)
            if self.extra is not None:
                for i, columna in enumerate(self.extra):
                    grafica.node("%screatetableconstraintuniquelista%s" % (str(i),self.mi_id), columna)
                    grafica.edge("createtableconstraintisunique%s" % self.mi_id, "%screatetableconstraintuniquelista%s" % (str(i),self.mi_id))
        elif self.numero_propiedad == 4: #CHECK
            grafica.node("createtableconstraintcheck%s" % self.mi_id, 'Check')
            grafica.edge(self.mi_id, "createtableconstraintcheck%s" % self.mi_id)
            #self.extra.graficarasc("createtableconstraintcheck%s" % self.mi_id, grafica)
        elif self.numero_propiedad == 5: #FORANEA
            grafica.node("createtableconstraintforanea%s" % self.mi_id, 'Foreign Key')
            grafica.edge(self.mi_id, "createtableconstraintforanea%s" % self.mi_id)
            for i, columna in enumerate(self.extra['lista_columnas']):
                grafica.node("%screatetableconstraintforanealista%s" % (str(i),self.mi_id), columna)
                grafica.edge("createtableconstraintforanea%s" % self.mi_id, "%screatetableconstraintforanealista%s" % (str(i),self.mi_id))
            grafica.node("createtableconstraintforaneanameref%s" % self.mi_id, 'Tabla Ref: %s' % self.extra['nombre_ref'])
            grafica.edge(self.mi_id, "createtableconstraintforaneanameref%s" % self.mi_id)
            for i, columna in enumerate(self.extra['lista_columnas_ref']):
                grafica.node("%screatetableconstraintforanealistaref%s" % (str(i), self.mi_id), columna)
                grafica.edge("createtableconstraintforaneanameref%s" % self.mi_id, "%screatetableconstraintforanealistaref%s" % (str(i), self.mi_id))
        elif self.numero_propiedad == 6: #PRIMARIA
            grafica.node("createtableconstraintprimaria%s" % self.mi_id, 'Primary Key')
            grafica.edge(self.mi_id, "createtableconstraintprimaria%s" % self.mi_id)
            for i, columna in enumerate(self.extra):
                grafica.node("%screatetableconstraintprimarialista%s" % (str(i),self.mi_id), columna)
                grafica.edge("createtableconstraintprimaria%s" % self.mi_id, "%screatetableconstraintprimarialista%s" % (str(i),self.mi_id))
        else:
            grafica.node("createtableconstrainterror%s" % self.mi_id, 'MAL CONSTRUCCION AST')
            grafica.edge(self.mi_id, "createtableconstrainterror%s" % self.mi_id)

class AlterTable(Nodo):
    def __init__(self, fila, columna, nombre_tabla, hijo):
        super().__init__(fila, columna)
        self.nombre_tabla = hijo.nombre_tabla = nombre_tabla
        self.hijo = hijo
        
    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        if nombre_DB == 'None':
            Errores.insertar(err.Nodo_Error('P0002', 'no data found, no hay una base de datos seleccionada', self.fila, self.columna))
            return 'P0002: no data found, no hay una base de datos seleccionada\n'
        respuesta = self.hijo.ejecutar(TS, Errores)
        if respuesta == 0:
            return 'ALTER TABLE EXITOSO\n'
        else:
            return '%s: %s\n' % (Errores.fin.tipo, Errores.fin.descripcion)

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node('alter_table%s' % self.mi_id, 'Nombre Tabla: %s' % self.nombre_tabla)
        grafica.edge(self.mi_id, 'alter_table%s' % self.mi_id)
        self.hijo.graficarasc(self.mi_id, grafica)

class AlterTBAdd(Nodo):
    def __init__(self, fila, columna, numero_tipo_add, extra):
        super().__init__(fila, columna)
        self.nombre_tabla = None
        self.numero_tipo_add = numero_tipo_add
        self.extra = extra

    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        respuesta = 0
        if self.numero_tipo_add == 1: #Column id tipo
            respuesta = TypeChecker.getIfTipoColumnaIsReserverd(self.extra['tipo']['tipo'])
            if respuesta == 14:#Si el tipo no es uno determinado
                respuesta = TypeChecker.obtenerTiposEnum(self.extra['tipo']['tipo'])
                if respuesta is None:
                    Errores.insertar(err.Nodo_Error('42704', 'undefined_object, no existe el tipo <<%s>>' % self.extra['tipo']['tipo'], self.fila, self.columna))
                    return 1
            elif respuesta == 4:#Si el tipo es Numeric
                if self.extra['tipo']['size'] > 1000 or self.extra['tipo']['size'] < 1:
                    Errores.insertar(err.Nodo_Error('22023', 'la precisión %s de NUMERIC debe estar entre 1 y 1000' % str(self.extra['tipo']['size']), self.fila, self.columna))
                    return 1
            elif respuesta >= 8 and respuesta <= 11:#Si el tipo es char, varchar, character, character varying
                if self.extra['tipo']['size'] < 1:
                    Errores.insertar(err.Nodo_Error('22023', 'el largo para el tipo %s debe ser al menos 1' % self.extra['tipo']['tipo'], self.fila, self.columna))
                    return 1

            respuesta = JM.alterAddColumn(nombre_DB, self.nombre_tabla, None)
            if respuesta == 0:
                respuesta = TypeChecker.createColumn(nombre_DB, self.nombre_tabla, self.extra['id'], self.extra['tipo'])
                if respuesta == 0:
                    return 0
            #Se elimina la columna cualquier cosa
            TypeChecker.dropColumn(nombre_DB, self.nombre_tabla, self.extra['id'])
        elif self.numero_tipo_add == 2: #id_constraint t_foreign t_key Lista_ID t_references id Lista_ID
            '''Validar que ambas listas sean del mismo tamaño'''
            if len(self.extra['Lista_ID_ref']) == len(self.extra['Lista_ID']):
                '''validar foraneas sean del mismo tipo'''
                for i, columna in enumerate(self.extra['Lista_ID']):
                    tipo_lista_columna = TypeChecker.obtenerTipoColumna(nombre_DB, self.nombre_tabla, columna)
                    tipo_lista_columna_ref = TypeChecker.obtenerTipoColumna(nombre_DB, self.extra['id_ref'], self.extra['Lista_ID_ref'][i])
                    if tipo_lista_columna_ref is None or tipo_lista_columna is None:
                        _id_columna = self.extra['Lista_ID_ref'][i] if tipo_lista_columna_ref is None else columna
                        Errores.insertar(err.Nodo_Error('42703', 'No existe la columna <<%s>> referida en la llave foránea' % _id_columna, self.fila, self.columna))
                        return 1
                    if tipo_lista_columna['tipo'] != tipo_lista_columna_ref['tipo']:
                        Errores.insertar(err.Nodo_Error('42804', 
                        'datatype_mismatch, Las columnas llave «%s» y «%s» son de tipos incompatibles: %s y %s' % (columna, self.extra['Lista_ID_ref'][i], tipo_lista_columna['tipo'], tipo_lista_columna_ref['tipo'])))
                        return 1
                respuesta = TypeChecker.alterAddFK(nombre_DB, self.nombre_tabla, self.extra['id_constraint'], self.extra['Lista_ID'], self.extra['id_ref'], self.extra['Lista_ID_ref'])
            else:
                Errores.insertar(err.Nodo_Error('42830', 'el número de columnas referidas en la llave foránea no coincide con el número de columnas de referencia', self.fila, self.columna))
                return 1
        elif self.numero_tipo_add == 3:#id_constraint t_unique par1 id par2
            _constraint = TypeChecker.create_new_constraint(self.extra['id_constraint'], self.numero_tipo_add, None)
            respuesta = TypeChecker.addConstraint(nombre_DB, self.nombre_tabla, self.extra['id'], _constraint)
        elif self.numero_tipo_add == 4: #id_constraint t_check EXP
            _constraint = TypeChecker.create_new_constraint(self.extra['id_constraint'], self.numero_tipo_add, self.extra['EXP'])
            respuesta = TypeChecker.add_constraint_general_check(nombre_DB, self.nombre_tabla, _constraint)

        if respuesta == 0:
            return 0
        elif respuesta == 1:
            Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
        elif respuesta == 2:
            Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % nombre_DB, self.fila, self.columna))
        elif respuesta == 3:
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.nombre_tabla, self.fila, self.columna))
        elif respuesta == 4:
            if self.numero_tipo_add == 2:
                Errores.insertar(err.Nodo_Error('42710', 'duplicate_object <<%s>>' % self.extra['id_constraint'], self.fila, self.columna))
            elif self.numero_tipo_add == 3:
                Errores.insertar(err.Nodo_Error('42703', 'undefined_column <<%s>>' % self.extra['id'], self.fila, self.columna))
            else:
                Errores.insertar(err.Nodo_Error('42701', 'duplicate_column <<%s>>' % self.extra['id'], self.fila, self.columna))
        elif respuesta == 5:
            Errores.insertar(err.Nodo_Error('42710', 'duplicate_object, propiedad ya existente <<%s>>' % self.extra['id_constraint'], self.fila, self.columna))
        return 1
        
        


    def getC3D(self, TS):
        pass
    
    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        if self.numero_tipo_add == 1: #column id tipo
            #id
            grafica.node('1altertb%s' % self.mi_id, 'Column: %s' % self.extra['id'])
            grafica.edge(self.mi_id, '1altertb%s' % self.mi_id)
            #tipo
            grafica.node('2altertb%s' % self.mi_id, 'Tipo: %s' % self.extra['tipo']['tipo'])
            grafica.edge(self.mi_id, '2altertb%s' % self.mi_id)
        elif self.numero_tipo_add == 2: #id_constraint t_foreign t_key Lista_ID t_references id Lista_ID
            #id_constraint
            if self.extra['id_constraint'] is not None:
                grafica.node('altertb_id_constraint%s' % self.mi_id, 'Constraint name: %s' % self.extra['id_constraint'])
                grafica.edge(self.mi_id, 'altertb_id_constraint%s' % self.mi_id)    
            #FOREIGN KEY 
            grafica.node('altertb_foreign%s' % self.mi_id, 'FOREIGN KEY')
            grafica.edge(self.mi_id, 'altertb_foreign%s' % self.mi_id)
            #Lista_ID
            grafica.node('1altertb%s' % self.mi_id, 'Lista_ID')
            grafica.edge(self.mi_id, '1altertb%s' % self.mi_id)
            for i, id in enumerate(self.extra['Lista_ID']):
                grafica.node('%saltertb_lista_id%s' % (str(i), self.mi_id), 'Column: %s' % id)
                grafica.edge('1altertb%s' % self.mi_id, '%saltertb_lista_id%s' % (str(i), self.mi_id))
            #id_ref
            grafica.node('2altertb%s' % self.mi_id, 'Tabla Referencia: %s' % self.extra['id_ref'])
            grafica.edge(self.mi_id, '2altertb%s' % self.mi_id)
            #Lista_ID_ref
            grafica.node('3altertb%s' % self.mi_id, 'Lista_ID_References')
            grafica.edge(self.mi_id, '3altertb%s' % self.mi_id)
            for i, id in enumerate(self.extra['Lista_ID_ref']):
                grafica.node('%saltertb_lista_id_references%s' % (str(i), self.mi_id), 'Column: %s' % id)
                grafica.edge('3altertb%s' % self.mi_id, '%saltertb_lista_id_references%s' % (str(i), self.mi_id))
        elif self.numero_tipo_add == 3: #id_constraint t_unique par1 id par2
            #id_constraint
            if self.extra['id_constraint'] is not None:
                grafica.node('altertb_id_constraint%s' % self.mi_id, 'Constraint name: %s' % self.extra['id_constraint'])
                grafica.edge(self.mi_id, 'altertb_id_constraint%s' % self.mi_id)
            #Unique
            grafica.node('altertb_unique%s' % self.mi_id, 'Unique: %s' % self.extra['id'])
            grafica.edge(self.mi_id, 'altertb_unique%s' % self.mi_id)
        elif self.numero_tipo_add == 4: #id_constraint t_check EXP
            #id_constraint
            if self.extra['id_constraint'] is not None:
                grafica.node('altertb_id_constraint%s' % self.mi_id, 'Constraint name: %s' % self.extra['id_constraint'])
                grafica.edge(self.mi_id, 'altertb_id_constraint%s' % self.mi_id)
            #CHECK
            grafica.node('altertb_check%s' % self.mi_id, 'CHECK')
            grafica.edge(self.mi_id, 'altertb_check%s' % self.mi_id)
            #EXP
            #self.extra['EXP'].graficarasc('altertb_check%s' % self.mi_id, grafica)

class AlterTBDrop(Nodo):
    def __init__(self, fila, columna, numero_tipo_drop, nombre):
        super().__init__(fila, columna)
        self.nombre_tabla = None
        self.numero_tipo_drop = numero_tipo_drop
        self.nombre = nombre

    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        respuesta = 0
        if self.numero_tipo_drop == 1: #t_column id
            respuesta = TypeChecker.dropColumn(nombre_DB, self.nombre_tabla, self.nombre)
        else: #t_constraint id
            base = TypeChecker.obtenerBase(nombre_DB)
            if base is not None:
                tablaActual = base.listaTablas.obtenerTabla(self.nombre_tabla)
                if tablaActual is not None:
                    #Busco si esta en el check general
                    for i, _check in enumerate(tablaActual.check_general):
                        if _check.nombreConstraint == self.nombre:
                            tablaActual.check_general.pop(i)
                            return 0
                    #Busco si esta en la llave primaria
                    if tablaActual.primary.nombreConstraint == self.nombre:
                        respuesta = TypeChecker.alterDropPk(nombre_DB, self.nombre_tabla)
                        if respuesta == 0:
                            return 0
                        else:
                            Errores.insertar(err.Nodo_Error('XX000', 'internal_error <<%s>>' % str(respuesta), self.fila, self.columna))
                            return 1
                    #Busco si esta en las llaves foraneas
                    respuesta = TypeChecker.alterDropFK(nombre_DB, self.nombre_tabla, self.nombre)
                    if respuesta == 0:
                        return 0
                    elif respuesta == 4:
                        columnas = TypeChecker.showColumns(nombre_DB, self.nombre_tabla)
                        #Busco si esta entre las columnas
                        for columna in columnas:
                            respuesta = TypeChecker.dropConstraint(nombre_DB, self.nombre_tabla, columna, self.nombre)
                            if respuesta == 0:
                                return 0
                            elif respuesta != 5:
                                break
                        if respuesta == 5:
                            Errores.insertar(err.Nodo_Error('42704', 'No existe la constraint <<%s>> en la tabla <<%s>>' % (self.nombre, self.nombre_tabla), self.fila, self.columna))
                            return 1
                else:
                    respuesta = 3
            else:
                respuesta = 2

        if respuesta == 0:
            return 0
        elif respuesta == 1:
            Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
        elif respuesta == 2:
            Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % nombre_DB, self.fila, self.columna))
        elif respuesta == 3:
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.nombre_tabla, self.fila, self.columna))
        elif respuesta == 4:
            Errores.insertar(err.Nodo_Error('42703', 'undefined_column <<%s>>' % self.nombre, self.fila, self.columna))
        elif respuesta == 5:
            Errores.insertar(err.Nodo_Error('P0004', 'No se puede borrar la columna <<%s>> porque es llave primaria' % self.nombre, self.fila, self.columna))
        return 1

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        if self.numero_tipo_drop == 1: #t_column id
            grafica.node('altertbdrop%s' % self.mi_id, 'Column')
        else: #t_constraint id
            grafica.node('altertbdrop%s' % self.mi_id, 'Constraint')
        grafica.edge(self.mi_id, 'altertbdrop%s' % self.mi_id)
        #id
        grafica.node('altertbdrop_id%s' % self.mi_id, 'Nombre: %s' % self.nombre)
        grafica.edge(self.mi_id, 'altertbdrop_id%s' % self.mi_id)
        
class AlterTBAlter(Nodo):
    def __init__(self, fila, columna, nombre_columna, alter_columns):
        super().__init__(fila, columna)
        self.nombre_tabla = None
        self.nombre_columna = nombre_columna
        self.alter_columns = alter_columns

    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        respuesta = 0
        if self.nombre_columna is not None: #id t_set t_not t_null
            _constraint = TypeChecker.create_new_constraint(None, 2, False)
            respuesta = TypeChecker.addConstraint(nombre_DB, self.nombre_tabla, self.nombre_columna, _constraint)
        else: #alter_columns
            #Primero compruebo que puedo hacer el cambio a las columnas
            is_error = False
            for column in self.alter_columns:
                tipoActual = TypeChecker.obtenerTipoColumna(nombre_DB, self.nombre_tabla, column['nombre_columna'])
                if tipoActual is not None:
                    if tipoActual['tipo'] != 'varchar':
                        Errores.insertar(err.Nodo_Error('XX000', 'internal_error, el tipo debe ser un varchar pero viene un <<%s>>' % tipoActual['tipo'], self.fila, self.columna))
                        return 1
                    if tipoActual['size'] > column['entero']:
                        Errores.insertar(err.Nodo_Error('XX000', 'internal_error, el nuevo valor <<%s>> debe ser mayor al valor que hay: %s' % (column['entero'], str(tipoActual['size'])), self.fila, self.columna))
                        return 1
                else:
                    actualBase = TypeChecker.obtenerBase(nombre_DB)
                    if actualBase is not None:
                        if not actualBase.listaTablas.existeTabla(self.nombre_tabla): 
                            respuesta = 3
                            is_error = True
                            break
                        else:
                            respuesta = 4
                            is_error = True
                            break
                    else:
                        respuesta = 2
                        is_error = True
                        break
            if not is_error:
                for column in self.alter_columns:
                    tipoActual = TypeChecker.obtenerTipoColumna(nombre_DB, self.nombre_tabla, column['nombre_columna'])
                    tipoActual['size'] = column['entero']
                    respuesta = TypeChecker.alterTypeColumn(nombre_DB, self.nombre_tabla, column['nombre_columna'], tipoActual)
                    if respuesta != 0:
                        Errores.insertar(err.Nodo_Error('XX000', 'internal_error, se hicieron algunos cambios en los tipos pero no fueron todos, error de <<%s>>' % str(respuesta), self.fila, self.columna))
                        return 1

        if respuesta == 0:
            return 0
        elif respuesta == 1:
            Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
        elif respuesta == 2:
            Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % nombre_DB, self.fila, self.columna))
        elif respuesta == 3:
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.nombre_tabla, self.fila, self.columna))
        elif respuesta == 4:
            Errores.insertar(err.Nodo_Error('42703', 'undefined_column <<%s>>' % self.nombre, self.fila, self.columna))
        elif respuesta == 5:
            Errores.insertar(err.Nodo_Error('42710', 'duplicate_object, propiedad ya existente para columna <<%s>> de tabla <<%s>>' % (self.nombre_columna, self.nombre_tabla), self.fila, self.columna))
        return 1

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        if self.nombre_columna is not None:
            #Nombre Columna
            grafica.node('1altertbalter%s' % self.mi_id, 'Columna: %s' % self.nombre_columna)
            grafica.edge(self.mi_id, '1altertbalter%s' % self.mi_id)
            grafica.node('2altertbalter%s' % self.mi_id, 'Set Not Null')
            grafica.edge(self.mi_id, '2altertbalter%s' % self.mi_id)
        else:
            #alter_columns
            for i,column in enumerate(self.alter_columns):
                #Nombre Columna
                grafica.node('%saltertbalter_column_name%s' % (str(i), self.mi_id), 'Columna: %s' % column['nombre_columna'])
                grafica.edge(self.mi_id, '%saltertbalter_column_name%s' % (str(i), self.mi_id))
                grafica.node('%saltertbalter_col%s' % (str(i), self.mi_id), 'Type Varchar')
                grafica.edge('%saltertbalter_column_name%s' % (str(i), self.mi_id), '%saltertbalter_col%s' % (str(i), self.mi_id))
                #Entero
                grafica.node('%saltertbalter_entero%s' % (str(i), self.mi_id), str(column['entero']))
                grafica.edge('%saltertbalter_column_name%s' % (str(i), self.mi_id), '%saltertbalter_entero%s' % (str(i), self.mi_id))

class AlterTBRename(Nodo):
    def __init__(self, fila, columna, nombre_columna_anterior, nombre_columna_nueva):
        super().__init__(fila, columna)
        self.nombre_tabla = None
        self.nombre_columna_anterior = nombre_columna_anterior
        self.nombre_columna_nueva = nombre_columna_nueva

    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        respuesta = TypeChecker.alterRenameColumn(nombre_DB, self.nombre_tabla, self.nombre_columna_anterior, self.nombre_columna_nueva)
        if respuesta == 0:
            return 0
        elif respuesta == 1:
            Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
        elif respuesta == 2:
            Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % nombre_DB, self.fila, self.columna))
        elif respuesta == 3:
            Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.nombre_tabla, self.fila, self.columna))
        elif respuesta == 4:
            Errores.insertar(err.Nodo_Error('42703', 'undefined_column <<%s>>' % self.nombre_columna_anterior, self.fila, self.columna))
        elif respuesta == 5:
            Errores.insertar(err.Nodo_Error('42710', 'duplicate_object, ya existe una columna con nombre <<%s>>' % self.nombre_columna_nueva, self.fila, self.columna))
        return 1

    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node('1altertbrename%s' % self.mi_id, 'Nombre antes: %s' % self.nombre_columna_anterior)
        grafica.edge(self.mi_id, '1altertbrename%s' % self.mi_id)
        grafica.node('2altertbrename%s' % self.mi_id, 'Nombre nuevo: %s' % self.nombre_columna_nueva)
        grafica.edge(self.mi_id, '2altertbrename%s' % self.mi_id)

class DropTable(Nodo):
    def __init__(self, fila, columna, nombre_tabla):
        super().__init__(fila, columna)
        self.nombre_tabla = nombre_tabla
    
    def ejecutar(self, TS, Errores):
        nombre_DB = os.environ['DB']
        if nombre_DB == 'None':
            Errores.insertar(err.Nodo_Error('P0002', 'no data found, no hay una base de datos seleccionada', self.fila, self.columna))
            return 'P0002: no data found, no hay una base de datos seleccionada\n'
        respuesta = TypeChecker.dropTable(nombre_DB, self.nombre_tabla)
        if respuesta != 0:
            if respuesta == 1:
                Errores.insertar(err.Nodo_Error('XX000', 'internal_error', self.fila, self.columna))
                return 'XX000: internal_error\n'
            elif respuesta == 2:
                Errores.insertar(err.Nodo_Error('3D000', 'No existe base de datos <<%s>>' % nombre_DB, self.fila, self.columna))
                return '3D000: No existe base de datos <<%s>>\n' % nombre_DB
            else:
                Errores.insertar(err.Nodo_Error('42P01', 'No existe la tabla <<%s>>' % self.nombre_tabla, self.fila, self.columna))
                return '42P01: No existe la tabla <<%s>>\n' % self.nombre_tabla
        return 'Tabla <<%s>> eliminada\n' % self.nombre_tabla


    def getC3D(self, TS):
        pass

    def graficarasc(self, padre, grafica):
        super().graficarasc(padre, grafica)
        grafica.node('createTable_%s' % self.mi_id, 'nombre: %s' % self.nombre_tabla)
        grafica.edge(self.mi_id, 'createTable_%s' % self.mi_id)
    
