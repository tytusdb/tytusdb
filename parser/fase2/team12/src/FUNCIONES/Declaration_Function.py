import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)

function_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\FUNCIONES\\')
sys.path.append(function_dir)

entorno_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\ENTORNO\\')
sys.path.append(entorno_dir)

from Nodo import Nodo
from Object_Function import *
from Tipo_Expresion import Type_Expresion
from Tipo import Data_Type
from Simbolo import *

class Declaration_Function(Nodo):

    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
    
    def execute(self, enviroment):

        tipoMetodo = Type_Expresion(Data_Type.non)        

        # Simbolo guardar
        simboloMetodo = Simbolo_Metodo()

        nodo1 = self.hijos[0]
        
        if nodo1.nombreNodo == 'ORREPLACE' :

            nodoNombreFunction  = self.hijos[1]
            nombreFunction = nodoNombreFunction.valor.lower()

            # Nombre a guardar en tabla de símbolos
            nombreAlmacenarFuncion = 'f_' + nodoNombreFunction.valor.lower()

            # Nombre Simbolo 
            simboloMetodo.nombreMetodo = nombreFunction
            
            nodo2 = self.hijos[2]
            if nodo2.nombreNodo == 'LISTA_ARG_FUNCION':
                
                # Se asigna la lista al objeto del método a crear
                simboloMetodo.listaParametros = nodo2

                nodo3 = self.hijos[3]
                if nodo3.nombreNodo == 'SENTENCIA RETORNO':

                    simboloMetodo.sentenciaReturn = nodo3

                    tipoDato = nodo3.hijos[0].hijos[0]

                    if tipoDato.nombreNodo == 'SMALLINT':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'smallint'
                        pass

                    elif tipoDato.nombreNodo == 'INTEGER':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'integer'
                        pass
                    
                    elif tipoDato.nombreNodo == 'BIGINT':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'bigint'
                        pass

                    elif tipoDato.nombreNodo == 'DECIMAL':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'decimal'
                        pass

                    elif tipoDato.nombreNodo == 'NUMERIC':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'numeric'
                        pass

                    elif tipoDato.nombreNodo == 'REAL':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'real'
                        pass
                    
                    elif tipoDato.nombreNodo == 'MONEY':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'money'
                        pass
                    
                    elif tipoDato.nombreNodo == 'TEXT':

                        tipoMetodo.data_type = Data_Type.character
                        tipoMetodo.data_specific = 'text'
                        pass

                    elif tipoDato.nombreNodo == 'DATE':

                        tipoMetodo.data_type = Data_Type.data_time
                        tipoMetodo.data_specific = 'date'
                        pass

                    elif tipoDato.nombreNodo == 'BOOLEAN':

                        tipoMetodo.data_type = Data_Type.boolean
                        tipoMetodo.data_specific = 'boolean'
                        pass

                    nodo4 = self.hijos[4]
                    simboloMetodo.bloqueEjecutar = nodo4

                    if enviroment.existeSimboloEntornoActual(nombreAlmacenarFuncion) :

                        simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                        enviroment.actualizar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                        pass

                    else:

                        simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                        enviroment.ingresar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                        pass

                else:

                    simboloMetodo.bloqueEjecutar = nodo3
                    tipoMetodo.data_specific = 'void'

                    if enviroment.existeSimboloEntornoActual(nombreAlmacenarFuncion) :

                        simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                        enviroment.actualizar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                        pass

                    else:

                        simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                        enviroment.ingresar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                        pass

                    pass

                pass

            elif nodo2.nombreNodo == 'SENTENCIA RETORNO':
                
                tipoDato = nodo2.hijos[0].hijos[0]

                if tipoDato.nombreNodo == 'SMALLINT':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'smallint'
                    pass

                elif tipoDato.nombreNodo == 'INTEGER':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'integer'
                    pass
                    
                elif tipoDato.nombreNodo == 'BIGINT':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'bigint'
                    pass

                elif tipoDato.nombreNodo == 'DECIMAL':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'decimal'
                    pass

                elif tipoDato.nombreNodo == 'NUMERIC':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'numeric'
                    pass

                elif tipoDato.nombreNodo == 'REAL':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'real'
                    pass
                    
                elif tipoDato.nombreNodo == 'MONEY':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'money'
                    pass
                    
                elif tipoDato.nombreNodo == 'TEXT':

                    tipoMetodo.data_type = Data_Type.character
                    tipoMetodo.data_specific = 'text'
                    pass

                elif tipoDato.nombreNodo == 'DATE':

                    tipoMetodo.data_type = Data_Type.data_time
                    tipoMetodo.data_specific = 'date'
                    pass

                elif tipoDato.nombreNodo == 'BOOLEAN':

                    tipoMetodo.data_type = Data_Type.boolean
                    tipoMetodo.data_specific = 'boolean'
                    pass

                nodo3 = self.hijos[3]
                simboloMetodo.bloqueEjecutar = nodo3

                if enviroment.existeSimboloEntornoActual(nombreAlmacenarFuncion) :

                    simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                    enviroment.actualizar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                    pass

                else:

                    simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                    enviroment.ingresar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                    pass

                pass
            
            else:
                
                simboloMetodo.bloqueEjecutar = nodo2
                tipoMetodo.data_specific = 'void'

                if enviroment.existeSimboloEntornoActual(nombreAlmacenarFuncion) :

                    simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                    enviroment.actualizar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                    pass

                else:

                    simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                    enviroment.ingresar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                    pass

            pass

        else:

            nombreFunction = nodo1.valor.lower()
            simboloMetodo.nombreMetodo = nombreFunction
            nombreAlmacenarFuncion = 'f_' + nombreFunction

            nodo2 = self.hijos[1]
            if nodo2.nombreNodo == 'LISTA_ARG_FUNCION':
                
                # Se asigna la lista al objeto del método a crear
                simboloMetodo.listaParametros = nodo2

                nodo3 = self.hijos[2]
                if nodo3.nombreNodo == 'SENTENCIA RETORNO':

                    simboloMetodo.sentenciaReturn = nodo3

                    tipoDato = nodo3.hijos[0].hijos[0]

                    if tipoDato.nombreNodo == 'SMALLINT':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'smallint'
                        pass

                    elif tipoDato.nombreNodo == 'INTEGER':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'integer'
                        pass
                    
                    elif tipoDato.nombreNodo == 'BIGINT':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'bigint'
                        pass

                    elif tipoDato.nombreNodo == 'DECIMAL':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'decimal'
                        pass

                    elif tipoDato.nombreNodo == 'NUMERIC':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'numeric'
                        pass

                    elif tipoDato.nombreNodo == 'REAL':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'real'
                        pass
                    
                    elif tipoDato.nombreNodo == 'MONEY':

                        tipoMetodo.data_type = Data_Type.numeric
                        tipoMetodo.data_specific = 'money'
                        pass
                    
                    elif tipoDato.nombreNodo == 'TEXT':

                        tipoMetodo.data_type = Data_Type.character
                        tipoMetodo.data_specific = 'text'
                        pass

                    elif tipoDato.nombreNodo == 'DATE':

                        tipoMetodo.data_type = Data_Type.data_time
                        tipoMetodo.data_specific = 'date'
                        pass

                    elif tipoDato.nombreNodo == 'BOOLEAN':

                        tipoMetodo.data_type = Data_Type.boolean
                        tipoMetodo.data_specific = 'boolean'
                        pass

                    nodo4 = self.hijos[3]
                    simboloMetodo.bloqueEjecutar = nodo4

                    if enviroment.existeSimboloEntornoActual(nombreAlmacenarFuncion) :

                        print('Error: Ya se ha ingresado el método previamente')
                        pass

                    else:

                        simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                        enviroment.ingresar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                        pass

                else:

                    simboloMetodo.bloqueEjecutar = nodo3
                    tipoMetodo.data_specific = 'void'

                    if enviroment.existeSimboloEntornoActual(nombreAlmacenarFuncion) :

                        print('Error: Ya se ha ingresado el método previamente')
                        pass

                    else:

                        simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                        enviroment.ingresar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                        pass

                    pass

                pass

            elif nodo2.nombreNodo == 'SENTENCIA RETORNO':
                
                tipoDato = nodo2.hijos[0].hijos[0]

                if tipoDato.nombreNodo == 'SMALLINT':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'smallint'
                    pass

                elif tipoDato.nombreNodo == 'INTEGER':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'integer'
                    pass
                    
                elif tipoDato.nombreNodo == 'BIGINT':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'bigint'
                    pass

                elif tipoDato.nombreNodo == 'DECIMAL':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'decimal'
                    pass

                elif tipoDato.nombreNodo == 'NUMERIC':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'numeric'
                    pass

                elif tipoDato.nombreNodo == 'REAL':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'real'
                    pass
                    
                elif tipoDato.nombreNodo == 'MONEY':

                    tipoMetodo.data_type = Data_Type.numeric
                    tipoMetodo.data_specific = 'money'
                    pass
                    
                elif tipoDato.nombreNodo == 'TEXT':

                    tipoMetodo.data_type = Data_Type.character
                    tipoMetodo.data_specific = 'text'
                    pass

                elif tipoDato.nombreNodo == 'DATE':

                    tipoMetodo.data_type = Data_Type.data_time
                    tipoMetodo.data_specific = 'date'
                    pass

                elif tipoDato.nombreNodo == 'BOOLEAN':

                    tipoMetodo.data_type = Data_Type.boolean
                    tipoMetodo.data_specific = 'boolean'
                    pass

                nodo3 = self.hijos[2]
                simboloMetodo.bloqueEjecutar = nodo3

                if enviroment.existeSimboloEntornoActual(nombreAlmacenarFuncion) :

                    print("Error: Ya ha sido ingresado el método previamente")
                    pass

                else:

                    simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                    enviroment.ingresar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                    pass

                pass

            else:
                
                simboloMetodo.bloqueEjecutar = nodo2
                tipoMetodo.data_specific = 'void'

                if enviroment.existeSimboloEntornoActual(nombreAlmacenarFuncion) :

                    print('Error: Ya se ha ingresado el método previamente')
                    pass                    

                else:

                    simboloGuardar = Symbol(nombreFunction,tipoMetodo,simboloMetodo)
                    enviroment.ingresar_simbolo(nombreAlmacenarFuncion,simboloGuardar)
                    pass

                pass
            
            pass

        pass

    def compile(self, enviroment):
        pass

    def getText(self):
        pass