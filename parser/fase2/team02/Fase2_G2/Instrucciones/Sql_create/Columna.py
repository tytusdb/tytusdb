from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
class Columna(Instruccion):
    def __init__(self, nombre, tipo, constraint, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.nombre = nombre
        self.tipo = tipo
        self.constraint=constraint
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

    def analizar(self, tabla, arbol):
        pass

    def traducir(self, tabla, arbol):
        cadena = self.nombre

       #   print(" cadenakii ")
        try: 
            try: 
                #  print(" probara tipo")
               #   print(self.tipo)

                if(self.tipo != None):
                        #  print(" ccv")

                        if(self.tipo.tipo != None):
                          print(" tipo no es nulo")
                           #   print(self.tipo.tipo)
                          cadena += " "+self.tipo.toString()
                        #  print(" tipo 888")
                          cadena += " "+ self.tipo.dimension8()
                         #  cadena += " "+self.tipo.traducir(tabla, arbol)
                         #     print(" ccv2")
                        else:
                            print("tipo si es falso")    
             # except:
               #  print(" fallo 55")

            except Exception as e:
                    print(e)
            # print(" cadooooena ")

            if(self.constraint != None):
                for x in range(0, len(self.constraint)):
                    #  print(" cuiuiui")
                    try: 
                         cadena += self.constraint[x].traducir(tabla,arbol)
                         #  print(" 222eee")
                    except:
                            print(" fallo222222")

            #  print(" cadelpopna ")

        except:
              #  print(" fallo 55")
                                                
              pass  

        return cadena