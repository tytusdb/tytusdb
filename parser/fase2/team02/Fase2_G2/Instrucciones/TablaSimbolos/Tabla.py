
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo as N
from numpy.core.numeric import indices
class Tabla():
    'Esta clase representa la tabla de símbolos.'

    def __init__(self, anterior):
        self.anterior = anterior
        self.variables = []
        self.funciones = []
        self.indices = []

        self.temporal = 0
        self.etiqueta = 0
        self.heap = 0
        self.stack = 0
        self.my_dic=[]
        self.j=0
        # self.f = 0
    def setIndex(self, index):
        tabla = self
        for f in tabla.indices:
            if f.id == index.idIndex:
                print("El indice " + f.id + " ya ha sido declarada.")
                return "El indice " + f.id + " ya ha sido declarada."
        print("se agrego el indice")
        self.indices.append(index)
        try: 
        #    a=simbolo.simbolo(funcion.id,"funcion/proc",funcion.linea,funcion.columna)

             a = N(index.idIndex,"","",index.linea,index.columna)
             self.setVariable(a)

             print("se agrego indice --1 ")

        except Exception as e:
                print(e) 

        return None

    def aum(self):
        self.j=self.j+1
    def getj(self):
        return self.j
    def setVariable(self,simbolo):
        tabla = self
        for variable in tabla.variables:
            if variable.id == simbolo.id:
                return "La variable " + variable.id + " ya ha sido declarada."
        self.variables.append(simbolo)
        return None
    def tableof(self):
        mensaje="------------Tabla de simbolos------------------"
        while self != None:
            for variable in self.variables:

                 try: 
       
            
                          mensaje += "id: "+str(variable.id) +", tipo: "+str(variable.tipo) +", valor: "+str(variable.valor)+  '\n'

                 except Exception as e:
                         print(e)  

              
            # tabla = tabla.anterior
        print(mensaje)

        self.txtsalida[self.tab.index("current")].insert(INSERT,mensaje)

    def getVariable(self,id):
        tabla = self
        # while tabla != None:
        for variable in tabla.variables:
                if variable.id == id:
                    return variable 
            # tabla = tabla.anterior
        return None
 
    def setFuncion(self, funcion):
        tabla = self
        for f in tabla.funciones:
            if f.id == funcion.id:
                print("La variable " + f.id + " ya ha sido declarada.")
                return "La variable " + f.id + " ya ha sido declarada."
        print("se agrego la funcion")
        self.funciones.append(funcion)
        try: 
        #    a=simbolo.simbolo(funcion.id,"funcion/proc",funcion.linea,funcion.columna)

             a = N(funcion.id,funcion.nameid,"",funcion.linea,funcion.columna)
             self.setVariable(a)

             print("se agrego 8 funcion ")

        except Exception as e:
                print(e) 

        return None


   

    def delFuncion(self, nombre):
        tabla = self
        print("buscara funcion ")

        while tabla != None:

            for funcion in tabla.funciones:
                 print("id de funcion es ---",funcion.id,"--con id --",nombre)
                 if str(funcion.id).strip() == str(nombre).strip():
                     print("es valido 66")
                     funcion.id=""
                     self.reemplazarentabla(str(nombre).strip())
                #  print("seguira")
 
            tabla = tabla.anterior
        # print("salio ")
   
        return None

    def reemplazarentabla(self,val):
        tabla = self
       

        for variable in tabla.variables:
                print("iterara")

                if variable.id == val:
                    print("es variable ")
                    variable.id=""
                    variable.nameid=""
                    variable.tipo=""
                    variable.linea=""
                    variable.columna=""
           
        return None
    def getFuncion(self, nombre):
        tabla = self
        print("buscara funcion ")

        while tabla != None:

            for funcion in tabla.funciones:
                print("id de funcion es ---",funcion.id,"--con id --",nombre)
                

                """   try: 
                    vv=funcion.id
                    funcion.id =vv.replace(" ","")
                    nombre = nombre.replace(" ","")

                except Exception as e:
                     print(e) """
                if str(funcion.id).strip() == str(nombre).strip():
                    print("es valido")
                    return funcion 
                print("seguira")
 
            tabla = tabla.anterior
        print("salio ")
   
        return None
    def addvalues(self, name,value,function):
  
        print("entro a diccionerio ")         

        try: 
           #  self.my_dict.update({"name":queue.id,"value" :queue.val})
             print("agrego a diccionariotable : ")
  
             self.my_dic.append({"name":name,"value" :value,"tipo" :function})      
            

        except Exception as e:
              print(e)


    def getTemporal(self):
        t = "t" + str(self.temporal)
        self.temporal += 1
        return t
    
    def getTemporalActual(self):
        return "t" + str(self.temporal)
    
    def getEtiqueta(self):
        l = "l" + str(self.etiqueta)
        self.etiqueta += 1
        return l
    
    def getEtiquetaActual(self):
        return "l" + str(self.etiqueta)


'''
from Simbolo import Simbolo

s1 = Simbolo("a","int","aa",1,1)
s2 = Simbolo("b","int","aa",2,1)
s3 = Simbolo("c","int","aa",3,1)

tablaGlobal = Tabla(None)

tablaGlobal.variables.append(s1)
tablaGlobal.variables.append(s2)
tablaGlobal.variables.append(s3)


s4 = Simbolo("a1","int","aa",1,1)
s5 = Simbolo("a1","int","aa",2,1)
s6 = Simbolo("c3","int","aa",3,1)


local1 = Tabla(tablaGlobal)

local1.setVariable(s4)
resultado = local1.setVariable(s5)
local1.setVariable(s6)

print(resultado)

encontro = local1.getVariable("a")
if encontro != None:
    print("encontro! " +encontro.id)
else:
    print("Error semántico!")

'''