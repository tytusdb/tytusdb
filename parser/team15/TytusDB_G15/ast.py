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
            indice = indice +1
        dot.view('reportes/AST', cleanup=True)

    def crearNodoCreateDatabase(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'CREATE DATABASE')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)
        self.crearNodoNombreDatabase(temp1,instruccion)
        if instruccion.usuario.id != "":
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
            if expresion.id != "":
                contadorNodos = contadorNodos + 1
                dot.node("node" + str(contadorNodos), str(expresion.id))
                dot.edge(padre, "node" + str(contadorNodos))
        elif isinstance(expresion, ExpresionNumeroSimple):
            contadorNodos = contadorNodos + 1
            dot.node("node" + str(contadorNodos), str(expresion.val))
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
        dot.node("node" + str(contadorNodos), instruccion.id)
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
        self.crearNodoExpresion(temp1,instruccion.id)

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
        self.crearNodoExpresion(temp1,instruccion.id)

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
                self.crearNodoExpresion(temp1,ids.id)

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
        elif instruccion.tipo == 'FOREING':
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
        self.crearNodoExpresion(temp1,instruccion.id)

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
        elif instruccion.tipo == 'FOREING':
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
                    self.crearNodoExpresion(temp1,ids.id)
        
    def crearNodoConstraintForaneaId(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREING':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,instruccion.columna)

    def crearNodoConstraintForaneaTablaRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'TABLA REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREING':
            if instruccion.opciones_constraint != []:
                for ids in instruccion.opciones_constraint:
                    self.crearNodoExpresion(temp1,instruccion.referencia)

    def crearNodoConstraintForaneaIdRef(self, padre, instruccion):
        global  contadorNodos, dot
        contadorNodos = contadorNodos + 1
        dot.node("node" + str(contadorNodos), 'ID REFERENCIA')
        dot.edge(padre, "node" + str(contadorNodos))
        temp1 = "node" + str(contadorNodos)  
        if instruccion.tipo == 'FOREING':
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
                        self.crearNodoExpresion(temp1,ids.exp1.id)
                    else: 
                        self.crearNodoExpresion(temp1,ids.exp2.id)
