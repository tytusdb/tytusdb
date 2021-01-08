from Optimizacion.Instruccion import Instruccion
from Optimizacion.reporteOptimizacion import *

class Asignacion(Instruccion):
    def __init__(self,id=None, valorizq=None,operador=None,valorder=None,linea=''):
        self.valorder=valorder
        self.valorizq=valorizq
        self.operador=operador
        self.id=id
        self.linea=linea

    def Optimizar(self):
            'Metodo Abstracto para obtener el valor de la Instrruccion'
          
            anterior="";
            optimizado ="";
           

            if(self.valorder!=None and self.operador!=None):

                if (self.valorizq=='['):
                    'ES STACK'
                elif(self.valorizq in 'stack'):
                    ''
                else:
                    print (self.valorizq,'-----------',self.valorder)
                    if(self.id==self.valorizq):
                        if(self.operador=="+"):
                            if(self.valorder=="0"):
                                optimizado="Eliminado";
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 8', anterior,optimizado,self.linea))
                                return self.valorizq

                        elif(self.operador=="-"):
                            if(self.valorder=="0"):
                                optimizado="Eliminado";
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 9', anterior,optimizado,self.linea))
                                return self.valorizq

                        elif(self.operador=="*"):
                            if(self.valorder=="1"):
                                optimizado="Eliminado";
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 10', anterior,optimizado,self.linea))
                                print("anterior",anterior)
                                return self.valorizq
                            
                        elif(self.operador=="/"):
                            if(self.valorder=="1"):
                                optimizado="Eliminado";
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 11', anterior,optimizado,self.linea))
                                return self.valorizq
                    
                    if(self.id==self.valorder):
                        if(self.operador=="+"):
                            if(self.valorizq=="0"):
                                optimizado="Eliminado";
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 8', anterior,optimizado,self.linea))
                                return self.valorder

                        elif(self.operador=="*"):
                            if(self.valorizq=="1"):
                                optimizado="Eliminado";
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 10', anterior,optimizado,self.linea))
                                print("anterior",anterior)
                                return self.valorder
      
            
                    if(self.id != self.valorizq ):
                        print("entrooooooooo")
                        if(self.operador=="+"):
                            if(self.valorder=="0"):
                                optimizado=self.id + '='+ self.valorizq 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 12', anterior,optimizado,self.linea))
                                return optimizado
        
                        elif(self.operador=="-"):
                            if(self.valorder=="0"): 
                                optimizado=self.id + '='+ self.valorizq 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 13', anterior,optimizado,self.linea))
                                return optimizado
                            
                        elif(self.operador=="*"):
                            if(self.valorder=="1"): 
                                optimizado=self.id + '='+ self.valorizq 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 14', anterior,optimizado,self.linea))
                                return optimizado

                            elif(self.valorder=="2"):
                                optimizado=self.id + '='+ self.valorizq +" + "+ self.valorizq
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 16', anterior,optimizado,self.linea))
                                return optimizado

                            elif(self.valorder=="0"):
                                optimizado=self.id + '='+ self.valorder 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 17', anterior,optimizado,self.linea))
                                return optimizado

                        elif(self.operador=="/"):
                            if(self.valorder=="1"):
                                optimizado=self.id + '='+ self.valorizq 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 15', anterior,optimizado,self.linea))
                                return optimizado
                       
                    
                    if(self.id != self.valorder):
                        if(self.operador=="+"):
                            if(self.valizq=="0"):   
                                optimizado=self.id + '='+ self.valorder 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 12', anterior,optimizado,self.linea))
                                return optimizado
                            
                        elif(self.operador=="*"):
                            if(self.valorizq=="1"): 
                                optimizado=self.id + '='+ self.valorder 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 14', anterior,optimizado,self.linea))
                                return optimizado

                            elif(self.valorizq=="2"):
                                optimizado=self.id + '='+ self.valorder +" + "+ self.valorder
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 16', anterior,optimizado,self.linea))
                                return optimizado

                            elif(self.valorizq=="0"):
                                optimizado=self.id + '='+ self.valorizq 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 17', anterior,optimizado,self.linea))
                                return optimizado

                        elif(self.operador=="/"):
                            if(self.valorizq=="0"):
                                optimizado=self.id + '='+ self.valorizq 
                                anterior =self.id + '='+ self.valorizq +" "+self.operador+" "+ self.valorder
                                repOptimizado.append(reporteOptimizacion('Mirilla','Regla 18', anterior,optimizado,self.linea))
                                return optimizado
                         
                        
                        
                               