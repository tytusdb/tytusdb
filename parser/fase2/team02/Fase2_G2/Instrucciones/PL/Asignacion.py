from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones import Aritmetica, Logica, Primitivo, Relacional, Between

class Asignacion(Instruccion):
    def __init__(self, id,expresion, strGram ,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.expresion = expresion
        self.id = id
        self.val=""

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
             print("Primitivo self.expresion es",self.expresion)        

             if isinstance(self.expresion, Primitivo.Primitivo):
                 cadena += self.expresion.traducir(tabla,arbol).temporalAnterior
                 print("extraer Primitivo es"+cadena)        

             
        except Exception as e:
                   print(e)      
                   print("extraer primi")        

        
       # cadena+= "\" "

        return cadena
            
    def traducir(self, tabla, arbol):
        pass
        
    def traducir(self, typ,tabla, arbol):
        print("entro Asignaciona traduc")
        cadena = ""
        
        try: 
       
              cadena += self.extraer(tabla,arbol) 
        except Exception as e:
              print(e)

        print("cadena es ",cadena)

        arbol.addComenfunc("Asignar variable")
        temporal0 = tabla.getTemporal()
        arbol.addfunciones3d(f"{temporal0} = { cadena }")#resultado final a obtener
       #asignar temporal
        self.val=temporal0
       
        arbol.addComenfunc("se coloca el dato en la posicion de la pila")
        temporal1 = tabla.getTemporal()
        pos="0"
        arbol.addfunciones3d(f"{temporal1} = {pos }")
        arbol.addComenfunc("Asignacion de parametros a la posicion de parametro")
        arbol.addfunciones3d(f"Pila[{temporal1}] = {temporal0}")
       