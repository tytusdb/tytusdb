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
        t0 = c3d.getTemporal()
        code.append(c3d.asignacionString(t0, "ALTER DATABASE " + self.id + " OWNER TO " + self.owner + ";"))
        code.append(c3d.asignacionTemporalStack(t0))
        code.append(c3d.aumentarP())

        return code