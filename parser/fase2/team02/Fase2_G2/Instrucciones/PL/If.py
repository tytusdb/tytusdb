from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion
from Instrucciones.Expresiones import Aritmetica, Logica, Primitivo, Relacional, Between
from Instrucciones.Identificador import Identificador

from Instrucciones.Excepcion import Excepcion
from Instrucciones.PL import Func, Declaracion,Execute,Asignacion,Return,If,Drop


class If(Instruccion):
    def __init__(self,condicion, expresion, expresion2,strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.condicion = condicion
        self.expresion = expresion
        self.expresion2 = expresion2




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

    def obtienesiexiste(self,name,valuestable, j,tabla,arbol):
        print("obendra name= "+name+"con valuestable= ",valuestable," y j",j)        

    
            # pro


        for key in valuestable:
           
            nam=key["name"]
            if name==str(nam) :
                print("va a comp var con --"+str(key["tipo"])+"----")         

                if str(key["tipo"])=="var":

                    try: 
                        h1=str(key["j"]).replace(" ","")
                        print("h1 es  --"+h1+"----")         

                        if str(j)==h1:
                                return key["value"]          
                    except Exception as e:
                        print(e)
                else :
                 return key["value"]     
        return None         

    def addvalues(self,j,my_dic, queue,tabla):
  
        print("entro a diccionerio ")         

        try: 
           #  self.my_dict.update({"name":queue.id,"value" :queue.val})
             print("agrego a diccionario : ")
  
             my_dic.append({"name":queue.id,"value" :queue.val,"tipo" :"","j" :j})      
             

        except Exception as e:
              print(e)

    def traducir(self, tabla, arbol):
        pass

    def versiexisteyactualiza(self,valuestable,objeto, k, tabla,arbol):
       
         for key in valuestable:
           
            nam=key["name"]
            
            f=str(key["j"]).replace(" ","")
                #cadena es mi id de retorno           
            if(objeto.id==str(nam) and str(k)==f):
                    print("ya existe se sustituira su valor") 

                    cadena = ""
        
                    try: 
                    
                        #    cadena += objecto.extraer(tabla,arbol)
                           
                            key["value"]=objeto.val 

                            print("nuevo valor",objeto.val) 

                    except Exception as e:
                            print(e)

    def instr(self,expresiones,valuestable,tipe,tabla,arbol):
            
        for ele in expresiones: 

                    print("entro a TIPO instrucciones")           
                    print(ele)           
                    print("enTIPO")           
                    try:
                            # print("insta 4k es ",ele) 
                            # print("insta 4kstr es ",str(ele)) 
                            Esif=False
                            if str(ele).find('.If.If') > 0:
                                Esif=True

                            if isinstance(ele, Asignacion.Asignacion):
                                  print("es insta Asignacion ") 
                                  arbol.addComenfunc("Comienza instruccion de expresion")

                                  ele.traducir("No",tabla,arbol)
                                  if self.versiexisteyactualiza(valuestable,ele,tipe, tabla,arbol):
                                    pass
                                  else:
                                     self.addvalues(tipe,valuestable,ele,tabla) 


                            elif  Esif:
                                  print("es insta If ") 
                                  arbol.addComenfunc("Comienza instruccion de expresion")

                                  ele.traducir(valuestable,0,tabla,arbol)



                            elif isinstance(ele, Return.Return):
                                  print("es Return") 
                                  arbol.addComenfunc("Comienza instruccion de Return")
                                  print("inicio de codigo return") 
                                  print(valuestable) 


                                  if isinstance(ele.expresion, Identificador):
                                    node= ele.expresion
                                    valu = node.devolverId(tabla,arbol)                      
                                    value1 =self.obtienesiexiste(valu,valuestable,tipe, tabla,arbol)

                                    print("obtuvoe el valor retun= ",value1)

                                    if value1==None:
                                        return
                                  else:
                                    value1 = value1.traducir(tabla,arbol).temporalAnterior
                                  print("value1 es",value1) 
#compara si las vars de asignacion son iguales a la que retorna en return a, retorna solo su valor
                               
                                  print(" arbol.addfunciones3") 
                                  ele.traducir(valuestable,0,tabla,arbol)  

                                  return 1
                               
                                  
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



    
    def instr0(self,expresiones,valuestable,tabla,arbol):
       pass
    def traducir(self,valuestable,tipe,tabla, arbol):


        paso=False    
 
        #self.operador = operador
        print("va a sacar condicional")


        try:
                if isinstance(self.condicion, Relacional.Relacional):
                        print("es insta Asignacion ") 
                        value1=self.condicion.opIzq
                        value2=self.condicion.opDer
                        print(value1) 
                       # print(value2) 
                        print("es invalpppue2 ") 

                        if isinstance(value1, Identificador):
                            try: 
                                print("es invooooalpppue2 ") 
                                #valu = value1.devolverId(tabla,arbol)  

                              #  valu = value1.devolverId.id  
                               
                                print("es invooommpue2 ")
                                try:  
                                        valu = value1.devolverId(tabla,arbol) 

                                        print("obtuvoe el valor deentrada= ",valu)
                                except Exception as e:
                                   print(e) 

                                value1 =self.obtienesiexiste(valu,valuestable,tipe, tabla,arbol)
                            except Exception as e:
                                 print(e)
                            print("obtuvoe el valor deentrada= ",value1)

                            if value1==None:
                                 return
                        else:
                            print("no es instancia1 es")
                            value1 = value1.traducir(tabla,arbol).temporalAnterior
                        print("value1 es",value1)

                        print("value2k3 es",value2)

                        if isinstance(value2, Identificador):
                        
                            try: 
                           
                                try:  
                                        valu = value2.devolverId(tabla,arbol) 

                                        print("obtuvoe el valor deentrada= ",valu)
                                except Exception as e:
                                   print(e) 

                                value2=self.obtienesiexiste(valu,valuestable,tipe, tabla,arbol)
                            except Exception as e:
                                 print(e)
                            print("obtuvoe el valor value2= ",value2)
                  

                        else:
                            print("value2k es",value2)

                            value2 = value2.traducir(tabla,arbol).temporalAnterior
              
                        print("value2 es",value2)


                        print("va a scara operador")
                        signo=self.condicion.operador
                        print("operador es ",signo)
                     #para caluclar el val1 en base a t1

                                                      # ele.traducir(1,key["value"],tabla,arbol)     
                       #  w=w+1 
                       # if str(signo)=="=":
                           #    signo="=="

                        print("value1---"+value1+"-- and value2=-"+value2+"---") 
                        value1 = value1.replace(" ","")
                        value2 = value2.replace(" ","")
                        """  valu2=""
                        j=0
                        while j < len(value2):
                            print("caracter "+str(j)+"es ",value2[j])
                            if value2[j] != "\n" or value2[j] != "\r" :
                                      valu2=valu2+str(value2[j])
                            j=j+1          
                        value2 =valu2 """

                        Paso=False
                        if(signo=="="):
                            if(value1 == value2):   
                                 Paso=True
                                 print("paso es true") 
                            else:
                                 print("paso es false")   

                        if(signo=="!="):
                            if(value1 != value2):   
                                 Paso=True     
                        if(signo==">"):
                            if(value1 > value2):   
                                 Paso=True   
                        if(signo=="<"):
                            if(value1 < value2):   
                                 Paso=True  
                        if(signo==">="):
                            if(value1 >= value2):   
                                 Paso=True   
                        if(signo=="<="):
                            if(value1 <= value2):   
                                 Paso=True 
                       # calcular el codigo intermedio
                            # var1 = tabla.getTemporal()

                      #  arbol.addfunciones3d(f"if {value1} {signo}  {value2} :")
                      #  arbol.addfunciones3d(f"\tgoto . flag{var1}")
                       # arbol.addfunciones3d(f"\t#sentencias if...")
                      #  arbol.addfunciones3d(f"\tprint('es if')")
                        if Paso :
                            print("entro a if condicion")
                            try:
                              a=0
                            #   si hay if anidado
                              """    if(tipe==1): 
                                    a=self.instr0(self.expresion,valuestable,tabla,arbol)
                              else : """
                              a=self.instr(self.expresion,valuestable,tipe,tabla,arbol)
                              if a==1 : return
                              pass
                            except Exception as e:
                                print(e)  
                        else:
                            print("entro a else condicion")

                            j=0
                            for key in self.expresion2:
                                j=j+1
                            if j>0:
                             # arbol.addfunciones3d(f"else: ")
                            #  arbol.addfunciones3d(f"\t#sentencias else...")
                            #  arbol.addfunciones3d(f"\tprint('es else')")
                                try:
                                   
                                    """ if(tipe==1): 
                                       a=self.instr0(self.expresion2,valuestable,tabla,arbol)
                                    else : """
                                    a=self.instr(self.expresion2,valuestable,tipe,tabla,arbol)
                           

                                    if a==1 : return

                                except Exception as e:
                                    print(e)  

                       # arbol.addfunciones3d(f"label . flag{var1}")


 

                         

 

        except Exception as e:
                          print(e)

        print("entro a cuerpo if")
        for m in self.expresion:
            try:
                print("eexpre es,",m)
            except Exception as e:
                          print(e)


     
