from enum import Enum
from ast.Expresion import Expresion
from Reportes.Datos import Datos
import Reportes.Errores as Reporte
from ast.Symbol import TIPOVAR as Tipo

import hashlib

class TIPO(Enum) :
    SUM = 1
    REST= 2
    MULT= 3
    DIV= 4
    PORC= 5
    VALOR= 10
    MD5= 11
    ID = 20
class Operar(Expresion):
    def __init__(self):
        self.tipo     = None
        self.value    = None
        self.line     = 0
        self.column   = 0
        self.right    = None 
        self.left    = None  

    def Value_normal(self,value):
        self.tipo = TIPO.VALOR
        self.value = value
    def Value_md5(self,value):
        print("seltipo=")

        self.tipo = TIPO.MD5
        print("self.tipo "+str(self.tipo))
        self.value = value

    def computeMD5hash(self,my_string):
         m = hashlib.md5()
         m.update(my_string.encode('utf-8'))
         return m.hexdigest()
        

    def Node(self,left,right,tipo,line,col):
        self.tipo = tipo
        self.right = right
        self.left = left        
        self.line = line
        self.column = col 

    def getvalue(self,value):
        decimal = False
        valor = ""
        for letra in value:
            if(letra.isdigit()):
                valor +=letra

        if(valor==""):
            return 0

        return int(valor)


    def getTipo(self,entorno,tree):
        print("getTipo ")
    
        if(self.tipo == TIPO.VALOR):
           
            return self.tipo             
        if(self.tipo == TIPO.MD5):
            print("entro a tipomd5 ")
            
            return self.tipo    
        return ""       

    def getValor(self,entorno,tree):
        print("wwq ")
       # print(self.tipo)
        print("ww77 ")
        if(self.tipo == TIPO.VALOR):
            print("ww9999 ")
           
            print("wwqd "+str(self.tipo))
            print("ww99990 ")
            print(self.value.getValor(entorno,tree))
            return self.value.getValor(entorno,tree)              
        if(self.tipo == TIPO.MD5):
            print("entro a tipomd5 ")
            
            return self.value.Value_md5()              

        elif(self.tipo == TIPO.SUM):
            param1 = self.left.getValor(entorno,tree)
            param2 = self.right.getValor(entorno,tree)
            if(isinstance(param1,str) and isinstance(param2,str)):
                return param1 + param2

            if(isinstance(param1,str)): param1 = self.convertir_a_numero(valor1)
            if(isinstance(param2,str)): param2 = self.convertir_a_numero(valor2)
            
            if isinstance(param1, int) and isinstance(param2, int):
                return int(param1) + int(param2)
            elif isinstance(param1, float) and isinstance(param2, int): 
                return round(float(float(param1) + float(param2)),2)
            elif isinstance(param1, int) and isinstance(param2, float):
                return round(float(float(param1) + float(param2)),2)            
            elif isinstance(param1, float) and isinstance(param2, float): 
                return round(float(float(param1) + float(param2)),2)
            else:                
                p = Datos("SEMANTICO","Error sumando datos, verifique que sean validos",self.line,self.column)
                Reporte.agregar(p)
                return None
        elif(self.tipo == TIPO.REST):
            param1 = self.left.getValor(entorno,tree)
            param2 = self.right.getValor(entorno,tree)
            if(isinstance(param1,str) and isinstance(param2,str)):
                return param1 + param2

            if(isinstance(param1,str)): param1 = self.convertir_a_numero(valor1)
            if(isinstance(param2,str)): param2 = self.convertir_a_numero(valor2)
            
            if isinstance(param1, int) and isinstance(param2, int):
                return int(param1) - int(param2)
            elif isinstance(param1, float) and isinstance(param2, int): 
                return round(float(float(param1)- float(param2)),2)
            elif isinstance(param1, int) and isinstance(param2, float):
                return round(float(float(param1) - float(param2)),2)            
            elif isinstance(param1, float) and isinstance(param2, float): 
                return round(float(float(param1) - float(param2)),2)
            else:                
                p = Datos("SEMANTICO","Error restando datos, verifique que sean validos",self.line,self.column)
                Reporte.agregar(p)
                return None
        elif(self.tipo == TIPO.MULT):
            param1 = self.left.getValor(entorno,tree)
            param2 = self.right.getValor(entorno,tree)
         
            if(isinstance(param1,str)): param1 = self.convertir_a_numero(valor1)
            if(isinstance(param2,str)): param2 = self.convertir_a_numero(valor2)
            
            if isinstance(param1, int) and isinstance(param2, int):
                return int(param1) * int(param2)
            elif isinstance(param1, float) and isinstance(param2, int): 
                return round(float(float(param1)  * float(param2)),2)
            elif isinstance(param1, int) and isinstance(param2, float):
                return round(float(float(param1)  * float(param2)),2)            
            elif isinstance(param1, float) and isinstance(param2, float): 
                return round(float(float(param1)  * float(param2)),2)
            else:                
                p = Datos("SEMANTICO","Error multiplicando datos, verifique que sean validos",self.line,self.column)
                Reporte.agregar(p)
                return None

        elif(self.tipo == TIPO.DIV):
            param1 = self.left.getValor(entorno,tree)
            param2 = self.right.getValor(entorno,tree)
        
            if(isinstance(param1,str)): param1 = self.convertir_a_numero(valor1)
            if(isinstance(param2,str)): param2 = self.convertir_a_numero(valor2)
            if  isinstance(param2, int):
                if int(param2)==0 :
                    p = Datos("SEMANTICO","Error dividiendo datos entre 0, verifique que sean validos",self.line,self.column)
                    Reporte.agregar(p)
                    return None
            if isinstance(param1, int) and isinstance(param2, int):
                return int(param1) / int(param2)
            elif isinstance(param1, float) and isinstance(param2, int): 
                return round(float(float(param1)  / float(param2)),2)
            elif isinstance(param1, int) and isinstance(param2, float):
                return round(float(float(param1)  / float(param2)),2)            
            elif isinstance(param1, float) and isinstance(param2, float): 
                return round(float(float(param1)  / float(param2)),2)
            else:                
                p = Datos("SEMANTICO","Error dividiendo datos, verifique que sean validos",self.line,self.column)
                Reporte.agregar(p)
                return None
        elif(self.tipo == TIPO.ID):
            symbolic = entorno.get(str(self.value))
            if(symbolic == None):
                valueaagregar = Datos("SEMANTICO","No es existe la Variable "+self.value,self.line,self.column)
                Reporte.agregar(valueaagregar)
                return None

            value = symbolic.getValor(entorno,tree)
        

            return value

        print("wwq44 ")


    def convertir_a_numero(self,string_a_convertir):
        
         cadena_convertida = 0
         try:
            cadena_convertida = int(string_a_convertir)
         except ValueError:
             p = Datos("SEMANTICO","error convirtiendo la cadena "+string_a_convertir+" a un digito",self.line,self.column)
             Reporte.agregar(p)
            
         return cadena_convertida


    def getTypeofvar(self,entorno,tree):
        value = self.getValor(entorno,tree)
        if isinstance(value, str):
            return Tipo.STRING
        elif isinstance(value, int):
            return Tipo.ENTERO
        elif isinstance(value, float):
            return Tipo.DOBLE
        elif (value == True or value == False):
            return Tipo.BOOL
        else:
            return Tipo.NULL
