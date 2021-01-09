from sql.Instrucciones.TablaSimbolos.Instruccion import Instruccion
# Para todas las definiciones que incluyan owner solamente aceptarlo en la sintaxis no hacer nada con ellos

class AlterDBOwner(Instruccion):
    def __init__(self, id, owner, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id
        self.owner = owner
        

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        arbol.consola.append("Consulta devuelta correctamente.")

