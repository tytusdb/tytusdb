from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion

class Declaracion(Instruccion):
    def __init__(self, id, constante, tipo, notnull, default, expresion, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna,"strGram")
        print("entro a Declaracion")
        self.id = id
        self.constante = constante
        self.notnull = notnull
        self.default = default
        self.expresion = expresion
        print("entro a Deon")

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass
    def extraer(self,tabla,arbol):
        
        cadena = " "

        try: 
             
             cadena += self.expresion.extraer(tabla,arbol)
           
             
        except Exception as e:
                    print(e)
       # cadena+= "\" "

        return cadena
            
    def analizar(self, tabla, arbol):
       print("entro a analizar")

       pass
        
    def traducir(self, tabla, arbol):
        print("entro a traduc")
        cadena = ""
        
        try: 
       
              cadena += self.extraer(tabla,arbol) 
        except Exception as e:
              print(e)

        
        arbol.addComen("Asignar cadena")
        temporal1 = tabla.getTemporal()
        arbol.addc3d(f"{temporal1} = { cadena }")
