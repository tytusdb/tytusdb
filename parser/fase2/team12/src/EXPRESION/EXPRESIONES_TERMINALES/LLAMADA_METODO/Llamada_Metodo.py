import sys, os.path
import math

dir_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\EXPRESION\\EXPRESION\\')
sys.path.append(dir_nodo)

ent_nodo = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\ENTORNO\\')
sys.path.append(ent_nodo)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')) + '\\C3D\\')
sys.path.append(c3d_dir)


from Expresion import Expresion
from Tipo import Data_Type
from Tipo_Expresion import Type_Expresion
from Entorno import *
from Simbolo import *
from Label import *
from Temporal import *

class Llamada_Metodo(Expresion):

    def __init__(self, nombreNodo, fila, columna, valor):
        Expresion.__init__(self, nombreNodo, fila, columna, valor)    
    
    def execute(self, enviroment):

        print('Llamada a Métodos')
        identificador = self.hijos[0]
        listaParams = self.hijos[1]
        self.tipo = Type_Expresion(Data_Type.non)

        # El entorno es la tabla de Símbolos
        try:
            nombreIdentificador = 'f_' + identificador.valor.lower()
            simbolo = enviroment.obtener_simbolo(nombreIdentificador)

            if simbolo == None :

                self.tipo = Type_Expresion(Data_Type.error)
                self.valorExpresion = None
                return self.valorExpresion
            
            else:

                #print('Está el método')
                valorMetodo = simbolo.valor

                # Verificar que la cantidad de parametros sea correcta
                cantParametros = len(listaParams.hijos)
                #print('lista Params: ',cantParametros)

                if valorMetodo.listaParametros == None :
                    
                    if cantParametros == 0 :

                        entornoLocal = Entorno(enviroment.Global)
                        entornoLocal.Global = enviroment.Global
                        entornoLocal.nombreEntorno = identificador.valor.lower()
                        enviroment.entornosLocales.append(entornoLocal)
                        
                        cantidadHijos = len(valorMetodo.bloqueEjecutar.hijos)

                        if cantidadHijos == 2 :

                            declaracion = valorMetodo.bloqueEjecutar.hijos[0]
                            bloque = valorMetodo.bloqueEjecutar.hijos[1]

                            # Ejecutamos la declaracion de variables
                            declaracion.execute(entornoLocal)
                            valorBloque = bloque.execute(entornoLocal)

                            #Validacion Return
                            if valorBloque != None :

                                if simbolo.data_type == valorBloque.tipo.data_type :
                                    print('Va todo bien crack n.n')

                                pass
                            else:

                                if simbolo.data_type == Data_Type.non:

                                    self.tipo = Type_Expresion(Data_Type.non)
                                    self.valorExpresion = None
                                    return self.valorExpresion
                                
                                else:

                                    self.tipo = Type_Expresion(Data_Type.error)
                                    self.valorExpresion = None
                                    return self.valorExpresion

                            pass
                            
                        else:
                            
                            bloque = valorMetodo.bloqueEjecutar.hijos[0]
                            valorBloque = bloque.execute(entornoLocal)

                            if valorBloque != None :

                                print('El valor de bloque no fue none')
                                print(simbolo.data_type.data_type)
                                print(valorBloque.tipoReturn.data_type)

                                if simbolo.data_type.data_type == valorBloque.tipoReturn.data_type :
                                    self.tipo = valorBloque.tipoReturn
                                    self.valorExpresion = valorBloque.valorReturn
                                    return self.valorExpresion
                                pass
                            else:
                                
                                if simbolo.data_type == Data_Type.non:

                                    self.tipo = Type_Expresion(Data_Type.non)
                                    self.valorExpresion = None
                                    return self.valorExpresion
                                
                                else:

                                    self.tipo = Type_Expresion(Data_Type.error)
                                    self.valorExpresion = None
                                    return self.valorExpresion                                

                            pass

                    else :

                        self.tipo = Type_Expresion(Data_Type.error)
                        self.valorExpresion = None
                        return self.valorExpresion

                else :

                    print('Vienen parametros')
                    cantParametrosMetodo = len(valorMetodo.listaParametros.hijos)
                    
                    if cantParametros == cantParametrosMetodo :
                        
                        entornoLocal = Entorno(enviroment.Global)
                        entornoLocal.Global = enviroment.Global
                        entornoLocal.nombreEntorno = identificador.valor.lower()
                        enviroment.entornosLocales.append(entornoLocal)

                        if self.insertParametros(listaParams, valorMetodo.listaParametros, entornoLocal, enviroment) :
                            
                            print('Se insertaron bien los parametros')
                            cantidadHijos = len(valorMetodo.bloqueEjecutar.hijos)
                            # print('cant hijos: ',cantidadHijos)

                            if cantidadHijos == 2 :

                                print('Viene declaración y bloque')

                                declaracion = valorMetodo.bloqueEjecutar.hijos[0]
                                bloque = valorMetodo.bloqueEjecutar.hijos[1]

                                # Ejecutamos la declaracion de variables
                                declaracion.execute(entornoLocal)
                                valorBloque = bloque.execute(entornoLocal)
                                

                                #Validacion Return
                                if valorBloque != None :

                                    print('El valor de bloque no fue none')
                                    print(simbolo.data_type.data_type)
                                    print(valorBloque.tipoReturn.data_type)

                                    if simbolo.data_type.data_type == valorBloque.tipoReturn.data_type :
                                        self.tipo = valorBloque.tipoReturn
                                        self.valorExpresion = valorBloque.valorReturn
                                        return self.valorExpresion
                                    pass
                                else:
                                
                                    if simbolo.data_type == Data_Type.non:

                                        self.tipo = Type_Expresion(Data_Type.non)
                                        self.valorExpresion = None
                                        return self.valorExpresion
                                
                                    else:

                                        self.tipo = Type_Expresion(Data_Type.error)
                                        self.valorExpresion = None
                                        return self.valorExpresion                                


                                pass
                            
                            else:

                                bloque = valorMetodo.bloqueEjecutar.hijos[0]
                                valorBloque = bloque.execute(entornoLocal)
                                
                                #Validacion Return
                                if valorBloque != None :

                                    print('El valor de bloque no fue none')
                                    print(simbolo.data_type.data_type)
                                    print(valorBloque.tipoReturn.data_type)

                                    if simbolo.data_type.data_type == valorBloque.tipoReturn.data_type :
                                        self.tipo = valorBloque.tipoReturn
                                        self.valorExpresion = valorBloque.valorReturn
                                        return self.valorExpresion
                                    pass
                                else:
                                
                                    if simbolo.data_type == Data_Type.non:

                                        self.tipo = Type_Expresion(Data_Type.non)
                                        self.valorExpresion = None
                                        return self.valorExpresion
                                
                                    else:

                                        self.tipo = Type_Expresion(Data_Type.error)
                                        self.valorExpresion = None
                                        return self.valorExpresion                                

                            pass
                        
                        else:

                            # Hacer segunda verificacion después

                            self.tipo = Type_Expresion(Data_Type.error)
                            self.valorExpresion = None
                            return self.valorExpresion

                        pass

                    else :

                        self.tipo = Type_Expresion(Data_Type.error)
                        self.valorExpresion = None
                        return self.valorExpresion

                    pass
                
                pass

            pass
        
        # El entorno es una tabla
        except:
            pass

        return self.valorExpresion    

    def insertParametros(self, listaExpresiones, listaParametros, entornoLocal, entorno):

        cantidadRecorrido = len(listaExpresiones.hijos)
        i = 0

        while i < cantidadRecorrido :
            #print('variable i: ',i)
            
            expresionExecute = listaExpresiones.hijos[i]
            value = expresionExecute.execute(entorno)

            parametroActual = listaParametros.hijos[i]
            tamParametro = len(parametroActual.hijos)


            if tamParametro == 4 :

                argNombre = parametroActual.hijos[1].hijos[0]
                nombreVariable = argNombre.valor.lower()
                tipoDeclaracion = parametroActual.hijos[2].hijos[0]

                if tipoDeclaracion.nombreNodo == 'TEXT':

                    if expresionExecute.tipo.data_type == Data_Type.character :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.character)
                            tipoVariable.data_specific = 'text'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False
                
                elif tipoDeclaracion.nombreNodo == 'SMALLINT':

                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'smallint'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False
                    
                elif tipoDeclaracion.nombreNodo == 'INTEGER':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'integer'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False
                    
                elif tipoDeclaracion.nombreNodo == 'BIGINT':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'bigint'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'DECIMAL':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'decimal'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'NUMERIC':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'numeric'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False                

                elif tipoDeclaracion.nombreNodo == 'REAL':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'real'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'MONEY':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'money'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'DATE':
                    
                    if expresionExecute.tipo.data_type == Data_Type.data_time :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.data_time)
                            tipoVariable.data_specific = 'data'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'BOOLEAN':

                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.boolean)
                            tipoVariable.data_specific = 'boolean'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False                

                pass

            elif tamParametro == 3 :

                nodo1 = parametroActual.hijos[0]
                nodo2 = parametroActual.hijos[1]
                nodo3 = parametroActual.hijos[2]

                if nodo1.nombreNodo == 'MODO_ARGUMENTO':
                    
                    argNombre = parametroActual.hijos[1].hijos[0]
                    nombreVariable = argNombre.valor.lower()
                    tipoDeclaracion = parametroActual.hijos[2].hijos[0]

                    if tipoDeclaracion.nombreNodo == 'TEXT':

                        if expresionExecute.tipo.data_type == Data_Type.character :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.character)
                                tipoVariable.data_specific = 'text'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False
                
                    elif tipoDeclaracion.nombreNodo == 'SMALLINT':

                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'smallint'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False
                    
                    elif tipoDeclaracion.nombreNodo == 'INTEGER':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'integer'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False
                    
                    elif tipoDeclaracion.nombreNodo == 'BIGINT':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'bigint'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'DECIMAL':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'decimal'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'NUMERIC':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'numeric'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False                

                    elif tipoDeclaracion.nombreNodo == 'REAL':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'real'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'MONEY':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'money'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'DATE':
                    
                        if expresionExecute.tipo.data_type == Data_Type.data_time :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.data_time)
                                tipoVariable.data_specific = 'data'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'BOOLEAN':

                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.boolean)
                                tipoVariable.data_specific = 'boolean'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    pass
                
                else :

                    argNombre = parametroActual.hijos[0].hijos[0]
                    nombreVariable = argNombre.valor.lower()
                    tipoDeclaracion = parametroActual.hijos[1].hijos[0]

                    if tipoDeclaracion.nombreNodo == 'TEXT':

                        if expresionExecute.tipo.data_type == Data_Type.character :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.character)
                                tipoVariable.data_specific = 'text'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False
                
                    elif tipoDeclaracion.nombreNodo == 'SMALLINT':

                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'smallint'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False
                    
                    elif tipoDeclaracion.nombreNodo == 'INTEGER':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'integer'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False
                    
                    elif tipoDeclaracion.nombreNodo == 'BIGINT':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'bigint'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'DECIMAL':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'decimal'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'NUMERIC':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'numeric'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False                

                    elif tipoDeclaracion.nombreNodo == 'REAL':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'real'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'MONEY':
                    
                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.numeric)
                                tipoVariable.data_specific = 'money'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'DATE':
                    
                        if expresionExecute.tipo.data_type == Data_Type.data_time :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.data_time)
                                tipoVariable.data_specific = 'data'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    elif tipoDeclaracion.nombreNodo == 'BOOLEAN':

                        if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                            if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                                return False
                            else:
                            
                                # Creamos Simbolo
                                tipoVariable = Type_Expresion(Data_Type.boolean)
                                tipoVariable.data_specific = 'boolean'
                                simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                                entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                                pass

                            pass
                        else :
                            return False

                    pass

            elif tamParametro == 2 :
                                
                argNombre = parametroActual.hijos[0].hijos[0]
                nombreVariable = argNombre.valor.lower()
                tipoDeclaracion = parametroActual.hijos[1].hijos[0]

                if tipoDeclaracion.nombreNodo == 'TEXT':

                    if expresionExecute.tipo.data_type == Data_Type.character :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.character)
                            tipoVariable.data_specific = 'text'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False
                
                elif tipoDeclaracion.nombreNodo == 'SMALLINT':

                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'smallint'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False
                    
                elif tipoDeclaracion.nombreNodo == 'INTEGER':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'integer'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False
                    
                elif tipoDeclaracion.nombreNodo == 'BIGINT':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'bigint'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'DECIMAL':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'decimal'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'NUMERIC':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'numeric'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False                

                elif tipoDeclaracion.nombreNodo == 'REAL':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'real'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'MONEY':
                    
                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.numeric)
                            tipoVariable.data_specific = 'money'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'DATE':
                    
                    if expresionExecute.tipo.data_type == Data_Type.data_time :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.data_time)
                            tipoVariable.data_specific = 'data'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False

                elif tipoDeclaracion.nombreNodo == 'BOOLEAN':

                    if expresionExecute.tipo.data_type == Data_Type.numeric :
                        
                        if entornoLocal.existeSimboloEntornoActual(nombreVariable) :
                            return False
                        else:
                            
                            # Creamos Simbolo
                            tipoVariable = Type_Expresion(Data_Type.boolean)
                            tipoVariable.data_specific = 'boolean'
                            simboloVariable = Symbol(nombreVariable,tipoVariable,value)
                            entornoLocal.ingresar_simbolo(nombreVariable,simboloVariable)
                            pass

                        pass
                    else :
                        return False
                
                pass

            i += 1
            pass

        return True
    
    def compile(self, enviroment):
        pass

    def getText(self):

        identificador = self.hijos[0]
        listaParams = self.hijos[1]

        stringParametros = ''
        for par in listaParams.hijos:
            stringParametros += par.getText()


        stringLlamada = str(identificador.valor) + '(' + str(stringParametros) + ')'
        return stringLlamada