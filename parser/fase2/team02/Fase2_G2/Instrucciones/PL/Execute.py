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
    def generar(self, j,tabla, arbol):
            try:
                    cadena = self.extraer(tabla,arbol) 
                    caden = cadena.replace('()', '')

                    for ele in self.parametros:

                            hasparam=True
                            param=ele.traducir(tabla,arbol).temporalAnterior

                          
                            self.agregar("",param,caden,j)

                         

          
            except Exception as e:
              print(e) 
    def traducir(self,tipe, tabla, arbol):

        cadena = ""
        myfunc=None
        try: 
              namf=self.id 
              if tipe>0 : namf+= str(tipe)

              cadena +=namf+'()'
            #   cadena += self.extraer(tabla,arbol) 
            #   caden = cadena.replace('()', '')
        # tabla.setFuncion(self)

        except Exception as e:
              print(e)


        hayf=""
        try: 
       
            
            hayf=tabla.getFuncion(self.id)

        except Exception as e:
              print(e)  



        if  hayf==None:  
              return

        if tipe>0 :hayf.traducir(tipe,tabla, arbol)


        hasparam=False
        paramvalue=""
        my_dic=[]
        tp=1



        try: 
            print("if len(self.parametros ",self.parametros)
           # print( self.parametros.traducir(tabla,arbol).temporalAnterior )
            print("if le")

            h=0
            val2param=""
            val1param=""
            try:
                    for ele in self.parametros: 
                            hasparam=True
                            print("listadotraducir es ",ele.traducir(tabla,arbol).temporalAnterior)
                            param=ele.traducir(tabla,arbol).temporalAnterior
                            my_dic.append(param)
                            #   if(h==0):val1param=param
                             #  if(h==1):val2param=param
                        #    self.agregar(self,"",param,cadena)

                           #    h=h+1  
                            # tabla.addvalues("",param,cadena)

                    myfunc.agregarsiexiste(val1param,val2param, tabla,arbol)
                    print("se asignaron valores de entrada del lado de execute...",myfunc.my_dic)         

            except Exception as e:
              print(e) 
            
            temporal2 = tabla.getTemporal()
            arbol.addc3d(f"{temporal2} = P+1")

            for key in my_dic:
                      temporal1 = tabla.getTemporal()
                      arbol.addc3d(f"{temporal1} = { key}")
                      
                      arbol.addComen("Asignacion de parametro a pila")
                      arbol.addc3d(f"{temporal2} = { temporal2}+1")

                     
                      arbol.addc3d(f"Pila[{temporal2}] = {temporal1}")
                      tp=tp+1

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
        if(hasparam):
            arbol.addComen("Llamada de funcion")
            arbol.addc3d(f"P = P+2")
            arbol.addc3d(cadena)
            arbol.addc3d(f"P = P-2")
            arbol.addComen("Salida de funcion")



        else:
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
        temporalRz=temporalR


        arbol.addComen("Entrar al ambito")
        temporal2 = tabla.getTemporal()
        arbol.addc3d(f"{temporal2} = P+2")
        temporal3 = tabla.getTemporal()
        arbol.addComen("parametro 1")
        arbol.addc3d(f"{temporal3} = { temporal2}+1")
        arbol.addComen("Asignacion de parametros")
        a="\"print('\"+str("+temporalR+")+\"');\""
        arbol.addc3d(f"Pila[{temporal3}] ={a}")

        arbol.addComen("Llamada de funcion")
        arbol.addc3d(f"P = P+2")
        arbol.addc3d(f"funcionintermedia()")
        
        arbol.addComen("obtener resultado")
        temporalX = tabla.getTemporal()
        arbol.addc3d(f"{temporalX} = P+2")
        temporalR = tabla.getTemporal()
        arbol.addc3d(f"{temporalR} = Pila[{ temporalX }]")

        arbol.addComen("Salida de funcion")
        arbol.addc3d(f"P = P-2")    


        return "str("+str(temporalRz)+")"
  
    def agregar(self,name,value,funcion,j):
        f = open ('reporteast.txt', "a+")
        f.write(name+"ý"+value+"ý"+funcion+"ý"+str(j)+"\n")
        f.close()    
