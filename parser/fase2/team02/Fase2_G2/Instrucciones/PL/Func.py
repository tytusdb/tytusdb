from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion
from Instrucciones.PL import Func, Declaracion,Execute,Asignacion,Return
from Instrucciones.Identificador import Identificador

class Func(Instruccion):
    def __init__(self, id, replace, parametros, instrucciones,declare, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.replace = replace
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.declare = declare
        self.my_dict={}
        self.my_dic=[]
    def getparam(self):
         return self.my_dic

    def addvalues(self, queue):
  
        print("entro a diccionerio ")         

        try: 
           #  self.my_dict.update({"name":queue.id,"value" :queue.val})
             print("agrego a diccionario : ")
  
             self.my_dic.append({"name":queue.id,"value" :queue.val})      
             print(self.my_dic)

        except Exception as e:
              print(e)

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        passWelcome2
        passWelcome2

    def analizar(self, tabla, arbol):
        super().analizar(tabla,arbol)
        resultado = self.expresion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        return resultado
        
    def traducir(self, tabla, arbol):
        cadena = ""
        funcname = ""
        tabla.setFuncion(self)

        valuestable=self.getparam()
        try: 
              funcname = "def "+self.id
                
              print("entro con namefuncion: ",self.id)         

              arbol.addfunciones3dtitulo(funcname+"(): ")
              arbol.addfunciones3d('global P\n')
              arbol.addfunciones3d('global Pila\n')
              temporal2 = tabla.getTemporal()
              arbol.addfunciones3d(f"{temporal2} = P+0")  

              for ele in self.instrucciones: 

                    print("entro a TIPO instrucciones")           
                    print(ele)           
                    print("enTIPO")           
                    try:
                            if isinstance(ele, Asignacion.Asignacion):
                                  print("es insta Asignacion ") 
                                  arbol.addComenfunc("Comienza instruccion de expresion")

                                  ele.traducir(1,tabla,arbol)
                                  self.addvalues(ele) 


                            elif isinstance(ele, Return.Return):
                                  print("es Return") 
                                  arbol.addComenfunc("Comienza instruccion de expresion")
                                  print("inicio de codigo return") 
                                  print(valuestable) 
                                  for ke in valuestable:
                                        print("ke es ",ke) 

                                  for key in valuestable:
                                        print("mi id es ",key["name"]) 
                                        nam=key["name"]
                                        print("nam es ",nam) 
                                        print("ele.expresion es ",ele.expresion) 
                                        if isinstance(ele.expresion, Identificador):
                                            cadena = ele.expresion.devolverId(tabla,arbol)            
                                            if(cadena==str(nam)):
                                                print("concuerda return con "+str(nam)) 
                                                ele.traducir(1,key["value"],tabla,arbol)     

                               
                                  
                            else:
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


        except Exception as e:
              print(e)

        print("salio con caena= ",cadena)           
  
    