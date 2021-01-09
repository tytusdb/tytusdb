from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato
from Instrucciones.TablaSimbolos.Nodo3D import Nodo3D
from Instrucciones.Excepcion import Excepcion
from Instrucciones.PL import Func, Declaracion,Execute,Asignacion,Return,If,Drop
from Instrucciones.Identificador import Identificador
from Instrucciones.Sql_insert import insertTable

class Func(Instruccion):
    def __init__(self, nameid,id, replace, parametros, instrucciones,declare, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.replace = replace
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.declare = declare
        self.my_dict={}
        self.my_dic=[]
        self.linea=linea
        self.columna=columna
        self.j=0

        self.nameid=nameid


    def getparam(self):
         return self.my_dic

    def addvalues(self,k, queue,tabla):
  
        print("entro a diccionerio ")         

        try: 
           #  self.my_dict.update({"name":queue.id,"value" :queue.val})
             print("agrego a diccionario : ")
  
             self.my_dic.append({"name":queue.id,"value" :queue.val,"tipo" :"","j" :k})      
             print(self.my_dic)

        except Exception as e:
              print(e)

    def actualizaalaprimera(self,valor1,valor2,j, tabla,arbol):
         print("ya selfalor",self.my_dic) 

         k=0
         temp=""
         for key in self.my_dic:
           
         
                #cadena es mi id de retorno 
            if( str(key["j"])==str(j) ):  
                 k=k+1 
                 if(key["tipo"]=="var" ):
           
                    if(k==1) :key["name"]=valor1
                    if(k==2): key["name"]=valor2
                    
         print("ya act valor",self.my_dic) 

     # my_dict.update({lst[i] :str(y)})
         


    def addvalues2(self, name,value,tipo,k):
  
        print("entro a add  "+name+" value="+value)         
        Pase2=False
        if(value):
          if(len(value)>0):Pase2=True
        if Pase2:  
            try: 
                print("entro a add3  "+name+" value="+value)         

            #  self.my_dict.update({"name":queue.id,"value" :queue.val})
                print("agrego a diccionario : ")
    
                self.my_dic.append({"name":name,"value" :value,"tipo" :"var","j" :k})      

            except Exception as e:
                print(e)     

        print("agrego a diccionario1'02 : ",self.my_dic)
      

    def versiexisteyactualiza(self,valuestable,objeto, k,tabla,arbol):
       
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
                  


    def agregarsiexiste(self,valor1,valor2, tabla,arbol):
       
         k=0
         for key in self.my_dic:
            k=k+1
         
                #cadena es mi id de retorno           
            if(key["tipo"]=="var"):

                    print("ya existe se sustituira su valor") 
                    if(k==1) :key["value"]=valor1
                    if(k==2): key["value"]=valor2
                   

                  




    def obtienesiexiste(self,name,valuestable, j,tabla,arbol):
        print("obendra name= "+name+"con valuestable= ",valuestable)        

    
            # pro


        for key in valuestable:
           
            nam=key["name"]
            f=str(key["j"]).replace(" ","")
            
            if(name==str(nam)and str(j)==f):
                    return key["value"]          
            
        return None   


    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        passWelcome2
        passWelcome2

    def analizar(self, tabla, arbol):
        """   super().analizar(tabla,arbol)
        resultado = self.expresion.analizar(tabla,arbol)
        if not isinstance(resultado, Excepcion):
            self.tipo = resultado
        return resultado """
        pass
    def traducir(self, tabla, arbol):
        pass

    def traducir(self,k, tabla, arbol):
        self.j=k
        # tabla.aum()
        if k==0 : tabla.setFuncion(self)
        cadena = ""
        funcname = ""
        print("j es  -------------------------------------"+str(self.j)+"----")         


        if k==0 : self.valtable(self.my_dic)

        h=0
        val2param=""
        val1param=""
        try:
                print("actuaparam in self.parametros") 

                for param in self.parametros: 
                        print("actualizaa999mera ",param) 

                        if(h==0):val1param=param
                        if(h==1):val2param=param
                    #    self.agregar(self,"",param,cadena)

                        h=h+1 
                """     print("actualizaalaprimera ",val1param,val2param) 
                print("start")  """

                self.actualizaalaprimera(val1param,val2param,k, tabla,arbol)

        except Exception as e:
            print(e) 
        


        print("dicc actuslizafo es",self.my_dic) 


        valuestable=self.getparam()
        try:
              funcname = "def "+self.id
              if k>0 : funcname += str(k)

              print("entro con namefuncion: ",self.id)         

              arbol.addfunciones3dtitulo(funcname+"(): ")
              arbol.addfunciones3d('global P\n')
              arbol.addfunciones3d('global Pila\n')
              temporal2 = tabla.getTemporal()
              arbol.addfunciones3d(f"{temporal2} = P+0")  
              temporalvar1 = tabla.getTemporal()
              arbol.addfunciones3d(f"{temporalvar1} = Pila[{ temporal2 }]")
              arbol.addfunciones3d(f"{temporal2} = { temporal2}+1")
              temporalvar2= tabla.getTemporal()
              arbol.addfunciones3d(f"{temporalvar2} = Pila[{ temporal2 }]")

              val1param=""
              val2param=""
              h=0
              print("tabla.my_dic es ",tabla.my_dic)         
              

              
              '''
              try: 
                  for el2 in tabla.my_dic: 
                      namef=el2["tipo"]
                      if(namef==self.id):
                           
                           if(h==0):val1param=el2["value"]
                           if(h==1):val2param=el2["value"]
                           h=h+1  
                  print("asignar ... val1param",val1param," y param2= ",val2param)         

                  self.agregarsiexiste(val1param,val2param, tabla,arbol)      

              except Exception as e:
                       print(e)      

              print("se asignaron valores de entrada ...",self.my_dic)         
              '''
              
              
              valuestable=self.my_dic


              for ele in self.instrucciones: 

                    print("entro a TIPO instrucciones")           
                    print(ele)           
                    print("enTIPO")           
                    try:
                            if isinstance(ele, Asignacion.Asignacion):
                                  print("es insta Asignacion ") 
                                  arbol.addComenfunc("Comienza instruccion de expresion")

                                  ele.traducir("No",tabla,arbol)
                                  if self.versiexisteyactualiza(self.my_dic,ele, k,tabla,arbol):
                                    print("si existe ") 

                                    pass
                                  else:
                                    print("no existe ") 
                                    self.addvalues(k,ele,tabla) 
                            elif isinstance(ele, If.If):
                                  print("es insta If ") 
                                  arbol.addComenfunc("Comienza instruccion de expresion")

                                  ele.traducir(self.my_dic,k,tabla,arbol)
                                 
                            elif isinstance(ele, Drop.Drop):
                                  print("es insta Drop ") 
                                  arbol.addComenfunc("Borrara funcion o procedimiento")

                                  ele.traducir(tabla,arbol)
                                 

                            elif isinstance(ele, Return.Return):
                                  print("es Return") 
                                  arbol.addComenfunc("Comienza instruccion de Return")
                                  print("inicio de codigo return") 
                                  print(valuestable) 


                                  if isinstance(ele.expresion, Identificador):
                        
                                    valu = ele.expresion.devolverId(tabla,arbol)                      
                                    value1 =self.obtienesiexiste(valu,valuestable,k, tabla,arbol)

                                    print("obtuvoe el valor retun= ",value1)

                                    if value1==None:
                                        return
                                  else:
                                    value1 = value1.traducir(tabla,arbol).temporalAnterior
                                  print("value1 es",value1) 
#compara si las vars de asignacion son iguales a la que retorna en return a, retorna solo su valor
                               
                                  print(" arbol.addfunciones3") 
                                  ele.traducir(1,value1,tabla,arbol)     
                                  
                               
                                  
                            else:
                                    if isinstance(ele, insertTable.insertTable):
                                         cadena = ele.extraer(0,tabla,arbol) 
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


    def valtable(self,mydict) :
        try: 
            nam=self.id
          
            
            # Using readlines() 
            file1 = open('reporteast.txt', 'r') 
            Lines = file1.readlines() 
            
            count = 0

            # Strips the newline character 
            for line in Lines: 
                name=""
                value=""
                tipo="var"
                no=""
                h= 0
                for num in line.strip().split('ý'):
                      print("num split es= ",num)  

                      if(h==0):name=num
                      if(h==1):value=num
                      if(h==2):tipo=num
                      if(h==3):no=num
                      h=h+1
                if(tipo==nam)  :        
                    self.addvalues2(name,value,tipo,no)
        except Exception as e:
              print(e)
    

              #   if(h==0):val1param=param
                             #  if(h==1):val2param=param
                        #    self.agregar(self,"",param,cadena)

                           #    h=h+1  