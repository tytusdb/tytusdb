from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Expresiones import Aritmetica, Logica, Primitivo, Relacional, Between
from Instrucciones.Identificador import Identificador

class Where(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        if not arbol.getUpdate():
            arbol.setWhere(True)
            val = self.valor.ejecutar(tabla,arbol)
            arbol.setWhere(False)
            return val
            
        val = self.valor.ejecutar(tabla,arbol)
        print("hola me ejecuto en el where porque ahora soy un update")
        return val
        
        
    def analizar(self, tabla, arbol):
        pass


    def extraerwhere(self,tabla,arbol):
        cadena = " "

        try:
               

                if isinstance(self.valor, Relacional.Relacional):
                        signo=self.valor.operador
                        print("operador es ",signo)
                        print("es insta Asignacion ") 
                        value1=self.valor.opIzq
                        value2=self.valor.opDer
                        print(value1) 
                       # print(value2) 
                        print("es invalpppue2 ") 

                        if isinstance(value1, Identificador):
                    
                          
                                print("es invooommpue2 ")
                                try:  
                                        valu = value1.devolverId(tabla,arbol) 

                                        print("obtuvoe el valor deentrada= ",valu)
                                        cadena += valu+" "
                                except Exception as e:
                                   print(e) 

                         

                        cadena += signo+" "


                        if isinstance(value2, Identificador):
                        
                                print("es invooommpue2 ")
                                try:  
                                        valu = value2.devolverId(tabla,arbol) 

                                        print("obtuvoe el valor deentrada= ",valu)
                                        cadena += valu
                                except Exception as e:
                                   print(e) 

                        else:
                            value2 = value2.traducir(tabla,arbol).temporalAnterior
                            cadena += value2


                         

 

        except Exception as e:
                          print(e)

        return cadena  

    def extraer(self,tabla,arbol):
        
        cadena = " "

        
        try: 
              cadena += " where "+ self.extraerwhere(tabla,arbol)

        except Exception as e:
              print(e)
        
        return cadena  
    def traducir(self, tabla, arbol):
       pass