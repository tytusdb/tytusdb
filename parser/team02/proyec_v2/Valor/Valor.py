from ast.Expresion import Expresion
import hashlib 

class Valor(Expresion):
    def __init__(self,value,line,column):
        self.value= value
        self.line = line
        self.column = column

    def getValor(self,entorno,tree):
        return self.value

    def Value_md5(self):
        print("entro a Value_md5 ")
        val= self.computeMD5hash(self.value) 
        print("val es ")
      #   print(self.value)
        print(val)
        return val
    def computeMD5hash(self,cad):

          try:
          
              hash_object = hashlib.md5(cad.encode())
              md5_hash = hash_object.hexdigest()
              result =str(md5_hash)
   
          except:
                         result ="no cadena"
                         pass
       
          return result
        

