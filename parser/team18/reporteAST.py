#Imports

from graphviz import Digraph
from expresiones import *
from instrucciones import *
import tablasimbolos as TS
import AST as arbol
import Funciones as f
import math

from storageManager import jsonMode as EDD

contador = 0
lista_instrucciones = []

class DOTAST: 

    def __init__(self):
        print("Generando el TextDot del AST")

    def getDot(self,instrucciones):
        global contador, TextDot, lista_instrucciones
        lista_instrucciones = instrucciones
        contador = 2
        TextDot = Digraph('AST', node_attr={'shape': 'box', 'style': 'filled','color': 'whitesmoke'}, edge_attr={'color':'blue'})
        TextDot.node('node1','INICIO')
        TextDot.node('node2','INSTRUCCIONES')
        TextDot.edge('node1','node2')
        tam = 0
        while tam < len(lista_instrucciones) :
            instruccion = lista_instrucciones[tam]

            if isinstance(instruccion, CrearBD):
                self.getTextDotCrearDB("node2",instruccion)
            elif isinstance(instruccion, CrearTabla):
                self.getTextDotCrearTabla("node2",instruccion)
            elif isinstance(instruccion,EliminarDB):
                self.getTextDotEliminarBD("node2",instruccion)
            elif isinstance(instruccion,CrearType):
                self.getTextDotCrearType("node2",instruccion)
            elif isinstance(instruccion,EliminarTabla):
                self.getTextDotEliminarTabla("node2",instruccion)
            elif isinstance(instruccion,Insertar):
                self.getTextDotInsertar("node2",instruccion)
            elif isinstance(instruccion,Actualizar):
                self.getTextDotActualizarTabla("node2",instruccion)
            elif isinstance(instruccion,DBElegida):
                self.getTextDotUseDB("node2",instruccion)
            elif isinstance(instruccion,MostrarDB):
                self.getTextDotShowDB("node2",instruccion)
            elif isinstance(instruccion, ALTERDBO) : print('Alter dbo')
            elif isinstance(instruccion, ALTERTBO) : print('Alter tbo')
            else:
                for val in instruccion:
                    if(isinstance (val,SELECT)):
                        self.getTextDotSelect("node2",val)
               
                    else : print('Error: instrucción no válida') 
            tam = tam +1
            print(TextDot)
        TextDot.view('reporte_AST', cleanup=True)


    #Creacion de base de datos
    def getTextDotCrearDB(self,padre,instr):
        global contador,TextDot
        contador=contador+1
        TextDot.node("node"+str(contador),"CREATE_BD")
        TextDot.edge(padre,"node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.nombre)
        

    #Creacion de tabla 
    def getTextDotCrearTabla(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"CREATE_TABLE")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotNombreTabla(aux,instr)

        if instr.columnas != []:
            for ins in instr.columnas:
                if isinstance(ins, columnaTabla): 
                    self.getTextDotColumna(aux,ins)
              

    def getTextDotColumna(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"DATOS_COLUMNA")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotNombreColumna(aux,instr.id)
        self.getTextDotTipoDato(aux,instr)
        
    def getTextDotNombreTabla(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"NOMBRE TABLA")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.nombre)    

    def getTextDotNombreColumna(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"NOMBRE COLUMNA")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.id)

    def getTextDotTipoDato(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"TIPO_DATO")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.tipo)
        #TextDot.node(aux,instr.tipo)

    #Creacion de type   
    def getTextDotCrearType(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"CREATE_TYPE")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotNombreType(aux,instr.nombre)

        '''if instr.valores != []:
            for indice, valor in enumerate(instr.valores):
                self.getTextDotListaType(aux.valor[indice])'''
              

    def getTextDotNombreType(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"NOMBRE TYPE")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr)
    
    def getTextDotListaType(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"VALOR")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr)


    #Eliminar database
    def getTextDotEliminarBD(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"DROP_DATABASE")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.nombre)

    def getTextDotEliminarTabla(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"DROP_TABLE")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.nombre)

    def getTextDotInsertar(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"INSERT")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotNombreTabla(aux,instr)
        self.getTextDotValores(aux,instr)

    def getTextDotValores(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"VALUES")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        if(instr.valores != []):
            for ins in instr.valores:
                self.getTextDotExpresion(aux,ins)



    def getTextDotActualizarTabla(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"ACTUALIZAR TABLA")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        #Nombre tabla
        self.getTextDotNombreTabla(aux,instr)
        #condicion del where
        self.getCondicionActualizar(aux,instr)
        #Valores a cambiar
        self.getTextDotValoresActualizar(aux,instr)

    def getCondicionActualizar(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"CONDICION_WHERE")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        if(isinstance (instr.condicion,Operacion_Relacional)):
            self.getOperador(aux,instr)

    def getOperador(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        print(instr.condicion.operador)
        TextDot.node("node"+str(contador),str(instr.condicion.operador))
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.condicion.op1)
        self.getTextDotExpresion(aux,instr.condicion.op2)
    
    #Valores a actualizar
    def getTextDotValoresActualizar(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"VALUES")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        if(instr.valores != []):
            for ins in instr.valores:
                if(isinstance (ins,columna_actualizar)):
                    print("estamos aqui")
                    self.getNombreColumnaActualizar(aux,ins)
                else:
                    print("No se esta logrando")

    def getNombreColumnaActualizar(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),str(instr.nombre.id))
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.valor)

    def getTextDotUseDB(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"USE DATABASE")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getTextDotExpresion(aux,instr.nombre)

    def getTextDotShowDB(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"SHOW DATABASES")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)

        listado = EDD.showDatabases()
        if not listado:
            print("No hay base de datos")
        else:
            for val in listado:
                self.getTextDotListaBD(aux,val)
                print("Si hay bd")

    def getTextDotListaBD(self,padre,instr):
        global contador,TextDot
        contador = contador +1
        TextDot.node("node"+str(contador),str(instr))
        TextDot.edge(padre,"node"+str(contador))
        


    #Implementando
    def getTextDotSelect(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"SELECT")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        if instr.funcion_alias is not None:
            for val in instr.funcion_alias:
                if(isinstance (val,Funcion_Alias)):
                    self.getTextDotSelectMathFunc(aux,val)
        else: print('No funciono')


    def getTextDotSelectMathFunc(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"FUNCION")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getNombreFuncion(aux,instr)
        self.getAlias(aux,instr)

    #def getTextotSelectDateFunc(self,padre,instr):


    def getNombreFuncion(self,padre,instr):
        global contador,TextDot
        contador = contador+1

        if hasattr(instr.nombre, 'operador'):
            TextDot.node("node"+str(contador),str(instr.nombre.operador))
            TextDot.edge(padre, "node"+str(contador))
        elif hasattr(instr.nombre, 'tipo'):
            TextDot.node("node"+str(contador),"CURRENT_"+str(instr.nombre.tipo))
            TextDot.edge(padre, "node"+str(contador))
        elif hasattr(instr.nombre, 'valor'):
            TextDot.node("node"+str(contador),str(instr.nombre.valor.valor))
            TextDot.edge(padre, "node"+str(contador))
            print("nose que pasa")
        elif hasattr(instr.nombre, 'val1'):
            TextDot.node("node"+str(contador),"DATE_PART")
            TextDot.edge(padre, "node"+str(contador))
        elif hasattr(instr.nombre, 'medida'):
            TextDot.node("node"+str(contador),"EXTRACT")
            TextDot.edge(padre, "node"+str(contador))
        
        else:
            print("Exito")

        aux = "node"+str(contador)

        if isinstance(instr.nombre, Operacion_Math_Unaria):
            valor = arbol.resolver_operacion(instr.nombre.op,"")
            self.getTextDotExpresion(aux,valor)
        elif isinstance(instr.nombre, Operacion_Math_Binaria):
            op1 = arbol.resolver_operacion(instr.nombre.op1,"")
            op2 = arbol.resolver_operacion(instr.nombre.op2,"")
            self.getTextDotExpresion(aux,op1)
            self.getTextDotExpresion(aux,op2)
        elif isinstance(instr.nombre,Operacion__Cubos):
            op1 = arbol.resolver_operacion(instr.nombre.op1,"")
            op2 = arbol.resolver_operacion(instr.nombre.op2,"")
            op3 = arbol.resolver_operacion(instr.nombre.op3,"")
            op4 = arbol.resolver_operacion(instr.nombre.op4,"")
            self.getTextDotExpresion(aux,op1)
            self.getTextDotExpresion(aux,op2)
            self.getTextDotExpresion(aux,op3)
            self.getTextDotExpresion(aux,op4)
        elif isinstance(instr.nombre, Operacion_Definida):
            #if instr.nombre.operador == OPERACION_MATH.PI: self.getTextDotExpresion(aux,"Pi()")
            #elif instr.nombre.operador == OPERACION_MATH.RANDOM: self.getTextDotExpresion(aux,"Random()")
            print("funciones definidas")
        elif isinstance(instr.nombre, Operacion_Strings):
            op = arbol.resolver_operacion(instr.nombre.cadena,"")
            self.getTextDotExpresion(aux,op)
        elif isinstance(instr.nombre,Operacion_String_Binaria):
            op1 = arbol.resolver_operacion(instr.nombre.op1,ts)
            op2 = arbol.resolver_operacion(instr.nombre.op2,ts)
            self.getTextDotExpresion(aux,op1)
            self.getTextDotExpresion(aux,op2)
        elif isinstance(instr.nombre,Operacion_String_Compuesta):
            op1 = arbol.resolver_operacion(instr.nombre.op1,"")
            op2 = arbol.resolver_operacion(instr.nombre.op2,"")
            op3 = arbol.resolver_operacion(instr.nombre.op3,"")
            self.getTextDotExpresion(aux,op1)
            self.getTextDotExpresion(aux,op2)
            self.getTextDotExpresion(aux,op3)
        elif isinstance(instr.nombre, Operacion_Patron):
            op1 = arbol.resolver_operacion(instr.nombre.op1,"")
            self.getTextDotExpresion(aux,op1)
        elif isinstance(instr.nombre, Operacion_NOW):
            TextDot.node("node"+str(contador),"NOW")
            TextDot.edge(padre, "node"+str(contador))
        elif isinstance(instr.nombre, Operacion_CURRENT):
            op = arbol.resolver_operacion(instr.nombre,"")
            self.getTextDotExpresion(aux,op)
        elif isinstance(instr.nombre, Operando_EXTRACT): 
            op = arbol.resolver_operacion(instr.nombre,"")
            self.getTextDotExpresion(aux,op)
        elif isinstance(instr.nombre, Operacion_DATE_PART): 
            op1 = arbol.resolver_operacion(instr.nombre.val1,"")
            op2 = arbol.resolver_operacion(instr.nombre.val2,"")
            self.getTextDotExpresion(aux,op1)
            self.getTextDotExpresion(aux,op1)
        elif isinstance(instr.nombre, Operacion_TIMESTAMP):
            op = arbol.resolver_operacion(instr.nombre,"")
            self.getTextDotExpresion(aux,op)
        elif isinstance(instr.nombre, Operacion_Great_Least):
            op = arbol.resolver_operacion(instr.nombre,"")
            self.getTextDotExpresion(aux,op)
            


        
        

    def getAlias(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        TextDot.node("node"+str(contador),"ALIAS")
        TextDot.edge(padre, "node"+str(contador))
        aux = "node"+str(contador)
        self.getNombreAlias(aux,instr)

    def getNombreAlias(self,padre,instr):
        global contador,TextDot
        contador = contador+1
        if isinstance (instr.alias,Operando_ID):
            TextDot.node("node"+str(contador),str(instr.alias.id))
            TextDot.edge(padre, "node"+str(contador))
        elif isinstance (instr.alias,Operando_Cadena):
            TextDot.node("node"+str(contador),str(instr.alias.valor))
            TextDot.edge(padre, "node"+str(contador))

    #Expresiones resultantes 
    def getTextDotExpresion(self, padre, expresion):
        global contador, TextDot
        if isinstance(expresion, Operando_ID):
            contador = contador + 1
            TextDot.node("node" + str(contador), str(expresion.id))
            TextDot.edge(padre, "node" + str(contador))
        elif isinstance(expresion, Operando_Numerico):
            contador = contador + 1 
            TextDot.node("node" + str(contador), str(expresion.valor))
            TextDot.edge(padre, "node" + str(contador))
        elif isinstance(expresion, Operando_Cadena):
            contador = contador + 1
            TextDot.node("node"+str(contador),str(expresion.valor))
            TextDot.edge(padre,"node"+str(contador))
        else:
            contador = contador + 1
            TextDot.node("node"+str(contador),str(expresion))
            TextDot.edge(padre,"node"+str(contador))

    