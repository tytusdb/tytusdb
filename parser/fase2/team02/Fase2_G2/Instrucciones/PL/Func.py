from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion

class Func(Instruccion):
    def __init__(self, id, replace, parametros, instrucciones,declare, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.replace = replace
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.declare = declare

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        pass

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        resultado = self.expresion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        return resultado
        
    def traducir(self, tabla, arbol):
        cadena = ""
        funcname = ""


        try: 
              funcname = "def "+self.id
                
              print("entro con namefuncion: ",self.id)         

              arbol.addfunciones3dtitulo(funcname+"(): ")
              arbol.addfunciones3d('global P\n')
              arbol.addfunciones3d('global Pila\n')
        
              for ele in self.instrucciones: 

                    print("entro a TIPO instrucciones")           
                    print(ele)           
                    print("enTIPO")           

                    cadena = ele.extraer(tabla,arbol) 
                    print("cadena ES ",cadena)           

                    try: 


                        arbol.addComenfunc("Asignar cadena")
                        temporal1 = tabla.getTemporal()
                        arbol.addfunciones3d(f"{temporal1} = { cadena }")

                        arbol.addComenfunc("Entrar al ambito")
                        temporal2 = tabla.getTemporal()
                        arbol.addfunciones3d(f"{temporal2} = P+2")
                        temporal3 = tabla.getTemporal()
                        arbol.addComenfunc("parametro 1")
                        arbol.addfunciones3d(f"{temporal3} = { temporal2}+1")
                        arbol.addComenfunc("Asignacion de parametros")
                        arbol.addfunciones3d(f"Pila[{temporal3}] = {temporal1}")

                        arbol.addComenfunc("Llamada de funcion")
                        arbol.addfunciones3d(f"P = P+2")
                        arbol.addfunciones3d(f"funcionintermedia()")
                        
                        arbol.addComenfunc("obtener resultado")
                        temporalX = tabla.getTemporal()
                        arbol.addfunciones3d(f"{temporalX} = P+2")
                        temporalR = tabla.getTemporal()
                        arbol.addfunciones3d(f"{temporalR} = Pila[{ temporalX }]")

                        arbol.addComenfunc("Salida de funcion")
                        arbol.addfunciones3d(f"P = P-2")    

                    except Exception as e:
                        print(e)



        except Exception as e:
              print(e)

        print("salio con caena= ",cadena)           
  
    