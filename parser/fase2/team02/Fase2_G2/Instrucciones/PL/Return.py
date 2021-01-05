from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones import Aritmetica, Logica, Primitivo, Relacional, Between

class Return(Instruccion):
    def __init__(self, expresion, strGram ,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.expresion = expresion
        

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        resultado = self.expresion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        return resultado
        
    def extraer(self,tabla,arbol):
        
        cadena = " "

        try: 
            pass         

             
        except Exception as e:
                   print(e)      
                   print("extraer primi")        

        
       # cadena+= "\" "

        return cadena
            
    def traducir(self, tabla, arbol):
        pass
        
    def traducir(self, typ,temporal,tabla, arbol):
        print("entro  traduc return")
        temporal1 = tabla.getTemporal()
        arbol.addfunciones3d(f"{temporal1} = P+0")
    
        arbol.addfunciones3d(f"Pila[{temporal1}] = {temporal}")
