from Optimizacion.Instruccion import Instruccion

class Etiqueta(Instruccion):
    def __init__(self,etiqueta,linea):
        self.etiqueta=etiqueta
        self.linea=linea

    def Optimizar(self):
            'Metodo Abstracto para obtener el valor de la Instrruccion'
            print('etiqueta----------------------------------',self.etiqueta)
            return self.etiqueta
 
