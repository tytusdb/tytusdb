from Optimizacion.Instruccion import Instruccion

class CondicionIF(Instruccion):
    def __init__(self,valorizq,operador,valorder,saltoV,saltoF,linea):
        self.valorizq=valorizq
        self.valorder=valorder
        self.operador=operador
        self.saltoV=saltoV
        self.saltoF=saltoF       
        self.linea=linea

    def Optimizar(self):
            'Metodo Abstracto para obtener el valor de la Instrruccion'
           
            anterior="";
            optimizado ="";
        
            if(self.saltoF ==''):

                #etiquetaf= self.saltoF.Optimizar();
                optimizado='if '+ self.valorizq +self.operador+self.valorder+': \n '+self.saltoV;
                print('IF OPTIMIZADO----------------------------------',optimizado)
                return optimizado;
            print('IF----------------------------------',self.valorizq)
            return self.valorizq
 


      