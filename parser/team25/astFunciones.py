from astExpresion import Expresion, ExpresionCadena, ExpresionID, ExpresionNumero, TIPO_DE_DATO
from reporteErrores.errorReport import ErrorReport # EN EL AMBITO MAS EXTERIOR SE INGRESAN A LA LISTA , EN ESTAS SUB CLASES SOLO SE SUBE EL ERROR
import math
import hashlib

class FuncionNumerica(Expresion):
    def __init__(self, funcion, parametro1=None, parametro2=None, linea = 0):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.funcion = funcion
        self.linea = linea

    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label =\"" + self.funcion + "\" ];"

        # Retorno
        if self.parametro1:
            nodo += "\n" + identificador + " -> " + \
                str(hash(self.parametro1)) + ";"
            nodo += self.parametro1.dibujar()
        if self.parametro2:
            nodo += "\n" + identificador + " -> " + \
                str(hash(self.parametro2)) + ";"
            nodo += self.parametro2.dibujar()

        return nodo
    
    def ejecutar(self, ts = None):
        if self.parametro2 != None and self.parametro3 != None: # 3 PARAMETROS 
            print("3 parametros")
        elif self.parametro2 != None: # 2 PARAMETROS
            print("2 parametros")
        elif self.parametro1 != None: # 1 PARAMETRO
            print("1 parametro") 
        else:# SIN PARAMETROS
            
            if self.funcion == 'PI':
                print("RETORNA: "+ str(3.1416))
                return ExpresionNumero( 3.1416, TIPO_DE_DATO.DECIMAL , self.linea)
        
    








class FuncionCadena():
    def __init__(self, funcion, parametro1, parametro2=None, parametro3=None, linea = 0 ):
        self.funcion = funcion
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        self.parametro3 = parametro3
        self.linea = linea
        
    def dibujar(self):
        identificador = str(hash(self))

        nodo = "\n" + identificador + "[ label = \"" + self.funcion + "\" ];"
        nodo += "\n" + identificador + " -> " + \
            str(hash(self.parametro1)) + ";"
        nodo += "\n" + str(hash(self.parametro1)) + \
            "[label = \"" + self.parametro1 + "\"];"

        if self.parametro2:
            if isinstance(self.parametro2, str):
                nodo += "\n" + identificador + " -> " + \
                    str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + \
                    "[label = \"" + self.parametro2 + "\"];"
            else:
                nodo += "\n" + identificador + " -> " + \
                    str(hash(self.parametro2)) + ";"
                nodo += "\n" + str(hash(self.parametro2)) + \
                    "[label = \"" + str(self.parametro2) + "\"];"

        return nodo
    def ejecutar(self, ts):
        
        if self.parametro2 != None and self.parametro3 != None: # 3 PARAMETROS
            res1 = self.parametro1.ejecutar(ts)
            res2 = self.parametro2.ejecutar(ts)
            res3 = self.parametro3.ejecutar(ts)
            if isinstance(res1 , ErrorReport):
                return res1
            if isinstance(res2 , ErrorReport):
                return res2
            if isinstance(res3 , ErrorReport):
                return res3
            
            if self.funcion == "SUBSTRING":
                if isinstance(res1 , ExpresionID) or isinstance(res1 , ExpresionCadena):
                    if isinstance(res2 , ExpresionNumero) or isinstance(res3 , ExpresionNumero):
                        if res2.tipo == TIPO_DE_DATO.ENTERO and res3.tipo == TIPO_DE_DATO.ENTERO:
                            print("RETORNA: "+ str(res1)[int(res2.val) : int(res3.val)])
                            return ExpresionCadena(str(res1)[int(res2.val) : int(res3.val)], TIPO_DE_DATO.CADENA , self.linea)
                    # si no entra hasta el ultimo if  llega aca 
                    return ErrorReport('semantico', 'error de tipo en el parametro 2 o parametro 3' ,self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo en el parametro 1' ,self.linea)
           
            
        elif self.parametro2 != None:       # 2 PARAMETROS
            print("2 parametros")
            
        elif self.parametro1 != None:       # 1 PARAMETRO
            nodoSimplificado = self.parametro1.ejecutar(ts)
            if isinstance(nodoSimplificado , ErrorReport):
                return nodoSimplificado # SOLO SE SUBE EL ERROR
        
            if self.funcion == "LENGTH":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
                    print("RETORNA: "+ str(len(nodoSimplificado.val)))
                    return ExpresionNumero(len(nodoSimplificado.val), TIPO_DE_DATO.ENTERO , self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "TRIM":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
                    print("RETORNA: "+ str((nodoSimplificado.val)).strip())
                    return ExpresionCadena(str((nodoSimplificado.val)).strip(), TIPO_DE_DATO.CADENA , self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
            elif self.funcion == "MD5":
                if  isinstance(nodoSimplificado , ExpresionCadena) or isinstance(nodoSimplificado , ExpresionID):
                   # print("RETORNA: "+ str(hashlib.md5('dsdd').hexdigest()) )
                    return ExpresionCadena(":v", TIPO_DE_DATO.CADENA , self.linea)
                else:
                    return ErrorReport('semantico', 'error de tipo' ,self.linea)
                
                
                
                
             
        else:
            print("SIN PARAMAETROS") 



