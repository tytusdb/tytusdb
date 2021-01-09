from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
import numpy as np

class GroupBy(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        tabla = []
        for x in range(0,len(self.valor)):
            val = self.valor[x].ejecutar(tabla,arbol)
            if(tabla == []):
                tabla = np.array((val))
            else:
                arreglo = self.devolverColumnaArreglo(val)
                tabla = np.insert(tabla, tabla.shape[1], np.array(arreglo), 1)
            
        return tabla
        
    def devolverColumnaArreglo(self,columna):
        res = []
        for x in range(0,len(columna)):
            val = columna[x]
            res.append(val[0])
        return res
    
'''
instruccion = GroupBy("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''