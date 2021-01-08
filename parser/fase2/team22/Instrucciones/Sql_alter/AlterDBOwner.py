from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Optimizador.C3D import *
from Instrucciones.TablaSimbolos import Instruccion3D as c3d
# Para todas las definiciones que incluyan owner solamente aceptarlo en la sintaxis no hacer nada con ellos

class AlterDBOwner(Instruccion):
    def __init__(self, id, owner, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.owner = owner
        

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        arbol.consola.append("Consulta devuelta correctamente.")

    def generar3D(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append(c3d.asignacionH())
        code.append(c3d.aumentarP())
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "ALTER DATABASE " + self.id + " OWNER TO " + self.owner + ";"))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.LlamFuncion('call_funcion_intermedia'))

        return code
    
    def generar3DV2(self, tabla, arbol):
        super().generar3D(tabla,arbol)
        code = []
        code.append('h = p')
        code.append('h = h + 1')
        t0 = c3d.getTemporal()
        code.append(t0 + ' = "' + self.id + '"')
        code.append('heap[h] = ' + t0)
        code.append('h = h + 1')
        t1 = c3d.getTemporal()
        code.append(t1 + ' = "' + self.owner + '"')
        code.append('heap[h] = ' + t1)
        code.append('p = h')
        code.append('call_alterowner_database()')
        
        return code