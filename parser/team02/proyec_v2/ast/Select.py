from ast.Expresion import Expresion
from ast.Symbol import Symbol
from ast.Expresion import Expresion
from ast.Symbol import TIPOVAR as Tipo
from ast.Sentencia import Sentencia
import Reportes.ReporteD as Sentencias
from py_linq import Enumerable

class Select(Sentencia):
    #SELECT selectclausules FROM  selectbody wherecondicion
    #Selecttable : SELECT selectclausules FROM  selectbody wherecondicion
    #St[0] = Select(t[2],t[4],t.slice[1].lineno,find_column(t.slice[1]),t[5])

    def __init__(self,id,value,line, column,declare):

        self.id = id
        self.line= line
        self.column = column
        self.value = value
        self.type = declare


    def exist_label(self,id,typo,campo,type1):
       
            comparaciontype =True
            comparacion =True
            print("1  ")  

            try:
               
                if(id== campo):
                      comparacion=False
                
            except:
                pass
            try:
               
                if(typo == type1):
                      comparaciontype=False
                
            except:
                pass
            print("12  ")
            if(comparacion and comparaciontype):
                #print("k ")
                return True
            #print("y ")

            return False



    def ejecutar(self,entorno,tree):
        print("zVV Select")
        
        #print("sentencias v "+Expres.id)     

        y= {} 
        try:         
            if self.id.type=="*":
                print("xxc")
                try:       
                    print("zVV 1")
                    if self.value.type=="ID":
                        y =  self.value.value 
                        print(" y= "+str(y))
                        SentenciasR = Sentencias.ReporteD()
                        print("7000a ")
                        SentenciasR.sentencia_titulo("Select*from "+y)

                        SentenciasR.write(y,entorno,tree)
                        print("7001 ")
                    
                except:
                        pass
        except:
            pass

        try:         
            if self.id.type=="valores":
                print("xxcvalores")
                try:       
                    print("zVV 1valores")
                    if self.value.type=="ID":
                        idtabla=  self.value.value 
                        print(" y= "+str(idtabla))
                        SentenciasR = Sentencias.ReporteD()
                        print("7000a ")
                       
                        A = tree.getlabels()
                        lst = []
                        for Expres in A:
                                print("comparativaddf  ")  
                                typo=""
                                try:
                                            typo=Expres.type
                                            
                                except:
                                            
                                            pass
                                print("comparativaddf 2 ")    
                                #comparativa=self.exist_label(self,idtabla,"table",Expres.id,typo)
                                



                                comparaciontype =False
                                comparacion =False
                                print("1  ")  

                                try:
                                
                                    if(idtabla== Expres.id):
                                        comparacion=True
                                    
                                except:
                                    pass
                                try:
                                    print("tipo es")
                                    print(typo)
                                    if("TABLE" == typo):
                                        comparaciontype=True
                                    
                                except:
                                    pass
                                print("12  ")
                                if(comparacion and comparaciontype):
                                
                                # print("comparativa es "+comparativa)  
                                 #if comparativa :
                              #if Expres.id==idtabla : 
                                    print("iterara tre "+Expres.id)      
                                    for sent in Expres.sentencias:
                                            print("campo es tre "+sent.id)      
                                            print("7001 ") 
                                            lst.append(sent.id)

                                          
                                #armar array de campos de id de tabla
                        print("recorrera values de tabla ") 
                        arrayjson= []
                        
                       
                          #my_dict.update({'third_key' : 1})
                         # my_dict.update({'third_key888' : 8})

                        #print(my_dict) 
                         #arrayjson.append(my_dict)
                          #arrayjson.append({'b':'2'})
                         # arrayjson.append({'b9':'29'})
                        #print(arrayjson) 

                           #students = Enumerable([{ 'name': 'Joe Smith', 'mark': 80}, { 'name': 'Joanne Smith', 'mark': 90}])

                        #print("valor 2 es ") 
                        #print(lst[1]) 
                        #print("valor 3 es ") 
                        #print(lst[2]) 

                        for Expres in tree.nodos:
                            print("112ep "+Expres.id)      
                            if Expres.id==idtabla : 
                                   i=-1
                                   my_dict={}
                                   for key in Expres.sentencias:
                                        print("g7 ")     
                                        i=i+1
                                        try:
                                            y= {} 
                                            y = key.getValor(entorno,tree) 
                                            print(" tipodefile "+lst[i] )
                                            print(" y= "+str(y))
                                            my_dict.update({lst[i] :str(y)})
                                            
                                        except:
                                            
                                            pass
                                    
                                   arrayjson.append(my_dict)      
                             # arrayjson.append(my_dict) 
                        print("final table es") 
                        print(arrayjson)  
                        tablequerie = Enumerable(arrayjson)
                        #students = Enumerable([{ 'name': 'Joe Smith', 'mark': 80}, { 'name': 'Joanne Smith', 'mark': 90}])
                        #names = students.select(lambda x: x['name']) # results in ['Joe Smith', 'Joanne Smith']
                        #print(names) 
                        #for label in self.id.value:
                          # ver si esta en alguno de los condicionales
                        
                        print("cc1") 
                        a=""
                        
                        
                        if self.id.type=="valores":
                            my_cols= []    
                            my_rows= []
                            for identificador in self.id.value:
                                print("cc3")
                                
                                print(identificador.value) 
                                if identificador.type=="ID":
                                    my_rows= []  
                                    try:
                                            
                                            print("VALOR ES") 
                                            VALOR=identificador.value
                                            a += VALOR+","
                                            print(VALOR) 
                                            names = tablequerie.select(lambda x: x[VALOR]) # results in ['Joe Smith', 'Joanne Smith']
                                            print("names es") 
                                            print(names) 

                                            str1 = ""  
                                            print("z2")
                                            for ele in names: 
                                                print("p2m")
                                                input4 = ele 
                                                print("p2")
                                                my_rows.append(input4)
                                                print("ñ2")
                                                print("input4 ")
                                                print(input4)
                                            print("z4 ")
                                                # str1 += ele   
                                            #a=a+str1
                                            my_cols.append(my_rows)

                                            #my_dict5.update(names)
                                            #columnaswhere.append(tablequerie.select(lambda x: x[VALOR]))
                                           
                                            
                                    except:
                                                    
                                        pass     
                           
                            print("7000a ")
                            print(my_cols) 

                            SentenciasR.write1(my_cols,my_rows,"Select "+a+" from "+idtabla,entorno,tree)
                            print("7001 ")   
                           
                       
                        # datan = tablequerie.select(lambda y: y['nombre'],lambda x: x['apellido'], lambda result: result) # results in ['Joe Smith', 'Joanne Smith']
                         #print(data) 


                       

                

                except:
                        pass
        except:
            pass

               
                     
        
        tree.agregarnodos(self)
        return False

        def listToString(s):  
            
            
            str1 = ""  
            
            
            for ele in s:  
                str1 += ele   
            
            
            return str1  