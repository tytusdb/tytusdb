import instrucciones as inst
import reglas as r

class Relacional():
    def __init__(self, expresion, linea):
        self.expresion = expresion
        self.linea = linea

    def optimizacion(self):

        if self.expresion[1] != None:
            valor1 = self.expresion[0]
            valor2 = self.expresion[2]
            op = self.expresion[1]
            ret = str(valor1) + ' ' + op + ' ' + str(valor2)
            
            #********************
            #****** IGUAL *******
            #********************
            if op == '==':
                
                #Se valida que sean valores constantes
                dato1 = constante(valor1)
                dato2 = constante(valor2)

                if dato1 and dato2:
                    #Se validan las reglas 4 y 5
                    if valor1 == valor2:
                        r.Reglas.regla5 = False #No se cumple porque los 2 valores son iguales
                    elif valor1 != valor2:
                        r.Reglas.regla4 = False #No se cumple porque los 2 valores no son iguales
                        r.Reglas.rela_negada = str(valor1) + ' != ' + str(valor2)
                else:
                    r.Reglas.rela_negada = str(valor1) + ' != ' + str(valor2)
                
            elif op == '!=':

                #Se valida que sean valores constantes
                dato1 = constante(valor1)
                dato2 = constante(valor2)

                if dato1 and dato2:
                    #Se validan las reglas 4 y 5
                    if valor1 == valor2:
                        r.Reglas.regla5 = False #No se cumple porque los 2 valores son iguales
                        r.Reglas.rela_negada = str(valor1) + ' == ' + str(valor2)
                    elif valor1 != valor2:
                        r.Reglas.regla4 = False #No se cumple porque los 2 valores no son iguales
                else:
                    r.Reglas.rela_negada = str(valor1) + ' == ' + str(valor2)

            else:
                if op == '>':
                    r.Reglas.rela_negada = str(valor1) + ' < ' + str(valor2)
                elif op == '<':
                    r.Reglas.rela_negada = str(valor1) + ' > ' + str(valor2)
                elif op == '>=':
                    r.Reglas.rela_negada = str(valor1) + ' <= ' + str(valor2)
                elif op == '<=':
                    r.Reglas.rela_negada = str(valor1) + ' >= ' + str(valor2)
            
        return ret

def constante(entrada):
    s = str(entrada)
    p = ord(s[0])

    if p > 47 and p < 58:
        return True
    
    return False