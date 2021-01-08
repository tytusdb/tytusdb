import sys, os.path
nodo_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\AST\\')
sys.path.append(nodo_dir)

c3d_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\C3D\\')
sys.path.append(c3d_dir)

ent_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '\\ENTORNO\\')
sys.path.append(ent_dir)

from Nodo import Nodo
from Tipo_Expresion import *
from Entorno import Entorno
from Label import *

class Sentencia_If(Nodo):

    def __init__(self, nombreNodo, fila = -1, columna = -1, valor = None):
        Nodo.__init__(self,nombreNodo, fila, columna, valor)
    
    def execute(self, enviroment):
                
        condicional = self.hijos[0]
        valueCondicional = condicional.execute(enviroment)

        if condicional.tipo.data_type == Data_Type.boolean :

            if valueCondicional :

                # Entorno Local
                entornoLocal = Entorno(enviroment)
                entornoLocal.nombreEntorno = 'if ' + enviroment.nombreEntorno
                entornoLocal.Global = enviroment.Global
                enviroment.entornosLocales.append(entornoLocal)

                bloque = self.hijos[1]
                valorBloque = bloque.execute(entornoLocal)
                return valorBloque
                
            else:

                cantidadHijos = len(self.hijos)

                if cantidadHijos == 2 :
                    return None                    
                elif cantidadHijos == 3 :

                    nodo = self.hijos[2]

                    if nodo.nombreNodo == 'SENTENCIA_ELSE':
                        return nodo.execute(enviroment)
                    else:

                        for sentenciaElif in nodo.hijos:
                            
                            condicionalElif = sentenciaElif.hijos[0]
                            valueCondicionalElif = condicionalElif.execute(enviroment)

                            if condicionalElif.tipo.data_type == Data_Type.boolean :

                                if valueCondicionalElif :

                                    entornoLocal = Entorno(enviroment)
                                    entornoLocal.nombreEntorno = 'elif ' + enviroment.nombreEntorno
                                    entornoLocal.Global = enviroment.Global
                                    enviroment.entornosLocales.append(entornoLocal)

                                    bloque = sentenciaElif.hijos[1]

                                    return bloque.execute(entornoLocal)

                                pass
                            else:
                                print('Error')
                            pass
                            

                        pass

                    return None

                elif cantidadHijos == 4 :

                    nodo = self.hijos[2]
                    nodoElse = self.hijos[3]

                    for sentenciaElif in nodo.hijos:
                            
                        condicionalElif = sentenciaElif.hijos[0]
                        valueCondicionalElif = condicionalElif.execute(enviroment)

                        if condicionalElif.tipo.data_type == Data_Type.boolean :

                            if valueCondicionalElif :

                                entornoLocal = Entorno(enviroment)
                                entornoLocal.nombreEntorno = 'elif ' + enviroment.nombreEntorno
                                entornoLocal.Global = enviroment.Global
                                enviroment.entornosLocales.append(entornoLocal)

                                bloque = sentenciaElif.hijos[1]

                                return bloque.execute(entornoLocal)

                            pass
                        else:
                            print('Error')
                        pass
                    
                    # No se encontró nada, por tanto se ejecuta el else

                    return nodoElse.execute(enviroment)                    

        else:

            print('Error. Tipo de dato inválido')
            return None

    def compile(self, enviroment):
        stringIf = []

        condicional = self.hijos[0]
        codigoCondicional = condicional.compile(enviroment)

        if condicional.tipo.data_type == Data_Type.boolean :
            listaCondicional = codigoCondicional.splitlines()
            entornoLocal = Entorno(enviroment)
            entornoLocal.nombreEntorno = ' if ' + enviroment.nombreEntorno
            entornoLocal.Global = enviroment.Global
            enviroment.entornosLocales.append(entornoLocal)

            # Bloque If
            bloque = self.hijos[1]
            
            # Generando Etiqueta verdadera
            e1 = instanceLabel.getLabel()

            # Generando Etiqueta Falsa
            e2 = instanceLabel.getLabel()

            # Generando Etiqueta Salida
            e3 = instanceLabel.getLabel()
            stringIf+=listaCondicional
            stringIf.append('if ' + condicional.dir + ' == 1 :')
            stringIf.append('\tgoto '+ e1)
            stringIf.append('goto ' + e2)
            stringIf.append('label ' + e1)
            stringIf += bloque.compile(entornoLocal)
            stringIf.append('goto ' + e3)

            # Etiquetas falsas
            stringIf.append('label ' + e2 )

            cantidadHijos = len(self.hijos)

            if cantidadHijos == 3 :
                
                nodo = self.hijos[2]
                if nodo.nombreNodo == 'SENTENCIA_ELSE':

                    stringIf += nodo.compile(enviroment)

                else:

                    for sentenciaElif in nodo.hijos:
                            
                        condicionalElif = sentenciaElif.hijos[0]
                        valueCondicionalElif = condicionalElif.compile(enviroment)

                        if condicionalElif.tipo.data_type == Data_Type.boolean :

                            # Generando Etiqueta verdadera
                            e1 = instanceLabel.getLabel()

                            # Generando Etiqueta Falsa
                            e2 = instanceLabel.getLabel()

                            # Generando Etiqueta Salida
                            e3 = instanceLabel.getLabel()   

                            entornoLocal = Entorno(enviroment)
                            entornoLocal.nombreEntorno = 'elif ' + enviroment.nombreEntorno
                            entornoLocal.Global = enviroment.Global
                            enviroment.entornosLocales.append(entornoLocal)

                            bloque = sentenciaElif.hijos[1]

                            stringIf += valueCondicionalElif
                            stringIf.append('if ' + condicionalElif.dir + ' == 1 :')
                            stringIf.append('\tgoto '+ e1)
                            stringIf.append('goto ' + e2)
                            stringIf.append('label ' + e1)
                            stringIf += bloque.compile(entornoLocal)
                            stringIf.append('goto ' + e3)

                            # Etiquetas falsas
                            stringIf.append('label ' + e2)

                        else:
                            print('Error')

            elif cantidadHijos == 4:

                nodo = self.hijos[2]
                nodo2 = self.hijos[3]

                for sentenciaElif in nodo.hijos:
                            
                    condicionalElif = sentenciaElif.hijos[0]
                    valueCondicionalElif = condicionalElif.compile(enviroment)

                    if condicionalElif.tipo.data_type == Data_Type.boolean :

                        # Generando Etiqueta verdadera
                        e1 = instanceLabel.getLabel()

                        # Generando Etiqueta Falsa
                        e2 = instanceLabel.getLabel()

                        # Generando Etiqueta Salida
                        e3 = instanceLabel.getLabel()   

                        entornoLocal = Entorno(enviroment)
                        entornoLocal.nombreEntorno = 'elif ' + enviroment.nombreEntorno
                        entornoLocal.Global = enviroment.Global
                        enviroment.entornosLocales.append(entornoLocal)

                        bloque = sentenciaElif.hijos[1]

                        stringIf += valueCondicionalElif
                        stringIf.append('if ' + condicionalElif.dir + ' == 1 :')
                        stringIf.append('\tgoto '+ e1)
                        stringIf.append('goto ' + e2)
                        stringIf.append('label ' + e1)
                        stringIf += bloque.compile(entornoLocal)
                        stringIf.append('goto ' + e3)

                        # Etiquetas falsas
                        stringIf.append('label ' + e2)

                    else:
                        string += ''
                        print('Error')

                stringIf += nodo2.compile(enviroment)


                pass
            # Etiqueta Salida
            stringIf.append('label ' + e3)
            return stringIf
        else :

            print('Error')

        return stringIf

    def getText(self):
        pass