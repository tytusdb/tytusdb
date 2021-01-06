
from Interpreter.Instruction.instruction import Instruction
from Statics.console import Console
from Scripts.jsonMode import *



class Delete_Reg(Instruction):
    def __init__(self, tabla, where = None):
        self.tabla = tabla
        self.where = where
 
    def execute(self, env):
        print("Se ejecutó la instrucción 'DELETE'")
        
        #Lista 'registros' de prueba, remplazarla por la tabla enviada del where
        registros= [[{'idusuario':{'id':'idusuario','type':'integer','not_null':True,'pk':True}},
                    {'nombre':{'id':'nombre','type':'string','not_null':True,'pk':True}},
                    {'direccion':{'id':'direccion','type':'string','not_null':True,'pk':False}}],
                    [['1','Brayan','guate'],['2','Glendy','guate'],['3','otro','guate']]]

        listpk = []                               #Lista de llave o llaves primarias de la tabla [0,1]
        cont = 0 
        for dicc1 in registros[0]:                #accedemos a la lista
            for atributo,dicc2 in dicc1.items():  #acedemos a cada clave del diccionario: idusuario, nombre, dirección
                for elem,valor in dicc2.items():  #accedemos a cada clave y valor de cada diccionario: id,idusuario,type,integer...
                    
                    if (elem == 'pk' and valor == True):
                        listpk.append(cont)
                    
                cont = cont + 1      
       
                                                  
        cont2 = 0      
        for elem in registros[1]:
            listdel = []                           #Lista de llave o llaves a eliminar 
            for elem2 in listpk:         
                listdel.append(registros[1][cont2][elem2])
            cont2 = cont2 + 1
            
            resultado = delete(env.currentDB, self.tabla.getValue(env) , listdel)  #Funcion eleiminar
            Console.add(resultado)
      

      
