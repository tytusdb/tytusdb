from Optimizacion.optimizaciones import *

class Ast():
    def __init__(self, instrucciones, arbol):
        self.instrucciones = instrucciones
        self.arbol = arbol
        
    def optimizar(self):
        optimizacion_uno(self.instrucciones, self.arbol)
        
        optimizacion_ocho(self.instrucciones, self.arbol)
        optimizacion_nueve(self.instrucciones, self.arbol)
        optimizacion_diez(self.instrucciones, self.arbol)
        optimizacion_once(self.instrucciones, self.arbol)
        optimizacion_doce(self.instrucciones, self.arbol)
        optimizacion_trece(self.instrucciones, self.arbol)
        optimizacion_catorce(self.instrucciones, self.arbol)
        optimizacion_quince(self.instrucciones, self.arbol)
        optimizacion_dieciseis(self.instrucciones, self.arbol)
        optimizacion_diecisiete(self.instrucciones, self.arbol)
        optimizacion_dieciocho(self.instrucciones, self.arbol)
        
        mensaje = f""
        for inst in self.instrucciones:
            mensaje += inst.toString()
            
        return mensaje