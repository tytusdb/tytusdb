import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)

entorno_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\ENTORNO\\')
sys.path.append(entorno_dir)

from Nodo import Nodo
from Entorno import *
from Tipo_Expresion import *
from Tipo import Data_Type
from Tipo import Type
from Label import *
from Temporal import *
from Simbolo import *

class Declaracion_Variable(Nodo):

    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
    
    def execute(self, enviroment):

        cantidadHijos = len(self.hijos)

        if cantidadHijos == 2 :
            
            identificador = self.hijos[0]
            tipoDeclaracion = self.hijos[1].hijos[0]

            nombreVariable = identificador.valor.lower()

            if tipoDeclaracion.nombreNodo == 'TEXT':

                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.character)
                    tipoVariable.data_specific = 'text'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,'')
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass
                
            elif tipoDeclaracion.nombreNodo == 'SMALLINT':

                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.numeric)
                    tipoVariable.data_specific = 'smallint'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,0)
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass
                    
            elif tipoDeclaracion.nombreNodo == 'INTEGER':
                    
                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.numeric)
                    tipoVariable.data_specific = 'integer'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,0)
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass
                    
            elif tipoDeclaracion.nombreNodo == 'BIGINT':
                    
                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.numeric)
                    tipoVariable.data_specific = 'bigint'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,0)
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass

            elif tipoDeclaracion.nombreNodo == 'DECIMAL':
                    
                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.numeric)
                    tipoVariable.data_specific = 'decimal'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,0)
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass

            elif tipoDeclaracion.nombreNodo == 'NUMERIC':
                    
                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.numeric)
                    tipoVariable.data_specific = 'numeric'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,0)
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass

            elif tipoDeclaracion.nombreNodo == 'REAL':
                    
                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.numeric)
                    tipoVariable.data_specific = 'real'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,0)
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass

            elif tipoDeclaracion.nombreNodo == 'MONEY':
                    
                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.numeric)
                    tipoVariable.data_specific = 'money'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,0)
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass

            elif tipoDeclaracion.nombreNodo == 'DATE':
                    
                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.data_time)
                    tipoVariable.data_specific = 'data'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,'2000-10-01')
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass

            elif tipoDeclaracion.nombreNodo == 'BOOLEAN':

                if enviroment.existeSimboloEntornoActual(nombreVariable) :
                    
                    print('error')
                    return False

                else:
                            
                    # Creamos Simbolo
                    tipoVariable = Type_Expresion(Data_Type.boolean)
                    tipoVariable.data_specific = 'boolean'
                    simboloVariable = Symbol(nombreVariable,tipoVariable,True)
                    enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                    pass

                pass
                
            pass

        elif cantidadHijos == 3 :
            
            identificador = self.hijos[0]
            nombreVariable = identificador.valor.lower()

            tipoDeclaracion = self.hijos[1].hijos[0]

            expresionExecute = self.hijos[2].hijos[0]
            value = expresionExecute.execute(enviroment)

            print('vienen tres nodos')

            if tipoDeclaracion.nombreNodo == 'TEXT':

                if expresionExecute.tipo.data_type == Data_Type.character :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.character)
                        tipoVariable.data_specific = 'text'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False
                
            elif tipoDeclaracion.nombreNodo == 'SMALLINT':

                if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.numeric)
                        tipoVariable.data_specific = 'smallint'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False
                    
            elif tipoDeclaracion.nombreNodo == 'INTEGER':
                    
                if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.numeric)
                        tipoVariable.data_specific = 'integer'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False
                    
            elif tipoDeclaracion.nombreNodo == 'BIGINT':
                    
                if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.numeric)
                        tipoVariable.data_specific = 'bigint'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False

            elif tipoDeclaracion.nombreNodo == 'DECIMAL':
                    
                if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.numeric)
                        tipoVariable.data_specific = 'decimal'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False

            elif tipoDeclaracion.nombreNodo == 'NUMERIC':
                    
                if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.numeric)
                        tipoVariable.data_specific = 'numeric'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False

            elif tipoDeclaracion.nombreNodo == 'REAL':
                    
                if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.numeric)
                        tipoVariable.data_specific = 'real'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False

            elif tipoDeclaracion.nombreNodo == 'MONEY':
                    
                if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.numeric)
                        tipoVariable.data_specific = 'money'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False

            elif tipoDeclaracion.nombreNodo == 'DATE':
                    
                if expresionExecute.tipo.data_type == Data_Type.data_time :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.data_time)
                        tipoVariable.data_specific = 'data'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False

            elif tipoDeclaracion.nombreNodo == 'BOOLEAN':

                if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                    if enviroment.existeSimboloEntornoActual(nombreVariable) :
                        return False
                    else:
                            
                        # Creamos Simbolo
                        tipoVariable = Type_Expresion(Data_Type.boolean)
                        tipoVariable.data_specific = 'boolean'
                        simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                        enviroment.ingresar_simbolo(nombreVariable,simboloVariable)
                        pass

                    pass
                else :
                    return False
                
            pass
    
    def compile(self, enviroment):
        
        codigoCompile = ''
        cantidadHijos = len(self.hijos)

        if cantidadHijos == 2 :
            
            identificador = self.hijos[0]
            tipoDeclaracion = self.hijos[1].hijos[0]

            nombreVariable = identificador.valor.lower()

            if tipoDeclaracion.nombreNodo == 'TEXT':

                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile
                
            elif tipoDeclaracion.nombreNodo == 'SMALLINT':

                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile
                    
            elif tipoDeclaracion.nombreNodo == 'INTEGER':
                    
                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile
                    
            elif tipoDeclaracion.nombreNodo == 'BIGINT':
                    
                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile

            elif tipoDeclaracion.nombreNodo == 'DECIMAL':
                    
                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile

            elif tipoDeclaracion.nombreNodo == 'NUMERIC':
                    
                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile

            elif tipoDeclaracion.nombreNodo == 'REAL':
                    
                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile

            elif tipoDeclaracion.nombreNodo == 'MONEY':
                    
                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile

            elif tipoDeclaracion.nombreNodo == 'DATE':
                    
                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile

            elif tipoDeclaracion.nombreNodo == 'BOOLEAN':

                codigoCompile += nombreVariable + ' = None\n'
                return codigoCompile
                
            pass

        elif cantidadHijos == 3 :
            
            identificador = self.hijos[0]
            nombreVariable = identificador.valor.lower()

            tipoDeclaracion = self.hijos[1].hijos[0]

            expresionExecute = self.hijos[2].hijos[0]
            value = None
            auxiliar = False

            if expresionExecute.nombreNodo == 'SENTENCIA_SELECT':
                value = expresionExecute.execute(enviroment)
                print('Se ejecuto la sentencia select')
                print('Tipo result: ',expresionExecute.tipo.data_type)
            else:
                value = expresionExecute.compile(enviroment)
                auxiliar = True

            if auxiliar == True :

                codigoCompile += value
                codigoCompile += nombreVariable + ' = ' + expresionExecute.dir + '\n'
                return codigoCompile
            
            else:

                if expresionExecute.tipo.data_type == Data_Type.listaDatos :
                    codigoCompile += nombreVariable + ' = None\n'
                    return codigoCompile
                else :
                    codigoCompile += nombreVariable + ' = ' + str(value) + '\n'
                    return codigoCompile
            
                
            pass

    def getText(self):
        pass