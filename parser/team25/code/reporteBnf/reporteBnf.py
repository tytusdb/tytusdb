import os
class ReporteBnf:
    
    def  __init__(self):
        self.listaBnf = []
    
    def addProduccion(self,cadena):
        self.listaBnf.insert(0,cadena)
    
    def generarReporte(self):
        archivo = open('data/Reportes/gramaticaEjecucion.md' ,'w')# w es escritura, si no existe lo crea
        archivo.write("# GRAMATICA EN EJECUCION"+'\n---\n')
        for i in range(len(self.listaBnf)):
            archivo.write(self.listaBnf[i]+'\n\n')
        archivo.close()
        
    def showProduccionesConsola(self):
        for i in range(len(self.listaBnf)):
            print(self.listaBnf[i]+'\n')
            
    def showReporte(self):
        self.generarReporte()
        os.system('cd data/Reportes & gramaticaEjecucion.md')
        
    def clear(self):
        self.listaBnf = []
        
# INSTANCE
bnf = ReporteBnf()