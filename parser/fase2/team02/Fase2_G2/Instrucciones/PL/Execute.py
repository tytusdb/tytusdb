from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion

class Execute(Instruccion):
    def __init__(self, id, parametros, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.parametros = parametros
    def ejecutar(self, tabla, arbol):
        print("ejecutara-----")

        super().ejecutar(tabla,arbol)

    def analizar(self, tabla, arbol):
   
        pass

    def analizar11(self, tabla, arbol):
        print("al9888")

        super().analizar(tabla,arbol)
        print("al088")

        resultado = self.expresion.analizar(tabla,arbol)
        print("al08888")

        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        return resultado
        
    def extraer(self,tabla,arbol):
        
        cadena = ""

        try: 
             
             cadena +=  self.id
             cadena += "()"

           
             
        except Exception as e:
                    print(e)

        return cadena
    
    def traducir(self, tabla, arbol):
        
        cadena = ""
        
        try: 
       
              cadena += self.extraer(tabla,arbol) 
        except Exception as e:
              print(e)


       # arbol.addComen("Entrar al ambito")
       # temporal2 = tabla.getTemporal()
       # arbol.addc3d(f"{temporal2} = P+2")
       # temporal3 = tabla.getTemporal()
       # arbol.addComen("parametro 1")
        #arbol.addc3d(f"{temporal3} = { temporal2}+1")
      # arbol.addComen("Asignacion de parametros")
        #arbol.addc3d(f"Pila[{temporal3}] = {temporal1}")

        arbol.addComen("Llamada de funcion")
        arbol.addc3d(f"P = P+2")
        arbol.addc3d(cadena)
        arbol.addc3d(f"P = P-2")
        arbol.addComen("Salida de funcion")

        arbol.addComen("obtener resultado")
        temporalX = tabla.getTemporal()

        arbol.addc3d(f"{temporalX} = P+2")
        temporalR = tabla.getTemporal()
        arbol.addc3d(f"{temporalR} = Pila[{ temporalX }]")
        arbol.addc3d(f"print({temporalR}) ")


  