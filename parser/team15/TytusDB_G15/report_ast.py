import ts as TS
from expresiones import *
from instrucciones import *
from graphviz import Digraph

dot = Digraph('AST', node_attr={'shape': 'note','color': 'lightblue2', 'style': 'filled'})
contadorNodos = 0
instrucciones_Global = []

class AST: 

    def __init__(self):
        '''print('AST')'''


    def generarAST(self,instrucciones):
        global contadorNodos, dot, instrucciones_Global
        instrucciones_Global = instrucciones
        dot = Digraph('AST')
        contadorNodos = 2
        dot.node('node1','INIT')
        dot.node('node2','INSTRUCCIONES')
        dot.edge('node1','node2')
        indice = 0
        while indice < len(instrucciones_Global) :
            instruccion = instrucciones_Global[indice]
            if isinstance(instruccion, CreateDatabase):
                self.crearNodoCreateDatabase("node2", instruccion)
            elif isinstance(instruccion, Create_Table):
                self.crearNodoCreateTable("node2", instruccion)
            elif isinstance(instruccion, showDatabases):
                self.crearNodoshowDatabases("node2", instruccion)
            elif isinstance(instruccion, dropDatabase):
                self.crearNododropDatabase("node2", instruccion)
            elif isinstance(instruccion, useDatabase) : 
                self.crearNodo_useDatabase("node2", instruccion)
            elif isinstance(instruccion, Create_Alterdatabase) : 
                self.crearNodo_alterDatabase("node2", instruccion)
            elif isinstance(instruccion, showTables):
                self.crearNodoshowTables("node2", instruccion)
            elif isinstance(instruccion, Create_update):
                self.crearNodoUpdate("node2",instruccion)
            elif isinstance(instruccion, Crear_Drop):
                self.crearNodoDropTable("node2",instruccion)
            elif isinstance(instruccion, Crear_altertable):
                self.crearNodoAlterTable("node2",instruccion)
            elif isinstance(instruccion, Definicion_Insert):
                self.crearNodoInsert("node2",instruccion)
            elif isinstance(instruccion, Create_type):
                self.crearNodoEnum("node2",instruccion)
            elif isinstance(instruccion, Definicion_delete):
                self.crearNodoDelete("node2",instruccion)
            # SELECT
            elif isinstance(instruccion, Create_select_general):
                self.crearNodo_SelectTable("node2",instruccion)
            elif isinstance(instruccion, Create_select_time):
                self.crearNode_SelectTime("node2",instruccion)
            '''elif isinstance(instruccion, Create_select_uno):
                self.crearNode_SelectGL("node2",instruccion)'''
            indice = indice +1
        dot.view('reportes/AST', cleanup=True)

    def crearNodoCreateDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreDatabase(temp1,instruccion)
        if instruccion.usuario.val != "":
            self.crearNodoUsuarioDatabase(temp1,instruccion)
        self.crearNodoModoDatabase(temp1,instruccion)

    def crearNodoNombreDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'NOMBRE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.nombre)

    def crearNodoUsuarioDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'USUARIO DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.usuario)

    def crearNodoModoDatabase(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'MODO DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.modo)

    def crearNodoExpresion(self, padre, expresion):
        global contadorNodos, dot
        if isinstance(expresion, ExpresionIdentificador):
            if expresion.val != "":
                contadorNodos = contadorNodos + 1
                dot.node("node" + str(contadorNodos), str(expresion.val))
                dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionNumeroSimple):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
            dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionComillaSimple):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
            dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionEntero):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
            dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionRelacional):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.exp1))
            dot.node("node" + str(contadorNodos), str(expresion.exp2))
            dot.node("node" + str(contadorNodos), str(expresion.operador))
            dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionBinaria):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.exp1))
            dot.node("node" + str(contadorNodos), str(expresion.exp2))
            dot.node("node" + str(contadorNodos), str(expresion.operador))
            dot.edge(padre, "node" + str(contadorNodos))
        else:
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion))
            dot.edge(padre, "node" + str(contadorNodos))

    def crearNodoCreateTable(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreTabla(temp1,instruccion)
        if instruccion.instrucciones != []:
            for ins in instruccion.instrucciones:
                if isinstance(ins, Definicion_Columnas): 
                    self.crearNodoDefinicion(temp1, ins)
                elif isinstance(ins, LLave_Primaria): 
                    self.crearNodoConstraintLlavePrimaria(temp1, ins)
                elif isinstance(ins, Definicon_Foranea): 
                    self.crearNodoConstraintLlaveForanea(temp1, ins)
                elif isinstance(ins, Lista_Parametros): 
                    self.crearNodoConstraintUnique(temp1, ins)
                elif isinstance(ins, definicion_constraint): 
                    self.crearNodoConstraint(temp1, ins)
    
    def crearNodoNombreTabla(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'NOMBRE TABLA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreTablaID(temp1,instruccion)

    def crearNodoNombreTablaID(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), instruccion.val)
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

    def crearNodoDefinicion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DEFINICION')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoDefinicionNombreTabla(temp1,instruccion)
        self.crearNodoDefinicionTipoDato(temp1,instruccion)
        self.crearNodoDefinicionRestriccion(temp1,instruccion)
        self.crearNodoDefinicionReferencia(temp1,instruccion)
       
    def crearNodoDefinicionNombreTabla(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'NOMBRE COLUMNA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.val)

    def crearNodoDefinicionTipoDato(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO DATO')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.tipo_datos.etiqueta)

    def crearNodoDefinicionRestriccion(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'RESTRICCION')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.etiqueta)

    def crearNodoDefinicionReferencia(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id_referencia)
    
    def crearNodoConstraintLlavePrimaria(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintLlavePrimariaTipoConstraint(temp1,instruccion)
        self.crearNodoConstraintLlavePrimariaId(temp1,instruccion)

    def crearNodoConstraintLlavePrimariaTipoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintLlavePrimariaTipo(temp1,instruccion)

    def crearNodoConstraintLlavePrimariaTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(OPCIONESCREATE_TABLE.PRIMARIA))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
    
    def crearNodoConstraintLlavePrimariaId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.val)

    def crearNodoConstraintLlaveForanea(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintLlaveForaneaTipoConstraint(temp1,instruccion)
        self.crearNodoConstraintLlaveForaneaId(temp1,instruccion)
        self.crearNodoConstraintLlaveForaneaTablaRef(temp1,instruccion)
        self.crearNodoConstraintLlaveForaneaIdRef(temp1,instruccion)

    def crearNodoConstraintLlaveForaneaTipoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintLlaveForaneaTipo(temp1,instruccion)

    def crearNodoConstraintLlaveForaneaTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(OPCIONESCREATE_TABLE.FORANEA))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
    
    def crearNodoConstraintLlaveForaneaId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.nombre_tabla)

    def crearNodoConstraintLlaveForaneaTablaRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TABLA REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.referencia_tabla)

    def crearNodoConstraintLlaveForaneaIdRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.campo_referencia)

    def crearNodoConstraintUnique(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintUniqueTipoConstraint(temp1,instruccion)
        self.crearNodoConstraintUniqueListaIds(temp1,instruccion)
       
    def crearNodoConstraintUniqueTipoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintUniqueTipo(temp1,instruccion)

    def crearNodoConstraintUniqueTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), str(OPCIONESCREATE_TABLE.UNIQUE))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  

    def crearNodoConstraintUniqueListaIds(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'LISTA ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.identificadores != []:
            for ids in instruccion.identificadores:
                self.crearNodoExpresion(temp1,ids.val)

    def crearNodoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        self.crearNodoConstraintTipoConstraint(temp1,instruccion)
        self.crearNodoConstraintId(temp1,instruccion)
        if instruccion.tipo == 'UNIQUE':
            self.crearNodoConstraintLISTA(temp1,instruccion)
        elif instruccion.tipo == 'FOREIGN':
            self.crearNodoConstraintForaneaId(temp1,instruccion)
            self.crearNodoConstraintForaneaTablaRef(temp1,instruccion)
            self.crearNodoConstraintForaneaIdRef(temp1,instruccion)
        elif instruccion.tipo == 'CHECK':
            self.crearNodoConstraintCheckId(temp1,instruccion) 

    def crearNodoConstraintId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        self.crearNodoExpresion(temp1,instruccion.val)

    def crearNodoConstraintTipoConstraint(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TIPO CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoConstraintTipo(temp1,instruccion)

    def crearNodoConstraintTipo(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        if instruccion.tipo == 'UNIQUE':
            dot.node("node" + str(contadorNodos), str(OPCIONES_CONSTRAINT.UNIQUE))
        elif instruccion.tipo == 'FOREIGN':
            dot.node("node" + str(contadorNodos), str(OPCIONES_CONSTRAINT.FOREIGN))
        elif instruccion.tipo == 'CHECK':
            dot.node("node" + str(contadorNodos), str(OPCIONES_CONSTRAINT.CHECK))
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
     
    def crearNodoConstraintLISTA(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'LISTA ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'UNIQUE':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,ids.val)
        
    def crearNodoConstraintForaneaId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREIGN':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,instruccion.columna)

    def crearNodoConstraintForaneaTablaRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TABLA REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREIGN':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,instruccion.referencia)

    def crearNodoConstraintForaneaIdRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREIGN':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,ids)

    def crearNodoConstraintCheckId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'CHECK':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    if type(ids.exp1) == ExpresionIdentificador:
                        self.crearNodoExpresion(temp1,ids.exp1.val)
                    else: 
                        self.crearNodoExpresion(temp1,ids.exp2.val)

    def crearNodoshowDatabases(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'SHOW DATABASES')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

    def crearNodoshowTables(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'SHOW TABLES')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

    def crearNododropDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DROP DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNododropDatabaseID(temp1,instruccion)

    def crearNododropDatabaseID(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.val)

    def crearNodo_useDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'USE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodo_useDatabaseID(temp1,instruccion)

    def crearNodo_useDatabaseID(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.val)

    def crearNodo_alterDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ALTER DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodo_alterDatabaseDatabase(temp1,instruccion)
        self.crearNodo_alterDatabaseID(temp1,instruccion)
        
    def crearNodo_alterDatabaseDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.id_tabla)

    def crearNodo_alterDatabaseID(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        if isinstance(instruccion.tipo_id,ExpresionIdentificador) : 
            dot.node("node" + str(contadorNodos), 'OWNER ID')
        elif isinstance(instruccion.tipo_id, ExpresionComillaSimple) : 
            dot.node("node" + str(contadorNodos), 'OWNER ID')            
        else:
            dot.node("node" + str(contadorNodos), 'NEW ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.tipo_id)

    def crearNodoUpdate(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'UPDATE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.CrearNombreTabla(temp1, instruccion)
        self.Crear_lista_parametros(temp1, instruccion)

    def CrearNombreTabla(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Nombre Tabla')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador.val)

    def Crear_lista_parametros(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Lista_parametros')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.lista_update != []:
            for datos in instruccion.lista_update:
                self.crearNodoExpresion(temp1,datos.ids.val)
                self.crearNodoExpresion(temp1,"=")
                self.crearNodoExpresion(temp1,datos.expresion.val)
        self.crearNodoWhere(temp1, instruccion)

    def crearNodoWhere(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'WHERE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 

        if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.MENQUE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYIGQUE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.MENIGQUE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.DOBLEIGUAL:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.NOIG:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.DIFERENTE:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)
        if instruccion.expresion.operador == OPERACION_RELACIONAL.IGUAL:
                self.Valores1(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2(temp1, instruccion)  

    def operador(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Operador')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1, instruccion.expresion.operador)      

    def Valores1(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'expresion 1')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        if instruccion.expresion.exp1.etiqueta == TIPO_VALOR.IDENTIFICADOR:
            self.crearNodoExpresion(temp1,instruccion.expresion.exp1.val)

          
    def Valores2(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'expresion 2')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.expresion.exp2.etiqueta == TIPO_VALOR.NUMERO:
            self.crearNodoExpresion(temp1, instruccion.expresion.exp2.val)  

    def crearNodoDropTable(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DROP_TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.Crear_lista_parametros1(temp1,instruccion)
        

    def Crear_lista_parametros1(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Tablas')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.lista_ids != []:
            for datos in instruccion.lista_ids:
                self.crearNodoExpresion(temp1,datos.val)

            
    def crearNodoAlterTable(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ALTER TABLE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_CHECK:
            self.crearAlterTable_addcheck(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_FOREIGN:
            self.crearAlterTable_foreign(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_CHECK:
            self.crearAlterTable_addContraintCheck(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_UNIQUE:
            self.crearAlterTable_Unique(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_CONSTRAINT_FOREIGN:
            self.crearAlterTable_ConstraintForeign(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN:
            self.crearAlterTable_Column(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ADD_COLUMN:
            self.crearAlterAddDropColumn(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.DROP_COLUMN:
            self.crearAlterDrop_Column(temp1,instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN_NULL:
            self.crearNodoAlterColumSET_NULL(temp1,instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.ALTER_COLUMN_NOT_NULL:
            self.crearNodoAlterColumSET_NONULL(temp1,instruccion)
        elif instruccion.etiqueta == TIPO_ALTER_TABLE.DROP_CONSTRAINT:
            self.crearNodoAlterDROPCONSTRAINT(temp1,instruccion)

    def crearNodoAlterDROPCONSTRAINT(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DROP CONSTRAINT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador)
        if instruccion.lista_campos != []:
            for datos in instruccion.lista_campos:
                self.crearNodoExpresion(temp1,datos)

    def crearNodoAlterColumSET_NONULL(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ALTER COLUMN SET NOT NULL')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearNodoExpresion(temp1,instruccion.columnid)

    def crearNodoAlterColumSET_NULL(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ALTER COLUMN SET NULL')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearNodoExpresion(temp1,instruccion.columnid)

    def crearAlterDrop_Column(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Alter Add Column')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        self.crearNodoExpresion(temp1,instruccion.identificador)
        if instruccion.lista_campos != []:
            for datos in instruccion.lista_campos:
                self.crearNodoExpresion(temp1,datos.val)

    def crearAlterTable_Column(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Alter Column')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)   
        self.crearNodoExpresion(temp1,instruccion.identificador)
        if instruccion.lista_campos != []:
            for datos in instruccion.lista_campos:
                self.crearNodoExpresion(temp1,datos.identificador.val)
                self.crearNodoExpresion(temp1,datos.tipo.val)
                if datos.par1 != None:
                    self.crearNodoExpresion(temp1,datos.par1)
                if datos.par2 != None:
                    self.crearNodoExpresion(temp1,datos.par2)

    def crearAlterTable_ConstraintForeign(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Constraint Foreign')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearNodoExpresion(temp1,instruccion.columnid)
        self.crearAlterTable_foreign_columna(temp1, instruccion)
        self.crearAlterTable_foreign_referencia(temp1, instruccion)

    def crearAlterTable_Unique(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Unique')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearNodoExpresion(temp1,instruccion.columnid)
        self.crearAlterTable_foreign_columna(temp1, instruccion)


    def crearAlterTable_addContraintCheck(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Add Contraint Check')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearNodoExpresion(temp1,instruccion.columnid)   
        self.crearAlterTable_addcheck_Condicion(temp1, instruccion)


    def crearAlterTable_foreign(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Add Foreign')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)                
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearAlterTable_foreign_columna(temp1, instruccion)
        self.crearAlterTable_foreign_referencia(temp1, instruccion)

    def crearAlterTable_foreign_columna(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Columna')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)                
        self.crearNodoExpresion(temp1,instruccion.columnid)


    def crearAlterTable_foreign_referencia(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'referencia')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)      
        self.crearNodoExpresion(temp1,instruccion.tocolumnid)          
        self.crearNodoExpresion(temp1,instruccion.lista_campos)      

    def crearAlterTable_addcheck(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Add check')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)                
        self.crearNodoExpresion(temp1,instruccion.identificador)
        self.crearAlterTable_addcheck_Condicion(temp1, instruccion)

    def crearAlterTable_addcheck_Condicion(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Condicion')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.expresionlogica.operador == OPERACION_LOGICA.AND or instruccion.expresionlogica.operador == OPERACION_LOGICA.OR: 
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp1.exp1.val)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp1.exp2.val)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.operador)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp2.exp1.val)
            self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp2.exp2.val)
        else:
            if isinstance(instruccion.expresionlogica.exp1,ExpresionIdentificador):
                self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp1.val)
            elif isinstance(instruccion.expresionlogica.exp2,ExpresionIdentificador):
                self.crearNodoExpresion(temp1,instruccion.expresionlogica.exp2.val)

    
    def crearNodoInsert(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'INSERT')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoTABLA(temp1,instruccion)
        self.crearNodoLISTA_PARAMETROS(temp1, instruccion)
        self.CrearNodoLista_VALORES(temp1, instruccion)

    def crearNodoTABLA(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TABLA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1, instruccion.val)

    def crearNodoLISTA_PARAMETROS(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'LISTA PARAMETROS')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

        if instruccion.etiqueta == TIPO_INSERT.CON_PARAMETROS:
            if instruccion.lista_parametros != []:
                for parametros in instruccion.lista_parametros:
                    self.crearNodoExpresion(temp1,parametros.val)

    def CrearNodoLista_VALORES(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'LISTA DATOS')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)

        if instruccion.lista_datos != []:
            for parametros in instruccion.lista_datos:
                self.crearNodoExpresion(temp1,parametros)
        

    #ENUM TYPE
    def crearNodoEnum(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Enum')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1,instruccion.identificador.val)
        self.crearNodoEnum_lista(temp1,instruccion)

    def crearNodoEnum_lista(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Lista_parametros')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.lista_datos != []:
            for datos in instruccion.lista_datos:
                self.crearNodoExpresion(temp1,datos.val)

    def crearNodoDelete(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DELETE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.etiqueta == TIPO_DELETE.DELETE_NORMAL:
            self.crearNodoDelete_Normal(temp1, instruccion) 
        elif instruccion.etiqueta == TIPO_DELETE.DELETE_RETURNING:
            self.crearNodoDelete_returning(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_DELETE.DELETE_EXIST:
            self.crearNodoExpresion(temp1,instruccion.val)
            self.crearNodoWhereDelete(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_DELETE.DELETE_EXIST_RETURNING:
            self.Nombre_existes_returning(temp1, instruccion)
            self.crearNodoDelete_returning(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_DELETE.DELETE_USING:
            self.crearNodoExpresion(temp1, instruccion.val)
            self.crearNodO_USING(temp1, instruccion)
            self.crearNodoWhereDelete(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_DELETE.DELETE_USING_returnin:
            self.crearNodoExpresion(temp1, instruccion.val)
            self.crearNodO_USING(temp1, instruccion)
            self.crearNodoWhereDelete(temp1, instruccion)

    def crearNodO_USING(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'USING')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)    
        self.crearNodoExpresion(temp1, instruccion.id_using)

    def crearNodoDelete_Normal(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DELETE NORMAL')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)    
        if instruccion.etiqueta == TIPO_DELETE.DELETE_NORMAL:
            self.crearNodoExpresion(temp1,instruccion.val)

    def crearNodoDelete_returning(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DELETE_RETURNING')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        
        if instruccion.etiqueta == TIPO_DELETE.DELETE_RETURNING:
            self.crearNodoExpresion(temp1, instruccion.val)
            self.NombreTabla_returning(temp1, instruccion)
        elif instruccion.etiqueta == TIPO_DELETE.DELETE_USING_returnin:
            self.NombreTabla_returning(temp1, instruccion)


    def crearNodoWhereDelete(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'WHERE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 


        print(instruccion.etiqueta)

        if instruccion.etiqueta == TIPO_DELETE.DELETE_EXIST:
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MENQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYIGQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MENIGQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.DOBLEIGUAL:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.NOIG:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.DIFERENTE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.IGUAL:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)

        elif instruccion.etiqueta == TIPO_DELETE.DELETE_USING:
            
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MENQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYIGQUE:
                self.Valores1(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MENIGQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.DOBLEIGUAL:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.NOIG:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.DIFERENTE:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.IGUAL:
                self.Valores1Delete(temp1, instruccion)
                self.operadorDelete(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)

        elif instruccion.etiqueta == TIPO_DELETE.DELETE_USING_returnin:
            
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MENQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MAYIGQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.MENIGQUE:
                self.Valores1Delete(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.DOBLEIGUAL:
                self.Valores1Delete(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.NOIG:
                self.Valores1Delete(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.DIFERENTE:
                self.Valores1Delete(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)
            if instruccion.expresion.operador == OPERACION_RELACIONAL.IGUAL:
                self.Valores1Delete(temp1, instruccion)
                self.operador(temp1, instruccion)
                self.Valores2Delete(temp1, instruccion)

    def Nombre_existes_returning(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DATOS DELETE RETURNING')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  

        if instruccion.etiqueta == TIPO_DELETE.DELETE_EXIST_RETURNING:
            self.crearNodoExpresion(temp1, instruccion.val)
            self.NombreTabla_returning(temp1, instruccion)

    def NombreTabla_returning(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'DATOS DELETE RETURNING')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)                

        if instruccion.etiqueta == TIPO_DELETE.DELETE_RETURNING:
            if instruccion.returning != []:
                    for retornos in instruccion.returning:
                        self.crearNodoExpresion(temp1, retornos.etiqueta)

    def operadorDelete(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Operador')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoExpresion(temp1, instruccion.expresion.operador)      

    def Valores1Delete(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'expresion 1')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos) 
        if instruccion.expresion.exp1.etiqueta == TIPO_VALOR.IDENTIFICADOR:
            self.crearNodoExpresion(temp1,instruccion.expresion.exp1.val)

    def Valores2Delete(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'expresion 2')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.expresion.exp2.etiqueta == TIPO_VALOR.NUMERO:
            self.crearNodoExpresion(temp1, instruccion.expresion.exp2.val)   

    def crearAlterAddDropColumn(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Alter Add Column')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.lista_campos != []:
            for datos in instruccion.lista_campos:
                self.crearNodoExpresion(temp1,datos.identificador.val)
                self.crearNodoExpresion(temp1,datos.tipo.val)
                if datos.par1 != None:
                    self.crearNodoExpresion(temp1,datos.par1)
                if datos.par2 != None:
                    self.crearNodoExpresion(temp1,datos.par2)



#SELECTTTTTTTTTTTTTTTTTTTT

    def crearNodo_SelectTable(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Select Table')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if  instruccion.instr1 != None and instruccion.instr2 == None and instruccion.instr3 == None and instruccion.listains == None and instruccion.listanombres != None:
            if instruccion.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
                for datos in instruccion.instr1.listac:
                    self.crearNodoExpresion(temp1,datos.val)

            if instruccion.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
                for datos in instruccion.instr1.lista_extras:
                    if datos.etiqueta == OPCIONES_SELECT.CASE:
                        for objs in datos.listacase:
                            self.crearNodoExpresion(temp1,objs.exp1.exp1.exp1.val) #SOLO ETIQUETAS
                            self.crearNodoExpresion(temp1,objs.exp1.exp1.operador) #SOLO ETIQUETAS
                            self.crearNodoExpresion(temp1,objs.exp1.exp1.exp2.val) #SOLO ETIQUETAS
                            self.crearNodoExpresion(temp1,objs.exp1.operador) #operador logico
                            self.crearNodoExpresion(temp1,objs.exp1.exp2.exp1.val)
                            self.crearNodoExpresion(temp1,objs.exp1.exp2.operador)
                            self.crearNodoExpresion(temp1,objs.exp1.exp2.exp2.val)
                            self.crearNodoExpresion(temp1,objs.operador)
                        self.crearNodoExpresion(temp1,datos.expresion.val)

                    elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                        self.crearNodoExpresion(temp1,datos.val)
                    elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                        self.crearNodoExpresion(temp1,datos.val+'.*')
                    else:
                        self.crearNodoExpresion(temp1,datos.etiqueta) #RESTO DE ETIQUETAS

            if instruccion.listanombres != []:
                for datos in instruccion.listanombres:
                    if datos.etiqueta == TIPO_VALOR.DOBLE:
                        self.crearNodoExpresion(temp1,datos.val+'.'+datos.val1)
                    elif datos.etiqueta == TIPO_VALOR.AS_ID:
                        self.crearNodoExpresion(temp1,datos.val)
                        self.crearNodoExpresion(temp1,datos.val1.val)
                    elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 != None:
                        self.crearNodoExpresion(temp1,datos.val)
                        self.crearNodoExpresion(temp1,datos.val1)
                    elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 == None:
                        self.crearNodoExpresion(temp1,datos.val)

        
        elif instruccion.instr1 != None and instruccion.instr2 != None and instruccion.instr3 == None and instruccion.listains == None and instruccion.listanombres != None:
            if instruccion.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
                for datos in instruccion.instr1.listac:
                    self.crearNodoExpresion(temp1,datos.val)
            if instruccion.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
                for datos in instruccion.instr1.lista_extras:
                    if datos.etiqueta == OPCIONES_SELECT.CASE:
                        for objs in datos.listacase:
                            self.crearNodoExpresion(temp1,objs.exp1.exp1.exp1.val) #SOLO ETIQUETAS
                            self.crearNodoExpresion(temp1,objs.exp1.exp1.etiqueta) #SOLO ETIQUETAS
                            self.crearNodoExpresion(temp1,objs.exp1.exp1.exp2.val) #SOLO ETIQUETAS
                            self.crearNodoExpresion(temp1,objs.exp1.etiqueta) #operador logico
                            self.crearNodoExpresion(temp1,objs.exp1.exp2.exp1.val)
                            self.crearNodoExpresion(temp1,objs.exp1.exp2.etiqueta)
                            self.crearNodoExpresion(temp1,objs.exp1.exp2.exp2.val)
                            self.crearNodoExpresion(temp1,objs.etiqueta)
                        self.crearNodoExpresion(temp1,datos.expresion.val)
                    elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                        self.crearNodoExpresion(temp1,datos.val)
                    elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                        self.crearNodoExpresion(temp1,datos.val+'.*')
                    else:
                        self.crearNodoExpresion(temp1,datos.etiqueta) #RESTO DE ETIQUETAS
        
            if instruccion.listanombres != []:
                for datos in instruccion.listanombres:
                    if datos.etiqueta == TIPO_VALOR.DOBLE:
                        self.crearNodoExpresion(temp1,datos.val+'.'+datos.val1)
                    elif datos.etiqueta == TIPO_VALOR.AS_ID:
                        self.crearNodoExpresion(temp1,datos.val)
                        self.crearNodoExpresion(temp1,datos.val1.val)
                    elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 != None:
                        self.crearNodoExpresion(temp1,datos.val)
                        self.crearNodoExpresion(temp1,datos.val1)
                    elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 == None:
                        self.crearNodoExpresion(temp1,datos.val)
            
            if instruccion.instr2.expwhere != None:
                self.crearNodoExpresion(temp1,instruccion.instr2.expwhere.etiqueta)
                self.crearNodoExpresion(temp1,instruccion.instr2.expwhere.expresion.etiqueta)
                if instruccion.instr2.expwhere.expresion.etiqueta != None:
                    self.VerificarWhere(temp1,instruccion.instr2.expwhere.expresion.etiqueta,instruccion.instr2.expwhere.expresion)
            if instruccion.instr2.expgb != None:
                self.crearNodoExpresion(temp1,instruccion.instr2.expgb.etiqueta)
                for datos in instruccion.instr2.expgb.expresion:
                    self.crearNodoExpresion(temp1,datos.id)
            if instruccion.instr2.expob != None:
                self.crearNodoExpresion(temp1,instruccion.instr2.expob.etiqueta)
                for datos in instruccion.instr2.expob.expresion:
                    self.crearNodoExpresion(temp1,datos.val)
            if instruccion.instr2.exphav != None:
                self.crearNodoExpresion(temp1,instruccion.instr2.exphav.etiqueta)
                self.crearNodoExpresion(temp1,instruccion.instr2.exphav.expresion)
            if instruccion.instr2.exporden != None:
                self.crearNodoExpresion(temp1,instruccion.instr2.exporden.etiqueta)
                self.crearNodoExpresion(temp1,instruccion.instr2.exporden.expresion.id)
            if instruccion.instr2.explimit != None:
                self.crearNodoExpresion(temp1,instruccion.instr2.explimit.etiqueta)
                if instruccion.instr2.explimit.expresion.etiqueta == TIPO_VALOR.NUMERO:
                    self.crearNodoExpresion(temp1,instruccion.instr2.explimit.expresion.val)
                else:
                    self.crearNodoExpresion(temp1,instruccion.instr2.explimit.expresion.val)
            if instruccion.instr2.expoffset != None:
                self.crearNodoExpresion(temp1,instruccion.instr2.expoffset.etiqueta)
                self.crearNodoExpresion(temp1,instruccion.instr2.expoffset.expresion.val)
            if instruccion.instr2.valor != None:
                self.crearNodoExpresion(temp1,instruccion.instr2.valor)
    
        elif instruccion.instr1 == None and instruccion.instr2 != None and instruccion.instr3 != None and instruccion.listains != None and instruccion.listanombres == None:
            if instruccion.instr2.etiqueta == OPCIONES_SELECT.DISTINCT:
                for datos in instruccion.instr2.listac:
                    self.crearNodoExpresion(temp1,datos.val)
            if instruccion.instr2.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
                for datos in instruccion.instr2.lista_extras:
                    if datos.etiqueta == OPCIONES_SELECT.CASE:
                        for objs in datos.listacase:
                            self.crearNodoExpresion(temp1,objs.operador) #SOLO ETIQUETAS
                        self.crearNodoExpresion(temp1,datos.expresion.etiqueta)
                    elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                        self.crearNodoExpresion(temp1,datos.val)
                    elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                        self.crearNodoExpresion(temp1,datos.val+'.*')
                    else:
                        self.crearNodoExpresion(temp1,datos.etiqueta) #RESTO DE ETIQUETAS 
    
                if instruccion.instr3[0] == TIPO_VALOR.AS_ID:
                    self.crearNodoExpresion(temp1,instruccion.instr3[1].val)
                elif instruccion.instr3[0] == TIPO_VALOR.DOBLE:
                    self.crearNodoExpresion(temp1,instruccion.instr3[1])
                else:
                    self.crearNodoExpresion(temp1,instruccion.instr3)   

                for objs in instruccion.listains:
                    if objs.instr2 != None:
                        self.crearNodoExpresion(temp1,objs.instr1.val)
                        if objs.instr2.expwhere != None:
                            self.crearNodoExpresion(temp1,objs.instr2.expwhere.etiqueta)
                            self.crearNodoExpresion(temp1,objs.instr2.expwhere.expresion.etiqueta)
                            if objs.instr2.expwhere.expresion.etiqueta != None:
                                self.VerificarWhere(temp1,objs.instr2.expwhere.expresion.etiqueta,objs.instr2.expwhere.expresion)
                        if objs.instr2.expgb != None:
                            self.crearNodoExpresion(temp1,objs.instr2.expgb.etiqueta)
                            for datos in objs.instr2.expgb.expresion:
                                self.crearNodoExpresion(temp1,datos.id)
                        if objs.instr2.expob != None:
                            self.crearNodoExpresion(temp1,objs.instr2.expob.etiqueta)
                            for datos in objs.instr2.expob.expresion:
                                self.crearNodoExpresion(temp1,datos.val)
                        if objs.instr2.exphav != None:
                            self.crearNodoExpresion(temp1,objs.instr2.exphav.etiqueta)
                            self.crearNodoExpresion(temp1,objs.instr2.exphav.expresion)
                        if objs.instr2.exporden != None:
                            self.crearNodoExpresion(temp1,objs.instr2.exporden.etiqueta)
                            self.crearNodoExpresion(temp1,objs.instr2.exporden.expresion.id)
                        if objs.instr2.explimit != None:
                            self.crearNodoExpresion(temp1,objs.instr2.explimit.etiqueta)
                            if objs.instr2.explimit.expresion.etiqueta == TIPO_VALOR.NUMERO:
                                self.crearNodoExpresion(temp1,objs.instr2.explimit.expresion.val)
                            else:
                                self.crearNodoExpresion(temp1,objs.instr2.explimit.expresion.val)
                        if objs.instr2.expoffset != None:
                            self.crearNodoExpresion(temp1,objs.instr2.expoffset.etiqueta)
                            self.crearNodoExpresion(temp1,objs.instr2.expoffset.expresion.val)
                        if objs.instr2.valor != None:
                            self.crearNodoExpresion(temp1,objs.instr2.valor)
                    elif objs.instr2 == None:
                        self.crearNodoExpresion(temp1,objs.instr1.val)

        elif instruccion.instr1 != None and instruccion.instr2 == None and instruccion.instr3 != None and instruccion.listains != None and instruccion.listanombres == None:
            if instruccion.instr1.etiqueta == OPCIONES_SELECT.DISTINCT:
                for datos in instruccion.instr1.listac:
                    self.crearNodoExpresion(temp1,datos.val)

            if instruccion.instr1.etiqueta == OPCIONES_SELECT.SUBCONSULTA:
                for datos in instruccion.instr1.lista_extras:
                    if datos.etiqueta == OPCIONES_SELECT.CASE:
                        for objs in datos.listacase:
                            self.crearNodoExpresion(temp1,objs.operador) #SOLO ETIQUETAS
                        self.crearNodoExpresion(temp1,datos.expresion.etiqueta)
                    elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                        self.crearNodoExpresion(temp1,datos.val)
                    elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                        self.crearNodoExpresion(temp1,datos.val+'.*')
                    else:
                        self.crearNodoExpresion(temp1,datos.etiqueta) #RESTO DE ETIQUETAS
                        

            for objs in instruccion.listains:
                self.crearNodoExpresion(temp1,objs.val)

            if instruccion.instr3.expwhere != None:
                self.crearNodoExpresion(temp1,instruccion.instr3.expwhere.etiqueta)
                if instruccion.instr3.expwhere.expresion.operador != None:
                    self.crearNodoExpresion(temp1,instruccion.instr3.expwhere.expresion.operador)
                    self.VerificarWhere(temp1,instruccion.instr3.expwhere.expresion.operador,instruccion.instr3.expwhere.expresion)
            if instruccion.instr3.expgb != None:
                self.crearNodoExpresion(temp1,instruccion.instr3.expgb.etiqueta)
                for datos in instruccion.instr3.expgb.expresion:
                    self.crearNodoExpresion(temp1,datos.id)
            if instruccion.instr3.expob != None:
                self.crearNodoExpresion(temp1,instruccion.instr3.expob.etiqueta)
                for datos in instruccion.instr3.expob.expresion:
                    self.crearNodoExpresion(temp1,datos.val)
            if instruccion.instr3.exphav != None:
                self.crearNodoExpresion(temp1,instruccion.instr3.exphav.etiqueta)
                self.crearNodoExpresion(temp1,instruccion.instr3.exphav.expresion)
            if instruccion.instr3.exporden != None:
                self.crearNodoExpresion(temp1,instruccion.instr3.exporden.etiqueta)
                self.crearNodoExpresion(temp1,instruccion.instr3.exporden.expresion.id)
            if instruccion.instr3.explimit != None:
                self.crearNodoExpresion(temp1,instruccion.instr3.explimit.etiqueta)
                if instruccion.instr3.explimit.expresion.etiqueta == TIPO_VALOR.NUMERO:
                    self.crearNodoExpresion(temp1,instruccion.instr3.explimit.expresion.val)
                else:
                    self.crearNodoExpresion(temp1,instruccion.instr3.explimit.expresion.val)
            if instruccion.instr3.expoffset != None:
                self.crearNodoExpresion(temp1,instruccion.instr3.expoffset.etiqueta)
                self.crearNodoExpresion(temp1,instruccion.instr3.expoffset.expresion.val)
            if instruccion.instr3.valor != None:
                self.crearNodoExpresion(temp1,instruccion.instr3.valor)
    
        elif instruccion.instr1 == None and instruccion.instr2 == None and instruccion.instr3 == None and instruccion.listains == None and instruccion.listanombres != None:
            for datos in instruccion.listanombres:
                #CON IDENTIFICADOR 
                if datos.expresion != None and datos.asterisco != None:
                    if datos.expresion.operador == OPERACION_ARITMETICA.WIDTH_BUCKET:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp3.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp4.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.E_DIV:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.GCD:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.MOD:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.POWER:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.TRUNC:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2D:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == CADENA_BINARIA.SUBSTRING:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp3.val)
                    elif datos.expresion.operador == CADENA_BINARIA.TRIM:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                    elif datos.expresion.operador == CADENA_BINARIA.SUBSTR:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp3.val)
                    elif datos.expresion.operador == CADENA_BINARIA.GET_BYTE:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == CADENA_BINARIA.SET_BYTE:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp3.val)
                    elif datos.expresion.operador == CADENA_BINARIA.ENCODE:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == CADENA_BINARIA.DECODE:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    else:
                        self.crearNodoExpresion(temp1,datos.expresion.operador)
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                    
                    if datos.asterisco[0] == TIPO_VALOR.AS_ID:
                        self.crearNodoExpresion(temp1,datos.asterisco[1].val)
                    elif datos.asterisco[0] == TIPO_VALOR.DOBLE:
                        self.crearNodoExpresion(temp1,datos.asterisco[1])
                    else:
                        self.crearNodoExpresion(temp1,datos.asterisco)
                #SIN IDENTIFICADOR
                if datos.expresion != None and datos.asterisco == None:
                    if datos.expresion.operador == OPERACION_ARITMETICA.WIDTH_BUCKET:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp3.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp4.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.E_DIV:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.GCD:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.MOD:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.POWER:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.TRUNC:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == OPERACION_ARITMETICA.ATAN2D:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == CADENA_BINARIA.SUBSTRING:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp3.val)
                    elif datos.expresion.operador == CADENA_BINARIA.TRIM:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                    elif datos.expresion.operador == CADENA_BINARIA.SUBSTR:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp3.val)
                    elif datos.expresion.operador == CADENA_BINARIA.GET_BYTE:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == CADENA_BINARIA.SET_BYTE:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp3.val)
                    elif datos.expresion.operador == CADENA_BINARIA.ENCODE:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    elif datos.expresion.operador == CADENA_BINARIA.DECODE:
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
                        self.crearNodoExpresion(temp1,datos.expresion.exp2.val)
                    else:
                        self.crearNodoExpresion(temp1,datos.expresion.operador)
                        self.crearNodoExpresion(temp1,datos.expresion.exp1.val)
        

    def VerificarWhere(self,padre,etiqueta,objeto):
        if etiqueta == OPCION_VERIFICAR.N_BETWEEN:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp2))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp2))
        elif etiqueta == OPCION_VERIFICAR.ISDISTINCT: #estoy aca
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp2))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp2))
        elif etiqueta == OPCION_VERIFICAR.NOT_DISTINCT:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp2))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp2))
        elif etiqueta == OPCION_VERIFICAR.LIKE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp2))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp2))
        elif etiqueta == OPCION_VERIFICAR.NOT_LIKE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1.exp2))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2.exp2))
        elif etiqueta == OPCION_VERIFICAR.NULL:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPCION_VERIFICAR.ISNULL:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPCION_VERIFICAR.NOTNULL:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPCION_VERIFICAR.TRUE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPCION_VERIFICAR.N_TRUE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPCION_VERIFICAR.FALSE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPCION_VERIFICAR.N_FALSE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPCION_VERIFICAR.UNKNOWN:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPCION_VERIFICAR.N_UNKNOWN:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
        elif etiqueta == OPERACION_ARITMETICA.ABS:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
        elif etiqueta == OPERACION_ARITMETICA.LENGTH:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
        elif etiqueta == OPERACION_ARITMETICA.CBRT:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
        elif etiqueta == OPERACION_ARITMETICA.CEIL:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
        elif etiqueta == OPERACION_ARITMETICA.CEILING:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
        elif etiqueta == OPCIONES_DATOS.SUBSTRING:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val2))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val3))
        elif etiqueta == OPCIONES_DATOS.TRIM:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
        elif etiqueta == OPCIONES_DATOS.SUBSTR:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val2))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val3))
        elif etiqueta == OPCIONES_DATOS.EXTRACT:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val2))
        elif etiqueta == OPCION_VERIFICAR.NOT_IN:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
            #procesar_select_general(objeto.val2)
        elif etiqueta == OPCION_VERIFICAR.INN:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
            #procesar_select_general(objeto.val2)
        elif etiqueta == OPCION_VERIFICAR.NOT_EXISTS: #NO FUNCIONA ACTUALMENTE
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
            #procesar_select_general(objeto.val2)
        elif etiqueta == OPCION_VERIFICAR.NOT_BETWEEN_SYMETRIC:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val2))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.val3))
        elif etiqueta == OPERACION_RELACIONAL.MAYQUE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2))
        elif etiqueta == OPERACION_RELACIONAL.MENQUE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2))
        elif etiqueta == OPERACION_RELACIONAL.MAYIGQUE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2))
        elif etiqueta == OPERACION_RELACIONAL.MENIGQUE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2))
        elif etiqueta == OPERACION_RELACIONAL.DOBLEIGUAL:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2))
        elif etiqueta == OPERACION_RELACIONAL.IGUAL:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2))
        elif etiqueta == OPERACION_RELACIONAL.NOIG:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2))
        elif etiqueta == OPERACION_RELACIONAL.DIFERENTE:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp1))
            self.crearNodoExpresion(padre,self.returnobjeto(objeto.exp2))
        else:
            self.crearNodoExpresion(padre,self.returnobjeto(objeto))

    def returnobjeto(self,cadena):
        try:
            if cadena.etiqueta == TIPO_VALOR.NUMERO:
                return cadena.val
            elif  cadena.etiqueta == TIPO_VALOR.IDENTIFICADOR:
                return cadena.val
            elif cadena.etiqueta == TIPO_VALOR.NEGATIVO:
                return cadena.val+cadena.val1
            elif cadena.etiqueta == TIPO_VALOR.DOBLE:
                return cadena.val+cadena.val1
            elif cadena.etiqueta == OPERACION_LOGICA.TRUE:
                return cadena.val
            elif cadena.etiqueta == OPERACION_LOGICA.FALSE:
                return cadena.val
            else:
                return None
        except:
            return None

    def crearNode_SelectTime(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Select_Time')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.etiqueta == SELECT_TIME.EXTRACT:
            self.crearNodoExpresion(temp1,instruccion.etiqueta)
            self.crearNodoExpresion(temp1,instruccion.val1.val)
            self.crearNodoExpresion(temp1,instruccion.val2)
        elif instruccion.etiqueta == SELECT_TIME.DATE_PART:
            self.crearNodoExpresion(temp1,instruccion.etiqueta)
            self.crearNodoExpresion(temp1,instruccion.val1)
            self.crearNodoExpresion(temp1,instruccion.val2)
        elif instruccion.etiqueta == SELECT_TIME.NOW:
            self.crearNodoExpresion(temp1,instruccion.etiqueta)
        elif instruccion.etiqueta == SELECT_TIME.CURRENT_TIME:
            self.crearNodoExpresion(temp1,instruccion.etiqueta)
        elif instruccion.etiqueta == SELECT_TIME.CURRENT_DATE:
            self.crearNodoExpresion(temp1,instruccion.etiqueta)
        elif instruccion.etiqueta == SELECT_TIME.TIMESTAMP:
            self.crearNodoExpresion(temp1,instruccion.etiqueta)
            self.crearNodoExpresion(temp1,instruccion.val1)

    def crearNode_SelectGL(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Select_Greatest_Or_Least')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        if instruccion.etiqueta == OPCIONES_SELECT.GREATEST:
            self.crearNodoExpresion(temp1,instruccion.etiqueta)
            if instruccion.lista_extras != []:
                for datos in instruccion.lista_extras:
                    if datos.etiqueta == TIPO_VALOR.DOBLE:
                        self.crearNodoExpresion(temp1,datos.val+'.'+datos.val1)
                    elif datos.etiqueta == TIPO_VALOR.NUMERO:
                        self.crearNodoExpresion(temp1,datos.val)
                    elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR:
                        self.crearNodoExpresion(temp1,datos.val)
                    elif datos.etiqueta == TIPO_VALOR.NEGATIVO:
                        self.crearNodoExpresion(temp1,datos.val+''+str(datos.val1))

        elif instruccion.etiqueta == OPCIONES_SELECT.LEAST:
            self.crearNodoExpresion(temp1,instruccion.etiqueta)
            if instruccion.lista_extras != []:
                for datos in instruccion.lista_extras:
                    if datos.etiqueta == TIPO_VALOR.DOBLE:
                        self.crearNodoExpresion(temp1,datos.val+'.'+datos.val1)
                    elif datos.etiqueta == TIPO_VALOR.NUMERO:
                        self.crearNodoExpresion(temp1,datos.val)
                    elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR:
                        self.crearNodoExpresion(temp1,datos.val)
                    elif datos.etiqueta == TIPO_VALOR.NEGATIVO:
                        self.crearNodoExpresion(temp1,datos.val+''+str(datos.val1))
  
    def crearNodo_SelectDistinct(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Distinct')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        for datos in instruccion.instr1.listac:
            self.crearNodoExpresion(temp1,datos.val)
        
    def crearNodo_SelectSubconsulta(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Subconsulta')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        for datos in instruccion.instr1.lista_extras:
                if datos.etiqueta == OPCIONES_SELECT.CASE:
                    for objs in datos.listacase:
                        self.crearNodoExpresion(temp1,objs.exp1.exp1.exp1.val) #SOLO ETIQUETAS
                        self.crearNodoExpresion(temp1,objs.exp1.exp1.etiqueta) #SOLO ETIQUETAS
                        self.crearNodoExpresion(temp1,objs.exp1.exp1.exp2.val) #SOLO ETIQUETAS
                        self.crearNodoExpresion(temp1,objs.exp1.etiqueta) #operador logico
                        self.crearNodoExpresion(temp1,objs.exp1.exp2.exp1.val)
                        self.crearNodoExpresion(temp1,objs.exp1.exp2.etiqueta)
                        self.crearNodoExpresion(temp1,objs.exp1.exp2.exp2.val)
                        self.crearNodoExpresion(temp1,objs.etiqueta)
                    self.crearNodoExpresion(temp1,datos.expresion.etiqueta)
                elif datos.etiqueta == TIPO_VALOR.ASTERISCO:
                    self.crearNodoExpresion(temp1,datos.val)
                elif datos.etiqueta == TIPO_VALOR.ID_ASTERISCO:
                    self.crearNodoExpresion(temp1,datos.val+'.*')
                else:
                    self.crearNodoExpresion(temp1,datos.etiqueta) #RESTO DE ETIQUETAS



    def crearNodo_SelectTipoValores(self,padre,instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'Tipo Valores')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        for datos in instruccion.listanombres:     
            if datos.etiqueta == TIPO_VALOR.DOBLE:
                self.crearNodoExpresion(temp1,datos.val+'.'+datos.val1)
            elif datos.etiqueta == TIPO_VALOR.AS_ID:
                self.crearNodoExpresion(temp1,datos.val)
                self.crearNodoExpresion(temp1,datos.val1.val)
            elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 != None:
                self.crearNodoExpresion(temp1,datos.val)
                self.crearNodoExpresion(temp1,datos.val1)
            elif datos.etiqueta == TIPO_VALOR.IDENTIFICADOR and datos.val1 == None:
                self.crearNodoExpresion(temp1,datos.val)

   
















